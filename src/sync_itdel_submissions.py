#!/usr/bin/env python3
"""
sync_itdel_submissions.py
=========================
Lossless ingestion, multi-language (ID/EN) translation, CSV export,
and student-centric showcase pipeline for IT Del & SUD student project submissions.

Features:
1. Discovers and archives newest WhatsApp export zip in ~/Downloads.
2. Preserves historical submissions across all exports so deleted messages/media are never lost.
3. Universal markdown and plain-text field extraction for Indonesian and English data.
4. Auto-unpacks nested attachments (zip, md, txt) with cross-file author inheritance.
5. Splits multi-project messages (Wendy, Briant, Annisa) while keeping single-project numbered forms intact (Honey).
6. Captures student identity: Full Name, WhatsApp Handle, Phone Number, NIM, Department, and School (IT Del vs SUD).
7. Translates every project title, description, and objective to English via itdel_translations.
8. Generates two CSV files: student_projects.csv (all projects) and student_summary.csv (per student).
9. Generates AGENTS.md-compliant project pages with dual-language (ID/EN) sections.
10. Generates student portfolio summaries, Master Matrix, Dataview Dashboard, Lossless Chat Audit, and WhatsApp Reminders.
"""

import os
import sys
import glob
import re
import json
import csv
import zipfile
import shutil
from datetime import datetime
from pathlib import Path

# Local translation engine
try:
    from src.itdel_translations import get_project_translation
except ImportError:
    from itdel_translations import get_project_translation

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DOWNLOADS_DIR = Path("/Users/Henrykoo/Downloads")
RAW_BASE_DIR = BASE_DIR / "raw" / "transcripts" / "itdel_whatsapp"
EXPORTS_DIR = RAW_BASE_DIR / "exports"
REGISTRY_FILE = RAW_BASE_DIR / "registry.json"

DOCS_BASE_DIR = BASE_DIR / "docs" / "teaching" / "itdel_projects"
PROJECTS_DIR = DOCS_BASE_DIR / "projects"
STUDENTS_DIR = DOCS_BASE_DIR / "students"
DASHBOARD_FILE = DOCS_BASE_DIR / "README.md"
MATRIX_FILE = DOCS_BASE_DIR / "student_project_matrix.md"
AUDIT_FILE = DOCS_BASE_DIR / "chat_audit.md"
PENDING_FILE = DOCS_BASE_DIR / "missing_or_pending.md"
CSV_PROJECTS_FILE = DOCS_BASE_DIR / "student_projects.csv"
CSV_SUMMARY_FILE = DOCS_BASE_DIR / "student_summary.csv"


def clean_unicode(text: str) -> str:
    """Strip invisible WhatsApp LTR marks and standardize whitespace."""
    if not text:
        return ""
    chars_to_replace = {
        "\u200e": "",  # LTR mark
        "\u200f": "",  # RTL mark
        "\u202f": " ", # Narrow no-break space
        "\u00a0": " ", # No-break space
        "\u2060": "",  # Word joiner
        "\ufeff": "",  # Zero-width no-break space (BOM)
        "\u202a": "",  # Left-to-right embedding
        "\u202c": "",  # Pop directional formatting
        "\u2011": "-", # Non-breaking hyphen
        "\r\n": "\n",  # CRLF normalization
        "\r": "\n",
    }
    for k, v in chars_to_replace.items():
        text = text.replace(k, v)
    return text.strip()


def slugify(text: str) -> str:
    """Create a URL/filename-safe kebab slug."""
    text = clean_unicode(text).lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')[:60]


def format_table_cell(text: str, max_len: int = 350) -> str:
    """Format text for markdown table cells: escape pipes and convert newlines to <br>."""
    if not text:
        return ""
    t = clean_unicode(text).strip()
    if max_len and len(t) > max_len:
        t = t[:max_len].rsplit(" ", 1)[0] + "..."
    t = t.replace("|", "\\|")
    t = re.sub(r'\r?\n+', '<br>', t)
    return t


def extract_field_value(text: str, label_regex: str) -> str:
    """
    Extract field value from markdown or plaintext.
    Handles:
    - Same-line: 'Judul: My Project', '**Judul:** My Project', '* **Judul:** My Project'
    - Next-line:
        * **Judul:**
          My Project
    - Numbered headers: '# 1. Judul', '1. Judul'
    """
    pattern = rf'(?i)(?:^|\n)\s*[*#-]*\s*(?:\d+\.\s*)?\*?\*?\s*{label_regex}[\s:*：\t]*([^\n\r]*)'
    m = re.search(pattern, text)
    if not m:
        return ""
    val = m.group(1).strip().strip('*_"`#:\t ')
    if not val or len(val) == 0:
        rest = text[m.end():].lstrip(" \t\r")
        if rest.startswith("\n"):
            lines = [l.strip().strip('*_"`#:\t ') for l in rest.splitlines() if l.strip()]
            if lines:
                val = lines[0]
    return val


def find_latest_export(custom_path=None) -> Path:
    """Find the newest WhatsApp export zip in Downloads or use provided path."""
    if custom_path:
        p = Path(custom_path)
        if p.exists():
            return p
        raise FileNotFoundError(f"Specified path not found: {custom_path}")

    patterns = [
        str(DOWNLOADS_DIR / "WhatsApp Chat - Peserta Conversational Programming*.zip"),
        str(DOWNLOADS_DIR / "*Conversational Programming*.zip"),
        str(DOWNLOADS_DIR / "WhatsApp Chat - *.zip"),
    ]
    candidates = []
    for pat in patterns:
        candidates.extend(glob.glob(pat))

    if not candidates:
        raise FileNotFoundError(f"No WhatsApp export zip files found in {DOWNLOADS_DIR}")

    candidates = list(set(candidates))
    candidates.sort(key=os.path.getmtime, reverse=True)
    return Path(candidates[0])


def archive_export(zip_path: Path) -> tuple[Path, Path]:
    """
    Extract the zip into a versioned raw archive directory.
    Returns (export_dir, chat_txt_path).
    """
    mtime = datetime.fromtimestamp(zip_path.stat().st_mtime)
    timestamp_str = mtime.strftime("%Y-%m-%d_%H%M%S")
    export_dir = EXPORTS_DIR / f"export_{timestamp_str}"
    export_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(export_dir)

    chat_txt = export_dir / "_chat.txt"
    if not chat_txt.exists():
        txt_files = list(export_dir.glob("*.txt"))
        if txt_files:
            chat_txt = txt_files[0]
        else:
            raise FileNotFoundError(f"No _chat.txt found in {export_dir}")

    return export_dir, chat_txt


