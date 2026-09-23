---
title: 'IT Del & SUD Project Catalog and Comparative Topic Analysis'
date: 2026-09-23
tags: [IT-Del, SUD, Teaching, Project-Catalog, Topic-Analysis, Comparative-Study]
type: synthesis
sources: [raw/transcripts/itdel_whatsapp/registry.json]
status: stable
liberal_art: Quadrivium-Geometry
---

# IT Del & SUD Project Catalog and Comparative Topic Analysis

> A comprehensive synthesis and cross-comparative deconstruction of **57 software, IoT, and simulation projects** created by **29 students** across **Institut Teknologi Del (IT Del)** and **SMA Unggul Del (SUD)** during the Conversational Programming Workshop.  
> Includes complete individual English project profiles, technical breakdowns, institutional comparisons, and topic clustering across the **Seven Liberal Arts**.

## 1. Executive Summary & Macro Metrics

| Metric | Count | Observations |
| :--- | :---: | :--- |
| **Total Projects** | **57** | Spanning interactive 3D WebGL games, IoT telemetry, campus automation, and language edtech |
| **Total Creators / Students** | **29** | 27 from Institut Teknologi Del (Undergraduate), 2 from SMA Unggul Del (High School) |
| **Multi-Project Creators** | **15** | Wendy Simanjuntak (7), Deddy Daniel Situmeang (5), Briant Sinaga (4), Nakula Nathanael Gultom (4), Rahel Sendler Sianturi (3), etc. |
| **Live Deployment Rate** | **14 / 57 (24.6%)** | 8 students have verified live demos or public GitHub repositories |
| **Dataset Exports** | **2 CSVs** | `student_projects.csv` (18 columns) & `student_summary.csv` (10 columns) |

--- 

## 2. Comparative Topic & Domain Analysis

The 57 projects display distinct clusters of engineering intent, ranging from localized campus infrastructure solutions to complex 3D WebGL computer graphics and embedded hardware.

### 2.1 Category Breakdown

| Category / Archetype | Count | Share (%) | Primary Focus & Archetypal Examples |
| :--- | :---: | :---: | :--- |
| **Interactive Game** | 32 | 56.1% | Action RPGs, Endless Runners, 3D WebGL simulations, Tactical sports, Detective social deduction |
| **Educational Tool** | 13 | 22.8% | Grammar & phrase parsers, Duolingo-style language games, math drills, 3D human brain visualizers |
| **Web Application** | 4 | 7.0% | Real-time Computer Vision fire detection, personal wealth budgeting, C++ coding assessments |
| **IoT & Hardware** | 4 | 7.0% | ESP32-C3 microcontroller firmware, Wi-Fi sensor servers, DHT11 telemetry, physical interactive games |
| **Productivity Tool** | 2 | 3.5% | Campus dormitory maintenance ticketing systems, developer utility playgrounds (Regex/JSON) |
| **Simulation & Telemetry** | 2 | 3.5% | 38-province national digital twin telemetry, multi-trophic ecosystem equilibrium models |

### 2.2 Functional Topic Clusters

Beyond top-level categories, the projects naturally group into **six functional topic clusters**:

1. **High-Performance 3D WebGL & Action Gaming (14 Projects)**:
   - **Three.js Graphics**: *Ghost of Tsushima 3D* (Deddy), *Subway Surfers 3D* (Deddy & Yonathan), *Brain Runner 3D* (Deddy), *Culinary Bistro 3D* (Immanuel), *Valo Hoops 2K* (Nakula), *Temple Run 3D* (Titania), *Syntax Island RPG* (Salsalina), *Library 3D Sorting* (Mayrinkha).
   - **Combat & Physics**: *Brawl Legends 2D* (Deddy), *Point Blank Tactical* (Louis Damas), *Atheria: Dimensional Paradox* (Mikael), *Late for Class! Canvas Runner* (Josephine Ruth), *The Floor is Lava* (Rahel), *Last Hope Zombie Bastion* (Nakula).
   - *Observation*: Students leveraged WebGL and HTML5 Canvas to implement real-time hitbox physics, camera projection matrices, and particle systems directly inside standard desktop and mobile browsers without requiring native game engines.

2. **Campus Operational Infrastructure & Smart Campus Living (6 Projects)**:
   - *RoomCheck IT Del* (Wendy): Dormitory maintenance ticketing connecting residents with the facilities division.
   - *SpotFinder IT Del* (Wendy): Real-time study desk availability mapping across campus libraries, gazebos, and labs.
   - *Teman Seperjalanan IT Del* (Wendy): Late-night student safe walking companion and ride-sharing coordinator.
   - *TugasKu* (Dominggo): Client-side academic homework manager and deadline calendar.
   - *Silangit Flight Board* (Claudia): Real-time flight information display system (FIDS) for the local Lake Toba airport.
   - *Kasir Simamora* (Stephen): Digital POS checkout and retail register system tailored for local campus kiosks.
   - *Observation*: Driven almost exclusively by **Sistem Informasi (SI)** students addressing immediate lived friction points of student boarding life at Laguboti.

3. **Language, Syntax & Medical EdTech (7 Projects)**:
   - *SintaksisFrasa* (Nathania Pelita): Grammar parsing platform for Indonesian phrase taxonomy under EYD rules.
   - *KataMaster* (Wendy): Duolingo-inspired language learning suite with Text-to-Speech audio synthesis.
   - *LastLetter* (Nathania Pelita): Minecraft-themed chain word association spelling game.
   - *Word Chain* (Annisa): Rapid-fire vocabulary categorization game.
   - *VocabQuest* (Diva Martauli): Multi-mode English vocabulary quest (idioms, antonyms, unscrambles).
   - *NeuroLearn* (Salsalina): Interactive 3D human brain anatomy visualizer with clickable lobe pathology.
   - *EduQuest* (Immanuel): Structured high-school STEM question bank and diagnostic assessment engine.

4. **Mathematical Cognition & Logic Puzzles (8 Projects)**:
   - *Mathemagica* (Deddy): 5-mode math logic suite (Make 24, Equation Grid, Icon Algebra, Number Patterns).
   - *PolaMatika* (Wendy): Mathematical sequence analysis, Fibonacci progressions, and 3x3 matrix logic.
   - *Math Adventure* (Wendy): Turn-based arithmetic combat RPG in the fantasy Realm of Numeria.
   - *Mathematical Penalty Shootout* (Jose Rafael): Arithmetic speed challenges gating penalty kick accuracy.
   - *Penalty Shootout Career* (Farel): High-stakes sports simulation career mode.
   - *Cheerful Addition Adventure* (Annisa): Multi-tiered elementary arithmetic game.
   - *The Number Mystery* (Honey): Terminal-based numeric deduction and clue elimination.
   - *GameHub 3-in-1* (Claudia): Sliding tile puzzle, language quiz, and logic riddles.

5. **Embedded Systems, Computer Vision & Physical Computing (6 Projects)**:
   - *Blink LED ESP32-C3* (Nakula): Embedded GPIO register control and hardware timer interrupts.
   - *Web LED Control & DHT11 Monitor* (Nakula): Wi-Fi AP asynchronous web server streaming ambient sensor telemetry.
   - *FlameVision AI* (Diva Aurel): Real-time computer vision fire detection using Python, OpenCV, and dual color-space segmentation.
   - *MindCanvas Second Brain* (Briant): Dynamic knowledge graph with interactive node-link network canvas.
   - *ASAH C++* (Rahel): Algorithmic C++ diagnostic assessment and memory pointer debugger.
   - *CodeCraft* (Briant): Developer Swiss-knife featuring client-side regex testers, hash generators, and formatters.

