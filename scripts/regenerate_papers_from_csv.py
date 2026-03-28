#!/usr/bin/env python3
"""Regenerate _data/papers.yml and _data/posters.yml from CSV + sorted_papers on disk."""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".vendor-yaml"))
import yaml  # noqa: E402

CSV_PATH = Path("/Users/jeaimehp/Desktop/sort-ADMI26-papers/paper-poster-reviews-3282026.csv")
SORTED = ROOT / "sorted_papers"
PAPERS_YML = ROOT / "_data" / "papers.yml"
POSTERS_YML = ROOT / "_data" / "posters.yml"

# Web path segments (spaces as %20 for Poster / Student paths, matching Jekyll site)
def pdf_web_path(submission_category: str, author_category: str, sid: int) -> str:
    n = f"ADMI_2026_paper_{sid}.pdf"
    if submission_category == "Full-Oral":
        base = "sorted_papers/Full-Oral"
        if author_category == "Faculty":
            return f"{base}/Faculty/{n}"
        if author_category == "Student - Graduate":
            return f"{base}/Student%20-%20Graduate/{n}"
        if author_category == "Student - Undergraduate":
            return f"{base}/Student%20-%20Undergraduate/{n}"
    if submission_category == "Poster":
        base = "sorted_papers/Poster"
        if author_category == "Student - Graduate":
            return f"{base}/Student%20-%20Graduate/{n}"
        if author_category == "Student - Undergraduate":
            return f"{base}/Student%20-%20Undergraduate/{n}"
    raise ValueError(f"Unknown combo: {submission_category!r} / {author_category!r}")


def pdf_disk_path(submission_category: str, author_category: str, sid: int) -> Path:
    n = f"ADMI_2026_paper_{sid}.pdf"
    if submission_category == "Full-Oral":
        base = SORTED / "Full-Oral"
        if author_category == "Faculty":
            return base / "Faculty" / n
        if author_category == "Student - Graduate":
            return base / "Student - Graduate" / n
        if author_category == "Student - Undergraduate":
            return base / "Student - Undergraduate" / n
    if submission_category == "Poster":
        base = SORTED / "Poster"
        if author_category == "Student - Graduate":
            return base / "Student - Graduate" / n
        if author_category == "Student - Undergraduate":
            return base / "Student - Undergraduate" / n
    raise ValueError(f"Unknown combo: {submission_category!r} / {author_category!r}")


def load_bib_map() -> dict[int, str]:
    out: dict[int, str] = {}
    for path in (PAPERS_YML, POSTERS_YML):
        if not path.exists():
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        for sec in data.get("sections", []):
            for item in sec.get("items", []):
                sid = item.get("submission_id")
                bib = item.get("bib")
                if sid is not None and bib:
                    out[int(sid)] = bib
    return out


def norm(s: str | None) -> str:
    if not s:
        return ""
    return " ".join(s.replace("\r\n", "\n").split())


def accepted(row: dict) -> bool:
    """ACCEPT* in Decision, or empty Decision with paper column ✔ (CSV data entry gap)."""
    d = (row.get("Decision") or "").strip().upper()
    if "ACCEPT" in d:
        return True
    if not d and (row.get("paper") or "").strip() == "✔":
        return True
    return False


