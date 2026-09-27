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

## 4. Pedagogical Mechanics & GASing Gameplay

* **Laminar Resonance ($\Delta t \in [500\text{ms}, 1500\text{ms}]$)**: Clicking in rhythm with droplet formation consumes minimal energy ($-5\%$ per click) and stabilizes entropy ($\Delta H < 0$).
* **Turbulent Friction ($\Delta t < 200\text{ms}$)**: Clicking too rapidly creates friction, consuming $20\%$ energy per click and generating $+15\%$ heat, simulating sensor saturation and cognitive burnout.
* **Under-Sampling ($\Delta t > 2000\text{ms}$)**: Clicking too slowly causes the bamboo reservoir to overflow unmeasured.
* **Failure State**: When energy hits $0\%$ or entropy exceeds $50\%$, the Demon overheats, representing the collapse of local observational sovereignty into chaotic noise.

---

## 5. Beginner's GASing Gameplay Guide (Easy, Fun, Enjoyable)

1. **Easy to Start (*Gampang*)**:
   * Open `index.html` directly in any modern web browser (Chrome, Safari, Firefox). No complex dependencies or installation steps required!
   * Click the **"Start Flow"** button.
2. **Fun to Play (*Asyik*)**:
   * Observe the water droplet accumulation animation flowing from the bamboo spout into the reservoir.
   * Each time a droplet forms, click the **"Catch Drop"** button to record one discrete count (*MCard*).
   * **Listen to the Synthesized Audio**: The simulator incorporates real-time Web Audio API synthesis:
     * 💧 A crisp water droplet *plink* when clicked within a calm, resonant rhythm (*laminar* flow).
     * 🔔 A resonant gamelan chime upon reaching multiples of 10 droplets!
     * ♨️ A steamy hiss if clicking too rapidly (*turbulent friction*).
3. **Enjoyable Mastery (*Menyenangkan*)**:
   * Monitor the Entropy and Energy telemetry gauges.
   * Finding the steady tempo teaches the art of **cognitive flow state**: neither frantic nor sluggish, flowing in harmony with physical rate limits. The droplets collected here serve as foundational accounting records that evolve into energy tokens in Chapter 05!