6. **Macro & Micro Scale Simulation and Telemetry (2 Projects)**:
   - *Nusantara Digital Twin* (Stephen Joy Marvel): Interactive national digital twin aggregating socioeconomic and demographic telemetry across all 38 Indonesian provinces with a What-If 2045 policy sandbox.
   - *Eco-Valley* (Nadine): Ecological balance and multi-trophic food chain simulation modeling predator-prey dynamics.

### 2.3 Cross-Institutional Comparison: IT Del vs. SMA Unggul Del

| Dimension | Institut Teknologi Del (IT Del) | SMA Unggul Del (SUD) |
| :--- | :--- | :--- |
| **Student Body** | 27 undergraduate engineering students (IF & SI) | 2 senior secondary students (Briant & Nathania Pelita) |
| **Project Volume** | 51 projects (avg. 1.89 projects / student) | 6 projects (avg. 3.00 projects / student) |
| **Dominant Themes** | Real-time 3D games, campus ticketing, POS systems, telemetry | Deep work productivity, knowledge graphs, linguistic syntax |
| **Gaming vs. Tooling** | **32 Games (62.7%)** vs. 19 Tools/Systems (37.3%) | **0 Pure Games (0%)** vs. **6 Tools/EdTech (100%)** |
| **Notable Trait** | High emphasis on visual flair, WebGL rendering, and campus life | High focus on cognitive tools, developer utilities, and EYD language mastery |

### 2.4 Cross-Departmental Comparison: Informatika (IF) vs. Sistem Informasi (SI)

| Dimension | Informatika (IF) | Sistem Informasi (SI) |
| :--- | :--- | :--- |
| **Student Count** | 9 registered students | 13 registered students |
| **Project Count** | 16 cataloged projects | 24 cataloged projects |
| **Technical Flavor** | Three.js WebGL 3D, Computer Vision (OpenCV), Math Logic | Enterprise workflows, FIDS, POS registers, Campus ticketing, Edutainment |
| **Key Showcases** | *FlameVision AI* (Diva Aurel), *Mathemagica* (Deddy), *Ghost of Tsushima* (Deddy) | *Nusantara Digital Twin* (Stephen), *RoomCheck* (Wendy), *SpotFinder* (Wendy) |

### 2.5 Seven Liberal Arts Alignment Matrix

Connecting projects to the classical **Trivium** (Mind & Communication) and **Quadrivium** (World & Architecture) per `AGENTS.md`:

| Classical Art | Mode & Definition | Projects Count | Representative Projects |
| :--- | :--- | :---: | :--- |
| **Quadrivium-Arithmetic** | Number, calculation, financial algorithms | **12** | *Mathemagica*, *FinPlan*, *PolaMatika*, *Smart Save Campus*, *Kasir Simamora* |
| **Trivium-Rhetoric** | Persuasion, expression, campus communication | **11** | *RoomCheck*, *SpotFinder*, *Werewolf*, *Deep-Sea Odyssey*, *Atheria* |
| **Quadrivium-Geometry** | Shape, spatial rendering, WebGL 3D, navigation | **10** | *Subway Surfers 3D*, *Ghost of Tsushima*, *Brain Runner 3D*, *Temple Run* |
| **Quadrivium-Music** | Rhythm, cadence, ambient soundscapes, timing | **8** | *FocusFlow*, *TypingFlow*, *Pomodoro Timer*, *VocabQuest*, *TugasKu* |
| **Trivium-Grammar** | Syntax, linguistic structures, rules, specifications | **8** | *SintaksisFrasa*, *LastLetter*, *Word Chain*, *GameHub 3-in-1*, *Library 3D* |
| **Quadrivium-Astronomy** | Motion, environment, sensor telemetry, digital twins | **6** | *Nusantara Digital Twin*, *ESP32-C3 Web Monitor*, *Blink LED*, *MindCanvas* |
| **Trivium-Logic** | Deduction, verification, elimination, code sandboxing | **2** | *CodeCraft Playground*, *The Number Mystery* |

--- 

## 3. Complete One-by-One English Project Catalog (57 Projects)

> Every project detailed sequentially with creator attribution, technical architecture, English explanation, objectives, and live repository links.

### 1. Pomodoro Focus & Study Timer
- **Original Title (Indonesian)**: *Podomoro Timer*
- **Creator (Who Did It)**: **Ananda Immanuel Siregar** — Institut Teknologi Del | NIM: 11S26024 (Informatika (IF)) | WA: `11S26024_Ananda.S_IF`
- **Category & Liberal Art**: `Educational Tool` · *Quadrivium-Music*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A web-based productivity application implementing the Pomodoro time-management technique, alternating 25-minute focused work intervals with 5-minute restorative breaks to optimize mental endurance and study discipline.
- **Key Objectives**: 1. Cultivate structured study habits and combat digital distractions. 2. Enhance sustained concentration through timed intervals. 3. Provide responsive, intuitive timer controls with ambient sound alerts.

### 2. Cheerful Addition Adventure
- **Original Title (Indonesian)**: *Petualangan Penjumlahan Ceria*
- **Creator (Who Did It)**: **Annisa Margareth Manalu** — Institut Teknologi Del (Informatika (IF)) | WA: `AnnisaManalu_S1_IF`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An interactive educational math game designed to make elementary arithmetic engaging and stress-free. Players solve random multiple-choice addition problems across three progressive difficulty tiers (Easy: 1-5, Medium: 1-10, Hard: 1-20). Features 3 lives, celebratory sound effects, and encouraging feedback.
- **Key Objectives**: 1. Strengthen mental arithmetic reflexes through timed challenges. 2. Overcome math anxiety through playful gamification. 3. Deliver lightweight, responsive educational gameplay across desktop and mobile devices.

### 3. Word Chain: Category Association Game
- **Original Title (Indonesian)**: *Kategori Berantai*
- **Creator (Who Did It)**: **Annisa Margareth Manalu** — Institut Teknologi Del (Informatika (IF)) | WA: `AnnisaManalu_S1_IF`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Grammar*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A casual, rapid-fire word association brain puzzle playable both digitally and socially. Players race against the clock to name thematic vocabulary sequentially through the alphabet from A to Z.
- **Key Objectives**: 1. Enhance mental sharpness, vocabulary recall, and quick reflexes under time pressure. 2. Foster group bonding and active communication through spontaneous gameplay. 3. Offer a flexible, zero-friction word game with configurable thematic categories.

### 4. FocusFlow: Deep Work & Ambient Audio Sanctuary
- **Original Title (Indonesian)**: *Focusflow : Deep Work & Ambient Sanctuary*
- **Creator (Who Did It)**: **Briant Sinaga** — SMA Unggul Del (SUD) (Sistem Informasi (SI)) | WA: `Briant Sinaga`
- **Category & Liberal Art**: `Educational Tool` · *Quadrivium-Music*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A distraction-free web productivity environment combining the Pomodoro technique with synthesized ambient audio generators (rain, waves, binaural café sounds) to induce and sustain cognitive flow states.
- **Key Objectives**: 1. Maximize productivity through seamless audio-visual focus triggers. 2. Provide customized soundscapes that block ambient auditory distractions. 3. Track daily focus sessions and deep-work consistency.

