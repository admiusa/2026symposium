---
layout: home
title: ADMI 2026 Symposium
permalink: /
---

<style>
.hero {
  position: relative;
  overflow: hidden;
  border-radius: 20px;
  margin: 1.25rem 0 2rem 0;
  min-height: 360px;
  background:
    
    url('ADMI2026_banner.jpg') top center/cover no-repeat;
  display: flex;
  align-items: end;
  box-shadow: 0 12px 28px rgba(0,0,0,0.16);
}
.hero-inner {
  padding: 2rem;
  color: #fff;
  max-width: 760px;
}
.hero-kicker {
  display: inline-block;
  font-size: 0.9rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  opacity: 0.95;
  margin-bottom: 0.6rem;
}
.hero h1 {
  margin: 0 0 0.65rem 0;
  font-size: 2.4rem;
  line-height: 1.15;
  color: #fff;
}
.hero p {
  margin: 0;
  font-size: 1.08rem;
  line-height: 1.7;
  color: #f3f4f6;
}

.branding {
  display: flex;
  gap: 1.25rem;
  align-items: center;
  flex-wrap: wrap;
  margin: 0 0 1.5rem 0;
}
.branding img {
  max-height: 84px;
  width: auto;
  object-fit: contain;
}
.branding-copy {
  flex: 1 1 420px;
}
.branding-copy p {
  margin: 0.35rem 0 0 0;
  line-height: 1.7;
}

.quick-links {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
}
.quick-link {
  display: block;
  text-decoration: none;
  color: inherit;
  border: 1px solid #d0d7de;
  border-radius: 18px;
  padding: 1.15rem 1.2rem;
  background: #fff;
  box-shadow: 0 6px 18px rgba(0,0,0,0.05);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.quick-link:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.10);
}
.quick-link-title {
  font-weight: 700;
  font-size: 1.05rem;
  margin-bottom: 0.35rem;
}
.quick-link-text {
  color: #4b5563;
  line-height: 1.6;
  font-size: 0.96rem;
}

.section-card {
  border: 1px solid #d0d7de;
  border-radius: 18px;
  padding: 1.35rem 1.4rem;
  background: #fff;
  box-shadow: 0 6px 18px rgba(0,0,0,0.04);
  margin: 1.5rem 0;
}
.section-card h2 {
  margin-top: 0;
}
.section-card p {
  line-height: 1.75;
}

.participating-list {
  margin: 0.65rem 0 0 0;
  padding-left: 1.35rem;
  line-height: 1.65;
  color: #374151;
  font-size: 0.98rem;
}
@media (min-width: 700px) {
  .participating-list {
    column-count: 2;
    column-gap: 2.5rem;
  }
  .participating-list li {
    break-inside: avoid;
    padding-right: 0.5rem;
  }
}
.participating-section-heading {
  margin: 0 0 0.5rem 0;
  font-size: 1.2rem;
  line-height: 1.35;
  font-weight: 700;
  color: #111827;
}
.participating-section-heading .participating-icon {
  margin-right: 0.35rem;
}
#participating-institutions .participating-title {
  margin-bottom: 0.85rem;
  font-size: 1.28rem;
}
#participating-institutions .participating-subheading {
  margin: 1.35rem 0 0.5rem 0;
  font-size: 1.08rem;
  font-weight: 700;
  color: #111827;
}
#participating-institutions .participating-subheading:first-of-type {
  margin-top: 0.5rem;
}
.participating-list a {
  color: #0969da;
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 2px;
}
.participating-list a:hover {
  color: #0550ae;
}

