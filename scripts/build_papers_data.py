#!/usr/bin/env python3
"""Parse admi26_papers.md tables into _data/papers.json and _data/posters.json; then run Ruby to emit YAML."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Snapshot of the pre-Liquid table markup (update from git if tables are re-edited without YAML)
MD = ROOT / "scripts" / "papers_source.md"

ROW_RE = re.compile(
    r'<tr><td colspan="4"><strong>(?P<title>.*?)</strong></td></tr>\s*'
    r'<tr><td>(?P<linkcell>.*?)</td><td>(?P<ptype>.*?)</td><td>(?P<acat>.*?)</td><td>(?P<authors>.*?)</td></tr>\s*'
    r'<tr><td colspan="4">(?P<abstract>.*?)</td></tr>',
    re.DOTALL,
)


def extract_hrefs(linkcell):
    pdf = re.search(r'href="([^"]+\.pdf)"', linkcell)
    bib = re.search(r'href="([^"]+\.bib)"', linkcell)
    return (pdf.group(1) if pdf else None, bib.group(1) if bib else None)


def parse_items(tbody_html: str) -> list[dict]:
    items = []
    for m in ROW_RE.finditer(tbody_html):
        pdf, bib = extract_hrefs(m.group("linkcell"))
        title = m.group("title").strip()
        title = re.sub(r"<[^>]+>", "", title)
        items.append(
            {
                "title": title,
                "pdf": pdf,
                "bib": bib,
                "submission_type": m.group("ptype").strip(),
                "author_category": m.group("acat").strip(),
                "authors": m.group("authors").strip(),
                "abstract": m.group("abstract").strip(),
            }
        )
    return items


def parse_section_block(block):
    """Return (section_meta, tbody_inner) or None."""
    h = re.search(r"###\s+(.+)", block)
    if not h:
        return None
    heading = h.group(1).strip()
    sc = re.search(r"\*\*Submission category:\*\*\s*`([^`]+)`", block)
    ac = re.search(r"\*\*Author category:\*\*\s*`([^`]+)`", block)
    ct = re.search(r"\*\*Count:\*\*\s*(\d+)", block)
    tb = re.search(r"<tbody>(.*?)</tbody>", block, re.DOTALL)
    if not tb:
        return None
    sid = heading.lower().replace(" ", "-").replace("/", "-")
    sid = re.sub(r"[^a-z0-9\-]", "", sid.replace("student---", "student-"))
    meta = {
        "id": sid,
        "heading": heading,
        "submission_category": sc.group(1).strip() if sc else "",
        "author_category": ac.group(1).strip() if ac else "",
        "count": int(ct.group(1)) if ct else len(parse_items(tb.group(1))),
    }
    return meta, tb.group(1)


def attach_anchor_ids(sections, kind):
    """Match legacy Kramdown anchor IDs used in Quick Navigation."""
    mapping = {
        ("papers", "faculty"): "full-oral-papers-faculty",
        ("papers", "student-graduate"): "full-oral-papers-student-graduate",
        ("papers", "student-undergraduate"): "full-oral-papers-student-undergraduate",
        ("posters", "student-graduate"): "posters-student-graduate",
        ("posters", "student-undergraduate"): "posters-student-undergraduate",
    }
    for sec in sections:
        sec["anchor_id"] = mapping.get((kind, sec["id"]), sec["id"])


def main():
    text = MD.read_text(encoding="utf-8")
    if "## Posters" not in text:
        print("No ## Posters marker", file=sys.stderr)
        sys.exit(1)
    papers_part, posters_part = text.split("## Posters", 1)

    # Full-Oral: from ## Full-Oral Papers through end of that region
    if "## Full-Oral Papers" in papers_part:
        _, oral_rest = papers_part.split("## Full-Oral Papers", 1)
    else:
        oral_rest = papers_part

    paper_sections = []
    for chunk in re.split(r"(?=### )", oral_rest):
        chunk = chunk.strip()
        if not chunk.startswith("###"):
            continue
        parsed = parse_section_block(chunk)
        if not parsed:
            continue
        meta, tbody = parsed
        meta = dict(meta)
        meta["items"] = parse_items(tbody)
        paper_sections.append(meta)
    attach_anchor_ids(paper_sections, "papers")

    poster_sections = []
    for chunk in re.split(r"(?=### )", posters_part.strip()):
        chunk = chunk.strip()
        if not chunk.startswith("###"):
            continue
        parsed = parse_section_block(chunk)
        if not parsed:
            continue
        meta, tbody = parsed
        meta = dict(meta)
        meta["items"] = parse_items(tbody)
        poster_sections.append(meta)
    attach_anchor_ids(poster_sections, "posters")

    out_p = ROOT / "_data" / "papers.json"
    out_po = ROOT / "_data" / "posters.json"
    out_p.parent.mkdir(parents=True, exist_ok=True)
    out_p.write_text(
        json.dumps({"sections": paper_sections}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    out_po.write_text(
        json.dumps({"sections": poster_sections}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Papers sections: {len(paper_sections)}, posters: {len(poster_sections)}", file=sys.stderr)

    rb = r"""
require 'json'
require 'yaml'
['papers','posters'].each do |name|
  j = JSON.parse(File.read('_data/' + name + '.json'))
  File.write('_data/' + name + '.yml', YAML.dump(j))
end
"""
    subprocess.run(["ruby", "-e", rb], cwd=str(ROOT), check=True)
    out_p.unlink()
    out_po.unlink()
    print("Wrote _data/papers.yml and _data/posters.yml", file=sys.stderr)


if __name__ == "__main__":
    main()