### 5. FinPlan: Smart Budgeting & Personal Wealth Accelerator
- **Original Title (Indonesian)**: *Finplan : Smart Budget & Wealth Accelerator*
- **Creator (Who Did It)**: **Briant Sinaga** — SMA Unggul Del (SUD) (Sistem Informasi (SI)) | WA: `Briant Sinaga`
- **Category & Liberal Art**: `Web Application` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A lightweight personal finance and budgeting web platform featuring automated expense categorization, visual financial allocation meters, and proactive savings milestone projections.
- **Key Objectives**: 1. Empower students and young professionals to take control of personal cash flows. 2. Prevent overspending through intuitive visual budget alerts. 3. Gamify savings milestones with clear projection trajectories.

### 6. MindCanvas: Second Brain & Dynamic Knowledge Graph
- **Original Title (Indonesian)**: *Mindcanvas : Second Brain & Knowledge Graph*
- **Creator (Who Did It)**: **Briant Sinaga** — SMA Unggul Del (SUD) (Sistem Informasi (SI)) | WA: `Briant Sinaga`
- **Category & Liberal Art**: `IoT & Hardware` · *Quadrivium-Astronomy*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An interconnected note-taking and knowledge representation workspace that visualizes notes, entities, and research insights as an interactive node-link graph with bidirectional hyperlinking.
- **Key Objectives**: 1. Bridge fragmented notes into a unified, visual knowledge network. 2. Accelerate cognitive synthesis and exploratory learning. 3. Provide local-first, low-latency graph navigation.

### 7. CodeCraft: Developer Swiss-Knife & Interactive Playground
- **Original Title (Indonesian)**: *Codecraft : Developer Swiss Knife & Playground*
- **Creator (Who Did It)**: **Briant Sinaga** — SMA Unggul Del (SUD) (Sistem Informasi (SI)) | WA: `Briant Sinaga`
- **Category & Liberal Art**: `Productivity Tool` · *Trivium-Logic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An all-in-one in-browser utility playground for software developers, featuring formatters (JSON, SQL, Markdown), regex testers, hash generators, and isolated HTML/CSS/JS prototyping sandboxes.
- **Key Objectives**: 1. Streamline daily engineering workflows into a single offline-capable web suite. 2. Eliminate reliance on ad-heavy external web tools. 3. Enable rapid experimentation and code snippet validation.

### 8. GameHub 3-in-1: Language Quiz, Sliding Puzzle & Logic Riddles
- **Original Title (Indonesian)**: *GameHub 3-in-1 (Kuis Bahasa, Puzzle Geser, Teka-Teki Seru)*
- **Creator (Who Did It)**: **Claudia Calista Aprilliana Sinaga** — Institut Teknologi Del | NIM: 12S26052 (Sistem Informasi (SI)) | WA: `12S26052_Claudia Sinaga`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Grammar*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A modern vanilla JS edutainment suite integrating three cognitive mini-games: linguistic vocabulary matching, spatial sliding grid puzzles, and analytical logic riddles with unified XP and daily challenges.
- **Key Objectives**: 1. Stimulate linguistic memory, spatial reasoning, and critical problem-solving. 2. Transform passive screen time into productive mental exercise through gamification. 3. Provide a responsive, zero-dependency offline web gaming experience.

### 9. Silangit Flight Board: Real-Time Airport Flight Information Display System (FIDS)
- **Original Title (Indonesian)**: *Silangit Flight Board (DTB)— Sistem Informasi Penerbangan Real-Time*
- **Creator (Who Did It)**: **Claudia Calista Aprilliana Sinaga** — Institut Teknologi Del | NIM: 12S26052 (Sistem Informasi (SI)) | WA: `12S26052_Claudia Sinaga`
- **Category & Liberal Art**: `Educational Tool` · *Trivium-Grammar*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A sleek, real-time Flight Information Display System (FIDS) web application tailored for Silangit International Airport (DTB), displaying scheduled departures, arrivals, gate assignments, and status updates.
- **Key Objectives**: 1. Streamline passenger flight tracking with clean visual schedules and status indicators. 2. Provide airport operators with a lightweight, high-performance web display board. 3. Ensure multi-device responsiveness across passenger smartphones and airport terminal monitors.

### 10. Mathemagica: Logic & Mental Math Puzzle Game
- **Original Title (Indonesian)**: *Mathemagica*
- **Creator (Who Did It)**: **Deddy Daniel Situmeang** — Institut Teknologi Del | NIM: 11S26037 (Informatika (IF)) | WA: `11S26037DanielsitumeangIF`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/ellesiddaniel/antigravity-DEL)
- **English Explanation & Description**: An interactive mathematical logic game featuring multiple structured puzzle modes (Make 24, Equation Grid, Icon Algebra, and Number Patterns) alongside a high-intensity Time Attack reflex mode.
- **Key Objectives**: 1. Sharpen numerical reasoning and analytical deduction through structured puzzle solving. 2. Train quick decision-making under time constraints. 3. Reinforce daily learning through streak bonuses, XP milestones, and achievement badges.

### 11. Subway Surfers: Urban Railway Endless Runner
- **Original Title (Indonesian)**: *Subway Surfers 3D - Ultimate Web Edition*
- **Creator (Who Did It)**: **Deddy Daniel Situmeang** — Institut Teknologi Del | NIM: 11S26037 (Informatika (IF)) | WA: `11S26037DanielsitumeangIF`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Geometry*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/ellesiddaniel/antigravity-DEL)
- **English Explanation & Description**: An endless runner web game where players navigate a young graffiti artist dodging subway cars, barriers, and pursuit along vibrant train tracks, collecting gold coins and high-score multipliers.
- **Key Objectives**: 1. Deliver fast-paced arcade entertainment with responsive lane jumping and sliding. 2. Implement score multipliers, power-ups, and daily word letter collection challenges. 3. Test hand-eye coordination and reflex agility under steadily increasing game speed.

### 12. Ghost of Tsushima: Way of the Samurai (3D Action RPG)
- **Original Title (Indonesian)**: *Ghost of Tsushima: Way of the Samurai*
- **Creator (Who Did It)**: **Deddy Daniel Situmeang** — Institut Teknologi Del | NIM: 11S26037 (Informatika (IF)) | WA: `11S26037DanielsitumeangIF`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Geometry*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/ellesiddaniel/antigravity-DEL)
- **English Explanation & Description**: A cinematic 3D web action RPG set in feudal Japan. Players wield katana blades, execute precise parries and counter-attacks, and face invading enemy warlords across scenic historic landscapes.
- **Key Objectives**: 1. Create an immersive cinematic swordplay experience using 3D web graphics. 2. Implement tight combat mechanics including stance shifts, parry timing, and combos. 3. Showcase procedural animation and atmospheric audio on the web platform.

### 13. Brawl Legends: 2D Platform Fighter Arena
- **Original Title (Indonesian)**: *BRAWL LEGENDS*
- **Creator (Who Did It)**: **Deddy Daniel Situmeang** — Institut Teknologi Del | NIM: 11S26037 (Informatika (IF)) | WA: `11S26037DanielsitumeangIF`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/ellesiddaniel/antigravity-DEL)
- **English Explanation & Description**: An explosive 2D browser-based platform fighter inspired by Brawlhalla. Players battle across suspended floating stages, utilizing aerial acrobatics, dynamic weapon drops, and knockback percentage physics.
- **Key Objectives**: 1. Implement responsive platform physics, hitboxes, and knockback vector calculations. 2. Deliver fast-paced competitive combat with diverse attack combos. 3. Provide local multiplayer and AI scrimmage battle modes.

