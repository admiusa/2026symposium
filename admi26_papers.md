---
layout: default
title: Papers & Posters
permalink: /admi26_papers
---

Browse the ADMI 2026 collection by submission type and author category. Titles link directly to the PDF when the file is present in the repository under `sorted_papers/`.

<style>
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0 2rem 0;
}
th, td {
  border: 1px solid #d0d7de;
  padding: 0.6rem 0.75rem;
  vertical-align: top;
}
thead th {
  background: #f6f8fa;
  text-align: left;
}
tbody tr:nth-child(3n+1) td {
  background: #f6f8fa;
  font-size: 1.05rem;
}
tbody tr:nth-child(3n+1):not(:first-child) td {
  padding-top: 1.35rem;
}
tbody tr:nth-child(3n+3) td {
  white-space: normal;
  border-bottom: 2px solid #d0d7de;
  padding-bottom: 1.35rem;
}
tbody tr:last-child td {
  border-bottom: 1px solid #d0d7de;
  padding-bottom: 0.6rem;
}
</style>

## Quick Navigation

- [Full-Oral Papers](#full-oral-papers)
  - [Faculty](#full-oral-papers-faculty)
  - [Student - Graduate](#full-oral-papers-student-graduate)
  - [Student - Undergraduate](#full-oral-papers-student-undergraduate)
- [Poster](#posters)
  - [Student - Graduate](#posters-student-graduate)
  - [Student - Undergraduate](#posters-student-undergraduate)

## Section Tags

[`Full-Oral Papers`](#full-oral-papers) [`Posters`](#posters) [`Faculty`](#full-oral-papers-faculty) [`Graduate`](#full-oral-papers-student-graduate) [`Undergraduate Papers`](#full-oral-papers-student-undergraduate) [`Graduate Posters`](#posters-student-graduate) [`Undergraduate Posters`](#posters-student-undergraduate)

## At a Glance

{% assign oral_total = 0 %}
{% for s in site.data.papers.sections %}
  {% assign oral_total = oral_total | plus: s.items.size %}
{% endfor %}
{% assign poster_total = 0 %}
{% for s in site.data.posters.sections %}
  {% assign poster_total = poster_total | plus: s.items.size %}
{% endfor %}
{% assign all_total = oral_total | plus: poster_total %}

- **Total linked PDFs:** {{ all_total }}
- **Full-Oral papers:** {{ oral_total }}
- **Posters:** {{ poster_total }}

<h2 id="full-oral-papers">Full-Oral Papers</h2>

{% for section in site.data.papers.sections %}
<h3 id="{{ section.anchor_id }}">{{ section.heading }}</h3>

**Submission category:** `{{ section.submission_category }}`  
**Author category:** `{{ section.author_category }}`  
**Count:** {{ section.count }}

<table>
  <thead>
    <tr><th>Link</th><th>Type</th><th>Author Category</th><th>Authors</th></tr>
  </thead>
  <tbody>
{% for item in section.items %}
    <tr><td colspan="4"><strong>{{ item.title }}</strong></td></tr>
    <tr><td>{% if item.pdf %}<a href="{{ item.pdf | relative_url }}">PDF</a>{% endif %}{% if item.pdf and item.bib %} | {% endif %}{% if item.bib %}<a href="{{ item.bib | relative_url }}">BIB</a>{% endif %}</td><td>{{ item.submission_type }}</td><td>{{ item.author_category }}</td><td>{{ item.authors }}</td></tr>
    <tr><td colspan="4">{{ item.abstract }}</td></tr>
{% endfor %}
  </tbody>
</table>

{% endfor %}

<h2 id="posters">Posters</h2>

{% for section in site.data.posters.sections %}
<h3 id="{{ section.anchor_id }}">{{ section.heading }}</h3>

**Submission category:** `{{ section.submission_category }}`  
**Author category:** `{{ section.author_category }}`  
**Count:** {{ section.count }}

<table>
  <thead>
    <tr><th>Link</th><th>Type</th><th>Author Category</th><th>Authors</th></tr>
  </thead>
  <tbody>
{% for item in section.items %}
    <tr><td colspan="4"><strong>{{ item.title }}</strong></td></tr>
    <tr><td>{% if item.pdf %}<a href="{{ item.pdf | relative_url }}">PDF</a>{% endif %}{% if item.pdf and item.bib %} | {% endif %}{% if item.bib %}<a href="{{ item.bib | relative_url }}">BIB</a>{% endif %}</td><td>{{ item.submission_type }}</td><td>{{ item.author_category }}</td><td>{{ item.authors }}</td></tr>
    <tr><td colspan="4">{{ item.abstract }}</td></tr>
{% endfor %}
  </tbody>
</table>

{% endfor %}
