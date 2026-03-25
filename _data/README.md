# Site data (`_data`)

Jekyll loads every file in this folder as **`site.data.<filename_without_extension>`**. These YAML files drive Liquid templates on several pages. Edit them when you need to change speaker bios, paper listings, or poster listings without touching the page markup.

---

## `speakers.yml`

**Used by:** `admi26_speakers.md` via `site.data.speakers`

**Shape:** A **list** of speaker records (top-level array). Order is display order on the Speakers page.

| Field | Description |
|--------|-------------|
| `id` | Stable slug for HTML `id` and deep links (for example `alfred-watkins`, `elva-jones`). Used in URLs like `/admi26_speakers#alfred-watkins` from the program page. |
| `name` | Full display name. |
| `title` | Role or position line. |
| `org` | Institution or affiliation. |
| `email` | Used for the mailto link when set; may be left empty. |
| `linkedin` | Optional profile URL (shown as a LinkedIn link when set). |
| `image` | Optional path to a headshot, relative to the site root (for example `images/speakers/cory-brooks.jpg`). Leave empty to show the default silhouette graphic (`images/speaker-placeholder.svg`) on the Speakers page. |
| `bio` | HTML string for the biography (typically one or more `<p>` tags). |

---

## `papers.yml`

**Used by:** `admi26_papers.md` via `site.data.papers`

**Shape:** One object with a **`sections`** array. Each section is a **Full-Oral** group (Faculty, Student - Graduate, Student - Undergraduate).

Section fields:

| Field | Description |
|--------|-------------|
| `id` | Short slug for the section. |
| `heading` | Subsection title shown on the page. |
| `submission_category` | Usually `Full-Oral`. |
| `author_category` | Must match the row labels (for example `Faculty`, `Student - Graduate`). |
| `count` | Expected number of entries (should match `items` length when maintained). |
| `anchor_id` | Fragment ID for in-page navigation (for example `full-oral-papers-faculty`). Do not rename casually; Quick Navigation links depend on it. |
| `items` | List of papers in that section. |

Each **item**:

| Field | Description |
|--------|-------------|
| `title` | Paper title. |
| `pdf` | Path to the PDF under the repo (for example `sorted_papers/Full-Oral/Faculty/...pdf`). |
| `bib` | Path to the `.bib` file under `admi2026_bib/` (optional but usual). |
| `submission_type` | `Full-Oral`. |
| `author_category` | Same category as the section row. |
| `authors` | Author string as shown in the table. |
| `abstract` | Plain text or HTML entities; rendered inside the table cell. |

---

## `posters.yml`

**Used by:** `admi26_papers.md` via `site.data.posters`

**Shape:** Same as **`papers.yml`** (`sections` with `items`), but for **Poster** submissions (Student - Graduate and Student - Undergraduate).

Fields match **`papers.yml`**, except:

- `submission_category` and `submission_type` are **`Poster`**.
- `pdf` paths usually live under `sorted_papers/Poster/...` and may include URL-encoded spaces (`%20`).

---

## Regenerating from HTML tables

If you need to rebuild **`papers.yml`** and **`posters.yml`** from a legacy HTML export instead of editing YAML by hand, see **`scripts/README.md`** and run **`scripts/build_papers_data.py`** (requires **`scripts/papers_source.md`**).

---

## Paths and GitHub Pages

PDF and BIB paths are **site-relative** (not absolute URLs). The Papers & Posters template uses Jekyll’s **`relative_url`** filter so links work when the site is published with a **`baseurl`** (for example `/2026symposium`).