### 14. Brain Runner 3D: Cyber Quiz Parkour
- **Original Title (Indonesian)**: *Brain Runner 3D: Cyber Quiz Parkour*
- **Creator (Who Did It)**: **Deddy Daniel Situmeang** — Institut Teknologi Del | NIM: 11S26037 (Informatika (IF)) | WA: `11S26037DanielsitumeangIF`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Geometry*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/ellesiddaniel/antigravity-DEL)
- **English Explanation & Description**: An adrenaline-fueled educational hybrid combining futuristic parkour running with rapid-fire trivia quizzes. Runners sprint across neon rooftops, jumping through gate portals corresponding to correct answers.
- **Key Objectives**: 1. Merge physical reflexes with intellectual trivia retrieval under high-speed constraints. 2. Gamify academic quiz modules into dynamic obstacle-avoidance gameplay. 3. Foster cognitive agility by forcing simultaneous motor control and logical reasoning.

### 15. Deep-Sea Odyssey: Deep Ocean Survival & Exploration Strategy
- **Original Title (Indonesian)**: *Deep-Sea Odyssey*
- **Creator (Who Did It)**: **Destria Lumban Batu** — Institut Teknologi Del | NIM: 12S26059 (Sistem Informasi (SI)) | WA: `12S26059_DESTRIA L.B`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A suspenseful deep-sea survival strategy game where players pilot a research submarine into uncharted ocean trenches, managing oxygen reserves, battery power, hull pressure, and evasive maneuvers around abyssal creatures.
- **Key Objectives**: 1. Challenge players with complex resource-management under harsh environmental constraints. 2. Cultivate strategic planning and crisis prioritization. 3. Deliver an atmospheric oceanic exploration experience with realistic pressure simulation.

### 16. TypingFlow: Minimalist Speed Typing Trainer
- **Original Title (Indonesian)**: *TypingFlow - Minimalist Speed Typing Trainer*
- **Creator (Who Did It)**: **Diva Aurel Anastacia Sirait** — Institut Teknologi Del | NIM: 11S26051 (Informatika (IF)) | WA: `11S26051_DivaAurelASirait`
- **Category & Liberal Art**: `Educational Tool` · *Quadrivium-Music*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/divaarlfs/Antigravity-IDE-Project-1.git)
- **English Explanation & Description**: An elegant, distraction-free speed typing web application designed to build muscle memory, Words Per Minute (WPM), and character accuracy through clean visual feedback and progressive typing drills.
- **Key Objectives**: 1. Increase typing speed, consistency, and precision through focused practice. 2. Provide an uncluttered, distraction-free environment with real-time WPM metrics. 3. Track longitudinal typing performance and accuracy improvements.

### 17. FlameVision AI: Real-Time Computer Vision Fire Detection System
- **Original Title (Indonesian)**: *Sistem Deteksi Api Real-Time Berbasis Computer Vision*
- **Creator (Who Did It)**: **Diva Aurel Anastacia Sirait** — Institut Teknologi Del | NIM: 11S26051 (Informatika (IF)) | WA: `11S26051_DivaAurelASirait`
- **Category & Liberal Art**: `Web Application` · *Quadrivium-Music*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/divaarlfs/Fire-Detector-Lite.git)
- **English Explanation & Description**: An automated early-warning fire detection application utilizing Python, OpenCV, and deep learning computer vision to recognize flame signatures, smoke patterns, and heat anomalies from live camera video feeds.
- **Key Objectives**: 1. Provide instantaneous fire recognition to mitigate industrial and residential fire risks. 2. Minimize false alarms through multi-spectral color and motion contour analysis. 3. Trigger automated alert broadcasts and emergency notifications upon fire detection.

### 18. VocabQuest: Interactive English Vocabulary Adventure
- **Original Title (Indonesian)**: *Vocabquest*
- **Creator (Who Did It)**: **Diva Martauli Raja Gukguk** — Institut Teknologi Del | NIM: 12S26048 (Sistem Informasi (SI)) | WA: `12S26048_Diva.M.Rgg_S1`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Music*
- **Delivery Status**: `⚠️ Pending Link` · [Live Demo](https://divamartauli-web.github.io/game-tebak-kata-bahasa-inggris/)
- **English Explanation & Description**: A gamified vocabulary learning quest where players encounter contextual word puzzles, phonetic pronunciations, and synonym challenges across varied quest scenarios.
- **Key Objectives**: 1. Expand practical English vocabulary through contextual sentences. 2. Improve pronunciation and auditory recognition using audio prompts. 3. Keep learners engaged through level progressions and achievement unlocks.

### 19. TugasKu: Interactive Homework Manager, Academic Calendar & Task Scheduler
- **Original Title (Indonesian)**: *TugasKu — Aplikasi Web Pengelola List PR, Kalender & Pengingat Tugas Interaktif*
- **Creator (Who Did It)**: **Dominggo Rajagukguk** — Institut Teknologi Del
- **Category & Liberal Art**: `Educational Tool` · *Quadrivium-Music*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A modern client-side academic task manager featuring a Monthly Calendar grid, Weekly Priority Schedule, and interactive Kanban-style assignment checklists with automated deadline countdowns.
- **Key Objectives**: 1. Help students organize schoolwork, deadlines, and study priorities in one place. 2. Eliminate missed homework deadlines through visual priority badges and countdown timers. 3. Offer an offline-capable, lightweight single-page productivity tool.

### 20. Penalty Shootout Career: Football Penalty Simulator
- **Original Title (Indonesian)**: *penalty shootout career*
- **Creator (Who Did It)**: **Farel Josepha Simangunsong** — Institut Teknologi Del | NIM: 12S26022 (Sistem Informasi (SI)) | WA: `12S26022_farel.j.smngsng`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Grammar*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/farelsimangunsong24-cyber/PENALTY-CAREER-CHAMPIONS)
- **English Explanation & Description**: A sports simulation game placing players in high-stakes football penalty shootouts throughout an evolving professional career mode, controlling ball trajectory, curve, and goalkeeper reads.
- **Key Objectives**: 1. Deliver intuitive ball-striking physics and dynamic goalkeeper artificial intelligence. 2. Provide an engaging career progression mode with skill upgrades and stadium unlocks. 3. Test timing and precision under simulated penalty pressure.

### 21. Smart Save Campus: Student Financial Management & Budgeting Platform
- **Original Title (Indonesian)**: *Smart Save Campus*
- **Creator (Who Did It)**: **Grasela Siska Viktoria Samosir** — Institut Teknologi Del | NIM: 11S26039 (Informatika (IF)) | WA: `11S26039_Grasela Smsr_IF`
- **Category & Liberal Art**: `Educational Tool` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A dedicated financial tracker tailored for university students, facilitating daily meal allowance budgeting, campus living cost tracking, and savings goal milestones.
- **Key Objectives**: 1. Prevent end-of-month student financial crises through daily expense limits. 2. Provide clear visual breakdowns of food, academic supplies, and social expenditures. 3. Encourage saving habits through gamified target rewards.

