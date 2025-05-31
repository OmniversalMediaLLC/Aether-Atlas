---
layout: default
title: Aether Atlas
---

<img src="{{ '/assets/images/aether-atlas-banner.png' | relative_url }}" alt="Aether Atlas Banner" class="banner-img" />

# Aether Atlas: Domain Control Panel

Welcome to the official Atlas for **Omniversal Media’s** web of domains.  
This site serves as a central interface for viewing, tracking, and managing our digital territory.

From registrar records to active infrastructure files, this is your **living dashboard** into the Dominascriptorum.

---

## 📚 Featured Writings

{% assign featured_article = site.articles | where: "featured", true | first %}
{% if featured_article %}
<div style="display: flex; align-items: center; gap: 1rem; background: #111; padding: 1rem; border-radius: 8px; border: 1px solid #333;">
  <img src="https://onebucket.omniversal.cloud/symbols/reincarnated2resist_emblem/Reincarnated_Hawk_Emblem.png" alt="Reincarnated Emblem" style="width: 80px; height: auto; border-radius: 6px;" />
  <div>
    <a href="{{ featured_article.url | relative_url }}" style="font-size: 1.2rem; font-weight: bold; color: #fff;">
      {{ featured_article.title }}
    </a><br />
    <span style="color: #bbb;">{{ featured_article.excerpt | strip_html | truncate: 220 }}</span>
  </div>
</div>
{% endif %}

---

## 📖 All Articles

{% include articles_list.html %}

---

## 🌐 About This Atlas

This interface was built using:

- [Jekyll](https://jekyllrb.com/) + GitHub Pages  
- [Cloudflare DNS](https://dash.cloudflare.com) + Custom Domain  
- Markdown, YAML, and your friendly AI assistant

We will be expanding it soon with:

- Live search and table integration  
- Domain status dashboards  
- Auto-generated “Coming Soon” sites  
- SEO-priming pages for every domain

---

## 🧭 Quick Links

- [Omniversal Media](https://omniversalmedia.org)
- [Reincarnated Store](https://reincarnated.store)
- [Aether Core](https://omniversalaether.net)
- [Omniversal News Network](https://omniversal.news)

---

## 🤝 Contributors

Maintained by **Ethan Womack** (aka Hawk Eye)  
Visit [Reincarnated2Resist](https://reincarnated2resist.com)

---

_Last updated: May 31, 2025_


