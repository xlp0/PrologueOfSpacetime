"""
itdel_translations.py
=====================
High-quality, authoritative English translations and translation engine 
for all IT Del & SUD student project submissions.
"""

import re

# Authoritative English translations for all cataloged projects
TRANSLATIONS = {
    "podomoro-timer": {
        "title_en": "Pomodoro Focus & Study Timer",
        "desc_en": "A web-based productivity application implementing the Pomodoro time-management technique, alternating 25-minute focused work intervals with 5-minute restorative breaks to optimize mental endurance and study discipline.",
        "obj_en": "1. Cultivate structured study habits and combat digital distractions.\n2. Enhance sustained concentration through timed intervals.\n3. Provide responsive, intuitive timer controls with ambient sound alerts."
    },
    "petualangan-penjumlahan-ceria": {
        "title_en": "Cheerful Addition Adventure",
        "desc_en": "An interactive educational math game designed to make elementary arithmetic engaging and stress-free. Players solve random multiple-choice addition problems across three progressive difficulty tiers (Easy: 1-5, Medium: 1-10, Hard: 1-20). Features 3 lives, celebratory sound effects, and encouraging feedback.",
        "obj_en": "1. Strengthen mental arithmetic reflexes through timed challenges.\n2. Overcome math anxiety through playful gamification.\n3. Deliver lightweight, responsive educational gameplay across desktop and mobile devices."
    },
    "kategori-berantai": {
        "title_en": "Word Chain: Category Association Game",
        "desc_en": "A casual, rapid-fire word association brain puzzle playable both digitally and socially. Players race against the clock to name thematic vocabulary sequentially through the alphabet from A to Z.",
        "obj_en": "1. Enhance mental sharpness, vocabulary recall, and quick reflexes under time pressure.\n2. Foster group bonding and active communication through spontaneous gameplay.\n3. Offer a flexible, zero-friction word game with configurable thematic categories."
    },
    "focusflow-deep-work-ambient-sanctuary": {
        "title_en": "FocusFlow: Deep Work & Ambient Audio Sanctuary",
        "desc_en": "A distraction-free web productivity environment combining the Pomodoro technique with synthesized ambient audio generators (rain, waves, binaural café sounds) to induce and sustain cognitive flow states.",
        "obj_en": "1. Maximize productivity through seamless audio-visual focus triggers.\n2. Provide customized soundscapes that block ambient auditory distractions.\n3. Track daily focus sessions and deep-work consistency."
    },
    "1-focusflow-deep-work-ambient-sanctuary": {
        "title_en": "FocusFlow: Deep Work & Ambient Audio Sanctuary",
        "desc_en": "A distraction-free web productivity environment combining the Pomodoro technique with synthesized ambient audio generators (rain, waves, binaural café sounds) to induce and sustain cognitive flow states.",
        "obj_en": "1. Maximize productivity through seamless audio-visual focus triggers.\n2. Provide customized soundscapes that block ambient auditory distractions.\n3. Track daily focus sessions and deep-work consistency."
    },
    "finplan-smart-budget-wealth-accelerator": {
        "title_en": "FinPlan: Smart Budgeting & Personal Wealth Accelerator",
        "desc_en": "A lightweight personal finance and budgeting web platform featuring automated expense categorization, visual financial allocation meters, and proactive savings milestone projections.",
        "obj_en": "1. Empower students and young professionals to take control of personal cash flows.\n2. Prevent overspending through intuitive visual budget alerts.\n3. Gamify savings milestones with clear projection trajectories."
    },
    "2-finplan-smart-budget-wealth-accelerator": {
        "title_en": "FinPlan: Smart Budgeting & Personal Wealth Accelerator",
        "desc_en": "A lightweight personal finance and budgeting web platform featuring automated expense categorization, visual financial allocation meters, and proactive savings milestone projections.",
        "obj_en": "1. Empower students and young professionals to take control of personal cash flows.\n2. Prevent overspending through intuitive visual budget alerts.\n3. Gamify savings milestones with clear projection trajectories."
    },
    "mindcanvas-second-brain-knowledge-graph": {
        "title_en": "MindCanvas: Second Brain & Dynamic Knowledge Graph",
        "desc_en": "An interconnected note-taking and knowledge representation workspace that visualizes notes, entities, and research insights as an interactive node-link graph with bidirectional hyperlinking.",
        "obj_en": "1. Bridge fragmented notes into a unified, visual knowledge network.\n2. Accelerate cognitive synthesis and exploratory learning.\n3. Provide local-first, low-latency graph navigation."
    },
    "3-mindcanvas-second-brain-knowledge-graph": {
        "title_en": "MindCanvas: Second Brain & Dynamic Knowledge Graph",
        "desc_en": "An interconnected note-taking and knowledge representation workspace that visualizes notes, entities, and research insights as an interactive node-link graph with bidirectional hyperlinking.",
        "obj_en": "1. Bridge fragmented notes into a unified, visual knowledge network.\n2. Accelerate cognitive synthesis and exploratory learning.\n3. Provide local-first, low-latency graph navigation."
    },
    "codecraft-developer-swiss-knife-playground": {
        "title_en": "CodeCraft: Developer Swiss-Knife & Interactive Playground",
        "desc_en": "An all-in-one in-browser utility playground for software developers, featuring formatters (JSON, SQL, Markdown), regex testers, hash generators, and isolated HTML/CSS/JS prototyping sandboxes.",
        "obj_en": "1. Streamline daily engineering workflows into a single offline-capable web suite.\n2. Eliminate reliance on ad-heavy external web tools.\n3. Enable rapid experimentation and code snippet validation."
    },
    "4-codecraft-developer-swiss-knife-playground": {
        "title_en": "CodeCraft: Developer Swiss-Knife & Interactive Playground",
        "desc_en": "An all-in-one in-browser utility playground for software developers, featuring formatters (JSON, SQL, Markdown), regex testers, hash generators, and isolated HTML/CSS/JS prototyping sandboxes.",
        "obj_en": "1. Streamline daily engineering workflows into a single offline-capable web suite.\n2. Eliminate reliance on ad-heavy external web tools.\n3. Enable rapid experimentation and code snippet validation."
    },
    "gamehub-3-in-1-kuis-bahasa-puzzle-geser-teka-teki-seru": {
        "title_en": "GameHub 3-in-1: Language Quiz, Sliding Puzzle & Logic Riddles",
        "desc_en": "A modern vanilla JS edutainment suite integrating three cognitive mini-games: linguistic vocabulary matching, spatial sliding grid puzzles, and analytical logic riddles with unified XP and daily challenges.",
        "obj_en": "1. Stimulate linguistic memory, spatial reasoning, and critical problem-solving.\n2. Transform passive screen time into productive mental exercise through gamification.\n3. Provide a responsive, zero-dependency offline web gaming experience."
    },
    "silangit-flight-board-dtb-sistem-informasi-penerbangan-real-time": {
        "title_en": "Silangit Flight Board: Real-Time Airport Flight Information Display System (FIDS)",
        "desc_en": "A sleek, real-time Flight Information Display System (FIDS) web application tailored for Silangit International Airport (DTB), displaying scheduled departures, arrivals, gate assignments, and status updates.",
        "obj_en": "1. Streamline passenger flight tracking with clean visual schedules and status indicators.\n2. Provide airport operators with a lightweight, high-performance web display board.\n3. Ensure multi-device responsiveness across passenger smartphones and airport terminal monitors."
    },
    "mathemagica": {
        "title_en": "Mathemagica: Logic & Mental Math Puzzle Game",
        "desc_en": "An interactive mathematical logic game featuring multiple structured puzzle modes (Make 24, Equation Grid, Icon Algebra, and Number Patterns) alongside a high-intensity Time Attack reflex mode.",
        "obj_en": "1. Sharpen numerical reasoning and analytical deduction through structured puzzle solving.\n2. Train quick decision-making under time constraints.\n3. Reinforce daily learning through streak bonuses, XP milestones, and achievement badges."
    },
    "subway-surfers-3d-ultimate-web-edition": {
        "title_en": "Subway Surfers 3D: Ultimate Web Edition",
        "desc_en": "A fast-paced 3D web endless runner inspired by urban railway escapes. Players dodge moving trains, hop hurdles, and collect gold coins and power-ups across an accelerating procedurally generated track.",
        "obj_en": "1. Test motor reflexes and spatial coordination in a dynamic 3D web canvas.\n2. Implement smooth collision detection, character physics, and lane-switching mechanics.\n3. Deliver arcade-quality responsive web gaming with WebGL rendering."
    },
    "ghost-of-tsushima-way-of-the-samurai": {
        "title_en": "Ghost of Tsushima: Way of the Samurai (3D Action RPG)",
        "desc_en": "A cinematic 3D web action RPG set in feudal Japan. Players wield katana blades, execute precise parries and counter-attacks, and face invading enemy warlords across scenic historic landscapes.",
        "obj_en": "1. Create an immersive cinematic swordplay experience using 3D web graphics.\n2. Implement tight combat mechanics including stance shifts, parry timing, and combos.\n3. Showcase procedural animation and atmospheric audio on the web platform."
    },
    "brawl-legends": {
        "title_en": "Brawl Legends: 2D Platform Fighter Arena",
        "desc_en": "An explosive 2D browser-based platform fighter inspired by Brawlhalla. Players battle across suspended floating stages, utilizing aerial acrobatics, dynamic weapon drops, and knockback percentage physics.",
        "obj_en": "1. Implement responsive platform physics, hitboxes, and knockback vector calculations.\n2. Deliver fast-paced competitive combat with diverse attack combos.\n3. Provide local multiplayer and AI scrimmage battle modes."
    },
    "brain-runner-3d-cyber-quiz-parkour": {
        "title_en": "Brain Runner 3D: Cyber Quiz Parkour",
        "desc_en": "An adrenaline-fueled educational hybrid combining futuristic parkour running with rapid-fire trivia quizzes. Runners sprint across neon rooftops, jumping through gate portals corresponding to correct answers.",
        "obj_en": "1. Merge physical reflexes with intellectual trivia retrieval under high-speed constraints.\n2. Gamify academic quiz modules into dynamic obstacle-avoidance gameplay.\n3. Foster cognitive agility by forcing simultaneous motor control and logical reasoning."
    },
    "deep-sea-odyssey": {
        "title_en": "Deep-Sea Odyssey: Deep Ocean Survival & Exploration Strategy",
        "desc_en": "A suspenseful deep-sea survival strategy game where players pilot a research submarine into uncharted ocean trenches, managing oxygen reserves, battery power, hull pressure, and evasive maneuvers around abyssal creatures.",
        "obj_en": "1. Challenge players with complex resource-management under harsh environmental constraints.\n2. Cultivate strategic planning and crisis prioritization.\n3. Deliver an atmospheric oceanic exploration experience with realistic pressure simulation."
    },
    "typingflow---minimalist-speed-typing-trainer": {
        "title_en": "TypingFlow: Minimalist Speed Typing Trainer",
        "desc_en": "An elegant, distraction-free speed typing web application designed to build muscle memory, Words Per Minute (WPM), and character accuracy through clean visual feedback and progressive typing drills.",
        "obj_en": "1. Increase typing speed, consistency, and precision through focused practice.\n2. Provide an uncluttered, distraction-free environment with real-time WPM metrics.\n3. Track longitudinal typing performance and accuracy improvements."
    },
    "sistem-deteksi-api-real-time-berbasis-computer-vision": {
        "title_en": "FlameVision AI: Real-Time Computer Vision Fire Detection System",
        "desc_en": "An automated early-warning fire detection application utilizing Python, OpenCV, and deep learning computer vision to recognize flame signatures, smoke patterns, and heat anomalies from live camera video feeds.",
        "obj_en": "1. Provide instantaneous fire recognition to mitigate industrial and residential fire risks.\n2. Minimize false alarms through multi-spectral color and motion contour analysis.\n3. Trigger automated alert broadcasts and emergency notifications upon fire detection."
    },
    "vocabquest": {
        "title_en": "VocabQuest: Interactive English Vocabulary Adventure",
        "desc_en": "A gamified vocabulary learning quest where players encounter contextual word puzzles, phonetic pronunciations, and synonym challenges across varied quest scenarios.",
        "obj_en": "1. Expand practical English vocabulary through contextual sentences.\n2. Improve pronunciation and auditory recognition using audio prompts.\n3. Keep learners engaged through level progressions and achievement unlocks."
    },
    "tugasku-aplikasi-web-pengelola-list-pr-kalender-pengingat-tu": {
        "title_en": "TugasKu: Interactive Homework Manager, Academic Calendar & Task Scheduler",
        "desc_en": "A modern client-side academic task manager featuring a Monthly Calendar grid, Weekly Priority Schedule, and interactive Kanban-style assignment checklists with automated deadline countdowns.",
        "obj_en": "1. Help students organize schoolwork, deadlines, and study priorities in one place.\n2. Eliminate missed homework deadlines through visual priority badges and countdown timers.\n3. Offer an offline-capable, lightweight single-page productivity tool."
    },
    "penalty-shootout-career": {
        "title_en": "Penalty Shootout Career: Football Penalty Simulator",
        "desc_en": "A sports simulation game placing players in high-stakes football penalty shootouts throughout an evolving professional career mode, controlling ball trajectory, curve, and goalkeeper reads.",
        "obj_en": "1. Deliver intuitive ball-striking physics and dynamic goalkeeper artificial intelligence.\n2. Provide an engaging career progression mode with skill upgrades and stadium unlocks.\n3. Test timing and precision under simulated penalty pressure."
    },
    "smart-save-campus": {
        "title_en": "Smart Save Campus: Student Financial Management & Budgeting Platform",
        "desc_en": "A dedicated financial tracker tailored for university students, facilitating daily meal allowance budgeting, campus living cost tracking, and savings goal milestones.",
        "obj_en": "1. Prevent end-of-month student financial crises through daily expense limits.\n2. Provide clear visual breakdowns of food, academic supplies, and social expenditures.\n3. Encourage saving habits through gamified target rewards."
    },
    "word-detective": {
        "title_en": "Word Detective: Vocabulary & Mystery Deduction Game",
        "desc_en": "An educational detective puzzle game where players uncover hidden clue words related to technology, English vocabulary, and general science to crack investigative cases.",
        "obj_en": "1. Stimulate lateral thinking and contextual deductive reasoning.\n2. Reinforce technical and academic vocabulary through case-solving narratives.\n3. Offer progressive mystery levels with hint systems."
    },
    "the-number-mystery": {
        "title_en": "The Number Mystery: Logic & Clue Deduction Puzzle",
        "desc_en": "A mathematical logic game where players deduce a secret number combination based on structural clues, parity hints, and arithmetic comparisons within limited guesses.",
        "obj_en": "1. Cultivate systematic deductive reasoning and process-of-elimination skills.\n2. Enhance numerical intuition and pattern recognition.\n3. Provide tiered challenges with score multipliers for rapid deductions."
    },
    "fruit-archer": {
        "title_en": "Fruit Archer: Precision Archery & Target Reaction Game",
        "desc_en": "An arcade archery challenge where players draw and release arrows to pop dynamic moving fruits, with increasing projectile velocities and shifting wind patterns testing player aim.",
        "obj_en": "1. Train visual tracking, timing reflexes, and precision targeting.\n2. Introduce progressive speed escalations to test focus under pressure.\n3. Provide clean, accessible arcade entertainment on any browser."
    },
    "culinary-bistro-realistic-gourmet-kitchen-simulator-3d": {
        "title_en": "Culinary Bistro: Realistic Gourmet Kitchen Simulator 3D",
        "desc_en": "A 3D culinary simulation game simulating the fast-paced operations of a gourmet restaurant kitchen. Players chop, sauté, season, and plate dishes following authentic culinary recipes under ticket timers.",
        "obj_en": "1. Recreate realistic kitchen physics, cooking times, and ingredient combinations in 3D.\n2. Test multitasking, prioritization, and time management during kitchen rush hours.\n3. Provide an educational appreciation of culinary techniques and kitchen safety."
    },
    "eduquest---platform-bank-soal-modul-pembelajaran-interaktif": {
        "title_en": "EduQuest: Interactive Question Bank & Learning Module Platform",
        "desc_en": "A modular e-learning platform providing categorized question banks, self-paced quizzes, automated answer explanations, and performance analytics across academic subjects.",
        "obj_en": "1. Standardize and centralize academic practice exams and curriculum study materials.\n2. Provide students with instant automated diagnostic feedback on test results.\n3. Track individual learning curves and recommend targeted remediation modules."
    },
    "interactive-mystery-investigation-interrogation-simulator": {
        "title_en": "Interactive Mystery Investigation & Interrogation Simulator",
        "desc_en": "A detective narrative simulator where players analyze crime scenes, cross-examine suspect testimonies, detect contradictions in statements, and present forensic evidence to identify perpetrators.",
        "obj_en": "1. Train critical analysis, textual reading comprehension, and logical deduction.\n2. Build dynamic branch-choice dialogue trees with consequential interrogation outcomes.\n3. Immerse players in a compelling mystery narrative."
    },
    "mathematical-penalty-shootout": {
        "title_en": "Mathematical Penalty Shootout: Penalty Kick Math Game",
        "desc_en": "A gamified sports-math hybrid where players earn goal attempts by accurately answering rapid math questions, aiming their shots past the goalkeeper to win tournament trophies.",
        "obj_en": "1. Make basic math practice competitive and entertaining for students.\n2. Foster rapid mental arithmetic under the excitement of a penalty duel.\n3. Build confidence in numerical fluency through sports gamification."
    },
    "telat-masuk-kelas---endless-runner-game-bertema-kehidupan-ma": {
        "title_en": "Late for Class! Campus Life Endless Runner",
        "desc_en": "A humorous 2D endless runner chronicling the frantic campus dash of a university student racing across campus obstacles (stairs, roaming pets, security gates) to reach the classroom before the lecturer closes the door.",
        "obj_en": "1. Capture relatable student life experiences in an engaging arcade format.\n2. Implement responsive hurdle jumps, slide mechanics, and power-up pick-ups.\n3. Entertain while promoting punctual campus attendance awareness."
    },
    "point-blank": {
        "title_en": "Point Blank: Tactical Online Shooter Strategy",
        "desc_en": "A tactical first-person combat simulation web game emphasizing weapon recoil control, map callouts, team positioning, and sharp shooting reflexes.",
        "obj_en": "1. Simulate tactical team combat scenarios and fast-paced shooting mechanics.\n2. Train quick situational decision-making and spatial awareness.\n3. Explore competitive multiplayer web game architecture."
    },
    "point-blunk": {
        "title_en": "Point Blank: Tactical Online Shooter Strategy",
        "desc_en": "A tactical first-person combat simulation web game emphasizing weapon recoil control, map callouts, team positioning, and sharp shooting reflexes.",
        "obj_en": "1. Simulate tactical team combat scenarios and fast-paced shooting mechanics.\n2. Train quick situational decision-making and spatial awareness.\n3. Explore competitive multiplayer web game architecture."
    },
    "werewolf": {
        "title_en": "Werewolf: Social Deduction & Role-Playing Game",
        "desc_en": "A digital adaptation of the classic Werewolf party game, automating day/night phase transitions, secret role distribution (Villager, Werewolf, Seer, Doctor), and anonymous village voting.",
        "obj_en": "1. Automate complex role tracking and night-phase moderator actions without human error.\n2. Facilitate deduction, public speaking, persuasion, and psychological observation.\n3. Provide a seamless multiplayer web interface for group social deduction."
    },
    "library": {
        "title_en": "Library: First-Person Interactive Book Sorting Simulation",
        "desc_en": "A cozy first-person 3D simulation where the player acts as a librarian organizing scattered books onto proper shelves according to genre, author codes, and Dewey Decimal classifications.",
        "obj_en": "1. Introduce library organization and cataloging systems through interactive gameplay.\n2. Deliver relaxing, therapeutic simulation gameplay focused on spatial organization.\n3. Promote literary appreciation and orderly study environments."
    },
    "atheria-dimensional-paradox": {
        "title_en": "Atheria: Dimensional Paradox (Sci-Fi Alien Survival)",
        "desc_en": "A sci-fi action adventure game set on an Earth ravaged by extraterrestrial invaders. Players navigate dimensional rifts, scavenge energy cores, and deploy futuristic weaponry to reclaim human outposts.",
        "obj_en": "1. Create an atmospheric sci-fi narrative with dimensional travel mechanics.\n2. Provide intense combat and puzzle-solving across diverse biomes.\n3. Implement inventory crafting and character enhancement trees."
    },
    "eco-valley-harmony-of-the-food-chain": {
        "title_en": "Eco-Valley: Harmony of the Food Chain (Ecosystem Simulation)",
        "desc_en": "An interactive ecological simulation inspired by Stardew Valley visual aesthetics. Players manipulate population sliders (Producers, Herbivores, Carnivores, Apex Predators) and weather cycles to observe ecological balance and trophic cascades.",
        "obj_en": "1. Teach biological food web dynamics and carrying capacity through hands-on causality experiments.\n2. Demonstrate the ecological consequences of apex predator extinction or overgrazing.\n3. Provide cozy pixel art aesthetics combined with rigorous ecological science simulation."
    },
    "blink-led-esp32-c3-super-mini": {
        "title_en": "Blink LED ESP32-C3 Super Mini Embedded Controller",
        "desc_en": "An introductory embedded systems hardware project programming an ESP32-C3 Super Mini microcontroller to drive on-board and external LEDs with custom pulse-width modulation (PWM) and blink sequences.",
        "obj_en": "1. Master GPIO pin configuration, register control, and timer interrupts on ESP32-C3.\n2. Establish firmware build and flashing toolchains using Arduino C++ and PlatformIO.\n3. Lay the physical hardware foundation for IoT telemetry projects."
    },
    "last-hope-road-to-zombie-bastion": {
        "title_en": "Last Hope: Road to Zombie Bastion",
        "desc_en": "A post-apocalyptic top-down survival shooter where the player fights through waves of infected undead to reach a fortified survival sanctuary, managing limited ammo clips and barricade defenses.",
        "obj_en": "1. Implement top-down twin-stick shooter aiming and dynamic enemy swarm pathfinding.\n2. Challenge players with resource scarcity and defensive positioning.\n3. Deliver satisfying tactical combat with weapon upgrades."
    },
    "valo-hoops-2k-tactical": {
        "title_en": "Valo Hoops: 2K Tactical Basketball Simulator",
        "desc_en": "A hybrid arcade sports game blending tactical shooter ability kits with fast-paced street basketball mechanics, allowing players to execute skill shots, teleport passes, and kinetic slam dunks.",
        "obj_en": "1. Innovate by fusing tactical hero abilities with basketball physics.\n2. Implement trajectory projection, rim collision physics, and shot timing gauges.\n3. Offer highly competitive, skill-based arcade gameplay."
    },
    "web-led-control-dht11-sensor-monitor-esp32-c3": {
        "title_en": "Web LED Control & DHT11 Environmental Sensor Monitor (ESP32-C3)",
        "desc_en": "A full-stack IoT telemetry prototype deploying an asynchronous web server on an ESP32-C3 to monitor live ambient temperature and humidity from a DHT11 sensor while toggling physical relay LEDs over Wi-Fi.",
        "obj_en": "1. Bridge physical sensor telemetry with a modern web dashboard without cloud reliance.\n2. Implement bidirectional asynchronous HTTP/WebSocket communication between ESP32 and browser.\n3. Deliver a complete IoT edge sensing and actuator control pipeline."
    },
    "sintaksisfrasa": {
        "title_en": "SintaksisFrasa: Indonesian Grammar & Phrase Syntax Learning Platform",
        "desc_en": "An interactive educational platform helping secondary school students master Indonesian phrase syntax, classification (nominal, verbal, adjectival, prepositional phrases), and grammatical parsing rules per enhanced spelling conventions (EYD).",
        "obj_en": "1. Deepen syntactic understanding of Indonesian phrase structures through interactive sentence breakdowns.\n2. Provide real-time phrase parsing validation and comprehensive feedback.\n3. Support Indonesian language curriculum mastery for high school students."
    },
    "lastletter": {
        "title_en": "LastLetter: Chain Word Association & Spelling Game",
        "desc_en": "A fast-paced word association game where players must submit new words starting with the terminal letter of the preceding word, testing spelling accuracy, vocabulary depth, and reaction speed.",
        "obj_en": "1. Expand Indonesian vocabulary and linguistic agility through gamified word chains.\n2. Prevent repetitive vocabulary through active lexical dictionary validation.\n3. Provide an engaging, light-hearted linguistic duel for students."
    },
    "echoes-at-1111---game-25d-psychological-mystery-side-scrolle": {
        "title_en": "Echoes at 11:11: 2.5D Psychological Mystery Side-Scroller",
        "desc_en": "An atmospheric 2.5D psychological side-scroller exploring memory distortion, temporal anomalies, and environmental storytelling. Players navigate eerie urban corridors solving auditory and visual perspective puzzles.",
        "obj_en": "1. Deliver an immersive psychological narrative through parallax backgrounds and dynamic lighting.\n2. Implement environmental puzzles driven by temporal clues at precisely 11:11.\n3. Showcase narrative game design grounded in atmospheric tension."
    },
    "kfc-chat-xi-4": {
        "title_en": "KFC-Chat XI-4: Class Web Messaging & Social Hub",
        "desc_en": "A localized web messaging application crafted specifically for high school classroom communication, sharing homework announcements, study schedules, and casual peer chats.",
        "obj_en": "1. Provide a focused, distraction-free class communication channel.\n2. Facilitate quick file exchanges and homework reminders.\n3. Cultivate digital collaboration skills within high school student cohorts."
    },
    "asah-c": {
        "title_en": "ASAH C++: Interactive C++ Programming Assessment Tool",
        "desc_en": "An interactive programming diagnostic tool providing structured coding exercises, algorithmic quiz questions, and syntax debugging challenges in modern C++.",
        "obj_en": "1. Assess student mastery of core C++ programming concepts (pointers, memory, loops, OOP).\n2. Provide progressive coding challenges with instantaneous error analysis.\n3. Prepare students for university computer science technical interviews."
    },
    "the-floor-is-lava-dokumen-deskripsi-spesifikasi-proyek": {
        "title_en": "The Floor is Lava: Interactive Obstacle & Sensor Game",
        "desc_en": "An interactive obstacle game turning physical spaces into hazardous lava zones, utilizing sensor detection and visual cues to require players to leap between designated safe zones.",
        "obj_en": "1. Combine physical motion with digital game state mechanics.\n2. Implement timing windows and hazard indicators for immersive gameplay.\n3. Promote active physical movement through gamified spatial challenges."
    },
    "pulau-sintaksis-python-quest-rpg-3d-webgl-edition": {
        "title_en": "Syntax Island: 3D WebGL Python Quest RPG",
        "desc_en": "An open-world educational RPG set on a surreal island where a stranded explorer must repair their crashed airplane by solving 10 progressive Python programming quests (syntax, branching, loops, functions, error handling) and conquering arcade mini-games.",
        "obj_en": "1. Teach Python fundamentals through an engaging open-world 3D narrative.\n2. Reinforce algorithmic thinking with in-game code validators and pseudocode puzzles.\n3. Balance intellectual learning with reflex-testing arcade mini-game challenges."
    },
    "website-edukasi-interaktif-anatomi-otak-manusia-neurolearn": {
        "title_en": "NeuroLearn: Interactive Human Brain Anatomy Visualizer",
        "desc_en": "A visual medical education web platform that allows users to explore a dynamic 3D anatomical model of the human brain. Clicking any brain lobe highlights the region and surfaces physiological functions, clinical pathology, and self-assessment quizzes.",
        "obj_en": "1. Make neuroanatomy accessible and intuitive through interactive 3D exploration.\n2. Increase knowledge retention compared to static textbook diagrams.\n3. Provide self-paced quiz modules to test anatomical identification in real time."
    },
    "nusantara-digital-twin-platform-simulasi-telemetri-indonesia": {
        "title_en": "Nusantara Digital Twin: Indonesia 38-Province Simulation & Telemetry Platform",
        "desc_en": "A unified national digital twin web platform mapping real-time demographic, economic, educational, and environmental data across Indonesia's 38 provinces. Features an interactive national map, What-If Sandbox 2045 policy simulation, and inter-regional comparative analytics.",
        "obj_en": "1. Democratize access to verified regional development data across Indonesia.\n2. Model long-term socio-economic policy outcomes through interactive sandbox scenarios.\n3. Foster public policy literacy and data-driven governance understanding."
    },
    "website-kasir": {
        "title_en": "Kasir Simamora: Digital Point of Sale (POS) & Retail Transaction System",
        "desc_en": "A responsive web-based Point of Sale (POS) application designed to streamline retail transactions, inventory management, price calculations, and receipt generation for small businesses, eateries, and campus kiosks.",
        "obj_en": "1. Simplify daily retail checkout workflows with rapid barcode/search lookup.\n2. Automate receipt printing, discount calculations, and revenue reporting.\n3. Provide small local businesses with an offline-capable, cost-effective digital cash register."
    },
    "temple-run": {
        "title_en": "Temple-Run: 3D Endless Adventure Runner",
        "desc_en": "A browser-based 3D endless runner capturing the iconic ancient temple escape adventure. Players swipe to turn sharp corners, jump over fiery gaps, and slide under obstacles while accumulating ancient relics.",
        "obj_en": "1. Deliver responsive 3D swipe controls and fluid camera perspectives on web browsers.\n2. Implement randomized obstacle generation and progressive velocity scaling.\n3. Provide thrilling arcade gameplay accessible on mobile and desktop."
    },
    "roomcheck-it-del": {
        "title_en": "RoomCheck IT Del: Campus Dormitory Facility Maintenance & Ticketing System",
        "desc_en": "An integrated web-based facility maintenance platform connecting dormitory residents with IT Del's infrastructure and facilities division. Students report plumbing, electrical, furniture, and lock issues, generating official DEL-SARPRAS tracking tickets with instant WhatsApp notifications and technician assignment boards.",
        "obj_en": "1. Accelerate dormitory facility repairs through automated ticketing and technician dispatch.\n2. Provide transparent, accountable maintenance status tracking for students.\n3. Enable facilities management to track spare parts inventory and service response times."
    },
    "teman-seperjalanan-it-del": {
        "title_en": "Teman Seperjalanan IT Del: Campus Safe Ride-Sharing & Walking Companion System",
        "desc_en": "A campus mobility and peer-safety platform helping IT Del students find walking or ride-sharing companions for late-night journeys to dormitories or off-campus transit. Features campus geolocation broadcast, ride scheduling, split-fare fuel calculators, and transport efficiency mini-games.",
        "obj_en": "1. Enhance student safety and mutual assistance during night-time campus travel.\n2. Lower student transportation costs through transparent fair-share cost splitting.\n3. Promote eco-friendly shared campus mobility to reduce carbon emissions."
    },
    "teman-seperjalanan": {
        "title_en": "Teman Seperjalanan IT Del: Campus Safe Ride-Sharing & Walking Companion System",
        "desc_en": "A campus mobility and peer-safety platform helping IT Del students find walking or ride-sharing companions for late-night journeys to dormitories or off-campus transit. Features campus geolocation broadcast, ride scheduling, split-fare fuel calculators, and transport efficiency mini-games.",
        "obj_en": "1. Enhance student safety and mutual assistance during night-time campus travel.\n2. Lower student transportation costs through transparent fair-share cost splitting.\n3. Promote eco-friendly shared campus mobility to reduce carbon emissions."
    },
    "spotfinder-it-del": {
        "title_en": "SpotFinder IT Del: Real-Time Study Desk & Discussion Space Booking Platform",
        "desc_en": "A real-time study space availability and desk reservation platform mapping open seats across IT Del's Library, Academic Buildings, Computer Labs, Gazebos, and Canteen. Includes interactive floorplans, 15-minute quick-hold reservations, facility filters (power outlets, quiet zones), and crowdsourced occupancy updates.",
        "obj_en": "1. Eliminate wasted time searching for study seats during exam periods.\n2. Provide transparent visual desk availability across all campus study zones.\n3. Foster an efficient, collaborative campus learning ecosystem."
    },
    "katamaster-game-edukasi-menyusun-kata-dan-kalimat": {
        "title_en": "KataMaster: Gamified Language Learning & Vocabulary Building Platform",
        "desc_en": "A Duolingo-inspired interactive language learning game designed to expand vocabulary and grammatical syntax through speech synthesis (Web Audio and Text-to-Speech), 5 structured learning units, hearts system, streaks, and leaderboards.",
        "obj_en": "1. Make language grammar and technology vocabulary acquisition engaging and habit-forming.\n2. Train listening comprehension and accurate pronunciation through synthesized voice feedback.\n3. Measure and reward consistent daily learning progress with gamified streaks."
    },
    "katamaster": {
        "title_en": "KataMaster: Gamified Language Learning & Vocabulary Building Platform",
        "desc_en": "A Duolingo-inspired interactive language learning game designed to expand vocabulary and grammatical syntax through speech synthesis (Web Audio and Text-to-Speech), 5 structured learning units, hearts system, streaks, and leaderboards.",
        "obj_en": "1. Make language grammar and technology vocabulary acquisition engaging and habit-forming.\n2. Train listening comprehension and accurate pronunciation through synthesized voice feedback.\n3. Measure and reward consistent daily learning progress with gamified streaks."
    },
    "math-adventure": {
        "title_en": "Math Adventure: Turn-Based RPG Arithmetic Quest",
        "desc_en": "A role-playing math adventure where players explore the fantasy Realm of Numeria, battling mystical beasts by solving mental arithmetic and logic puzzles. Features hero leveling, weapon/armor gear, step-by-step hints, and quest campaigns.",
        "obj_en": "1. Cultivate computational thinking and mathematical problem-solving through RPG mechanics.\n2. Overcome math learning reluctance by turning equations into combat spells.\n3. Deliver a structured, rewarding adventure progression."
    },
    "lifequest": {
        "title_en": "LifeQuest: Real-Life Productivity & Gamified Habit Tracker",
        "desc_en": "A gamified productivity ecosystem that converts daily student routines (study sessions, scientific reading, workout sessions, hydration, budgeting) into character experience points, hero leveling, and attribute boosts (Intelligence, Vitality, Discipline). Features daily quest boards, semester exam boss battles, Pomodoro timers, and reward redemption.",
        "obj_en": "1. Help university students establish consistent, productive daily habits.\n2. Gamify academic preparation and personal wellness through RPG progression.\n3. Provide tangible motivation and self-accountability through achievement tracking."
    },
    "polamatika-game-teka-teki-logika-dan-pola-bilangan": {
        "title_en": "PolaMatika: Mathematical Sequence & Logic Matrix Puzzle Game",
        "desc_en": "An interactive math puzzle game focusing on numerical pattern recognition, arithmetic series, geometric progressions, Fibonacci sequences, quadratic relations, and 3x3 logic matrices with progressive hints, step-by-step solution derivations, and combo streaks.",
        "obj_en": "1. Train sharp analytical deduction and pattern recognition for academic potential and technical tests.\n2. Reinforce foundational mathematical sequences through visual, interactive problem solving.\n3. Provide self-paced critical thinking exercises with detailed formula explanations."
    },
    "polamatika": {
        "title_en": "PolaMatika: Mathematical Sequence & Logic Matrix Puzzle Game",
        "desc_en": "An interactive math puzzle game focusing on numerical pattern recognition, arithmetic series, geometric progressions, Fibonacci sequences, quadratic relations, and 3x3 logic matrices with progressive hints, step-by-step solution derivations, and combo streaks.",
        "obj_en": "1. Train sharp analytical deduction and pattern recognition for academic potential and technical tests.\n2. Reinforce foundational mathematical sequences through visual, interactive problem solving.\n3. Provide self-paced critical thinking exercises with detailed formula explanations."
    },
    "subway-surfers": {
        "title_en": "Subway Surfers: Urban Railway Endless Runner",
        "desc_en": "An endless runner web game where players navigate a young graffiti artist dodging subway cars, barriers, and pursuit along vibrant train tracks, collecting gold coins and high-score multipliers.",
        "obj_en": "1. Deliver fast-paced arcade entertainment with responsive lane jumping and sliding.\n2. Implement score multipliers, power-ups, and daily word letter collection challenges.\n3. Test hand-eye coordination and reflex agility under steadily increasing game speed."
    }
}