### 22. Word Detective: Vocabulary & Mystery Deduction Game
- **Original Title (Indonesian)**: *Word Detective*
- **Creator (Who Did It)**: **Grasela Siska Viktoria Samosir** — Institut Teknologi Del | NIM: 11S26039 (Informatika (IF)) | WA: `11S26039_Grasela Smsr_IF`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Music*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An educational detective puzzle game where players uncover hidden clue words related to technology, English vocabulary, and general science to crack investigative cases.
- **Key Objectives**: 1. Stimulate lateral thinking and contextual deductive reasoning. 2. Reinforce technical and academic vocabulary through case-solving narratives. 3. Offer progressive mystery levels with hint systems.

### 23. The Number Mystery: Logic & Clue Deduction Puzzle
- **Original Title (Indonesian)**: *The Number Mystery*
- **Creator (Who Did It)**: **Honey Lumban Gaol** — Institut Teknologi Del | NIM: 12S26026 (Sistem Informasi (SI)) | WA: `12S26026_HoneyL.Gaol_S1SI`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Logic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A mathematical logic game where players deduce a secret number combination based on structural clues, parity hints, and arithmetic comparisons within limited guesses.
- **Key Objectives**: 1. Cultivate systematic deductive reasoning and process-of-elimination skills. 2. Enhance numerical intuition and pattern recognition. 3. Provide tiered challenges with score multipliers for rapid deductions.

### 24. Fruit Archer: Precision Archery & Target Reaction Game
- **Original Title (Indonesian)**: *Fruit Archer*
- **Creator (Who Did It)**: **Honey Lumban Gaol** — Institut Teknologi Del | NIM: 12S26026 (Sistem Informasi (SI)) | WA: `12S26026_HoneyL.Gaol_S1SI`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An arcade archery challenge where players draw and release arrows to pop dynamic moving fruits, with increasing projectile velocities and shifting wind patterns testing player aim.
- **Key Objectives**: 1. Train visual tracking, timing reflexes, and precision targeting. 2. Introduce progressive speed escalations to test focus under pressure. 3. Provide clean, accessible arcade entertainment on any browser.

### 25. Culinary Bistro: Realistic Gourmet Kitchen Simulator 3D
- **Original Title (Indonesian)**: *Culinary Bistro: Realistic Gourmet Kitchen Simulator 3D*
- **Creator (Who Did It)**: **Immanuel Siringoringo** — Institut Teknologi Del
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Astronomy*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A 3D culinary simulation game simulating the fast-paced operations of a gourmet restaurant kitchen. Players chop, sauté, season, and plate dishes following authentic culinary recipes under ticket timers.
- **Key Objectives**: 1. Recreate realistic kitchen physics, cooking times, and ingredient combinations in 3D. 2. Test multitasking, prioritization, and time management during kitchen rush hours. 3. Provide an educational appreciation of culinary techniques and kitchen safety.

### 26. EduQuest: Interactive Question Bank & Learning Module Platform
- **Original Title (Indonesian)**: *EduQuest - Platform Bank Soal & Modul Pembelajaran Interaktif*
- **Creator (Who Did It)**: **Immanuel Siringoringo** — Institut Teknologi Del
- **Category & Liberal Art**: `Educational Tool` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A modular e-learning platform providing categorized question banks, self-paced quizzes, automated answer explanations, and performance analytics across academic subjects.
- **Key Objectives**: 1. Standardize and centralize academic practice exams and curriculum study materials. 2. Provide students with instant automated diagnostic feedback on test results. 3. Track individual learning curves and recommend targeted remediation modules.

### 27. Interactive Mystery Investigation & Interrogation Simulator
- **Original Title (Indonesian)**: *Interactive Mystery Investigation & Interrogation Simulator*
- **Creator (Who Did It)**: **Jesica Irene** — Institut Teknologi Del | NIM: 11S26042 (Informatika (IF)) | WA: `11S26042_Jesica Irene`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Grammar*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A detective narrative simulator where players analyze crime scenes, cross-examine suspect testimonies, detect contradictions in statements, and present forensic evidence to identify perpetrators.
- **Key Objectives**: 1. Train critical analysis, textual reading comprehension, and logical deduction. 2. Build dynamic branch-choice dialogue trees with consequential interrogation outcomes. 3. Immerse players in a compelling mystery narrative.

### 28. Mathematical Penalty Shootout: Penalty Kick Math Game
- **Original Title (Indonesian)**: *Mathematical Penalty Shootout*
- **Creator (Who Did It)**: **Jose Rafael Siregar** — Institut Teknologi Del | NIM: 11S26026 (Informatika (IF)) | WA: `11S26026_Jose Siregar_IF`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/joserafaelsiregar/Mathematical-Penalty-Shootout-Project)
- **English Explanation & Description**: A gamified sports-math hybrid where players earn goal attempts by accurately answering rapid math questions, aiming their shots past the goalkeeper to win tournament trophies.
- **Key Objectives**: 1. Make basic math practice competitive and entertaining for students. 2. Foster rapid mental arithmetic under the excitement of a penalty duel. 3. Build confidence in numerical fluency through sports gamification.

### 29. Late for Class! Campus Life Endless Runner
- **Original Title (Indonesian)**: *Telat Masuk Kelas! - Endless Runner Game Bertema Kehidupan Mahasiswa*
- **Creator (Who Did It)**: **Josephine Ruth Situmorang** — Institut Teknologi Del | NIM: 11S26030 (Informatika (IF)) | WA: `11S26030_Josephine Ruth`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Geometry*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A humorous 2D endless runner chronicling the frantic campus dash of a university student racing across campus obstacles (stairs, roaming pets, security gates) to reach the classroom before the lecturer closes the door.
- **Key Objectives**: 1. Capture relatable student life experiences in an engaging arcade format. 2. Implement responsive hurdle jumps, slide mechanics, and power-up pick-ups. 3. Entertain while promoting punctual campus attendance awareness.

### 30. Point Blank: Tactical Online Shooter Strategy
- **Original Title (Indonesian)**: *Point Blank*
- **Creator (Who Did It)**: **Louis Damas Tampubolon** — Institut Teknologi Del | NIM: 12S6038 (Sistem Informasi (SI)) | WA: `12S6038_LouisTampubolon`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/louisdtmpbln/point-blunk)
- **English Explanation & Description**: A tactical first-person combat simulation web game emphasizing weapon recoil control, map callouts, team positioning, and sharp shooting reflexes.
- **Key Objectives**: 1. Simulate tactical team combat scenarios and fast-paced shooting mechanics. 2. Train quick situational decision-making and spatial awareness. 3. Explore competitive multiplayer web game architecture.

### 31. Werewolf: Social Deduction & Role-Playing Game
- **Original Title (Indonesian)**: *Werewolf*
- **Creator (Who Did It)**: **Mayrinkha Yosefine** — Institut Teknologi Del | NIM: 12S26036 (Sistem Informasi (SI)) | WA: `12S26036_Mayrinkha Y_S1SI`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A digital adaptation of the classic Werewolf party game, automating day/night phase transitions, secret role distribution (Villager, Werewolf, Seer, Doctor), and anonymous village voting.
- **Key Objectives**: 1. Automate complex role tracking and night-phase moderator actions without human error. 2. Facilitate deduction, public speaking, persuasion, and psychological observation. 3. Provide a seamless multiplayer web interface for group social deduction.