def extract_sender_info(raw_sender: str) -> dict:
    """Parse phone number, NIM, department, school, and clean name from sender handle."""
    sender = clean_unicode(raw_sender)
    if sender.startswith("~"):
        sender = sender[1:].strip()

    # Match phone number
    phone_match = re.search(r'(\+62[0-9\s-]{8,20}|08[0-9\s-]{8,15})', sender)
    phone = phone_match.group(1).replace(" ", "").replace("-", "") if phone_match else None

    # Match NIM: e.g. 11S26030, 12S26031, 12S6038
    nim_match = re.search(r'(1[1-4]S\d{4,5})', sender, re.IGNORECASE)
    nim = nim_match.group(1).upper() if nim_match else None

    # Derive department from NIM or explicit string
    department = None
    if nim:
        dept_prefix = nim[:3].upper()
        dept_map = {
            "11S": "Informatika (IF)",
            "12S": "Sistem Informasi (SI)",
            "13S": "Teknik Elektro (TE)",
            "14S": "Manajemen Rekayasa (MR)"
        }
        department = dept_map.get(dept_prefix)

    if not department:
        if any(k in sender.upper() for k in ["_IF", "_S1IF", "S1_IF", "IF"]):
            department = "Informatika (IF)"
        elif any(k in sender.upper() for k in ["_SI", "S1SI", "_S1_SI", "SI"]):
            department = "Sistem Informasi (SI)"
        elif any(k in sender.upper() for k in ["_TE", "TE"]):
            department = "Teknik Elektro (TE)"
        elif any(k in sender.upper() for k in ["_MR", "MR"]):
            department = "Manajemen Rekayasa (MR)"

    # Identify school
    school = "Institut Teknologi Del"
    if any(k in sender.upper() for k in ["(SUD)", "_SUD", "SUD", "SMA UNGGUL DEL"]):
        school = "SMA Unggul Del (SUD)"

    # Clean display name
    name_cand = sender
    name_cand = re.sub(r'^\+62[0-9\s-]+', '', name_cand).strip()
    name_cand = re.sub(r'^1[1-4]S\d{4,5}[_]?', '', name_cand, flags=re.IGNORECASE).strip()
    name_cand = re.sub(r'_(?:IF|SI|TE|MR|S1|S1SI|S1_IF)$', '', name_cand, flags=re.IGNORECASE).strip()
    name_cand = name_cand.replace("_", " ").strip()
    if not name_cand or name_cand.isdigit():
        name_cand = sender

    # Standardize common nicknames
    nick_map = {
        "nathan": "Nakula Nathanael Gultom",
        "rahel": "Rahel Sendler Sianturi",
        "deoo": "Pahala Deogratias Sihite",
        "salsa": "Salsalina Enoli Ginting",
        "Immanuel Levin": "Immanuel Siringoringo",
        "Mikael Marcello": "Mikael Marcello Lallino Tarigan",
        "Dominggo": "Dominggo Rajagukguk",
        "Niaa ( ꈍ◡ꈍ)": "Nathania Pelita Sitohang",
        "Nadine Hutapea": "Nadine Hutapea",
        "Briant Sinaga": "Briant Sinaga",
        "WEENDY SIMANJUNTAK": "Wendy Simanjuntak",
        "WENDY SIMANJUNTAK": "Wendy Simanjuntak",
        "wendysimanjuntak": "Wendy Simanjuntak",
    }
    for k, v in nick_map.items():
        if k.lower() == name_cand.lower() or k.lower() in sender.lower():
            name_cand = v
            break

    return {
        "raw_sender": raw_sender,
        "display_name": name_cand,
        "phone": phone,
        "nim": nim,
        "department": department,
        "school": school
    }


def classify_liberal_art(title: str, desc: str, obj: str) -> str:
    """Classify project into one of the 7 Liberal Arts per AGENTS.md."""
    combined = f"{title} {desc} {obj}".lower()

    if any(k in combined for k in ["esp32", "dht11", "sensor", "iot", "hardware", "led", "suhu", "kelembapan", "twin", "telemetri", "drone"]):
        return "Quadrivium-Astronomy"
    if any(k in combined for k in ["3d", "spatial", "graph", "peta", "runner", "game 2.5d", "koordinat", "webgl", "voxel", "space", "bistro 3d"]):
        return "Quadrivium-Geometry"
    if any(k in combined for k in ["matematika", "hitung", "penjumlahan", "aljabar", "budget", "keuangan", "anggaran", "finplan", "money", "save"]):
        return "Quadrivium-Arithmetic"
    if any(k in combined for k in ["timer", "pomodoro", "audio", "ambient", "frekuensi", "sound", "musik", "suara"]):
        return "Quadrivium-Music"
    if any(k in combined for k in ["sintaksis", "eyd", "frasa", "kata", "typing", "mengetik", "vocabulary", "kamus", "duolingo", "bahasa"]):
        return "Trivium-Grammar"
    if any(k in combined for k in ["logic", "logika", "teka-teki", "puzzle", "detektif", "investigasi", "interogasi", "c++", "codecraft"]):
        return "Trivium-Logic"
    return "Trivium-Rhetoric"


def extract_links(text: str) -> tuple[str | None, str | None]:
    """Extract Live Demo URL and GitHub Repository URL from text."""
    demo_url = None
    repo_url = None

    gh_match = re.search(r'https?://(?:www\.)?github\.com/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+', text)
    if gh_match:
        cand = gh_match.group(0)
        if not cand.endswith("cli.github.com"):
            repo_url = cand

    demo_match = re.search(r'https?://[a-zA-Z0-9_.-]+\.github\.io/[a-zA-Z0-9_.-]+/?', text)
    if demo_match:
        demo_url = demo_match.group(0)
    elif not demo_url:
        vercel_match = re.search(r'https?://[a-zA-Z0-9_.-]+\.(?:vercel\.app|netlify\.app|pages\.dev)[^\s]*', text)
        if vercel_match:
            demo_url = vercel_match.group(0)

    return demo_url, repo_url


def is_numbered_field_form(body: str) -> bool:
    """Checks if message is a single project with numbered fields (e.g. 1. Judul ... 2. Nama ...)."""
    m1 = re.search(r'(?:^|\n)\s*1\.\s*(?:judul|nama\s+game|nama\s+proyek)', body, re.IGNORECASE)
    m2 = re.search(r'(?:^|\n)\s*2\.\s*(?:nama|author|pengembang|judul)', body, re.IGNORECASE)
    return bool(m1 and m2)


def find_project_headings(text: str) -> list[tuple[int, str, str]]:
    """
    Find starting positions of numbered project headings (e.g. '1. FOCUSFLOW : DEEP WORK', '1. ROOMCHECK IT DEL').
    Returns [(start_pos, full_heading, title)].
    """
    pattern = re.compile(r'(?:^|\n)\s*((?:[1-9]|10)\.\s+([A-Z0-9\s:—–&()]+?))(?=\s{2,}|\n|$)')
    matches = []
    for m in pattern.finditer(text):
        full = m.group(1).strip()
        cand = m.group(2).strip()
        letters = re.sub(r'[^a-zA-Z]', '', cand)
        if letters and letters.isupper() and len(letters) >= 3:
            start_pos = m.start()
            prefix = text[max(0, start_pos - 40):start_pos].lower()
            if 'tujuan' not in prefix and 'manfaat' not in prefix and 'fungsi' not in prefix:
                matches.append((start_pos, full, cand))
    return matches


def is_multi_project_message(body: str) -> bool:
    """Detect if a message contains multiple distinct projects."""
    if re.search(r'(?i)(?:^|\n)\s*proyek\s*1\b', body) and re.search(r'(?i)(?:^|\n)\s*proyek\s*2\b', body):
        return True
    if is_numbered_field_form(body):
        return False
    headings = find_project_headings(body)
    return len(headings) >= 2


