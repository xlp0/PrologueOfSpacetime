---
title: "IT Del & SUD Student Projects Showcase Hub"
date: 2026-09-22
type: overview
tags: [IT-Del, SUD, Showcase, Projects, Curriculum]
status: stable
liberal_art: Quadrivium-Music
---

# IT Del & SUD Student Projects Showcase Hub

> **Context**: Conversational Programming, Prompt Engineering & AI Systems Workshop  
> **Cohorts**: Institut Teknologi Del (Informatika, Sistem Informasi, Teknik Elektro) & SMA Unggul Del (SUD)  
> **Last Synchronized**: `2026-09-22 18:02:27`  
> **Source Origin**: `WhatsApp Chat - Peserta Conversational Programming (3).zip` (83 chat interactions analyzed)

---

## 📊 Workshop Overview & Real-Time Metrics

- **Registered Students**: `29`
- **Total Cataloged Projects**: `57`
- **Verified Deliveries**: `14`
- **Pending Link Verification**: `43`
- **Master Student Matrix**: [[student_project_matrix|Open Master Student-Project Matrix]]
- **Action Reminders**: [[missing_or_pending|View Pending Link Checklist]]
- **Lossless Chat Audit**: [[chat_audit|Open Audit Log]]
- **Downloadable CSV Datasets**:
  - 📥 **[Download Full Projects CSV](student_projects.csv)** *(Title ID/EN, Description ID/EN, Objective ID/EN, Category, URLs, Status)*
  - 📥 **[Download Student Summary CSV](student_summary.csv)** *(Student Name, Contact, NIM, School, Project Count, English Titles)*

---

## 🧭 Live Dataview Portfolios

### 1. Interactive Games & Web Experiences
```dataview
TABLE title_en AS "English Title", author AS "Student", school AS "School", status AS "Status", demo_url AS "Demo"
FROM "docs/teaching/itdel_projects/projects"
WHERE category = "Interactive Game"
SORT file.name ASC
```

### 2. Educational & Cognitive Learning Tools
```dataview
TABLE title_en AS "English Title", author AS "Student", school AS "School", status AS "Status", repo_url AS "Repo"
FROM "docs/teaching/itdel_projects/projects"
WHERE category = "Educational Tool"
SORT file.name ASC
```

### 3. IoT, Sensors & Hardware Prototypes
```dataview
TABLE title_en AS "English Title", author AS "Student", school AS "School", liberal_art AS "Liberal Art", repo_url AS "Repo"
FROM "docs/teaching/itdel_projects/projects"
WHERE category = "IoT & Hardware"
SORT file.name ASC
```

### 4. Productivity & Web Applications
```dataview
TABLE title_en AS "English Title", author AS "Student", school AS "School", category AS "Type", status AS "Status"
FROM "docs/teaching/itdel_projects/projects"
WHERE category = "Productivity Tool" OR category = "Web Application"
SORT file.name ASC
```

### 5. Digital Twins & Telemetry Simulations
```dataview
TABLE title_en AS "English Title", author AS "Student", school AS "School", demo_url AS "Live Demo", repo_url AS "Repo"
FROM "docs/teaching/itdel_projects/projects"
WHERE category = "Simulation & Telemetry"
SORT file.name ASC
```

### 6. Student Portfolios
```dataview
TABLE author AS "Student", school AS "School", nim AS "NIM", department AS "Prodi"
FROM "docs/teaching/itdel_projects/students"
SORT file.name ASC
```
