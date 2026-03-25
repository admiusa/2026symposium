---
layout: default
title: Speakers
permalink: /admi26_speakers
---

<style>
.page-intro {
  max-width: 860px;
  margin: 0 0 1.5rem 0;
  font-size: 1.05rem;
  line-height: 1.75;
}

.speaker-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  margin-top: 2rem;
}

.speaker-card {
  scroll-margin-top: 5rem;
  display: flex;
  flex-direction: row;
  align-items: stretch;
  border: 1px solid #d0d7de;
  border-radius: 18px;
  overflow: hidden;
  background: #ffffff;
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}

.speaker-image {
  flex: 0 0 260px;
  width: 260px;
  min-height: 240px;
  background: linear-gradient(180deg, #f6f8fa 0%, #eef2f7 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 0.75rem;
}

.speaker-image img.speaker-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.speaker-image img.speaker-image-placeholder {
  width: 52%;
  max-width: 200px;
  height: auto;
  max-height: 88%;
  object-fit: contain;
  opacity: 0.38;
  filter: grayscale(1);
}

.speaker-content {
  flex: 1 1 auto;
  min-width: 0;
  padding: 1.25rem;
}

.speaker-name {
  font-size: 1.28rem;
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 0.35rem;
}

.speaker-title {
  font-size: 0.98rem;
  color: #374151;
  margin-bottom: 0.8rem;
  line-height: 1.5;
}

.speaker-contact {
  margin-bottom: 0.95rem;
}

.speaker-contact a {
  text-decoration: none;
  font-weight: 700;
  color: #0969da;
}

.speaker-bio {
  font-size: 0.97rem;
  line-height: 1.72;
  color: #111827;
}

@media (max-width: 700px) {
  .speaker-card {
    flex-direction: column;
  }
  .speaker-image {
    width: 100%;
    flex: 0 0 auto;
    min-height: 0;
    height: 220px;
  }
}

.speaker-org {
  font-size: 0.98rem;
  font-weight: 600;
  color: #111827;
  margin-bottom: 0.5rem;
  line-height: 1.45;
}

.speaker-affiliations {
  max-width: 860px;
  margin: 0 0 2rem 0;
  padding: 1.15rem 1.25rem;
  border: 1px solid #d0d7de;
  border-radius: 14px;
  background: #f8fafc;
}
.speaker-affiliations h2 {
  margin: 0 0 0.5rem 0;
  font-size: 1.15rem;
  font-weight: 700;
  color: #111827;
}
.speaker-affiliations-intro {
  margin: 0 0 0.85rem 0;
  font-size: 0.95rem;
  color: #4b5563;
  line-height: 1.55;
}
.speaker-affiliations ul {
  margin: 0;
  padding-left: 1.25rem;
  font-size: 0.96rem;
  line-height: 1.65;
  color: #374151;
}
.speaker-affiliations li {
  margin-bottom: 0.25rem;
}
</style>



<div class="speaker-grid">
{% for speaker in site.data.speakers %}
<div class="speaker-card" id="{{ speaker.id }}">
  <div class="speaker-image">
    {% if speaker.image %}
    <img class="speaker-photo" src="{{ speaker.image | relative_url }}" alt="{{ speaker.name | xml_escape }}">
    {% else %}
    <img class="speaker-image-placeholder" src="{{ '/images/speaker-placeholder.svg' | relative_url }}" alt="" role="presentation" width="64" height="64" decoding="async">
    {% endif %}
  </div>
  <div class="speaker-content">
    <div class="speaker-name">{{ speaker.name }}</div>
    <div class="speaker-title">{{ speaker.title }}</div>
    <div class="speaker-org">{{ speaker.org }}</div>
    <div class="speaker-contact">
      {% if speaker.email or speaker.linkedin %}
      {% if speaker.email %}<a href="mailto:{{ speaker.email }}">[Contact Information]</a>{% endif %}
      {% if speaker.email and speaker.linkedin %} · {% endif %}
      {% if speaker.linkedin %}<a href="{{ speaker.linkedin }}" rel="noopener noreferrer">LinkedIn</a>{% endif %}
      {% else %}
      <span>[Contact Information]</span>
      {% endif %}
    </div>
    <div class="speaker-bio">{{ speaker.bio }}</div>
  </div>
</div>
{% endfor %}
</div>
