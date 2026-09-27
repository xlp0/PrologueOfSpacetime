---
title: "HyperCard Water Clock: Interactive Demonstration"
date: 2026-09-27
tags: [HyperCard, Water-Clock, Simulation, Interactive, JavaScript, Chapter-01]
type: note
sources:
  - chapters/01_The_Value_of_Counting/README.md
  - chapters/01_The_Value_of_Counting/HyperCard_Water_Clock/water_clock.js
  - chapters/01_The_Value_of_Counting/HyperCard_Water_Clock/index.html
status: stable
liberal_art: Quadrivium-Arithmetic
---

# HyperCard Water Clock: Interactive Demonstration

> *"Observation costs energy. Count too fast, and you burn. Count too slow, and you drown."*

This directory houses the **HyperCard Water Clock** implementation stack—an interactive analog-to-digital converter (ADC) and Maxwellian Demon simulator realizing **Station 01 (The Inventory Station)** of Chapter 01.

---

## 1. Stack Components

1. **`index.html`**: A retro HyperCard-style browser application featuring:
   * Real-time water accumulation bar (Bamboo reservoir).
   * Monotonic counter display ($n \in \mathbb{N}$).
   * Tactile manual capture trigger (`[ Catch the Drop ]` button).
   * Thermodynamic feedback display: Energy remaining, Entropy generated, and Laminar vs. Turbulent flow indicator.
2. **`water_clock.js`**: Node.js executable module implementing the underlying `MaxwellsDemon` class, delta-timing logic, and thermodynamic dissipation equations.

---

## 2. How to Run

### Option A: Browser (Interactive UI)
Simply open `index.html` in any standard web browser:
```bash
open chapters/01_The_Value_of_Counting/HyperCard_Water_Clock/index.html
```

### Option B: Node.js CLI (Simulation Script)
Run the automated Maxwell's Demon simulation script:
```bash
node chapters/01_The_Value_of_Counting/HyperCard_Water_Clock/water_clock.js
```

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