#participating-locations-map #map {
  height: 600px;
  width: 100%;
  border-radius: 16px;
  margin-top: 1rem;
  border: 1px solid #d0d7de;
  z-index: 0;
}
#participating-locations-map .participating-map-intro {
  margin: 0 0 0.5rem 0;
  font-size: 0.98rem;
  color: #4b5563;
  line-height: 1.6;
}
.participating-map-filter {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin: 0 0 0.85rem 0;
}
.participating-map-filter-field {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 1rem;
}
.participating-map-filter label {
  font-weight: 600;
  font-size: 0.95rem;
  color: #374151;
}
#map-group-filter,
#map-affiliation-filter {
  min-width: min(100%, 26rem);
  max-width: 100%;
  padding: 0.5rem 0.65rem;
  font-size: 0.95rem;
  border: 1px solid #d0d7de;
  border-radius: 10px;
  background: #fff;
  color: #111827;
}

.main-site-banner {
  border: 1px solid #d0d7de;
  border-radius: 14px;
  padding: 1.1rem 1.2rem;
  background: linear-gradient(180deg, #f8fbff 0%, #ffffff 100%);
  margin: 0 0 1.5rem 0;
  font-size: 1rem;
  line-height: 1.65;
  color: #374151;
}
.main-site-banner p {
  margin: 0 0 0.55rem 0;
}
.main-site-banner p:last-child {
  margin-bottom: 0;
  color: #4b5563;
  font-size: 0.98rem;
}
.main-site-banner a {
  color: #0969da;
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 2px;
}
.main-site-banner a:hover {
  color: #0550ae;
}

.index-sponsors-intro {
  margin: 0 0 1rem 0;
  color: #374151;
  line-height: 1.7;
}
.index-sponsors-more {
  margin: 0 0 1.25rem 0;
  font-size: 0.98rem;
}
.index-sponsors-more a {
  color: #0969da;
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.sponsor-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.25rem;
  margin-top: 0.5rem;
}
.sponsor-card {
  display: block;
  text-decoration: none;
  color: inherit;
  background: #ffffff;
  border: 1px solid #d0d7de;
  border-radius: 18px;
  padding: 1.1rem;
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  text-align: center;
}
.sponsor-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.10);
}
.sponsor-logo-wrap {
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.75rem;
  background: #fff;
  border-radius: 12px;
  padding: 0.45rem;
}
.sponsor-logo-wrap img {
  max-width: 100%;
  max-height: 84px;
  width: auto;
  height: auto;
  object-fit: contain;
}
.sponsor-name {
  font-size: 0.98rem;
  font-weight: 700;
  line-height: 1.35;
  margin-bottom: 0.3rem;
}
.sponsor-link {
  font-size: 0.88rem;
  color: #0969da;
  font-weight: 600;
}

@media (max-width: 700px) {
  .hero {
    min-height: 290px;
  }
  .hero h1 {
    font-size: 1.9rem;
  }
  .hero-inner {
    padding: 1.35rem;
  }
}
</style>

<div class="hero">

</div>

<div class="main-site-banner" role="region" aria-label="Main ADMI 2026 event website">
  <p>
    <strong>Main event site:</strong>
    <a href="https://admiusa.org/admi2026/index.php" target="_blank" rel="noopener noreferrer">ADMI 2026 on admiusa.org</a>
    — registration, hotel, calls for participation, and official symposium information.
  </p>
  <p>
    This GitHub Pages site is a <strong>companion</strong> to that main site. Pages here host extended materials—such as
    the detailed schedule, speaker listings, proceedings, and sponsor recognition—for easy browsing and sharing.
  </p>
</div>

<div class="quick-links">
  <a class="quick-link" href="/2026symposium/admi26_president_letter">
    <div class="quick-link-title">President’s Letter</div>
    <div class="quick-link-text">Read the welcome message from ADMI President Alfred Watkins.</div>
  </a>

  <a class="quick-link" href="/2026symposium/admi26_program">
    <div class="quick-link-title">Schedule</div>
    <div class="quick-link-text">View the symposium program: sessions, keynotes, and daily highlights.</div>
  </a>

  <a class="quick-link" href="/2026symposium/admi26_speakers">
    <div class="quick-link-title">Speakers</div>
    <div class="quick-link-text">Meet the scholars, educators, and innovators featured at ADMI 2026.</div>
  </a>

  <a class="quick-link" href="/2026symposium/admi26_sponsors">
    <div class="quick-link-title">Sponsors</div>
    <div class="quick-link-text">Thank the organizations whose support helps make the symposium possible.</div>
  </a>

  <a class="quick-link" href="/2026symposium/admi26_papers">
    <div class="quick-link-title">Papers &amp; Posters</div>
    <div class="quick-link-text">Browse accepted submissions, abstracts, and linked PDFs from the proceedings page.</div>
  </a>
