---
title: "Blink LED ESP32-C3 Super Mini"
title_en: "Blink LED ESP32-C3 Super Mini Embedded Controller"
date: 2026-09-22
author: "Nakula Nathanael Gultom"
nim: ""
department: ""
school: "Institut Teknologi Del"
category: "IoT & Hardware"
type: concept
tags: [IT-Del, Student-Project, IoT-&-Hardware, Quadrivium-Astronomy]
status: stable
liberal_art: Quadrivium-Astronomy
demo_url: ""
repo_url: ""
source_ref: "attachment:00003032-deskripsi_proyek_nakula_nathanael_gultom.zip/PROJECT3.md"
---

# Blink LED ESP32-C3 Super Mini

> **English Title**: *Blink LED ESP32-C3 Super Mini Embedded Controller*  
> **Student / Author**: [[nakula-nathanael-gultom|Nakula Nathanael Gultom]]  
> **Institution**: Institut Teknologi Del | WA Handle: `nathan`  
> **Category**: `IoT & Hardware` | **Liberal Art Mode**: `[[Quadrivium|Quadrivium-Astronomy]]`  

---

## 1. Deskripsi Proyek (Indonesian)
PROJEK :

Proyek ini adalah implementasi dasar mikrokontroler ESP32-C3 Super Mini untuk mengontrol indikator lampu LED bawaan (*on-board LED*) yang terhubung pada pin GPIO 8. Program mengeksekusi logika *Active LOW* di mana LED akan menyala saat sinyal `LOW` dikirimkan dan mati saat sinyal `HIGH` dikirimkan secara bergantian dengan interval jeda (*delay*) 1 detik. Selain itu, status aktivasi LED ditransmisikan secara *real-time* ke Serial Monitor pada kecepatan transmisi 115200 bps untuk pemantauan eksekusi kode.

## 2. Project Description (English Translation)
An introductory embedded systems hardware project programming an ESP32-C3 Super Mini microcontroller to drive on-board and external LEDs with custom pulse-width modulation (PWM) and blink sequences.

---

## 3. Tujuan Proyek (Indonesian Objectives)
PROJEK :

1. **Memahami Dasar Sistem Tertanam**: Mempelajari alur pemrograman mikrokontroler ESP32-C3 Super Mini menggunakan arsitektur C/C++ pada Arduino IDE.
2. **Penguasaan Digital I/O**: Memahami konfigurasi pin Output digital, manipulasi status sinyal `HIGH` dan `LOW`, serta karakteristik *Active LOW* pada hardware.
3. **Penggunaan Serial Debugging**: Melatih penggunaan komunikasi serial (*Serial Monitor*) untuk keperluan validasi dan proses penelusuran kesalahan (*debugging*) program.
4. **Pengujian Perangkat Keras**: Mengonfirmasi bahwa board ESP32-C3 dan port komunikasi USB/CDC berfungsi dengan baik sebelum melangkah ke proyek IoT yang lebih kompleks.

## 4. Project Objectives (English Translation)
1. Master GPIO pin configuration, register control, and timer interrupts on ESP32-C3.
2. Establish firmware build and flashing toolchains using Arduino C++ and PlatformIO.
3. Lay the physical hardware foundation for IoT telemetry projects.

---

## 5. Technical Verification & Delivery Status
- **Repository / Demo**: *Pending submission by student*
- **Delivery Mode**: IoT & Hardware
- **Source Reference**: `attachment:00003032-deskripsi_proyek_nakula_nathanael_gultom.zip/PROJECT3.md`
- **Repository Status**: [Pending Link]
