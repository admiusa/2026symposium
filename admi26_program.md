---
layout: default
title: Program
permalink: /admi26_program
---

<p class="program-floor-map-link"><a href="{{ '/maps/Floor_Map.pdf' | relative_url }}">Floor Map (PDF)</a></p>

<div class="program-title-row">
<h1 id="admi-program">ADMI 2026 Symposium Program</h1>
<div class="program-page-share">
<button type="button" class="program-share-btn" aria-label="Share link to this program page"><img class="program-share-icon" src="{{ '/images/share-icon.svg' | relative_url }}" width="22" height="22" alt=""></button>
</div>
</div>

<style>
.program-floor-map-link {
  margin: 0 0 0.85rem 0;
  font-size: 1rem;
}
.program-floor-map-link a {
  font-weight: 600;
  color: #0969da;
  text-decoration: none;
}
.program-floor-map-link a:hover {
  text-decoration: underline;
}
.program-day {
  margin-top: 2.25rem;
  scroll-margin-top: 5rem;
  border-radius: 16px;
  padding: 1.1rem 1.15rem 1.35rem 1.15rem;
  border: 1px solid transparent;
}
.program-day-tone-a {
  background: #eef2ff;
  border-color: #e0e7ff;
}
.program-day-tone-b {
  background: #f0fdf4;
  border-color: #d1fae5;
}
.program-day-tone-c {
  background: #fff8f1;
  border-color: #ffe8d9;
}
.program-day h2 {
  border-bottom: 2px solid rgba(0, 0, 0, 0.08);
  padding-bottom: 0.4rem;
  margin-bottom: 1rem;
}
.program-title-row {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: space-between;
  gap: 0.75rem 1rem;
  margin: 0 0 1.25rem 0;
}
.program-title-row h1 {
  margin: 0;
  font-size: 1.75rem;
  line-height: 1.25;
  font-weight: 700;
  color: #111827;
  flex: 1 1 auto;
}
.program-page-share {
  flex: 0 0 auto;
}
.program-card {
  position: relative;
  border: 1px solid #d0d7de;
  border-radius: 14px;
  padding: 1rem 1.2rem;
  margin: 1rem 0;
  background: #ffffff;
  box-shadow: 0 4px 14px rgba(0,0,0,0.05);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease, background-color 0.2s ease;
}
.program-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(15, 23, 42, 0.1);
  border-color: #8cb4ff;
}
.program-card[id] {
  scroll-margin-top: 5rem;
}
.program-card-share {
  position: absolute;
  top: 0.65rem;
  right: 0.65rem;
  z-index: 2;
}
.program-share-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  padding: 0.35rem 0.45rem;
  background: #f6f8fa;
  border: 1px solid #d0d7de;
  border-radius: 10px;
  cursor: pointer;
  line-height: 0;
  transition: background 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease;
}
.program-share-btn:hover {
  background: #eef2ff;
  border-color: #8cb4ff;
  box-shadow: 0 2px 8px rgba(9, 105, 218, 0.12);
}
.program-share-btn:focus-visible {
  outline: 2px solid #0969da;
  outline-offset: 2px;
}
.program-share-icon {
  display: block;
  width: 20px;
  height: 20px;
}
.program-page-share .program-share-icon {
  width: 22px;
  height: 22px;
}
.program-highlight {
  border-left: 4px solid #0969da;
  background: #f8fbff;
}
.program-highlight:hover {
  background: #eef6ff;
  box-shadow: 0 10px 28px rgba(9, 105, 218, 0.14);
  border-color: #54a0ff;
}
.program-card.program-card-break {
  background: #3d3d3d;
  border-color: #525252;
  color: #fff;
}
.program-card.program-card-break .program-time,
.program-card.program-card-break .program-event {
  color: #fff;
}
.program-card.program-card-break .program-room {
  color: rgba(255, 255, 255, 0.9);
}
.program-card.program-card-break .program-event a {
  color: #93c5fd;
}
.program-card.program-card-break .program-event a:hover {
  color: #dbeafe;
}
.program-card.program-card-break .program-share-btn {
  background: #4a4a4a;
  border-color: #737373;
}
.program-card.program-card-break .program-share-btn:hover {
  background: #525252;
  border-color: #a3a3a3;
  box-shadow: 0 2px 8px rgba(255, 255, 255, 0.08);
}
.program-card.program-card-break:hover {
  background: #333333;
  border-color: #666666;
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.35);
}
@media (prefers-reduced-motion: reduce) {
  .program-card {
    transition: none;
  }
  .program-card:hover {
    transform: none;
  }
}
.program-time {
  font-weight: 700;
  color: #111827;
  margin-bottom: 0.25rem;
  padding-right: 2.75rem;
}
.program-room {
  font-size: 0.95rem;
  color: #0969da;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.program-event {
  color: #374151;
  line-height: 1.65;
}
.program-event a {
  color: #0969da;
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 2px;
}
.program-event a:hover {
  color: #0550ae;
}
.program-quicklinks {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.35rem 0.75rem;
  margin: 1rem 0 1.75rem 0;
  padding: 0.75rem 1rem;
  border: 1px solid #d0d7de;
  border-radius: 12px;
  background: #f6f8fa;
  font-size: 0.98rem;
}
.program-quicklinks-label {
  font-weight: 700;
  color: #111827;
  margin-right: 0.25rem;
}
.program-quicklinks a {
  color: #0969da;
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 2px;
}
.program-quicklinks a:hover {
  color: #0550ae;
}
.program-timezone-note {
  margin: 0 0 1rem 0;
  font-size: 0.96rem;
  color: #4b5563;
  line-height: 1.55;
}
.program-legend {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 1rem;
  margin: 0 0 1.25rem 0;
  padding: 0.65rem 1rem;
  border: 1px solid #d0d7de;
  border-radius: 12px;
  background: #ffffff;
  font-size: 0.95rem;
  color: #374151;
}
.program-legend-label {
  font-weight: 700;
  color: #111827;
  margin-right: 0.15rem;
}
.program-legend-list {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.65rem 1.15rem;
  margin: 0;
  padding: 0;
  list-style: none;
}
.program-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
}
.program-legend-swatch {
  display: inline-block;
  width: 1rem;
  height: 1rem;
  border-radius: 4px;
  flex-shrink: 0;
  border: 1px solid rgba(0, 0, 0, 0.12);
}
.program-legend-swatch-student {
  background: #e8f2ff;
  border-top: 3px solid #5b9bd5;
  border-left-color: #c7ddff;
  border-right-color: #c7ddff;
  border-bottom-color: #c7ddff;
}
.program-legend-swatch-faculty {
  background: #f5f3ff;
  border-top: 3px solid #7c3aed;
  border-left-color: #ddd6fe;
  border-right-color: #ddd6fe;
  border-bottom-color: #ddd6fe;
}
.program-legend-swatch-both {
  background: #ecfdf5;
  border-top: 3px solid #059669;
  border-left-color: #a7f3d0;
  border-right-color: #a7f3d0;
  border-bottom-color: #a7f3d0;
}
.program-card.program-session-student:not(.program-card-break) {
  border-top: 4px solid #5b9bd5;
  background: #e8f2ff;
}
.program-card.program-session-student:not(.program-card-break):hover {
  border-top-color: #4a8bc8;
  border-left-color: #8cb4ff;
  border-right-color: #8cb4ff;
  border-bottom-color: #8cb4ff;
  background: #d6e8ff;
}
.program-card.program-session-faculty:not(.program-card-break) {
  border-top: 4px solid #7c3aed;
  background: #f5f3ff;
}
.program-card.program-session-faculty:not(.program-card-break):hover {
  border-top-color: #7c3aed;
  border-left-color: #8cb4ff;
  border-right-color: #8cb4ff;
  border-bottom-color: #8cb4ff;
  background: #ede9fe;
}
.program-card.program-session-both:not(.program-card-break) {
  border-top: 4px solid #059669;
  background: #ecfdf5;
}
.program-card.program-session-both:not(.program-card-break):hover {
  border-top-color: #059669;
  border-left-color: #8cb4ff;
  border-right-color: #8cb4ff;
  border-bottom-color: #8cb4ff;
  background: #d1fae5;
}
.program-card.program-highlight.program-session-student:not(.program-card-break),
.program-card.program-highlight.program-session-faculty:not(.program-card-break),
.program-card.program-highlight.program-session-both:not(.program-card-break) {
  border-left: 4px solid #0969da;
}
.program-card.program-highlight.program-session-student:not(.program-card-break):hover,
.program-card.program-highlight.program-session-faculty:not(.program-card-break):hover,
.program-card.program-highlight.program-session-both:not(.program-card-break):hover {
  border-left-color: #54a0ff;
}
</style>