</div>

<div class="section-card">
  <h2>Welcome</h2>
  <p>
    The ADMI 2026 Symposium brings together students, faculty, researchers, and partners from Thursday, March 26 through
    Saturday, March 28, 2026, for three days of collaboration, discovery, and community in computing. Designed as both a
    scholarly gathering and a professional development experience, the symposium offers a dynamic program that includes
    keynote and plenary sessions, student-focused tracks on internships and graduate pathways, parallel faculty paper
    sessions, poster presentations, and a graduate school fair. Throughout the event, participants will find opportunities
    to engage with peers, connect with sponsors, and build relationships that extend beyond the symposium itself.
  </p>
  <p>
    Across the program, conversations are anchored in the evolving role of artificial intelligence and generative AI in
    education, research, and industry. Sessions explore topics ranging from emerging pedagogical approaches—such as
    “vibe coding” and AI-assisted learning—to broader discussions on responsible computing and ethical AI. A featured
    luncheon program highlights ethics in AI, while faculty sessions examine curriculum innovation and pathways for
    integrating AI into degree programs. The symposium also emphasizes hands-on and experiential learning through
    activities such as a virtual high-performance computing (HPC) crash course, student competitions in coding and
    cybersecurity, and both undergraduate and graduate research presentations. These elements culminate in an awards
    banquet celebrating excellence, innovation, and community impact across participating institutions.
  </p>
  <p>
    The Association of Computer Science Departments at Minority Institutions (ADMI) serves as the organizing body for
    this symposium and plays a critical role in advancing computing education and research at Historically Black Colleges
    and Universities (HBCUs) and other Minority Serving Institutions (MSIs). ADMI is dedicated to increasing the
    participation of underrepresented groups in computing by fostering collaboration among institutions, supporting
    student research and professional development, and creating pathways to graduate education and careers in technology.
    Through initiatives such as this symposium, ADMI continues to build a national community that promotes equity,
    excellence, and innovation in the computing disciplines.
  </p>
  <p>
    Together, the ADMI 2026 Symposium reflects a shared commitment to preparing the next generation of computing
    professionals—equipped not only with technical expertise, but also with the ethical awareness, collaborative mindset,
    and real-world experience needed to shape the future of technology.
  </p>
</div>

<div class="section-card index-sponsors" id="sponsors">
  <h2>Thank You to Our Sponsors</h2>
  <p class="index-sponsors-intro">
    ADMI 2026 is supported by partners who invest in computing education, research, and opportunity at Minority Serving Institutions.
  </p>
  <p class="index-sponsors-more">
    <a href="/2026symposium/admi26_sponsors">Sponsors page</a> — full list, details, and acknowledgments.
  </p>
  <div class="sponsor-grid">
{% for sponsor in site.data.sponsors %}
    <a class="sponsor-card" href="{{ sponsor.url }}" target="_blank" rel="noopener noreferrer">
      <div class="sponsor-logo-wrap">
        <img src="{{ sponsor.image | relative_url }}" alt="{{ sponsor.alt | escape }}">
      </div>
      <div class="sponsor-name">{{ sponsor.name }}</div>
      <div class="sponsor-link">Visit ↗</div>
    </a>
{% endfor %}
  </div>
</div>