def parse_single_project_block(cleaned: str, sender_info: dict, source_ref: str, default_author: str = None) -> dict | None:
    """Parse an individual project block into structured fields."""
    if not cleaned or len(cleaned) < 25:
        return None

    # Filter out system events
    low = cleaned.lower()
    system_phrases = [
        "this message was deleted",
        "added you",
        "added ~",
        "created this group",
        "end-to-end encrypted",
        "dear mahasiswa",
        "dimulai pukul",
        "izin ke dosen",
        "bisa hadir di gd713"
    ]
    if any(p in low for p in system_phrases) or re.search(r'\badded\b', low):
        return None

    # Title extraction
    title = extract_field_value(cleaned, r'judul(?:\s*(?:game|proyek|project))?')
    if not title:
        title = extract_field_value(cleaned, r'nama\s+(?:game|aplikasi|projek|proyek)')
    if not title:
        m_num_head = re.match(r'^\s*(?:[1-9]|10)\.\s+([A-Z0-9\s:—–&()]+?)(?:\s{2,}|\n+)([\s\S]*)', cleaned)
        if m_num_head:
            title = m_num_head.group(1).strip().title()
    if not title:
        m_game = re.search(r'(?i)nama game\s*[:：\t]*\s*([^\n]+)', cleaned)
        if m_game:
            title = m_game.group(1).strip().strip("*\"'#: ")
        elif cleaned.startswith("# "):
            first_line = cleaned.splitlines()[0]
            title = re.sub(r'^#+\s*', '', first_line).strip()
        else:
            lines = [l.strip() for l in cleaned.splitlines() if l.strip()]
            if lines:
                cand = lines[0]
                if not any(k in cand.lower() for k in ["nama", "deskripsi", "halo", "selamat", "izin", "baik", "terima", "laporan", "dibuat"]):
                    title = cand

    # Strip emojis and decorative prefixes from title
    title = re.sub(r'^[^\w\s]+', '', title).strip()
    title = re.sub(r'[^\w\s—–:&()]+$', '', title).strip()

    if not title or len(title) < 2:
        return None

    # Title normalizations for consistency
    if "kuis bahasa" in title.lower() and "puzzle geser" in title.lower():
        title = "GameHub 3-in-1 (Kuis Bahasa, Puzzle Geser, Teka-Teki Seru)"
    elif "point blunk" in title.lower():
        title = "Point Blank"

    # Name extraction
    name = default_author or sender_info.get("display_name", "")
    parsed_name = extract_field_value(cleaned, r'(?:nama\s*(?:lengkap|pengembang|siswa|mahasiswa)?|author|dibuat\s*oleh)')
    if parsed_name:
        if "(SUD)" in parsed_name or "(IT Del)" in parsed_name:
            sender_info["school"] = "SMA Unggul Del (SUD)" if "(SUD)" in parsed_name else "Institut Teknologi Del"
            parsed_name = re.sub(r'\s*\((?:SUD|IT Del)\)', '', parsed_name)
        parsed_name = re.sub(r'\s*LAPORAN.*$', '', parsed_name, flags=re.IGNORECASE).strip()
        if len(parsed_name) > 2 and not any(k in parsed_name.lower() for k in ["laporan", "projek", "aplikasi", "game"]):
            name = parsed_name

    name = name.title().strip(":# ")

    # Description extraction
    desc = ""
    pattern_desc = r'(?i)(?:^|\n)\s*[*#-]*\s*(?:\d+\.\s*)?\*?\*?\s*deskripsi\s*(?:proyek|project|produk|game|aplikasi)?[\s:*：\t]*\n*([\s\S]*?)(?=(?:(?:^|\n)\s*[*#-]*\s*(?:\d+\.\s*)?\*?\*?\s*tujuan|fungsi utama|link|https?://|\Z))'
    m_desc = re.search(pattern_desc, cleaned)
    if m_desc:
        desc = m_desc.group(1).strip()
    else:
        m_num_head = re.match(r'^\s*(?:[1-9]|10)\.\s+[A-Z0-9\s:—–&()]+?(?:\s{2,}|\n+)([\s\S]*)', cleaned)
        if m_num_head:
            desc = m_num_head.group(1).strip()
        else:
            sections = re.split(r'\n(?=##\s+)', cleaned)
            if len(sections) > 1:
                body_sections = [s.strip() for s in sections if not re.match(r'(?i)##\s*(?:manfaat|tujuan)', s.strip())]
                desc = "\n\n".join(body_sections).strip()

    # Objective extraction
    obj = ""
    pattern_obj = r'(?i)(?:^|\n)\s*[*#-]*\s*(?:\d+\.\s*)?\*?\*?\s*tujuan\s*(?:utama|proyek|project|game|aplikasi)?[\s:*：\t]*\n*([\s\S]*?)(?=(?:(?:^|\n)\s*[*#-]*\s*(?:\d+\.\s*)?\*?\*?\s*fungsi|link|https?://|\Z))'
    m_obj = re.search(pattern_obj, cleaned)
    if m_obj:
        obj = m_obj.group(1).strip()
    else:
        m_manfaat = re.search(r'(?i)##\s*(?:manfaat|tujuan)[\s\S]*', cleaned)
        if m_manfaat:
            obj = re.sub(r'(?i)^##\s*(?:manfaat|tujuan)[^\n]*\n*', '', m_manfaat.group(0)).strip()

    # Functions extraction (e.g. Wendy style: "Fungsi Utama: a. ... b. ...")
    m_fungsi = re.search(r'(?i)(?:fungsi utama\s*[:：\t]*\s*\n*)([\s\S]*?)(?=(?:link|https?://|\Z))', cleaned)
    if m_fungsi:
        fungsi_text = m_fungsi.group(1).strip()
        if not desc:
            desc = fungsi_text
        else:
            desc = f"{desc}\n\n### Fitur & Fungsi Utama\n{fungsi_text}"

    # Clean edits marker
    desc = re.sub(r'‎?<This message was edited>', '', desc).strip()
    obj = re.sub(r'‎?<This message was edited>', '', obj).strip()

    demo_url, repo_url = extract_links(cleaned)
    liberal_art = classify_liberal_art(title, desc, obj)

    # Determine project category / type
    combined_text = f"{title} {desc} {obj}".lower()
    category = "Web Application"
    if any(k in combined_text for k in ["esp32", "dht11", "sensor", "led", "mikrokontroler", "lava"]):
        category = "IoT & Hardware"
    elif any(k in combined_text for k in ["twin", "kembar digital", "telemetri", "simulasi kebijakan", "indonesia emas", "eco-valley"]):
        category = "Simulation & Telemetry"
    elif any(k in combined_text for k in ["game", "runner", "zombie", "duel", "temple run", "basket", "werewolf", "subway surfers", "brawl", "tsushima"]):
        category = "Interactive Game"
    elif any(k in combined_text for k in ["literasi", "edukasi", "matematika", "speed typing", "pomodoro", "timer", "kuis", "soal", "frasa", "belajar", "c++", "library", "otak", "neurolearn"]):
        category = "Educational Tool"
    elif any(k in combined_text for k in ["tugasku", "manajemen tugas", "spotfinder", "teman seperjalanan", "codecraft", "kasir", "flight board", "roomcheck"]):
        category = "Productivity Tool"

    return {
        "title": title,
        "author": name,
        "phone": sender_info.get("phone"),
        "raw_sender": sender_info.get("raw_sender"),
        "nim": sender_info.get("nim"),
        "department": sender_info.get("department"),
        "school": sender_info.get("school", "Institut Teknologi Del"),
        "description": desc,
        "objective": obj,
        "demo_url": demo_url,
        "repo_url": repo_url,
        "liberal_art": liberal_art,
        "category": category,
        "source_ref": source_ref,
        "raw_text": cleaned
    }