### 32. Library: First-Person Interactive Book Sorting Simulation
- **Original Title (Indonesian)**: *Library*
- **Creator (Who Did It)**: **Mayrinkha Yosefine** — Institut Teknologi Del | NIM: 12S26036 (Sistem Informasi (SI)) | WA: `12S26036_Mayrinkha Y_S1SI`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Grammar*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A cozy first-person 3D simulation where the player acts as a librarian organizing scattered books onto proper shelves according to genre, author codes, and Dewey Decimal classifications.
- **Key Objectives**: 1. Introduce library organization and cataloging systems through interactive gameplay. 2. Deliver relaxing, therapeutic simulation gameplay focused on spatial organization. 3. Promote literary appreciation and orderly study environments.

### 33. Atheria: Dimensional Paradox (Sci-Fi Alien Survival)
- **Original Title (Indonesian)**: *ATHERIA : DIMENSIONAL PARADOX*
- **Creator (Who Did It)**: **Mikael Marcello Lallino Tarigan** — Institut Teknologi Del | WA: `Mikael Marcello`
- **Category & Liberal Art**: `Interactive Game` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A sci-fi action adventure game set on an Earth ravaged by extraterrestrial invaders. Players navigate dimensional rifts, scavenge energy cores, and deploy futuristic weaponry to reclaim human outposts.
- **Key Objectives**: 1. Create an atmospheric sci-fi narrative with dimensional travel mechanics. 2. Provide intense combat and puzzle-solving across diverse biomes. 3. Implement inventory crafting and character enhancement trees.

### 34. Eco-Valley: Harmony of the Food Chain (Ecosystem Simulation)
- **Original Title (Indonesian)**: *ECO-VALLEY: Harmony of the Food Chain*
- **Creator (Who Did It)**: **Nadine Hutapea** — Institut Teknologi Del
- **Category & Liberal Art**: `Simulation & Telemetry` · *Quadrivium-Geometry*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An interactive ecological simulation inspired by Stardew Valley visual aesthetics. Players manipulate population sliders (Producers, Herbivores, Carnivores, Apex Predators) and weather cycles to observe ecological balance and trophic cascades.
- **Key Objectives**: 1. Teach biological food web dynamics and carrying capacity through hands-on causality experiments. 2. Demonstrate the ecological consequences of apex predator extinction or overgrazing. 3. Provide cozy pixel art aesthetics combined with rigorous ecological science simulation.

### 35. Blink LED ESP32-C3 Super Mini Embedded Controller
- **Original Title (Indonesian)**: *Blink LED ESP32-C3 Super Mini*
- **Creator (Who Did It)**: **Nakula Nathanael Gultom** — Institut Teknologi Del | WA: `nathan`
- **Category & Liberal Art**: `IoT & Hardware` · *Quadrivium-Astronomy*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An introductory embedded systems hardware project programming an ESP32-C3 Super Mini microcontroller to drive on-board and external LEDs with custom pulse-width modulation (PWM) and blink sequences.
- **Key Objectives**: 1. Master GPIO pin configuration, register control, and timer interrupts on ESP32-C3. 2. Establish firmware build and flashing toolchains using Arduino C++ and PlatformIO. 3. Lay the physical hardware foundation for IoT telemetry projects.

### 36. Last Hope: Road to Zombie Bastion
- **Original Title (Indonesian)**: *LAST HOPE: Road to Zombie Bastion*
- **Creator (Who Did It)**: **Nakula Nathanael Gultom** — Institut Teknologi Del | WA: `nathan`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Music*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A post-apocalyptic top-down survival shooter where the player fights through waves of infected undead to reach a fortified survival sanctuary, managing limited ammo clips and barricade defenses.
- **Key Objectives**: 1. Implement top-down twin-stick shooter aiming and dynamic enemy swarm pathfinding. 2. Challenge players with resource scarcity and defensive positioning. 3. Deliver satisfying tactical combat with weapon upgrades.

### 37. Valo Hoops: 2K Tactical Basketball Simulator
- **Original Title (Indonesian)**: *VALO HOOPS: 2K TACTICAL*
- **Creator (Who Did It)**: **Nakula Nathanael Gultom** — Institut Teknologi Del | WA: `nathan`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Geometry*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A hybrid arcade sports game blending tactical shooter ability kits with fast-paced street basketball mechanics, allowing players to execute skill shots, teleport passes, and kinetic slam dunks.
- **Key Objectives**: 1. Innovate by fusing tactical hero abilities with basketball physics. 2. Implement trajectory projection, rim collision physics, and shot timing gauges. 3. Offer highly competitive, skill-based arcade gameplay.

### 38. Web LED Control & DHT11 Environmental Sensor Monitor (ESP32-C3)
- **Original Title (Indonesian)**: *Web LED Control & DHT11 Sensor Monitor ESP32-C3*
- **Creator (Who Did It)**: **Nakula Nathanael Gultom** — Institut Teknologi Del | WA: `nathan`
- **Category & Liberal Art**: `IoT & Hardware` · *Quadrivium-Astronomy*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A full-stack IoT telemetry prototype deploying an asynchronous web server on an ESP32-C3 to monitor live ambient temperature and humidity from a DHT11 sensor while toggling physical relay LEDs over Wi-Fi.
- **Key Objectives**: 1. Bridge physical sensor telemetry with a modern web dashboard without cloud reliance. 2. Implement bidirectional asynchronous HTTP/WebSocket communication between ESP32 and browser. 3. Deliver a complete IoT edge sensing and actuator control pipeline.

### 39. SintaksisFrasa: Indonesian Grammar & Phrase Syntax Learning Platform
- **Original Title (Indonesian)**: *SintaksisFrasa*
- **Creator (Who Did It)**: **Nathania Pelita Sitohang** — SMA Unggul Del (SUD)
- **Category & Liberal Art**: `Educational Tool` · *Trivium-Grammar*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An interactive educational platform helping secondary school students master Indonesian phrase syntax, classification (nominal, verbal, adjectival, prepositional phrases), and grammatical parsing rules per enhanced spelling conventions (EYD).
- **Key Objectives**: 1. Deepen syntactic understanding of Indonesian phrase structures through interactive sentence breakdowns. 2. Provide real-time phrase parsing validation and comprehensive feedback. 3. Support Indonesian language curriculum mastery for high school students.

### 40. LastLetter: Chain Word Association & Spelling Game
- **Original Title (Indonesian)**: *LastLetter*
- **Creator (Who Did It)**: **Nathania Pelita Sitohang** — SMA Unggul Del (SUD)
- **Category & Liberal Art**: `Educational Tool` · *Trivium-Grammar*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A fast-paced word association game where players must submit new words starting with the terminal letter of the preceding word, testing spelling accuracy, vocabulary depth, and reaction speed.
- **Key Objectives**: 1. Expand Indonesian vocabulary and linguistic agility through gamified word chains. 2. Prevent repetitive vocabulary through active lexical dictionary validation. 3. Provide an engaging, light-hearted linguistic duel for students.

### 41. Echoes at 11:11: 2.5D Psychological Mystery Side-Scroller
- **Original Title (Indonesian)**: *Echoes at 11:11 - Game 2.5D Psychological Mystery Side-Scroller*
- **Creator (Who Did It)**: **Pahala Deogratias Sihite** — Institut Teknologi Del | WA: `deoo`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Geometry*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An atmospheric 2.5D psychological side-scroller exploring memory distortion, temporal anomalies, and environmental storytelling. Players navigate eerie urban corridors solving auditory and visual perspective puzzles.
- **Key Objectives**: 1. Deliver an immersive psychological narrative through parallax backgrounds and dynamic lighting. 2. Implement environmental puzzles driven by temporal clues at precisely 11:11. 3. Showcase narrative game design grounded in atmospheric tension.

