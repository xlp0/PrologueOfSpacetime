# AI Sprint Presentation Outline: "What Can AI Actually Do?"

> A presentation outline for a one-week AI sprint. The goal is not to teach students everything — it is to **surprise them with what AI can do**, then **channel that surprise into asking the right questions** and **researching the tools they will need to use**.

---

## The Core Idea

Most people think AI is either:
1. A chatbot that answers questions (too limited).
2. A threat that will replace humans (too scary).

Both are wrong. The truth is in the middle: AI is a **tool that can do surprising things** — including things people think it cannot, like designing PCBs and editing videos — but only if you know how to ask, how to verify, and how to choose the right tool.

This sprint is designed to show students the surprising things, then teach them to ask: "How did that work? What tool did that? How do I find the right tool for my task? How do I know if the output is correct?"

**The point is not the answers. The point is the questions — and the tools students will need to use.**

---

## The Opening: Three Surprises (20 minutes)

Start the sprint with three live demos that challenge what students think AI can do. Do not explain how they work yet — just show them. The surprise is the hook.

### Surprise 1: AI Designed This PCB (7 minutes)

**What to show**: The [Arduino Micro Quadruped project](../Arduino_Powered_Micro_Quadruped/plan.md) in this repo.

- Show the BOM (bill of materials): 12 servos, an Arduino Nano, capacitors, resistors, switches, battery holders.
- Show the 8 STL files for 3D-printed parts (body, coxa, femur, tibia, servo holder).
- Show the assembly plan: mechanical assembly, PCB preparation, servo calibration, code upload.

**The surprise**: An AI helped design this. It is not a toy example — it is a real, buildable robot with real components, real 3D-printed parts, and real code. The STL files are in this repo (each is 7,000-29,000 lines of CAD data).

**The question to plant**: "How did the AI know what components to pick? How did it design the mechanical parts? What tool did that? Could it do this for any project, or just this one?"

### Surprise 2: AI Edited This Video (7 minutes)

**What to show**: The PalmierPro MCP server (covered in [Chapter 7 of the handbook](handbook/07_mcp.md)).

- Show that an AI agent can: inspect a video timeline, add and trim clips, place text overlays, generate captions from spoken audio, generate AI images and video, search the media library by what is on screen or what was said, and export the cut.
- Show the MCP tool list: `add_clips`, `add_texts`, `add_captions`, `generate_video`, `generate_image`, `generate_audio`, `get_transcript`, `inspect_timeline`, `ripple_delete_ranges`, `set_keyframes`, `split_clip`.

**The surprise**: The AI is not just writing a script about video editing — it is **actually editing the video**. It places clips, trims them, adds captions, generates music, and exports the result. This is a creative task most people assume AI cannot do.

**The question to plant**: "How does the AI know what to cut? How does it know what someone said (for captions)? What tool makes this possible? Could it edit a whole movie, or just clips?"

### Surprise 3: AI Built This Hardware Probe (6 minutes)

**What to show**: The [Digital Scope narrative](../narrative/Digital%20Scope.md) — an ESP32-based hardware probe that captures electronic signals.

- Show that this project includes a real ESP32 microcontroller design that acts as an oscilloscope and logic analyzer.
- Show that the same project has hardware folders for: drone, lidar, microscope, oscilloscope, telescope, turbine, VR lenses, edge compute, IP cameras.
- Show the [hardware directory](../hardware/): real components, not toys.

**The surprise**: AI is not just software. It helps design, program, and test real physical hardware — sensors, microcontrollers, robots, drones.

**The question to plant**: "If AI can help with PCBs, video editing, and hardware probes, what can it NOT do? And what tool do I need for my task?"

---

## The Pivot: From Surprise to Questions (10 minutes)

After the three surprises, do not jump into "here is how it works." Instead, ask the students to generate questions.

### The Question Round

Have students write down (on paper or in a shared doc) **three questions** they have after seeing the surprises. Collect them. Read a few aloud.

**Questions you want to hear** (if students do not ask these, plant them):
- "How did the AI know what to do?"
- "Did a human check the work, or did the AI do it alone?"
- "What happens when the AI is wrong?"
- "How do I find the right AI tool for my task?"
- "What tool do I need to use for [my specific project]?"
- "Can I use this for my own project?"
- "Is this free, or does it cost money?"
- "How long does it take to learn this?"

### The Three Questions That Matter