def parse_projects_from_message(body: str, sender_info: dict, source_ref: str) -> list[dict]:
    """Parse one or multiple projects from a single chat message."""
    cleaned = clean_unicode(body)
    projects = []

    low = cleaned.lower()
    system_phrases = [
        "this message was deleted",
        "added you",
        "added ~",
        "created this group",
        "end-to-end encrypted",
        "<attached:",
        "dear mahasiswa",
        "dimulai pukul",
        "izin ke dosen",
        "bisa hadir di gd713"
    ]
    if any(p in low for p in system_phrases) or re.search(r'\badded\b', low) or len(cleaned) < 30:
        return []

    # Case A: Multi-project message
    if is_multi_project_message(cleaned):
        if re.search(r'(?i)(?:^|\n)\s*proyek\s*1\b', cleaned):
            # Proyek 1 ... Proyek 2 (e.g. Annisa Margareth Manalu)
            parts = [p.strip() for p in re.split(r'(?i)(?=(?:^|\n)\s*proyek\s*\d+\b)', cleaned) if p.strip()]
            for idx, part in enumerate(parts, 1):
                proj = parse_single_project_block(part, sender_info, f"{source_ref}#proyek{idx}", default_author=sender_info["display_name"])
                if proj:
                    projects.append(proj)
        else:
            # Numbered project titles (e.g. Wendy Simanjuntak, Briant Sinaga)
            headings = find_project_headings(cleaned)
            header = cleaned[:headings[0][0]] if headings else ""
            overall_name = sender_info["display_name"]
            m_name = re.search(r'(?i)(?:^|\n|\*)\s*(?:#+\s*)?(?:nama|author)\s*(?:lengkap|pengembang|siswa|mahasiswa)?\s*[:：\t]+\s*([^\n\r]+)', header)
            if m_name:
                cand = m_name.group(1).strip().strip("*\"'#: ")
                if "(SUD)" in cand:
                    sender_info["school"] = "SMA Unggul Del (SUD)"
                elif "(IT Del)" in cand:
                    sender_info["school"] = "Institut Teknologi Del"
                cand = re.sub(r'\s*LAPORAN.*$', '', cand, flags=re.IGNORECASE)
                cand = re.sub(r'\s*\((?:SUD|IT Del)\)', '', cand)
                if len(cand) > 2:
                    overall_name = cand.title()

            for idx in range(len(headings)):
                start = headings[idx][0]
                end = headings[idx + 1][0] if idx + 1 < len(headings) else len(cleaned)
                part = cleaned[start:end].strip()
                proj = parse_single_project_block(part, sender_info, f"{source_ref}#part{idx+1}", default_author=overall_name)
                if proj:
                    projects.append(proj)
    else:
        # Case B: Single project message (including Honey's numbered form)
        proj = parse_single_project_block(cleaned, sender_info, source_ref)
        if proj:
            projects.append(proj)

    return projects


def parse_attachments(messages: list[dict]) -> list[dict]:
    """Inspect and unpack any attached zip or markdown files across all historical exports."""
    attachment_projects = []

    # Gather all zip attachments from all historical export directories
    zip_files_dict = {}
    for exp_dir in sorted(EXPORTS_DIR.glob("export_*")):
        for zf in exp_dir.glob("*.zip"):
            if zf.name not in zip_files_dict:
                zip_files_dict[zf.name] = (zf, exp_dir)

    for zf_name, (zf_path, exp_dir) in zip_files_dict.items():
        sender_info = {"display_name": "Unknown", "nim": None, "department": None, "phone": None, "school": "Institut Teknologi Del"}
        for msg in messages:
            if zf_path.name in msg["body"]:
                sender_info = extract_sender_info(msg["sender"])
                break

        unpacked_dir = exp_dir / f"unpacked_{zf_path.stem}"
        unpacked_dir.mkdir(parents=True, exist_ok=True)
        try:
            with zipfile.ZipFile(zf_path, 'r') as zf:
                zf.extractall(unpacked_dir)

            # Remove any nested .git directories to prevent submodule gitlink conflicts
            for git_dir in unpacked_dir.rglob(".git"):
                if git_dir.is_dir():
                    shutil.rmtree(git_dir, ignore_errors=True)

            doc_files = list(unpacked_dir.rglob("*.md")) + list(unpacked_dir.rglob("*.txt"))
            
            # Detect common author across files or from directory name
            inferred_author = None
            dir_name = zf_path.stem
            if "deskripsi_proyek_" in dir_name or "deskripsi proyek " in dir_name or "Deskripsi Proyek " in dir_name:
                author_part = dir_name.replace("deskripsi_proyek_", "").replace("deskripsi proyek ", "").replace("Deskripsi Proyek ", "").replace("_", " ")
                author_part = re.sub(r'^\d+-', '', author_part)
                inferred_author = author_part.title().strip(":# ")
            elif "EcoSim" in dir_name:
                inferred_author = "Nadine Hutapea"
            elif "Dokumentasi_TugasKu" in dir_name:
                inferred_author = "Dominggo Rajagukguk"
            elif "Markdown" in dir_name:
                inferred_author = "Nathania Pelita Sitohang"
                sender_info["school"] = "SMA Unggul Del (SUD)"

            for doc in doc_files:
                if "__MACOSX" in str(doc) or doc.name.startswith("._") or doc.name.endswith(".COMMIT_EDITMSG"):
                    continue
                try:
                    text = clean_unicode(doc.read_text(encoding="utf-8", errors="replace"))
                    cand = extract_field_value(text, r'(?:nama\s*(?:lengkap|pengembang|siswa|mahasiswa)?|author|dibuat\s*oleh)')
                    if cand and len(cand) > 3 and not any(k in cand.lower() for k in ["laporan", "projek", "aplikasi", "game"]):
                        inferred_author = cand.title().strip(":# ")
                        break
                except Exception:
                    pass

            for doc in doc_files:
                if "__MACOSX" in str(doc) or doc.name.startswith("._") or doc.name.endswith(".COMMIT_EDITMSG") or doc.name == "RundOwn.txt":
                    continue
                with open(doc, "r", encoding="utf-8", errors="replace") as f:
                    doc_content = clean_unicode(f.read())

                if "## Proyek 1:" in doc_content and "## Proyek 2:" in doc_content:
                    parts = [part.strip() for part in re.split(r"(?=##\s*Proyek\s*\d+:)", doc_content) if part.strip() and "## Proyek" in part]
                    for idx, part in enumerate(parts, 1):
                        proj = parse_single_project_block(
                            part,
                            sender_info,
                            f"attachment:{zf_path.name}/{doc.name}#proyek{idx}",
                            default_author=inferred_author
                        )
                        if proj:
                            attachment_projects.append(proj)
                else:
                    proj = parse_single_project_block(
                        doc_content, 
                        sender_info, 
                        f"attachment:{zf_path.name}/{doc.name}",
                        default_author=inferred_author
                    )
                    if proj:
                        attachment_projects.append(proj)
        except Exception as e:
            print(f"[!] Error unpacking attachment {zf_path.name}: {e}")

    return attachment_projects