{{ site.data.schedule.intro }}
<p class="program-timezone-note">{{ site.data.schedule.timezone_note }}</p>

<div class="program-legend" role="group" aria-label="Session type legend">
  <span class="program-legend-label">Session types</span>
  <ul class="program-legend-list">
{% for item in site.data.schedule.legend %}
    <li class="program-legend-item">
      <span class="program-legend-swatch program-legend-swatch-{{ item.track }}" aria-hidden="true"></span>
      <span>{{ item.label }}</span>
    </li>
{% endfor %}
  </ul>
</div>

<nav class="program-quicklinks" aria-label="Jump to conference day">
  <span class="program-quicklinks-label">Jump to:</span>
{% for day in site.data.schedule.days %}
  {% if forloop.first %}
  <a href="#{{ day.anchor_id }}">{{ day.nav_label }}</a>
  {% else %}
  <span aria-hidden="true">·</span>
  <a href="#{{ day.anchor_id }}">{{ day.nav_label }}</a>
  {% endif %}
{% endfor %}
</nav>

{% for day in site.data.schedule.days %}
<div class="program-day program-day-tone-{{ day.tone }}" id="{{ day.anchor_id }}">
<h2>{{ day.heading }}</h2>
{% assign sorted_events = day.events | sort: 'time_start' %}
{% for event in sorted_events %}
<div class="program-card{% if event.highlight %} program-highlight{% endif %}{% if event.break_card %} program-card-break{% endif %}{% if event.session_track %} program-session-{{ event.session_track }}{% endif %}" id="{{ event.id }}"><div class="program-card-share">
<button type="button" class="program-share-btn" aria-label="Share link to this session"><img class="program-share-icon" src="{{ '/images/share-icon.svg' | relative_url }}" width="20" height="20" alt=""></button>
</div>