Narrow the discussion to three questions that the rest of the sprint will answer:

1. **"What can AI actually do?"** (Not what the hype says — what can it really do today, with real tools, on real tasks?)
2. **"How do I find the right tool?"** (There are hundreds of AI tools. How do you pick? What do you actually need to install and use?)
3. **"How do I know if the output is right?"** (The AI is confident even when it is wrong. How do you verify?)

These three questions map to the three parts of the sprint:
- Part 1 (Days 1-2): What AI can do, and how it works.
- Part 2 (Days 3-4): How to find and use the right tools (MCP, skills, agents).
- Part 3 (Day 5): How to verify and be responsible.

---

## The Sprint Structure (5 Days)

### Day 1 (Monday): Surprise and Foundations

**Morning**: The three surprises (above) + the question round.

**Afternoon**: Foundations — read [Chapter 1](handbook/01_what_is_ai_coding.md) and [Chapter 2](handbook/02_how_ai_tools_work.md) of the handbook. Understand the model (brain) and the harness (body). Browse the git log of this project to see real AI-assisted work.

**Homework**: Each student picks one of the three surprises (PCB, video, hardware) and writes down 5 questions they would need to answer to do that task themselves with AI. These questions become their personal research track for the week — including **what tools they will need to use**.

---

### Day 2 (Tuesday): How AI Thinks

**Morning**: How AI sees text (tokens), how it remembers (context window), why "more is not better." Read [Chapter 4](handbook/04_tokens_and_context.md) and [Chapter 5](handbook/05_prompting_styles.md).

**Afternoon**: Hands-on prompting. Try caveman, few-shot, chain-of-thought. Read one narrative doc together (e.g., [Why Three?](../narrative/Why%20Three.md)) as an example of AI-assisted writing. Discuss: where is the human, where is the AI?

**Homework**: Each student writes a prompt for their chosen surprise task (PCB design, video editing, or hardware). The prompt should ask the AI to help with one specific step. Bring the result to class Wednesday.

---

### Day 3 (Wednesday): Finding the Right Tools

