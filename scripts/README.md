# Scripts

## `build_papers_data.py`

Rebuilds **`_data/papers.yml`** and **`_data/posters.yml`** from the HTML tables in **`papers_source.md`**.

The Papers & Posters page (`admi26_papers.html`) reads those YAML files at build time. Under normal maintenance you can **edit the YAML directly** and do not need this script.

### When to use it

- You have a **full export of the old table markup** (three rows per entry: title, PDF/BIB row, abstract) and want to regenerate both data files in one step.
- You are **migrating** a large batch of changes that exist only as HTML tables, not in YAML.

### Requirements

- **Python 3** (stdlib only: `json`, `re`, `subprocess`, `pathlib`)
- **Ruby** with standard libraries **`json`** and **`yaml`** (used to write pretty, readable `.yml` files)

### Input

- **`papers_source.md`** (in this directory): must contain the same structure the parser expects:
  - Sections introduced with `## Full-Oral Papers` / `## Posters` and `###` subsection headings (Faculty, Student - Graduate, etc.)
  - For each paper/poster, a `<table>` whose `<tbody>` repeats the pattern: title row → link/type/authors row → abstract row.

To refresh this file from an older committed version of the page:

```bash
git show <commit>:admi26_papers.html > scripts/papers_source.md
```

Replace `<commit>` with a hash that still had the monolithic HTML tables.

### Command

From the **repository root** (the folder that contains `_config.yml`):

```bash
python3 scripts/build_papers_data.py
```

### Output

- Writes **`_data/papers.yml`** and **`_data/posters.yml`**
- Adds section metadata such as **`anchor_id`** so in-page links (for example `#full-oral-papers-faculty`) stay stable.
- Temporary `papers.json` / `posters.json` files are created only during the run and are removed afterward.

### After running

Rebuild or serve the Jekyll site and open the Papers & Posters page to confirm tables and counts. If the parser fails after you edit `papers_source.md`, check that each entry still matches the three-row pattern and that PDF/BIB links use `href="...pdf"` / `href="...bib"`.
