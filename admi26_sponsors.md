---
layout: default
title: Sponsors
permalink: /admi26_sponsors
---

<style>
.page-hero {
  max-width: 920px;
  margin-bottom: 2rem;
}
.page-hero h1 {
  margin-bottom: 0.4rem;
}
.page-hero p {
  font-size: 1.06rem;
  line-height: 1.75;
  color: #374151;
}

.thankyou-banner {
  border: 1px solid #d0d7de;
  border-radius: 18px;
  padding: 1.4rem 1.5rem;
  background: linear-gradient(180deg, #f8fbff 0%, #ffffff 100%);
  box-shadow: 0 6px 20px rgba(0,0,0,0.05);
  margin: 1.5rem 0 2rem 0;
}

.thankyou-banner p {
  margin: 0;
  line-height: 1.8;
}

.sponsor-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.sponsor-card {
  display: block;
  text-decoration: none;
  color: inherit;
  background: #ffffff;
  border: 1px solid #d0d7de;
  border-radius: 18px;
  padding: 1.2rem;
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  text-align: center;
}

.sponsor-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.10);
}

.sponsor-logo-wrap {
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
  background: #fff;
  border-radius: 12px;
  padding: 0.5rem;
}

.sponsor-logo-wrap img {
  max-width: 100%;
  max-height: 100px;
  width: auto;
  height: auto;
  object-fit: contain;
}

.sponsor-name {
  font-size: 1.02rem;
  font-weight: 700;
  line-height: 1.4;
  margin-bottom: 0.35rem;
}

.sponsor-link {
  font-size: 0.92rem;
  color: #0969da;
  font-weight: 600;
}

.section-note {
  margin-top: 2rem;
  font-size: 0.95rem;
  color: #6b7280;
}

@media (max-width: 640px) {
  .sponsor-grid {
    grid-template-columns: 1fr;
  }
}

.auc-dsi-section {
  max-width: 920px;
  margin: 2rem 0 2.5rem 0;
  padding: 0;
  border: 1px solid #d0d7de;
  border-radius: 18px;
  overflow: hidden;
  background: #ffffff;
  box-shadow: 0 6px 20px rgba(0,0,0,0.06);
}

.auc-dsi-section .auc-dsi-inner {
  padding: 1.5rem 1.5rem 1.75rem;
}

.auc-dsi-section h2 {
  margin: 0 0 0.5rem 0;
  font-size: 1.35rem;
  line-height: 1.35;
  color: #111827;
}

.auc-dsi-section .auc-dsi-lead {
  margin: 0 0 1.25rem 0;
  font-size: 1rem;
}

.auc-dsi-section .auc-dsi-lead a {
  color: #0969da;
  font-weight: 600;
}

.auc-dsi-banner {
  margin: 0;
  line-height: 0;
  background: #0f172a;
}

.auc-dsi-banner img {
  width: 100%;
  height: auto;
  display: block;
  vertical-align: middle;
}

.auc-dsi-section p {
  margin: 0 0 1rem 0;
  font-size: 1.06rem;
  line-height: 1.75;
  color: #374151;
}

.auc-dsi-section p:last-child {
  margin-bottom: 0;
}

.auc-dsi-section .auc-dsi-contact {
  margin-top: 1.1rem;
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
  font-size: 1.02rem;
}
</style>

<div class="page-hero">
  <h1>Thank You to Our Sponsors</h1>
  <p>
    The ADMI 2026 Symposium is made stronger through the generosity, partnership, and shared vision
    of organizations that believe in advancing computing education, broadening participation in
    technology, and supporting excellence across Minority Serving Institutions. We extend our sincere
    gratitude to our sponsors for helping make this year’s symposium possible.
  </p>
</div>

<div class="thankyou-banner">
  <p>
    On behalf of the ADMI community, thank you to each of our sponsors for investing in students,
    faculty, research, and the future of innovation. Your support helps create meaningful opportunities
    for collaboration, discovery, and growth throughout the symposium.
  </p>
</div>

<div class="sponsor-grid">
{% for sponsor in site.data.sponsors %}
    <a class="sponsor-card" href="{{ sponsor.url }}" target="_blank" rel="noopener noreferrer">
      <div class="sponsor-logo-wrap">
        <img src="{{ sponsor.image | relative_url }}" alt="{{ sponsor.alt | escape }}">
      </div>
      <div class="sponsor-name">{{ sponsor.name }}</div>
      <div class="sponsor-link">Visit Sponsor ↗</div>
    </a>
{% endfor %}
</div>

<section class="auc-dsi-section" aria-labelledby="auc-dsi-heading">
  <div class="auc-dsi-banner">
    <img src="{{ '/images/auc-dsi-fdsi-2026-banner.png' | relative_url }}" width="1024" height="1024" alt="The AUC Data Science Initiative: 2026 Faculty Development Summer Institute — Design. Develop. Deliver. Data Science Curriculum">
  </div>
  <div class="auc-dsi-inner">
    <h2 id="auc-dsi-heading">Atlanta University Center Data Science Initiative</h2>
    <p class="auc-dsi-lead">
      <a href="https://datascience.aucenter.org" target="_blank" rel="noopener noreferrer">datascience.aucenter.org</a>
    </p>
    <p>
      Atlanta continues to grow as a center for data science innovation and technology workforce development. The Atlanta University Center Data Science Initiative (AUC DSI) invites HBCU faculty to participate in the 2026 Faculty Development Summer Institute (FDSI), a collaborative program focused on designing and developing data science integrated courses across disciplines. The institute will be held in-person in Atlanta, May 25–29. Supported by Mastercard Center for Inclusive Growth, the 2026 FDSI will guide faculty to explore how data science skills can prepare students for emerging careers in analytics, artificial intelligence, computer science, biology, chemistry, public policy, social work, psychology and other social sciences, education, humanities, and technology-driven industries. Participants will work within a Peer Collaboration Model, where faculty engage in structured workshops, course design and development activities, and feedback sessions. Courses developed through the 2026 FDSI will align with the AUC Data Science Initiative Framework.
    </p>
    <p>
      Faculty selected for the program will join a growing network advancing data science education and workforce preparation across HBCUs.
    </p>
    <p class="auc-dsi-contact">
      <strong>For more information:</strong> Dr. King, Deputy Director —
      <a href="mailto:iking@aucenter.edu">iking@aucenter.edu</a>
    </p>
  </div>
</section>




