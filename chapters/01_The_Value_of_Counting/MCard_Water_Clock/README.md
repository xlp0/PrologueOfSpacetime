---
title: "MCard Water Clock: Interactive Demonstration"
date: 2026-09-27
tags: [MCard, Water-Clock, Simulation, Interactive, JavaScript, Chapter-01]
type: note
sources:
  - chapters/01_The_Value_of_Counting/README.md
  - chapters/01_The_Value_of_Counting/MCard_Water_Clock/locales.json
  - chapters/01_The_Value_of_Counting/MCard_Water_Clock/i18n.js
  - chapters/01_The_Value_of_Counting/MCard_Water_Clock/water_clock.js
  - chapters/01_The_Value_of_Counting/MCard_Water_Clock/index.html
status: stable
liberal_art: Quadrivium-Arithmetic
---

# MCard Water Clock: Interactive Demonstration

> *"Observation costs energy. Count too fast, and you burn. Count too slow, and you drown."*

This directory houses the **MCard Water Clock** implementation stack—an interactive analog-to-digital converter (ADC) and Maxwellian Demon simulator realizing **Station 01 (The Inventory Station)** of Chapter 01.

---

## 1. Stack Components

1. **`locales.json`**: The Single Source of Truth (SSOT) external linguistic repository:
   * 🇮🇩 **Indonesian (`id`)**: Bahasa Indonesia
   * 🕉️ **Sanskrit (`sa`)**: संस्कृतम् (Bali Agamic tradition)
   * 🇬🇧 **English (`en`)**: English
   * 🇹🇼 **Orthodox Chinese (`zh-TW`)**: 正體中文
   * Decouples all natural-language statements, Elder dialogues, thermodynamic telemetry alerts, and pedagogical hints from executable logic.
2. **`i18n.js`**: Standardized, reusable, isomorphic Internationalization (i18n) module:
   * Dynamically loads linguistic statements from `locales.json` via HTTP `fetch` in browsers or synchronous `fs` in Node.js.
   * Provides dot-notation key lookup (`t('header.mainTitle')`) and parameter interpolation (`t('logs.milestone', { count: 10 })`).
   * Provides automatic DOM localization bindings (`applyToDOM()`) and language switcher event listeners (`bindLanguageSwitcher()`).
   * Emits change events (`onLocaleChange`) for reactive UI updates without touching core game loops.
3. **`index.html`**: A retro MCard-style browser application featuring:
   * Real-time water accumulation bar (Bamboo reservoir).
   * Monotonic counter display ($n \in \mathbb{N}$).
   * Tactile manual capture trigger (`[ Catch the Drop ]` button).
   * Thermodynamic feedback display: Energy remaining, Entropy generated, and Laminar vs. Turbulent flow indicator.
   * Standardized i18n multilingual switcher (🇮🇩 Bahasa Indonesia / 🕉️ संस्कृतम् / 🇬🇧 English / 🇹🇼 正體中文).
   * Pure Web Audio API procedural sound synthesis (no external assets required).
4. **`water_clock.js`**: Node.js executable module implementing the underlying `MaxwellsDemon` class, delta-timing logic, thermodynamic dissipation equations, and multilingual CLI output driven by `i18n.js`.

---

## 2. How to Run

### Option A: Browser (Interactive Multilingual UI)
Serve or open `index.html` in any standard web browser:
```bash
# Serve locally via Python or your preferred dev server
python3 -m http.server 8000
# Navigate to: http://localhost:8000/chapters/01_The_Value_of_Counting/MCard_Water_Clock/
```
Click the language switch buttons at the top to toggle instantly between **🇮🇩 Bahasa Indonesia**, **🕉️ संस्कृतम्**, **🇬🇧 English**, and **🇹🇼 正體中文**!

### Option B: Node.js CLI (Simulation Script with i18n)
Run the automated Maxwell's Demon simulation script with your preferred locale:
```bash
# Default (Indonesian)
node chapters/01_The_Value_of_Counting/MCard_Water_Clock/water_clock.js id

# Sanskrit (Bali tradition)
node chapters/01_The_Value_of_Counting/MCard_Water_Clock/water_clock.js sa

# English
node chapters/01_The_Value_of_Counting/MCard_Water_Clock/water_clock.js en

# Orthodox Chinese (zh-TW or zh)
node chapters/01_The_Value_of_Counting/MCard_Water_Clock/water_clock.js zh-TW
```

---

## 3. Extending the i18n Standard (Adding New Languages)

Because linguistic statements are externalized into `locales.json`, application code remains 100% stable:
1. Open [`locales.json`](locales.json).
2. Add your new language key (e.g., `ja` for Japanese or `de` for German):
   ```json
   {
     "ja": {
       "meta": { "code": "ja", "name": "日本語", "flag": "🇯🇵" },
       "header": { "mainTitle": "MCard 水鐘：第01工位（竹節滴漏）", ... },
       ...
     }
   }
   ```
3. In `index.html`, add `<button class="lang-btn" data-lang="ja" onclick="switchLanguage('ja')">🇯🇵 日本語</button>`.
No changes to `water_clock.js`, physics simulation, or audio synthesizers are required!

---

## 3. Pedagogical Mechanics & GASing Gameplay

* **Laminar Resonance ($\Delta t \in [500\text{ms}, 1500\text{ms}]$)**: Clicking in rhythm with the droplet formation consumes minimal energy ($-5\%$ per click) and stabilizes entropy ($\Delta H < 0$).
* **Turbulent Friction ($\Delta t < 200\text{ms}$)**: Clicking too rapidly creates friction, consuming $20\%$ energy per click and generating $+15\%$ heat, simulating sensor saturation and cognitive burnout.
* **Under-Sampling ($\Delta t > 2000\text{ms}$)**: Clicking too slowly causes the bamboo reservoir to overflow unmeasured.
* **Failure State**: When energy hits $0\%$ or entropy exceeds $50\%$, the Demon overheats, representing the collapse of local observational sovereignty into chaotic noise.

---

## 4. 🇮🇩 Panduan Bermain GASing untuk Pemula (Gampang, Asyik, Menyenangkan)

1. **Gampang Dimulai**:
   * Buka berkas `index.html` langsung di peramban favorit Anda (Chrome, Safari, Firefox). Tanpa perlu instalasi rumit!
   * Klik tombol **"Mulai Aliran / Start Flow"**.
2. **Asyik Dimainkan**:
   * Perhatikan animasi tetesan air dari pancuran bambu ke wadah penampung.
   * Setiap kali tetesan terbentuk, klik tombol **"Tangkap Tetesan / Catch Drop"** untuk mencatat 1 hitungan (*MCard*).
   * **Dengarkan Suaranya**: Simulator dilengkapi sintesis suara Web Audio:
     * 💧 Denting renyah tetesan air (*plink*) saat Anda memencet dalam ritme tenang (*laminar*).
     * 🔔 Denting gamelan merdu saat Anda mencapai kelipatan 10 tetesan!
     * ♨️ Desisan uap panas jika Anda memencet terlalu cepat membabi-buta (*turbulent friction*).
3. **Menyenangkan Diresapi**:
   * Amati indikator termometer Entropi dan Energi.
   * Menemukan tempo yang tepat mengajarkan Anda seni **ketenangan kognitif** (*Flow State*): tidak panik, tidak lamban, tetapi mengalir selaras dengan alam semesta. Tetesan yang Anda kumpulkan di sini adalah modal dasar yang kelak menjadi token energi di Bab 05!