<div class="program-time">{{ event.time }}</div>
{% if event.room %}
<div class="program-room">Room: {{ event.room }}</div>
{% endif %}
<div class="program-event">{{ event.description_html | strip }}</div>
</div>
{% endfor %}
</div>
{% endfor %}

<script>
(function () {
  function buildShareUrl(btn) {
    var base = window.location.href.split("#")[0];
    var card = btn.closest(".program-card");
    if (card && card.id) return base + "#" + card.id;
    if (btn.closest(".program-page-share")) return base + "#admi-program";
    return base;
  }
  function shareTitle(btn) {
    var card = btn.closest(".program-card");
    if (!card) return "ADMI 2026 Symposium Program";
    var t = card.querySelector(".program-time");
    return t ? t.textContent.trim() + " — ADMI 2026 Program" : "ADMI 2026 Symposium Program";
  }
  function copyWithExecCommand(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.cssText = "position:fixed;left:-9999px;top:0;opacity:0";
    document.body.appendChild(ta);
    ta.select();
    ta.setSelectionRange(0, text.length);
    var ok = false;
    try {
      ok = document.execCommand("copy");
    } catch (e) {}
    document.body.removeChild(ta);
    return ok;
  }
  function copyUrlToClipboard(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).catch(function () {
        return copyWithExecCommand(text) ? Promise.resolve() : Promise.reject();
      });
    }
    return copyWithExecCommand(text) ? Promise.resolve() : Promise.reject();
  }
  function showCopiedFeedback(btn) {
    var prev = btn.getAttribute("aria-label");
    btn.setAttribute("aria-label", "Link copied to clipboard");
    setTimeout(function () {
      btn.setAttribute("aria-label", prev || "Share");
    }, 2000);
  }
  document.querySelectorAll(".program-share-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var url = buildShareUrl(btn);
      var title = shareTitle(btn);
      if (navigator.share) {
        navigator
          .share({ title: title, url: url })
          .catch(function () {
            copyUrlToClipboard(url)
              .then(function () {
                showCopiedFeedback(btn);
              })
              .catch(function () {
                window.prompt("Copy this link:", url);
              });
          });
        return;
      }
      copyUrlToClipboard(url)
        .then(function () {
          showCopiedFeedback(btn);
        })
        .catch(function () {
          window.prompt("Copy this link:", url);
        });
    });
  });
})();
</script>