def main() -> None:
    bib_map = load_bib_map()

    with CSV_PATH.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    id_key = None
    if rows:
        for k in rows[0].keys():
            if k.lstrip("\ufeff").strip() == "#":
                id_key = k
                break
        if id_key is None:
            id_key = list(rows[0].keys())[0]

    oral_items: dict[str, list[dict]] = {
        "faculty": [],
        "student-graduate": [],
        "student-undergraduate": [],
    }
    poster_items: dict[str, list[dict]] = {
        "student-graduate": [],
        "student-undergraduate": [],
    }

    skipped = []
    for row in rows:
        if not accepted(row):
            continue
        try:
            sid = int(str(row[id_key]).strip())
        except (ValueError, KeyError):
            continue
        sub = norm(row.get("Submission Category"))
        auth = norm(row.get("Author Category"))
        title = norm(row.get("Title"))
        authors = norm(row.get("Authors"))
        abstract = norm(row.get("Abstract"))
        if not title:
            continue

        try:
            disk = pdf_disk_path(sub, auth, sid)
        except ValueError:
            skipped.append((sid, sub, auth, "unknown category combo"))
            continue

        if not disk.is_file():
            skipped.append((sid, sub, auth, f"missing file {disk.relative_to(ROOT)}"))
            continue

        web = pdf_web_path(sub, auth, sid)
        item = {
            "title": title,
            "submission_id": sid,
            "pdf": web,
            "submission_type": sub,
            "author_category": auth,
            "authors": authors,
            "abstract": abstract,
        }
        if sid in bib_map:
            item["bib"] = bib_map[sid]

        if sub == "Full-Oral":
            if auth == "Faculty":
                oral_items["faculty"].append(item)
            elif auth == "Student - Graduate":
                oral_items["student-graduate"].append(item)
            elif auth == "Student - Undergraduate":
                oral_items["student-undergraduate"].append(item)
            else:
                skipped.append((sid, sub, auth, "unexpected author category for oral"))
        elif sub == "Poster":
            if auth == "Student - Graduate":
                poster_items["student-graduate"].append(item)
            elif auth == "Student - Undergraduate":
                poster_items["student-undergraduate"].append(item)
            else:
                skipped.append((sid, sub, auth, "unexpected author category for poster"))
        else:
            skipped.append((sid, sub, auth, f"unknown submission category {sub!r}"))

    for key in oral_items:
        oral_items[key].sort(key=lambda x: x["submission_id"])
    for key in poster_items:
        poster_items[key].sort(key=lambda x: x["submission_id"])

    papers_sections = [
        {
            "id": "faculty",
            "heading": "Faculty",
            "submission_category": "Full-Oral",
            "author_category": "Faculty",
            "count": len(oral_items["faculty"]),
            "items": oral_items["faculty"],
            "anchor_id": "full-oral-papers-faculty",
        },
        {
            "id": "student-graduate",
            "heading": "Student - Graduate",
            "submission_category": "Full-Oral",
            "author_category": "Student - Graduate",
            "count": len(oral_items["student-graduate"]),
            "items": oral_items["student-graduate"],
            "anchor_id": "full-oral-papers-student-graduate",
        },
        {
            "id": "student-undergraduate",
            "heading": "Student - Undergraduate",
            "submission_category": "Full-Oral",
            "author_category": "Student - Undergraduate",
            "count": len(oral_items["student-undergraduate"]),
            "items": oral_items["student-undergraduate"],
            "anchor_id": "full-oral-papers-student-undergraduate",
        },
    ]

    posters_sections = [
        {
            "id": "student-graduate",
            "heading": "Student - Graduate",
            "submission_category": "Poster",
            "author_category": "Student - Graduate",
            "count": len(poster_items["student-graduate"]),
            "items": poster_items["student-graduate"],
            "anchor_id": "posters-student-graduate",
        },
        {
            "id": "student-undergraduate",
            "heading": "Student - Undergraduate",
            "submission_category": "Poster",
            "author_category": "Student - Undergraduate",
            "count": len(poster_items["student-undergraduate"]),
            "items": poster_items["student-undergraduate"],
            "anchor_id": "posters-student-undergraduate",
        },
    ]

    def dump(data: dict) -> str:
        return (
            yaml.dump(
                data,
                default_flow_style=False,
                allow_unicode=True,
                sort_keys=False,
                width=1000,
            )
            .replace("\n\n", "\n")
        )

    PAPERS_YML.write_text("---\n" + dump({"sections": papers_sections}), encoding="utf-8")
    POSTERS_YML.write_text("---\n" + dump({"sections": posters_sections}), encoding="utf-8")

    print("papers.yml sections:", [(s["id"], s["count"]) for s in papers_sections])
    print("posters.yml sections:", [(s["id"], s["count"]) for s in posters_sections])
    if skipped:
        print("\nSkipped / warnings:", len(skipped))
        for row in skipped[:30]:
            print(" ", row)
        if len(skipped) > 30:
            print(" ...")


if __name__ == "__main__":
    main()