<div class="section-card" id="participating-locations-map">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="">
<h2 class="participating-section-heading participating-title">Participating institutions map</h2>
<p class="participating-map-intro">Approximate locations of participating institutions, research centers, and partners (OpenStreetMap).</p>
<div class="participating-map-filter">
  <div class="participating-map-filter-field">
    <label for="map-group-filter">Filter by category</label>
    <select id="map-group-filter" aria-label="Filter map markers by organization category">
      <option value="">All categories</option>
      <option value="academic">Academic Institutions</option>
      <option value="research">Research Centers, Institutes, and National Labs</option>
      <option value="industry">Industry &amp; Partners</option>
    </select>
  </div>
  <div class="participating-map-filter-field">
    <label for="map-affiliation-filter">Jump to affiliation</label>
    <select id="map-affiliation-filter" aria-label="Select an affiliation to show on the map">
      <option value="">All locations (overview)</option>
    </select>
  </div>
</div>
<div id="map" role="application" aria-label="Map of participating organization locations"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>
{% raw %}
<script>
function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

var map = L.map('map').setView([37.8, -96], 4);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 18,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// [display name, lat, lng, website URL, group id] — URLs & groups align with _data/participating-orgs.yml
const locations = [
  ["Bowie State University", 39.0458, -76.7594, "https://www.bowiestate.edu", "academic"],
  ["Claflin University", 33.4956, -80.8556, "https://www.claflin.edu", "academic"],
  ["Clemson University", 34.6767, -82.8374, "https://www.clemson.edu", "academic"],
  ["Elizabeth City State University", 36.2965, -76.2226, "https://www.ecsu.edu", "academic"],
  ["Florida A&M University", 30.4241, -84.2850, "https://www.famu.edu", "academic"],
  ["Florida State University", 30.4419, -84.2985, "https://www.fsu.edu", "academic"],
  ["Grambling State University", 32.5277, -92.7163, "https://www.gram.edu", "academic"],
  ["Hampton University", 37.0229, -76.3356, "https://home.hamptonu.edu", "academic"],
  ["Howard University", 38.9227, -77.0194, "https://www.howard.edu", "academic"],
  ["Johnson C. Smith University", 35.2436, -80.8556, "https://www.jcsu.edu", "academic"],
  ["Mississippi Valley State University", 33.5127, -90.3417, "https://www.mvsu.edu", "academic"],
  ["Moraine Valley Community College", 41.6066, -87.8603, "https://www.morainevalley.edu", "academic"],
  ["Morehouse College", 33.7488, -84.4133, "https://www.morehouse.edu", "academic"],
  ["Morgan State University", 39.3443, -76.5843, "https://www.morgan.edu", "academic"],
  ["Sinclair Community College", 39.7589, -84.1916, "https://www.sinclair.edu", "academic"],
  ["South Carolina State University", 33.4985, -80.8556, "https://www.scsu.edu", "academic"],
  ["Spelman College", 33.7455, -84.4115, "https://www.spelman.edu", "academic"],
  ["Stanford University", 37.4275, -122.1697, "https://www.stanford.edu", "academic"],
  ["Texas Southern University", 29.7216, -95.3597, "https://www.tsu.edu", "academic"],
  ["Tuskegee University", 32.4302, -85.7080, "https://www.tuskegee.edu", "academic"],
  ["UC Berkeley", 37.8715, -122.2730, "https://www.berkeley.edu", "academic"],
  ["University of Florida", 29.6516, -82.3248, "https://www.ufl.edu", "academic"],
  ["University of the District of Columbia", 38.9430, -77.0657, "https://www.udc.edu", "academic"],
  ["Voorhees University", 33.4951, -80.8546, "https://voorhees.edu", "academic"],
  ["Wilberforce University", 39.7167, -83.8791, "https://wilberforce.edu", "academic"],
  ["Winston-Salem State University", 36.0894, -80.2410, "https://www.wssu.edu", "academic"],
  ["Auburn University (CSSE)", 32.6035, -85.4890, "https://eng.auburn.edu/csse", "academic"],
  ["Oak Ridge National Laboratory", 35.9306, -84.3104, "https://www.ornl.gov", "research"],
  ["Texas Advanced Computing Center", 30.2861, -97.7366, "https://www.tacc.utexas.edu", "research"],
  ["AUC Data Science Initiative", 33.7488, -84.4120, "https://datascience.aucenter.edu", "research"],
  ["Howard HCAI", 38.9227, -77.0194, "https://sites.google.com/view/hcaiathoward", "research"],
  ["Omnibond Systems", 28.5383, -81.3792, "https://www.omnibond.com", "industry"],
  ["Stats Perform", 41.8781, -87.6298, "https://www.statsperform.com", "industry"]
];