def translate_text(text: str) -> str:
    """Fallback translator for general Indonesian educational/tech text."""
    if not text:
        return ""
    
    # Common vocabulary replacements
    replacements = [
        (r'\badalah\b', 'is'),
        (r'\bsebuah\b', 'a'),
        (r'\bgame\b', 'game'),
        (r'\bproyek\b', 'project'),
        (r'\bprojek\b', 'project'),
        (r'\baplikasi\b', 'application'),
        (r'\bberbasis\b', 'based on'),
        (r'\binteraktif\b', 'interactive'),
        (r'\bdirancang untuk\b', 'designed to'),
        (r'\bmemudahkan\b', 'facilitate'),
        (r'\bmeningkatkan\b', 'enhance'),
        (r'\bmembantu\b', 'help'),
        (r'\bpemain\b', 'players'),
        (r'\bpengguna\b', 'users'),
        (r'\bmahasiswa\b', 'students'),
        (r'\bbelajar\b', 'learn'),
        (r'\bpembelajaran\b', 'learning'),
        (r'\btujuan\b', 'objective'),
        (r'\butama\b', 'primary'),
        (r'\bdengan\b', 'with'),
        (r'\bdan\b', 'and'),
        (r'\byang\b', 'that'),
        (r'\bdi\b', 'in'),
        (r'\bke\b', 'to'),
        (r'\bdari\b', 'from'),
        (r'\bsecara\b', 'in a manner'),
        (r'\bserta\b', 'as well as'),
    ]
    res = text
    for pat, rep in replacements:
        res = re.sub(pat, rep, res, flags=re.IGNORECASE)
    return res


def slugify(text: str) -> str:
    text = (text or "").lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')[:60]


def get_project_translation(title: str, desc: str, obj: str, slug: str = "") -> dict:
    """
    Retrieve English translations for a project.
    Checks exact slug match, partial matches, or generates a clean fallback.
    """
    clean_slug = slugify(title)
    
    # 1. Exact match by provided slug or generated slug
    if slug and slug in TRANSLATIONS:
        return TRANSLATIONS[slug]
    if clean_slug in TRANSLATIONS:
        return TRANSLATIONS[clean_slug]
        
    # 2. Key search in dictionary
    for k, v in TRANSLATIONS.items():
        if k in clean_slug or clean_slug in k:
            return v
            
    # 3. Fallback: clean title and basic translation
    title_en = title
    # Clean standard prefixes
    title_en = re.sub(r'(?i)^(?:projek|proyek|aplikasi|game)\s*[:—–-]?\s*', '', title_en).strip()
    
    desc_en = translate_text(desc) if desc else "Project description in development."
    obj_en = translate_text(obj) if obj else "Project objectives defined in technical specifications."
    
    return {
        "title_en": title_en,
        "desc_en": desc_en,
        "obj_en": obj_en
    }