**Morning**: MCP (Model Context Protocol) and skills. Read [Chapter 7](handbook/07_mcp.md) and [Chapter 8](handbook/08_agent_skills.md). Browse [mcp.so](https://mcp.so) and [skills.sh](https://skills.sh) together.

**Afternoon**: Research session — **this is the core of the sprint**. Each student searches for the MCP servers and skills relevant to their chosen surprise:

- **PCB track**: Search mcp.so for "cad", "pcb", "hardware", "arduino", "3d print", "kicad", "eagle". Search skills.sh for "hardware", "design", "electronics". What tool will they need to use to design a PCB? To order it? To 3D-print parts?
- **Video track**: Re-read the PalmierPro tools in [Chapter 7](handbook/07_mcp.md). Search mcp.so for "video", "ffmpeg", "media", "caption", "transcription". What tool will they need to use to edit a video? To generate captions? To create music?
- **Hardware track**: Search mcp.so for "serial", "iot", "esp32", "sensor", "arduino", "mqtt". Look at the [hardware directory](../hardware/) in this repo. What tool will they need to use to program an ESP32? To read sensor data? To control a motor?

**Homework**: Each student writes a one-page **"tool research report"** — what tools exist for their task, what each does, **which one they would try first, and what they would need to install or sign up for to use it**.

---

### Day 4 (Thursday): Letting AI Run

**Morning**: Agentic workflows. Read [Chapter 9](handbook/09_agentic_workflows.md) and [Chapter 10](handbook/10_the_tools_people_use.md). Understand when to let AI run on its own and when to drive yourself.

**Afternoon**: Walk through the git log of this project. Show how the June 25 commits were made: scope the task, plan, execute, verify, commit. Read the [Agentic Trinitarianism narrative](../prologue_of_spacetime_improvement/Agentic%20Trinitarianism.md) — the Miner (data), Coder (logic), Trader (verification) framework.

**Homework**: Each student outlines how they would use an agentic workflow for their chosen task. What would they scope? What tools would the agent need? What would they verify? When would they intervene?

---

### Day 5 (Friday): Being Responsible

**Morning**: Code of conduct. Read [Chapter 11](handbook/11_code_of_conduct.md). The first rule: you are responsible. Verification discipline, security, IP, honesty.

**Afternoon**: Presentations. Each student presents:
1. The task they chose (PCB, video, or hardware).
2. The tools they found (MCP servers, skills, harnesses) and **which ones they would need to use**.
3. The questions they still have.
4. One thing that surprised them about the process.

**The closing message**: The sprint is not over. The questions you leave with are more important than the answers you got. Go research the tools. Go try them. Go verify the output. That is the professional workflow.

---

## The Surprise Examples in Detail

These are the concrete examples to show on Day 1, with enough detail that the teacher can present them confidently.

### Example 1: The Arduino Micro Quadruped (PCB + 3D Printing)

**Location in repo**: `docs/Arduino_Powered_Micro_Quadruped/`

**What it is**: A complete plan for building a small four-legged robot, including:
- A bill of materials (12 servos, Arduino Nano, capacitors, resistors, switches, batteries).
- 8 STL files for 3D-printed mechanical parts (body, coxa, femur, tibia, servo holder) — each is a real CAD file with 7,000-29,000 lines.
- A step-by-step assembly plan (mechanical assembly, PCB preparation, servo calibration, code upload).

**What AI did**: An AI agent (working with a human) helped design the robot, generate the BOM, create the 3D models, and write the assembly plan. The STL files are from PCBWay Community (a real 3D-printing service).

**Why it surprises people**: Most people think AI is for writing text and code, not for designing physical objects. This shows AI can help with hardware — from component selection to mechanical design to assembly instructions.

**Tools students will need to research**: KiCad or EasyEDA (PCB design), Blender or FreeCAD (3D modeling), Cura or PrusaSlicer (3D printing), Arduino IDE (microcontroller programming), PCBWay or JLCPCB (manufacturing). Which of these have MCP servers? Which have skills? Which can an AI agent drive directly?

**The follow-up question**: "Could the AI design a different robot? A drone? A sensor? What tools would I need to install to do this myself?"

---

### Example 2: PalmierPro Video Editing

**Location in handbook**: [Chapter 7, §4.9](handbook/07_mcp.md)

**What it is**: An MCP server that exposes a full AI-native video editor. The AI agent can:
- Inspect the timeline (see all clips, their positions, durations).
- Add and trim clips (place media on the timeline, cut to length).
- Place text overlays (titles, captions, lower-thirds).
- Generate captions from spoken audio (transcribe the audio, place caption clips).
- Generate AI images and video (from a text prompt).
- Generate audio (text-to-speech, text-to-music).
- Search the media library by content ("find the sunset shot") or by spoken words ("where does she mention the budget").
- Apply keyframes (animate volume, opacity, position, scale, rotation, crop).
- Export the final cut.

**What AI did**: The AI is not just "helping with video editing" — it is **doing the editing**. It reads the timeline, makes decisions about what to cut, places clips, adds captions, generates music, and produces a finished video.

**Why it surprises people**: Video editing is a creative, judgment-heavy task. Most people assume AI cannot do creative work. This shows AI can handle the mechanical parts of creativity (cutting, captioning, placing) so the human can focus on the creative decisions.

**Tools students will need to research**: PalmierPro (the MCP server itself), DaVinci Resolve or Premiere (traditional editors — can AI drive them too?), FFmpeg (command-line video processing), Whisper (open-source transcription), ElevenLabs (AI voice generation). Which of these have MCP servers? Which can an agent call as tools?

**The follow-up question**: "How does the AI know what to cut? Could it edit a documentary? A music video? A movie? Where is the line between AI assistance and AI replacement? What tools would I need to install to try this?"

---

### Example 3: The Digital Scope (Hardware + Code)

**Location in repo**: `docs/narrative/Digital Scope.md` and `hardware/`

**What it is**: An ESP32-based hardware probe that acts as an oscilloscope and logic analyzer. It samples analog voltage signals and digital protocols (I2C, SPI, UART), digitizes them, and streams the data for analysis.

**What AI did**: An AI agent (working with a human) helped design the probe, write the firmware, and document the architecture. The same project also has hardware directories for: drone, lidar, microscope, oscilloscope, telescope, turbine, VR lenses, edge compute, IP cameras — each a real hardware project with real components.

**Why it surprises people**: Most people think AI is software-only. This shows AI can help with the physical world — designing circuits, programming microcontrollers, analyzing sensor data, and documenting hardware systems.

**Tools students will need to research**: PlatformIO or Arduino IDE (ESP32 programming), Wireshark (protocol analysis), Saleae Logic (logic analyzer software), ESPHome (home automation firmware), Home Assistant (IoT platform). Which of these have MCP servers? Which have CLI tools an agent can call? Which have skills written for them?

**The follow-up question**: "If AI can help with ESP32 programming, sensor analysis, and circuit design, what hardware projects could I tackle that I thought were too hard? What tools would I need to buy or install?"

---

## The Questions Students Should Ask

The sprint is designed to produce students who ask these questions. If they leave the week asking these questions — and knowing which tools to research — the sprint succeeded.

### About the Task
- "What specific step am I trying to do?"
- "Is this step mechanical (AI can do it) or judgment-heavy (I should do it)?"
- "What would 'done' look like? Can I describe it clearly?"

### About the Tools They Will Need to Use
- "Is there an MCP server for this?" (Search mcp.so)
- "Is there a skill for this?" (Search skills.sh)
- "Which harness should I use?" (Terminal: opencode, Claude Code. Editor: Cursor. Chat: Claude Desktop.)
- "Which model should I use?" (Cheap for mechanical, expensive for reasoning.)
- "What do I need to install?" (An MCP server? A skill? A CLI tool? A desktop app?)
- "What do I need to sign up for?" (An API key? A free account? A paid plan?)
- "Is there a CLI tool the agent can call?" (If yes, an MCP server can wrap it.)
- "Is there an open-source alternative?" (Before paying, check if a free option exists.)

### About the Output
- "Did I read the actual diff, or just the AI's summary?"
- "Did I run the tests?"
- "Did I check the edge cases?"
- "Where could the AI be confidently wrong?"
- "Does the output match what I asked for? Or did the AI drift?"

### About Responsibility
- "If this breaks, who is responsible?" (Answer: you.)
- "Am I allowed to use AI for this?" (Check your school or employer's policy.)
- "Did I mark this as AI-assisted?"
- "Did I check the license of any code the AI generated?"

### About the Future
- "What will change next year?"
- "What should I learn that will still matter?"
- "How do I keep up?"
- "Which tools should I keep using, and which should I drop?"

---

## What the Teacher Needs to Prepare

Before the sprint:

- [ ] Read the [AI Coding Handbook](handbook/README.md) (all 14 chapters, ~2,100 lines). You do not need to understand the math in the narrative docs, but you should understand the handbook.
- [ ] Read this presentation outline and the [presentation plan](presentation_plan.md).
- [ ] Browse [mcp.so](https://mcp.so) and [skills.sh](https://skills.sh) so you can show students what is there.
- [ ] Have the three surprise examples ready to show (the quadruped plan, the PalmierPro tool list, the Digital Scope narrative).
- [ ] Make sure each student has access to a browser and a free ChatGPT or Claude account.
- [ ] (Optional) Install opencode or Cursor on lab machines for Day 4.

During the sprint:

- [ ] Do not lecture for more than 45 minutes at a time. Break up with hands-on work.
- [ ] Do not try to teach the narrative docs' content. Teach their structure.
- [ ] Let students get stuck. The questions they ask when stuck are the point.
- [ ] On Day 3 (Finding the Right Tools), let students research freely. Do not give them the answers — make them search mcp.so and skills.sh themselves.
- [ ] On Friday, let the students present. Do not evaluate them on correctness — evaluate them on the quality of their questions and the thoroughness of their tool research.

---

## The Closing Message

On Friday afternoon, after the student presentations, close with this message:

> "This week was not about learning AI. It was about learning to ask the right questions about AI — and finding the tools you will need to use.
>
> The tools will change. The models will get smarter. The specific MCP servers and skills you saw this week will be replaced by better ones next year. That is fine.
>
> What will not change:
> - The model is the brain; the harness is the body. Tools matter more than prompts.
> - The AI is confident even when it is wrong. Verify before you trust.
> - You are responsible for everything the AI writes under your name.
> - The right question is worth more than the right answer.
> - Before you start, ask: 'What tool do I need? Is there an MCP server for this? Is there a skill for this?'
>
> Go research the tools. Go install them. Go try them. Go verify the output. And come back next year with better questions — and a better toolbox."

---

*Last updated: 2026-06-25. Based on the [AI Coding Handbook](handbook/README.md), the *Prologue of Spacetime* project, and Ben Koo's narrative docs.*
