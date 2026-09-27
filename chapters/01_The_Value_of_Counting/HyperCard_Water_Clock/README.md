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

## 3. Pedagogical Mechanics

* **Laminar Resonance ($\Delta t \in [500\text{ms}, 1500\text{ms}]$)**: Clicking in rhythm with the droplet formation consumes minimal energy ($-5\%$ per click) and stabilizes entropy ($\Delta H < 0$).
* **Turbulent Friction ($\Delta t < 200\text{ms}$)**: Clicking too rapidly creates friction, consuming $20\%$ energy per click and generating $+15\%$ heat, simulating sensor saturation and cognitive burnout.
* **Under-Sampling ($\Delta t > 2000\text{ms}$)**: Clicking too slowly causes the bamboo reservoir to overflow unmeasured.
* **Failure State**: When energy hits $0\%$ or entropy exceeds $50\%$, the Demon overheats, representing the collapse of local observational sovereignty into chaotic noise.