### 42. The Floor is Lava: Interactive Obstacle & Sensor Game
- **Original Title (Indonesian)**: *THE FLOOR IS LAVA — Dokumen Deskripsi & Spesifikasi Proyek*
- **Creator (Who Did It)**: **Rahel Sendler Sianturi** — Institut Teknologi Del
- **Category & Liberal Art**: `IoT & Hardware` · *Quadrivium-Astronomy*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An interactive obstacle game turning physical spaces into hazardous lava zones, utilizing sensor detection and visual cues to require players to leap between designated safe zones.
- **Key Objectives**: 1. Combine physical motion with digital game state mechanics. 2. Implement timing windows and hazard indicators for immersive gameplay. 3. Promote active physical movement through gamified spatial challenges.

### 43. ASAH C++: Interactive C++ Programming Assessment Tool
- **Original Title (Indonesian)**: *ASAH C*
- **Creator (Who Did It)**: **Rahel Sendler Sianturi** — Institut Teknologi Del
- **Category & Liberal Art**: `Web Application` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An interactive programming diagnostic tool providing structured coding exercises, algorithmic quiz questions, and syntax debugging challenges in modern C++.
- **Key Objectives**: 1. Assess student mastery of core C++ programming concepts (pointers, memory, loops, OOP). 2. Provide progressive coding challenges with instantaneous error analysis. 3. Prepare students for university computer science technical interviews.

### 44. KFC-Chat XI-4: Class Web Messaging & Social Hub
- **Original Title (Indonesian)**: *KFC-Chat XI-4*
- **Creator (Who Did It)**: **Rahel Sendler Sianturi** — Institut Teknologi Del
- **Category & Liberal Art**: `Web Application` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A localized web messaging application crafted specifically for high school classroom communication, sharing homework announcements, study schedules, and casual peer chats.
- **Key Objectives**: 1. Provide a focused, distraction-free class communication channel. 2. Facilitate quick file exchanges and homework reminders. 3. Cultivate digital collaboration skills within high school student cohorts.

### 45. Syntax Island: 3D WebGL Python Quest RPG
- **Original Title (Indonesian)**: *Pulau Sintaksis: Python Quest RPG (3D WebGL Edition)*
- **Creator (Who Did It)**: **Salsalina Enoli Ginting** — Institut Teknologi Del
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Geometry*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An open-world educational RPG set on a surreal island where a stranded explorer must repair their crashed airplane by solving 10 progressive Python programming quests (syntax, branching, loops, functions, error handling) and conquering arcade mini-games.
- **Key Objectives**: 1. Teach Python fundamentals through an engaging open-world 3D narrative. 2. Reinforce algorithmic thinking with in-game code validators and pseudocode puzzles. 3. Balance intellectual learning with reflex-testing arcade mini-game challenges.

### 46. NeuroLearn: Interactive Human Brain Anatomy Visualizer
- **Original Title (Indonesian)**: *Website Edukasi Interaktif Anatomi Otak Manusia (NeuroLearn)*
- **Creator (Who Did It)**: **Salsalina Enoli Ginting** — Institut Teknologi Del
- **Category & Liberal Art**: `Educational Tool` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A visual medical education web platform that allows users to explore a dynamic 3D anatomical model of the human brain. Clicking any brain lobe highlights the region and surfaces physiological functions, clinical pathology, and self-assessment quizzes.
- **Key Objectives**: 1. Make neuroanatomy accessible and intuitive through interactive 3D exploration. 2. Increase knowledge retention compared to static textbook diagrams. 3. Provide self-paced quiz modules to test anatomical identification in real time.