var markers = [];
locations.forEach(function (loc) {
  var label = escapeHtml(loc[0]);
  var href = loc[3];
  var popup =
    '<b><a href="' +
    href +
    '" target="_blank" rel="noopener noreferrer">' +
    label +
    "</a></b>";
  var marker = L.marker([loc[1], loc[2]]).addTo(map).bindPopup(popup);
  markers.push(marker);
});

var groupSelect = document.getElementById("map-group-filter");
var filterSelect = document.getElementById("map-affiliation-filter");

function visibleIndicesForGroup(g) {
  var out = [];
  locations.forEach(function (loc, i) {
    if (g === "" || loc[4] === g) out.push(i);
  });
  return out;
}

function fitOverviewOrGroup() {
  var g = groupSelect.value;
  map.closePopup();
  if (g === "") {
    map.flyTo([37.8, -96], 4, { duration: 0.6 });
    return;
  }
  var vis = visibleIndicesForGroup(g);
  if (!vis.length) return;
  var layer = L.featureGroup(vis.map(function (i) { return markers[i]; }));
  map.flyToBounds(layer.getBounds().pad(0.12), { duration: 0.6, maxZoom: 12 });
}

function applyMarkerVisibility() {
  var g = groupSelect.value;
  locations.forEach(function (loc, i) {
    var show = g === "" || loc[4] === g;
    if (show) {
      if (!map.hasLayer(markers[i])) markers[i].addTo(map);
    } else {
      if (map.hasLayer(markers[i])) map.removeLayer(markers[i]);
    }
  });
}

function rebuildAffiliationOptions() {
  while (filterSelect.children.length > 1) {
    filterSelect.removeChild(filterSelect.lastChild);
  }
  var g = groupSelect.value;
  locations.forEach(function (loc, index) {
    if (g !== "" && loc[4] !== g) return;
    var opt = document.createElement("option");
    opt.value = String(index);
    opt.textContent = loc[0];
    filterSelect.appendChild(opt);
  });
}

groupSelect.addEventListener("change", function () {
  filterSelect.value = "";
  applyMarkerVisibility();
  rebuildAffiliationOptions();
  fitOverviewOrGroup();
});

filterSelect.addEventListener("change", function () {
  var v = filterSelect.value;
  if (v === "") {
    fitOverviewOrGroup();
    return;
  }
  var i = parseInt(v, 10);
  if (isNaN(i) || i < 0 || i >= locations.length) return;
  var loc = locations[i];
  var g = groupSelect.value;
  if (g !== "" && loc[4] !== g) return;
  var latlng = L.latLng(loc[1], loc[2]);
  map.flyTo(latlng, 11, { duration: 0.6 });
  markers[i].openPopup();
});

rebuildAffiliationOptions();
</script>
{% endraw %}
</div>

<div class="section-card" id="participating-institutions">
{% assign participating_data = site.data['participating-orgs'] %}
<h2 class="participating-section-heading participating-title">{% if participating_data.title_icon %}<span class="participating-icon" aria-hidden="true">{{ participating_data.title_icon }}</span>{% endif %}{{ participating_data.title }}</h2>
{% for sub in participating_data.subsections %}
<h3 class="participating-section-heading participating-subheading">{% if sub.icon %}<span class="participating-icon" aria-hidden="true">{{ sub.icon }}</span>{% endif %}{{ sub.heading }}</h3>
<ul class="participating-list">
{% for item in sub.items %}
  <li><a href="{{ item.url }}" target="_blank" rel="noopener noreferrer">{{ item.name }}</a></li>
{% endfor %}
</ul>
{% endfor %}
</div>

