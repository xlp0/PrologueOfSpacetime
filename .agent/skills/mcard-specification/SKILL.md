---
name: mcard-specification
description: Standardizes MCard (Monadic Card) nomenclature, HoTT Σ-type semantics, and multilingual representations across English, Indonesian, and Orthodox Chinese locales. Mandates translation of Hypercard as "超媒體卡牌" and MCard as "單子牌", strictly prohibiting "超卡".
---

# MCard Specification & Multilingual Terminology Standard

> **The Sovereign Rule**: In the *Prologue of Spacetime*, all cards and computational stacks previously referred to as *HyperCard* or *超卡* are strictly unified as **`MCard`** (Monadic Card / 單子牌) across English (`en`), Indonesian (`id`), and Orthodox Chinese (`zh-TW`). Whenever *Hypercard* / *HyperCard* is translated into Chinese, it **MUST ALWAYS** be translated as **「超媒體卡牌」** (Hypermedia Card), and the literal mistranslation 「超卡」 is strictly prohibited.

---

## 1. Multilingual Terminology Standard

| Locale | Canonical Form | Contextual UI / Stack Form | Strictly Forbidden / Deprecated |
|:---|:---|:---|:---|
| **English (`en`)** | `MCard` | `MCard Water Clock`, `MCard Stack`, `MCard Ledger` | `HyperCard` / `Hypercard` *(Permitted only when citing 1987 Bill Atkinson software)* |
| **Indonesian (`id`)** | `MCard` | `Jam Air MCard`, `Buku Kas MCard`, `Kartu Monadik MCard` | `Pancuran Jam Air` *(unanchored)*, `HyperCard` |
| **Orthodox Chinese (`zh-TW`)** | `MCard` / `單子牌` | `MCard 水鐘`, `MCard 帳本`, `單子牌` | ❌ **`超卡`** *(Strictly prohibited; Hypercard must always be translated as 「超媒體卡牌」)* |

### 1.1 Hypercard Translation Standard & The Proscription of "超卡"
- **Mandatory Translation**: Whenever *Hypercard* or *HyperCard* (referring to Bill Atkinson's 1987 software or the hypermedia card paradigm) is translated into Chinese, it **MUST ALWAYS** be translated as **「超媒體卡牌」** (Hypermedia Card).
- **The Proscription of "超卡"**: Machine translation historically rendered Apple's 1987 "HyperCard" literally as "超卡" (Super/Hyper Card). Any appearance of "超卡" in Chinese docs, comments, UI strings, or logs is a critical lint violation and is strictly forbidden.
- **Architectural Distinction**:
  - **`HyperCard` $\to$ 「超媒體卡牌」**: The historical 1987 hypermedia software and paradigm.
  - **`MCard` $\to$ 「單子牌」**: The foundational computational atom of *Prologue of Spacetime*, grounded in Leibniz's *Monadology*, Wadler's monadic computing, and Homotopy Type Theory $\Sigma$-types.
- **Enforcement**: Any appearance of "超卡" must be eradicated and replaced with either `超媒體卡牌` (when referring to Hypercard) or `MCard` / `單子牌` (when referring to the computational atom).

---

## 2. Theoretical & Mathematical Foundations

### 2.1 Homotopy Type Theory (HoTT) Grounding
An `MCard` represents the irreducible existential witness in the **MVP Cards Triad**:

$$\text{MCard} \equiv \sum_{x: A} B(x)$$

* **$\Sigma$-Type (Dependent Sum)**: The magnitude component ($M$), capturing raw fact-as-truth.
* **Existential Pair**: An MCard instance is a dependent pair $\langle a, b \rangle$, where $a: A$ is the basis index (or Content Identifier `CID`) and $b: B(a)$ is the payload evidence.
* **Windowless Monad**: An MCard is immutable, self-contained, and content-addressed via cryptographic Merkle-DAG hashes (e.g. SHA-256 / IPFS CIDv1 `bafy...`).

### 2.2 The Representation Engine (Tier 1 — Name)
In the D&D Representation Engine loop:
* **Tier 1 — Name (MCard)**: Distinction through [[Directionality]] (*"Cat" $\neq$ "Act"*). The card that names an entity is the MCard.
* **Tier 2 — Verb (PCard)**: Computation and paths ($\Pi$-types, functions, transformations).
* **Tier 3 — Proof (VCard)**: Verification and boundaries ($\text{Id}$-types, conservation laws, Hoare triples).

---

## 3. UI, Simulation & Codebase Guidelines

### 3.1 `locales.json` Standards
When internationalizing applications (such as Chapter 01's Water Clock simulation), enforce the following key bindings:

```json
{
  "id": {
    "header": { "mainTitle": "Jam Air MCard: Stasiun 01" },
    "counter": { "title": "Jumlah Tetesan Terhitung (MCard)" },
    "logs": { "title": "BUKU KAS MCARD (IMMUTABLE LOG):" }
  },
  "en": {
    "header": { "mainTitle": "MCard Water Clock: Station 01" },
    "counter": { "title": "Counted Droplets (MCard Ledger)" },
    "logs": { "title": "MCARD IMMUTABLE LEDGER:" }
  },
  "zh-TW": {
    "header": { "mainTitle": "MCard 水鐘：第01工位（竹節滴漏）" },
    "counter": { "title": "已驗證水滴總數（MCard 帳本）" },
    "logs": { "title": "MCARD 不可變帳本記錄：" }
  }
}
```

### 3.2 HTML & UI Markup
- Document Title: `<title>Chapter 01: MCard Water Clock / Jam Air MCard / MCard 水鐘</title>`
- Stack Containers: `<div class="card-stack"> <!-- MCard Stack Container -->`
- Badges: `STASIUN 01 (INVENTARIS MCARD)` / `STATION 01 (MCARD INVENTORY)` / `第 01 工位（記憶庫存 MCARD）`

### 3.3 CLI & Event Logs
- Simulation ticks emitted to console or ledger MUST prefix card records with `[MCard #{count}]`:
  ```text
  [MCard #1] Δt: 1042ms | E: 95% | H: 0% | CID: bafy...
  ```

---

## 4. Agent Audit & Verification Protocol

When creating or modifying chapters, simulations, docs, or UI components:
1. **Search for Forbidden Terms**:
   - Run regex checks for `超卡`, `Hypercard`, and `HyperCard` (excluding historical 1987 citations).
2. **Verify Locale Alignments**:
   - Ensure English uses `MCard Water Clock`.
   - Ensure Indonesian uses `Jam Air MCard` or `MCard`.
   - Ensure Orthodox Chinese uses `MCard 水鐘` or `MCard`.
3. **Verify Formal Consistency**:
   - In architectural docs, cross-link to [[docs/concepts/MCard.md|MCard (Monadic Card)]] and [[docs/narrative/MVP Cards Design Rationale.md|MVP Cards Design Rationale]].