### 47. Nusantara Digital Twin: Indonesia 38-Province Simulation & Telemetry Platform
- **Original Title (Indonesian)**: *Nusantara Digital Twin — Platform Simulasi & Telemetri Indonesia*
- **Creator (Who Did It)**: **Stephen Joy Marvel Simamora** — Institut Teknologi Del | NIM: 12S26031 (Sistem Informasi (SI)) | WA: `12S26031_StephenJSimamora`
- **Category & Liberal Art**: `Simulation & Telemetry` · *Quadrivium-Astronomy*
- **Delivery Status**: `⚠️ Pending Link` · [Live Demo](https://simamorastephen-byte.github.io/indonesia-digital/)
- **English Explanation & Description**: A unified national digital twin web platform mapping real-time demographic, economic, educational, and environmental data across Indonesia's 38 provinces. Features an interactive national map, What-If Sandbox 2045 policy simulation, and inter-regional comparative analytics.
- **Key Objectives**: 1. Democratize access to verified regional development data across Indonesia. 2. Model long-term socio-economic policy outcomes through interactive sandbox scenarios. 3. Foster public policy literacy and data-driven governance understanding.

### 48. Kasir Simamora: Digital Point of Sale (POS) & Retail Transaction System
- **Original Title (Indonesian)**: *Website Kasir*
- **Creator (Who Did It)**: **Stephen Joy Marvel Simamora** — Institut Teknologi Del | NIM: 12S26031 (Sistem Informasi (SI)) | WA: `12S26031_StephenJSimamora`
- **Category & Liberal Art**: `Educational Tool` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link` · [Live Demo](https://simamorastephen-byte.github.io/website-kasir-stephen-simamora/)
- **English Explanation & Description**: A responsive web-based Point of Sale (POS) application designed to streamline retail transactions, inventory management, price calculations, and receipt generation for small businesses, eateries, and campus kiosks.
- **Key Objectives**: 1. Simplify daily retail checkout workflows with rapid barcode/search lookup. 2. Automate receipt printing, discount calculations, and revenue reporting. 3. Provide small local businesses with an offline-capable, cost-effective digital cash register.

### 49. Temple-Run: 3D Endless Adventure Runner
- **Original Title (Indonesian)**: *Temple-Run*
- **Creator (Who Did It)**: **Titania Shakila Panggabean** — Institut Teknologi Del | NIM: 12S26034 (Sistem Informasi (SI)) | WA: `12S26034_Titania S.P_S1SI`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Geometry*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A browser-based 3D endless runner capturing the iconic ancient temple escape adventure. Players swipe to turn sharp corners, jump over fiery gaps, and slide under obstacles while accumulating ancient relics.
- **Key Objectives**: 1. Deliver responsive 3D swipe controls and fluid camera perspectives on web browsers. 2. Implement randomized obstacle generation and progressive velocity scaling. 3. Provide thrilling arcade gameplay accessible on mobile and desktop.

### 50. KataMaster: Gamified Language Learning & Vocabulary Building Platform
- **Original Title (Indonesian)**: *KataMaster (Game Edukasi Menyusun Kata dan Kalimat)*
- **Creator (Who Did It)**: **Wendy Simanjuntak** — Institut Teknologi Del | NIM: 12S26024 (Sistem Informasi (SI)) | WA: `12S26024_WendySimanjuntak`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A Duolingo-inspired interactive language learning game designed to expand vocabulary and grammatical syntax through speech synthesis (Web Audio and Text-to-Speech), 5 structured learning units, hearts system, streaks, and leaderboards.
- **Key Objectives**: 1. Make language grammar and technology vocabulary acquisition engaging and habit-forming. 2. Train listening comprehension and accurate pronunciation through synthesized voice feedback. 3. Measure and reward consistent daily learning progress with gamified streaks.

### 51. SpotFinder IT Del: Real-Time Study Desk & Discussion Space Booking Platform
- **Original Title (Indonesian)**: *SpotFinder IT Del (Sistem Pemantau dan Pemesanan Meja Belajar Kampus)*
- **Creator (Who Did It)**: **Wendy Simanjuntak** — Institut Teknologi Del | NIM: 12S26024 (Sistem Informasi (SI)) | WA: `12S26024_WendySimanjuntak`
- **Category & Liberal Art**: `Educational Tool` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A real-time study space availability and desk reservation platform mapping open seats across IT Del's Library, Academic Buildings, Computer Labs, Gazebos, and Canteen. Includes interactive floorplans, 15-minute quick-hold reservations, facility filters (power outlets, quiet zones), and crowdsourced occupancy updates.
- **Key Objectives**: 1. Eliminate wasted time searching for study seats during exam periods. 2. Provide transparent visual desk availability across all campus study zones. 3. Foster an efficient, collaborative campus learning ecosystem.

### 52. Teman Seperjalanan IT Del: Campus Safe Ride-Sharing & Walking Companion System
- **Original Title (Indonesian)**: *Teman Seperjalanan IT Del (Sistem Mobilitas dan Panggilan Jalan Bersama ke Asrama)*
- **Creator (Who Did It)**: **Wendy Simanjuntak** — Institut Teknologi Del | NIM: 12S26024 (Sistem Informasi (SI)) | WA: `12S26024_WendySimanjuntak`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A campus mobility and peer-safety platform helping IT Del students find walking or ride-sharing companions for late-night journeys to dormitories or off-campus transit. Features campus geolocation broadcast, ride scheduling, split-fare fuel calculators, and transport efficiency mini-games.
- **Key Objectives**: 1. Enhance student safety and mutual assistance during night-time campus travel. 2. Lower student transportation costs through transparent fair-share cost splitting. 3. Promote eco-friendly shared campus mobility to reduce carbon emissions.

### 53. PolaMatika: Mathematical Sequence & Logic Matrix Puzzle Game
- **Original Title (Indonesian)**: *PolaMatika (Game Teka-Teki Logika dan Pola Bilangan)*
- **Creator (Who Did It)**: **Wendy Simanjuntak** — Institut Teknologi Del | NIM: 12S26024 (Sistem Informasi (SI)) | WA: `12S26024_WendySimanjuntak`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An interactive math puzzle game focusing on numerical pattern recognition, arithmetic series, geometric progressions, Fibonacci sequences, quadratic relations, and 3x3 logic matrices with progressive hints, step-by-step solution derivations, and combo streaks.
- **Key Objectives**: 1. Train sharp analytical deduction and pattern recognition for academic potential and technical tests. 2. Reinforce foundational mathematical sequences through visual, interactive problem solving. 3. Provide self-paced critical thinking exercises with detailed formula explanations.

### 54. RoomCheck IT Del: Campus Dormitory Facility Maintenance & Ticketing System
- **Original Title (Indonesian)**: *Roomcheck It Del*
- **Creator (Who Did It)**: **Wendy Simanjuntak** — Institut Teknologi Del | NIM: 12S26024 (Sistem Informasi (SI)) | WA: `12S26024_WendySimanjuntak`
- **Category & Liberal Art**: `Productivity Tool` · *Trivium-Rhetoric*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: An integrated web-based facility maintenance platform connecting dormitory residents with IT Del's infrastructure and facilities division. Students report plumbing, electrical, furniture, and lock issues, generating official DEL-SARPRAS tracking tickets with instant WhatsApp notifications and technician assignment boards.
- **Key Objectives**: 1. Accelerate dormitory facility repairs through automated ticketing and technician dispatch. 2. Provide transparent, accountable maintenance status tracking for students. 3. Enable facilities management to track spare parts inventory and service response times.

### 55. Math Adventure: Turn-Based RPG Arithmetic Quest
- **Original Title (Indonesian)**: *Math Adventure*
- **Creator (Who Did It)**: **Wendy Simanjuntak** — Institut Teknologi Del | NIM: 12S26024 (Sistem Informasi (SI)) | WA: `12S26024_WendySimanjuntak`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A role-playing math adventure where players explore the fantasy Realm of Numeria, battling mystical beasts by solving mental arithmetic and logic puzzles. Features hero leveling, weapon/armor gear, step-by-step hints, and quest campaigns.
- **Key Objectives**: 1. Cultivate computational thinking and mathematical problem-solving through RPG mechanics. 2. Overcome math learning reluctance by turning equations into combat spells. 3. Deliver a structured, rewarding adventure progression.

### 56. LifeQuest: Real-Life Productivity & Gamified Habit Tracker
- **Original Title (Indonesian)**: *Lifequest*
- **Creator (Who Did It)**: **Wendy Simanjuntak** — Institut Teknologi Del | NIM: 12S26024 (Sistem Informasi (SI)) | WA: `12S26024_WendySimanjuntak`
- **Category & Liberal Art**: `Educational Tool` · *Quadrivium-Arithmetic*
- **Delivery Status**: `⚠️ Pending Link`
- **English Explanation & Description**: A gamified productivity ecosystem that converts daily student routines (study sessions, scientific reading, workout sessions, hydration, budgeting) into character experience points, hero leveling, and attribute boosts (Intelligence, Vitality, Discipline). Features daily quest boards, semester exam boss battles, Pomodoro timers, and reward redemption.
- **Key Objectives**: 1. Help university students establish consistent, productive daily habits. 2. Gamify academic preparation and personal wellness through RPG progression. 3. Provide tangible motivation and self-accountability through achievement tracking.

### 57. Subway Surfers: Urban Railway Endless Runner
- **Original Title (Indonesian)**: *Subway Surfers*
- **Creator (Who Did It)**: **Yonathan** — Institut Teknologi Del | NIM: 11S26054 (Informatika (IF)) | WA: `11S26054YonathanS1_IF`
- **Category & Liberal Art**: `Interactive Game` · *Quadrivium-Geometry*
- **Delivery Status**: `⚠️ Pending Link` · [GitHub Repository](https://github.com/Yonatan123-a11/Subway-Surf)
- **English Explanation & Description**: An endless runner web game where players navigate a young graffiti artist dodging subway cars, barriers, and pursuit along vibrant train tracks, collecting gold coins and high-score multipliers.
- **Key Objectives**: 1. Deliver fast-paced arcade entertainment with responsive lane jumping and sliding. 2. Implement score multipliers, power-ups, and daily word letter collection challenges. 3. Test hand-eye coordination and reflex agility under steadily increasing game speed.

--- 

## 4. Downloadable Datasets & Navigation

- **Master Student-Project Matrix (Obsidian Markdown)**: [[docs/teaching/itdel_projects/student_project_matrix|student_project_matrix.md]]
- **IT Del & SUD Project Showcase Hub**: [[docs/teaching/itdel_projects/README|README.md]]
- **Complete Projects Database CSV (18 Columns, Dual-Language)**: [student_projects.csv](student_projects.csv)
- **Student Summary Roll-up CSV (10 Columns)**: [student_summary.csv](student_summary.csv)
- **Pending Link Reminders for WhatsApp**: [[docs/teaching/itdel_projects/missing_or_pending|missing_or_pending.md]]
- **Lossless Chat Messages Audit Log**: [[docs/teaching/itdel_projects/chat_audit.md|chat_audit.md]]
