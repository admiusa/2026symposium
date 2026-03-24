
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

    <a class="sponsor-card" href="https://www.teachcswithai.org" target="_blank" rel="noopener noreferrer">
      <div class="sponsor-logo-wrap">
        <img src="sponsorlogos/GenAIinCSEdClogo.svg" alt="GenAI in CS Education Consortium logo">
      </div>
      <div class="sponsor-name">GenAI in CS Education Consortium</div>
      <div class="sponsor-link">Visit Sponsor ↗</div>
    </a>

    <a class="sponsor-card" href="https://datascience.aucenter.edu" target="_blank" rel="noopener noreferrer">
      <div class="sponsor-logo-wrap">
        <img src="sponsorlogos/AUCC_SCI_LOGO.png" alt="AUC Data Science Initiative logo">
      </div>
      <div class="sponsor-name">AUC Data Science Initiative</div>
      <div class="sponsor-link">Visit Sponsor ↗</div>
    </a>

    <a class="sponsor-card" href="https://www.ncyte.net" target="_blank" rel="noopener noreferrer">
      <div class="sponsor-logo-wrap">
        <img src="sponsorlogos/ncyte_logo.png" alt="NCyTE Center logo">
      </div>
      <div class="sponsor-name">NCyTE Center</div>
      <div class="sponsor-link">Visit Sponsor ↗</div>
    </a>

    <a class="sponsor-card" href="https://sciencegateways.org" target="_blank" rel="noopener noreferrer">
      <div class="sponsor-logo-wrap">
        <img src="sponsorlogos/sciencegateways.png" alt="SGX3 logo">
      </div>
      <div class="sponsor-name">SGX3</div>
      <div class="sponsor-link">Visit Sponsor ↗</div>
    </a>

    <a class="sponsor-card" href="https://www.statsperform.com" target="_blank" rel="noopener noreferrer">
      <div class="sponsor-logo-wrap">
        <img src="sponsorlogos/stats-perform-logo.png" alt="Stats Perform logo">
      </div>
      <div class="sponsor-name">Stats Perform</div>
      <div class="sponsor-link">Visit Sponsor ↗</div>
    </a>

    <a class="sponsor-card" href="https://www.auburn.edu" target="_blank" rel="noopener noreferrer">
      <div class="sponsor-logo-wrap">
        <img src="sponsorlogos/auburn_formal_v_fullcolor_digital.svg" alt="Auburn University logo">
      </div>
      <div class="sponsor-name">Auburn University</div>
      <div class="sponsor-link">Visit Sponsor ↗</div>
    </a>
</div>

<p class="section-note">
  Sponsor logos on this page are referenced from the repository directory <code>/sponsorlogos/</code>.
</p>