def parse_chat_messages(chat_txt: Path) -> list[dict]:
    """Parse WhatsApp text messages into structured entries with full multi-line support."""
    with open(chat_txt, "r", encoding="utf-8", errors="replace") as f:
        raw_content = f.read()

    content = clean_unicode(raw_content)

    pattern = re.compile(
        r'^\[(\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}),?\s+(\d{1,2}[.:]\d{2}(?:[.:]\d{2})?)\]\s+(?:~[\s]*|)([^:]+?):\s*',
        re.MULTILINE
    )

    matches = list(pattern.finditer(content))
    messages = []

    for i, match in enumerate(matches):
        date_str = match.group(1)
        time_str = match.group(2)
        sender = match.group(3)
        start_idx = match.end()
        end_idx = matches[i + 1].start() if i + 1 < len(matches) else len(content)

        msg_body = content[start_idx:end_idx].strip()
        messages.append({
            "date": date_str,
            "time": time_str,
            "sender": sender,
            "body": msg_body
        })

    return messages


def build_wiki_page(proj: dict) -> str:
    """Generate AGENTS.md-compliant Markdown for an individual project with English translations."""
    title = proj['title']
    title_en = proj.get('title_en', title)
    author = proj['author']
    date_str = datetime.now().strftime("%Y-%m-%d")
    nim_str = f" ({proj['nim']})" if proj.get('nim') else ""
    dept_str = f" - Prodi {proj['department']}" if proj.get('department') else ""
    phone_str = f" | WA Handle: `{proj['raw_sender'] or proj['phone']}`" if (proj.get('phone') or proj.get('raw_sender')) else ""

    links_block = []
    if proj.get('demo_url'):
        links_block.append(f"- **Live Demo**: [{proj['demo_url']}]({proj['demo_url']})")
    if proj.get('repo_url'):
        links_block.append(f"- **GitHub Repository**: [{proj['repo_url']}]({proj['repo_url']})")
    if not links_block:
        links_block.append("- **Repository / Demo**: *Pending submission by student*")

    content = f"""---
title: "{title}"
title_en: "{title_en}"
date: {date_str}
author: "{author}"
nim: "{proj.get('nim') or ''}"
department: "{proj.get('department') or ''}"
school: "{proj.get('school', 'Institut Teknologi Del')}"
category: "{proj['category']}"
type: concept
tags: [IT-Del, Student-Project, {proj['category'].replace(' ', '-')}, {proj['liberal_art']}]
status: stable
liberal_art: {proj['liberal_art']}
demo_url: "{proj.get('demo_url') or ''}"
repo_url: "{proj.get('repo_url') or ''}"
source_ref: "{proj.get('source_ref')}"
---

# {title}

> **English Title**: *{title_en}*  
> **Student / Author**: [[{slugify(author)}|{author}]]{nim_str}{dept_str}  
> **Institution**: {proj.get('school', 'Institut Teknologi Del')}{phone_str}  
> **Category**: `{proj['category']}` | **Liberal Art Mode**: `[[{proj['liberal_art'].split('-')[0]}|{proj['liberal_art']}]]`  

---

## 1. Deskripsi Proyek (Indonesian)
{proj['description'] or '*Deskripsi belum diserahkan.*'}

## 2. Project Description (English Translation)
{proj.get('desc_en') or '*English description pending.*'}

---

## 3. Tujuan Proyek (Indonesian Objectives)
{proj['objective'] or '*Tujuan proyek belum diserahkan.*'}

## 4. Project Objectives (English Translation)
{proj.get('obj_en') or '*English objectives pending.*'}

---

## 5. Technical Verification & Delivery Status
{chr(10).join(links_block)}
- **Delivery Mode**: {proj['category']}
- **Source Reference**: `{proj.get('source_ref')}`
- **Repository Status**: {'[Verified Live]' if proj.get('repo_url') else '[Pending Link]'}
"""
    return content


def run_pipeline(custom_zip=None):
    """Main execution workflow."""
    print("=== Starting IT Del WhatsApp Ingestion Pipeline ===")

    # 1. Find & Archive Export
    latest_zip = find_latest_export(custom_zip)
    print(f"[*] Processing newest export archive: {latest_zip.name}")
    export_dir, chat_txt = archive_export(latest_zip)
    print(f"[*] Archived to: {export_dir.relative_to(BASE_DIR)}")

    # 2. Parse Messages from all historical exports to guarantee zero lost deleted messages
    all_chat_projects = []
    recent_project_by_sender = {}
    audit_log = []

    # Get latest export messages for audit log
    latest_messages = parse_chat_messages(chat_txt)
    print(f"[*] Found {len(latest_messages)} chat messages in latest export.")

    for exp_dir in sorted(EXPORTS_DIR.glob("export_*")):
        c_txt = exp_dir / "_chat.txt"
        if c_txt.exists():
            exp_msgs = parse_chat_messages(c_txt)
            for msg in exp_msgs:
                s_info = extract_sender_info(msg["sender"])
                s_key = s_info["nim"] or s_info["phone"] or s_info["display_name"]
                projs = parse_projects_from_message(msg["body"], s_info, f"_chat.txt@{msg['date']} {msg['time']}")
                if projs:
                    for p in projs:
                        all_chat_projects.append(p)
                        recent_project_by_sender[s_key] = p
                else:
                    demo_url, repo_url = extract_links(msg["body"])
                    if (demo_url or repo_url) and s_key in recent_project_by_sender:
                        target_proj = recent_project_by_sender[s_key]
                        if demo_url and not target_proj["demo_url"]:
                            target_proj["demo_url"] = demo_url
                        if repo_url and not target_proj["repo_url"]:
                            target_proj["repo_url"] = repo_url

    # Populate audit log for latest messages
    for msg in latest_messages:
        s_info = extract_sender_info(msg["sender"])
        s_key = s_info["nim"] or s_info["phone"] or s_info["display_name"]
        projs = parse_projects_from_message(msg["body"], s_info, f"_chat.txt@{msg['date']} {msg['time']}")
        if projs:
            audit_log.append({
                "timestamp": f"{msg['date']} {msg['time']}",
                "sender": msg["sender"],
                "type": "PROJECT_SUBMISSION",
                "summary": f"Submitted {len(projs)} project(s): {', '.join([p['title'] for p in projs])}",
                "status": "PARSED"
            })
        else:
            demo_url, repo_url = extract_links(msg["body"])
            if demo_url or repo_url:
                audit_log.append({
                    "timestamp": f"{msg['date']} {msg['time']}",
                    "sender": msg["sender"],
                    "type": "FOLLOWUP_LINK",
                    "summary": f"Submitted link: {repo_url or demo_url}",
                    "status": "MERGED"
                })
            elif "<attached:" in msg["body"]:
                audit_log.append({
                    "timestamp": f"{msg['date']} {msg['time']}",
                    "sender": msg["sender"],
                    "type": "ATTACHMENT",
                    "summary": msg["body"],
                    "status": "UNPACKED"
                })
            elif "deleted" in msg["body"].lower():
                audit_log.append({
                    "timestamp": f"{msg['date']} {msg['time']}",
                    "sender": msg["sender"],
                    "type": "CHAT_DELETION",
                    "summary": "Message deleted in WhatsApp (preserved historically)",
                    "status": "PRESERVED"
                })
            else:
                audit_log.append({
                    "timestamp": f"{msg['date']} {msg['time']}",
                    "sender": msg["sender"],
                    "type": "CHAT_MESSAGE",
                    "summary": (msg["body"][:100] + "...") if len(msg["body"]) > 100 else msg["body"],
                    "status": "ARCHIVED"
                })

    # 3. Second Pass: Process Attachments across all exports
    attachment_projects = parse_attachments(latest_messages)
    print(f"[*] Found {len(attachment_projects)} projects inside attachments.")

    all_raw_projects = all_chat_projects + attachment_projects
    print(f"[*] Total raw project submissions collected: {len(all_raw_projects)}")

    # 4. English Translations & Deduplication into Students DB
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    STUDENTS_DIR.mkdir(parents=True, exist_ok=True)

    students_db = {}
    missing_links_by_student = {}

    for proj in all_raw_projects:
        author_name = proj["author"] or "Anonymous Student"
        author_slug = slugify(author_name)
        title_slug = slugify(proj["title"])

        # Translate to English
        translation = get_project_translation(proj["title"], proj["description"], proj["objective"], title_slug)
        proj["title_en"] = translation["title_en"]
        proj["desc_en"] = translation["desc_en"]
        proj["obj_en"] = translation["obj_en"]

        if author_slug not in students_db:
            students_db[author_slug] = {
                "name": author_name,
                "phone": proj.get("phone"),
                "raw_sender": proj.get("raw_sender"),
                "nim": proj.get("nim"),
                "department": proj.get("department"),
                "school": proj.get("school", "Institut Teknologi Del"),
                "projects": {}
            }
        else:
            if proj.get("phone") and not students_db[author_slug].get("phone"):
                students_db[author_slug]["phone"] = proj.get("phone")
            if proj.get("nim") and not students_db[author_slug].get("nim"):
                students_db[author_slug]["nim"] = proj.get("nim")
            if proj.get("department") and not students_db[author_slug].get("department"):
                students_db[author_slug]["department"] = proj.get("department")
            if proj.get("school") == "SMA Unggul Del (SUD)":
                students_db[author_slug]["school"] = "SMA Unggul Del (SUD)"

        # Merge / deduplicate project under student
        matched_key = None
        if title_slug in students_db[author_slug]["projects"]:
            matched_key = title_slug
        else:
            for ex_slug in students_db[author_slug]["projects"].keys():
                if (title_slug.startswith(ex_slug) or ex_slug.startswith(title_slug) or
                    (len(title_slug) > 6 and len(ex_slug) > 6 and title_slug[:8] == ex_slug[:8])):
                    matched_key = ex_slug
                    break

        if matched_key:
            existing_p = students_db[author_slug]["projects"][matched_key]
            if proj.get("demo_url") and not existing_p.get("demo_url"):
                existing_p["demo_url"] = proj["demo_url"]
            if proj.get("repo_url") and not existing_p.get("repo_url"):
                existing_p["repo_url"] = proj["repo_url"]
            if proj.get("description"):
                if not existing_p.get("description"):
                    existing_p["description"] = proj["description"]
                    existing_p["desc_en"] = proj["desc_en"]
                elif proj["description"] not in existing_p["description"]:
                    if len(proj["description"]) > len(existing_p["description"]):
                        existing_p["description"] = f"{proj['description']}\n\n{existing_p['description']}"
                    else:
                        existing_p["description"] = f"{existing_p['description']}\n\n{proj['description']}"
            if proj.get("objective"):
                if not existing_p.get("objective"):
                    existing_p["objective"] = proj["objective"]
                    existing_p["obj_en"] = proj["obj_en"]
                elif proj["objective"] not in existing_p["objective"]:
                    existing_p["objective"] = f"{existing_p['objective']}\n{proj['objective']}".strip()
        else:
            students_db[author_slug]["projects"][title_slug] = proj

    # 5. Clean up old markdown files & Write Individual Project Pages & Track Missing Links
    for old_file in PROJECTS_DIR.glob("*.md"):
        old_file.unlink()
    for old_file in STUDENTS_DIR.glob("*.md"):
        old_file.unlink()

    for author_slug, s_data in students_db.items():
        for title_slug, proj in s_data["projects"].items():
            if not (proj.get("repo_url") or proj.get("demo_url")):
                if s_data["name"] not in missing_links_by_student:
                    missing_links_by_student[s_data["name"]] = {
                        "nim": s_data.get("nim"),
                        "phone": s_data.get("phone"),
                        "raw_sender": s_data.get("raw_sender"),
                        "titles": []
                    }
                missing_links_by_student[s_data["name"]]["titles"].append(f"{proj['title']} ({proj['title_en']})")

            page_filename = f"{author_slug}_{title_slug}.md"
            page_path = PROJECTS_DIR / page_filename
            page_content = build_wiki_page(proj)
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(page_content)

    # 6. Write Student Portfolio Pages
    for s_slug, s_data in students_db.items():
        s_name = s_data["name"]
        nim_txt = f" ({s_data['nim']})" if s_data.get("nim") else ""
        dept_txt = f" — Prodi {s_data['department']}" if s_data.get("department") else ""
        contact_txt = f" | WA Handle: `{s_data.get('raw_sender') or s_data.get('phone')}`" if (s_data.get('raw_sender') or s_data.get('phone')) else ""
        s_file = STUDENTS_DIR / f"{s_slug}.md"

        projs_table = [
            "| # | Project Title (Original / English) | Type / Category | Liberal Art | Description (Indonesian & English) | Links | Status |",
            "| :---: | :--- | :--- | :--- | :--- | :--- | :--- |"
        ]
        for p_idx, (p_slug, p_val) in enumerate(s_data["projects"].items(), 1):
            p_file = f"[[{s_slug}_{slugify(p_val['title'])}\\|{p_val['title']}]]"
            t_en = p_val.get('title_en', p_val['title'])
            en_str = f"<br>*{t_en}*" if t_en != p_val['title'] else ""
            links_list = []
            if p_val.get("demo_url"): links_list.append(f"[Demo]({p_val['demo_url']})")
            if p_val.get("repo_url"): links_list.append(f"[Repo]({p_val['repo_url']})")
            links_txt = " · ".join(links_list) if links_list else "*Pending*"
            status_txt = "`Live` ✅" if (p_val.get("repo_url") or p_val.get("demo_url")) else "`Pending Link` ⚠️"
            desc_cell = f"**ID**: {format_table_cell(p_val.get('description', ''), 200)}<br><br>**EN**: {format_table_cell(p_val.get('desc_en', ''), 200)}"
            projs_table.append(f"| {p_idx} | **{p_file}**{en_str} | `{p_val['category']}` | `{p_val['liberal_art']}` | {desc_cell} | {links_txt} | {status_txt} |")

        student_content = f"""---
title: "Student Profile: {s_name}"
date: {datetime.now().strftime("%Y-%m-%d")}
author: "{s_name}"
nim: "{s_data.get('nim') or ''}"
department: "{s_data.get('department') or ''}"
school: "{s_data.get('school', 'Institut Teknologi Del')}"
phone: "{s_data.get('phone') or ''}"
raw_sender: "{s_data.get('raw_sender') or ''}"
type: note
tags: [IT-Del, Student, Profile]
status: stable
---

# Student Profile: {s_name}{nim_txt}{dept_txt}

> **Institution**: {s_data.get('school', 'Institut Teknologi Del')}  
> **Contact / WhatsApp**: `{s_data.get('raw_sender') or s_data.get('phone') or '-'}`  
> **Total Submitted Projects**: `{len(s_data['projects'])}`  

## 📂 Submitted Projects Portfolio (Indonesian & English)

{chr(10).join(projs_table)}
"""
        with open(s_file, "w", encoding="utf-8") as f:
            f.write(student_content)

    # 7. Write Master Categorized Matrix (student_project_matrix.md)
    with open(MATRIX_FILE, "w", encoding="utf-8") as f:
        f.write(f"""---
title: "IT Del & SUD Student Project Matrix"
date: {datetime.now().strftime("%Y-%m-%d")}
type: synthesis
tags: [IT-Del, SUD, Matrix, Student-Projects]
status: stable
liberal_art: Quadrivium-Geometry
---

# IT Del & SUD Student Project Matrix

> Master categorization of all student projects by **Creator (Who Did It)**, **Contact / WhatsApp Handle**, **School & NIM**, **Project Type**, and **Titles & Descriptions (Original Indonesian & English)**.  
> Every project has its own row, with all projects by the same creator grouped consecutively next to each other.  
> Last synchronized on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.  
> **Downloadable Datasets**: [Full Projects CSV](student_projects.csv) · [Student Summary CSV](student_summary.csv)

## 1. Master Projects Matrix (Consecutive Project Rows by Creator)

| # | Student / Creator | Contact & NIM | Project Title (ID / EN) | Category & Art | Description (Indonesian & English) | Status & Links |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
""")
        row_idx = 1
        for s_slug, s_data in sorted(students_db.items(), key=lambda x: x[1]['name']):
            total_proj = len(s_data['projects'])
            contact = s_data.get('raw_sender') or s_data.get('phone') or '-'
            nim_str = s_data.get('nim') or ''
            dept_str = f"({s_data.get('department')})" if s_data.get('department') else ''
            school_str = s_data.get('school', 'Institut Teknologi Del')

            contact_cell = f"`{contact}`"
            if nim_str:
                contact_cell += f"<br>{nim_str} {dept_str}"
            contact_cell += f"<br>*{school_str}*"

            for p_idx, (p_slug, p_val) in enumerate(s_data['projects'].items(), 1):
                s_cell = f"[[{s_slug}\\|{s_data['name']}]]"
                if total_proj > 1:
                    s_cell += f"<br>*(Project {p_idx}/{total_proj})*"

                t_id = p_val['title']
                t_en = p_val.get('title_en', t_id)
                p_file_slug = f"{s_slug}_{slugify(p_val['title'])}"
                p_link = f"[[{p_file_slug}\\|{t_id}]]"
                title_cell = f"**{p_link}**"
                if t_en != t_id:
                    title_cell += f"<br>*{t_en}*"

                cat_cell = f"`{p_val['category']}`<br>*{p_val['liberal_art']}*"

                desc_id = format_table_cell(p_val.get('description', ''), 280)
                desc_en = format_table_cell(p_val.get('desc_en', ''), 280)
                desc_cell = f"**ID**: {desc_id}<br><br>**EN**: {desc_en}"

                links = []
                if p_val.get('demo_url'):
                    links.append(f"[Demo]({p_val['demo_url']})")
                if p_val.get('repo_url'):
                    links.append(f"[Repo]({p_val['repo_url']})")
                status_txt = "`Live` ✅" if links else "`Pending Link` ⚠️"
                status_cell = f"{status_txt}"
                if links:
                    status_cell += "<br>" + " · ".join(links)

                f.write(f"| {row_idx} | {s_cell} | {contact_cell} | {title_cell} | {cat_cell} | {desc_cell} | {status_cell} |\n")
                row_idx += 1

        f.write(f"""
---

## 2. Summary by Student (At-a-Glance)

| # | Student Name | Contact / WA Handle | NIM / School | Total | Submitted Projects | Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
""")
        for s_idx, (s_slug, s_data) in enumerate(sorted(students_db.items(), key=lambda x: x[1]['name']), 1):
            s_name = f"[[{s_slug}\\|{s_data['name']}]]"
            contact = f"`{s_data.get('raw_sender') or s_data.get('phone') or '-'}`"
            nim_school = f"{s_data.get('nim')} ({s_data.get('department')})" if s_data.get('nim') else s_data.get('school', 'IT Del')
            total_proj = len(s_data['projects'])

            proj_items = []
            has_pending = False
            for p_slug, p_val in s_data['projects'].items():
                p_link = f"[[{s_slug}_{slugify(p_val['title'])}\\|{p_val['title']}]]"
                t_en = p_val.get('title_en', p_val['title'])
                en_display = f" (*{t_en}*)" if t_en != p_val['title'] else ""
                cat = p_val['category']
                if not (p_val.get('repo_url') or p_val.get('demo_url')):
                    has_pending = True
                    proj_items.append(f"• **{p_link}**{en_display} (`{cat}`) ⚠️")
                else:
                    proj_items.append(f"• **{p_link}**{en_display} (`{cat}`) ✅")

            proj_cell = "<br>".join(proj_items)
            status_cell = "`Pending Link` ⚠️" if has_pending else "`Complete` ✅"
            f.write(f"| {s_idx} | {s_name} | {contact} | {nim_school} | `{total_proj}` | {proj_cell} | {status_cell} |\n")

    # 8. Generate CSV Exports
    with open(CSV_PROJECTS_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "student_name",
            "contact_handle",
            "phone_number",
            "nim",
            "department",
            "school",
            "project_title_id",
            "project_title_en",
            "category",
            "liberal_art",
            "description_id",
            "description_en",
            "objective_id",
            "objective_en",
            "demo_url",
            "repo_url",
            "status",
            "source_ref"
        ])
        for s_slug, s_data in sorted(students_db.items(), key=lambda x: x[1]['name']):
            for p_slug, p in s_data["projects"].items():
                status_val = "Complete" if (p.get("repo_url") or p.get("demo_url")) else "Pending Link"
                writer.writerow([
                    s_data["name"],
                    s_data.get("raw_sender") or "",
                    s_data.get("phone") or "",
                    s_data.get("nim") or "",
                    s_data.get("department") or "",
                    s_data.get("school") or "Institut Teknologi Del",
                    p["title"],
                    p.get("title_en", p["title"]),
                    p["category"],
                    p["liberal_art"],
                    p.get("description", ""),
                    p.get("desc_en", ""),
                    p.get("objective", ""),
                    p.get("obj_en", ""),
                    p.get("demo_url", ""),
                    p.get("repo_url", ""),
                    status_val,
                    p.get("source_ref", "")
                ])

    with open(CSV_SUMMARY_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "student_name",
            "contact_handle",
            "phone_number",
            "nim",
            "department",
            "school",
            "total_projects",
            "projects_en",
            "categories",
            "status"
        ])
        for s_slug, s_data in sorted(students_db.items(), key=lambda x: x[1]['name']):
            projs = list(s_data["projects"].values())
            has_pending = any(not (p.get("repo_url") or p.get("demo_url")) for p in projs)
            status_val = "Pending Link" if has_pending else "Complete"
            titles_en_str = " | ".join([p.get("title_en", p["title"]) for p in projs])
            cats_str = ", ".join(sorted(list(set([p["category"] for p in projs]))))
            writer.writerow([
                s_data["name"],
                s_data.get("raw_sender") or "",
                s_data.get("phone") or "",
                s_data.get("nim") or "",
                s_data.get("department") or "",
                s_data.get("school") or "Institut Teknologi Del",
                len(projs),
                titles_en_str,
                cats_str,
                status_val
            ])

    # 9. Write Lossless Chat Audit Log
    with open(AUDIT_FILE, "w", encoding="utf-8") as f:
        f.write(f"""---
title: "IT Del Chat Ingestion Audit Log"
date: {datetime.now().strftime("%Y-%m-%d")}
type: changelog
tags: [IT-Del, Audit, Ingestion]
status: stable
---

# Lossless Chat Audit Log

> Exhaustive audit of all {len(latest_messages)} messages from latest WhatsApp export (`{latest_zip.name}`).

| Timestamp | Sender Handle | Event Type | Summary Content | Audit Status |
| :--- | :--- | :--- | :--- | :--- |
""")
        for item in audit_log:
            sender_clean = clean_unicode(item["sender"]).replace("|", "-")
            summary_clean = clean_unicode(item["summary"]).replace("|", "-").replace("\n", " ")[:120]
            f.write(f"| {item['timestamp']} | {sender_clean} | `{item['type']}` | {summary_clean} | {item['status']} |\n")

    # 10. Write Copy-Paste WhatsApp Action Reminders
    with open(PENDING_FILE, "w", encoding="utf-8") as f:
        f.write(f"""---
title: "Pending Action Reminders — IT Del Projects"
date: {datetime.now().strftime("%Y-%m-%d")}
type: note
tags: [IT-Del, Reminders, Action-Items]
status: stable
---

# Pending Action Reminders — IT Del Projects

> Generated list of students who have registered project specifications but have not yet provided their live GitHub Repository or Demo deployment links.

## 📋 Action Checklist ({len(missing_links_by_student)} Students Pending)

""")
        for s_name, data in sorted(missing_links_by_student.items()):
            nim_info = f" ({data['nim']})" if data['nim'] else ""
            handle_info = f" — WA: `{data['raw_sender'] or data['phone']}`" if (data['raw_sender'] or data['phone']) else ""
            f.write(f"- [ ] **{s_name}**{nim_info}{handle_info}:\n")
            for t in data["titles"]:
                f.write(f"  - Proyek: *{t}*\n")

        f.write("""
---

## 💬 Pre-formatted Group Reminder Message

```text
Halo teman-teman peserta Conversational Programming & AI Systems! 🚀

Berdasarkan sinkronisasi proyek terbaru, kami telah mencatat spesifikasi proyek teman-teman ke dalam master showcase wiki & CSV database.

Bagi teman-teman berikut yang belum mengirimkan link GitHub Repository atau Live Demo (Vercel/GitHub Pages):

""")
        for idx, (s_name, data) in enumerate(sorted(missing_links_by_student.items()), 1):
            nim_str = f" ({data['nim']})" if data['nim'] else ""
            f.write(f"{idx}. {s_name}{nim_str} — {', '.join(data['titles'])}\n")

        f.write("""
Mohon dapat segera mengirimkan link repo GitHub dan link live demo-nya langsung di grup ini agar portofolio proyek kalian dapat segera diuji dan ditampilkan lengkap di dashboard showcase kampus! Terima kasih. 🙏
```
""")

    # 11. Write Central Dashboard (README.md)
    total_students = len(students_db)
    total_projects = sum(len(s["projects"]) for s in students_db.values())
    pending_count = sum(len(v["titles"]) for v in missing_links_by_student.values())

    with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
        f.write(f"""---
title: "IT Del & SUD Student Projects Showcase Hub"
date: {datetime.now().strftime("%Y-%m-%d")}
type: overview
tags: [IT-Del, SUD, Showcase, Projects, Curriculum]
status: stable
liberal_art: Quadrivium-Music
---

# IT Del & SUD Student Projects Showcase Hub

> **Context**: Conversational Programming, Prompt Engineering & AI Systems Workshop  
> **Cohorts**: Institut Teknologi Del (Informatika, Sistem Informasi, Teknik Elektro) & SMA Unggul Del (SUD)  
> **Last Synchronized**: `{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}`  
> **Source Origin**: `{latest_zip.name}` ({len(latest_messages)} chat interactions analyzed)

---

## 📊 Workshop Overview & Real-Time Metrics

- **Registered Students**: `{total_students}`
- **Total Cataloged Projects**: `{total_projects}`
- **Verified Deliveries**: `{total_projects - pending_count}`
- **Pending Link Verification**: `{pending_count}`
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
""")

    # Save updated registry
    registry = {
        "students": students_db,
        "last_updated": datetime.now().isoformat(),
        "last_export_source": str(latest_zip)
    }
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)

    print("\n=== Pipeline Execution Completed Successfully ===")
    print(f"[✓] Students recorded: {total_students}")
    print(f"[✓] Total projects cataloged: {total_projects}")
    print(f"[✓] Students pending links: {len(missing_links_by_student)} ({pending_count} projects)")
    print(f"[✓] Master matrix written: docs/teaching/itdel_projects/student_project_matrix.md")
    print(f"[✓] Projects CSV written: docs/teaching/itdel_projects/student_projects.csv")
    print(f"[✓] Summary CSV written: docs/teaching/itdel_projects/student_summary.csv")
    print(f"[✓] Dashboard written: docs/teaching/itdel_projects/README.md")
    print(f"[✓] Audit log written: docs/teaching/itdel_projects/chat_audit.md")
    print(f"[✓] Reminders written: docs/teaching/itdel_projects/missing_or_pending.md")


if __name__ == "__main__":
    custom_zip_arg = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None
    run_pipeline(custom_zip_arg)
