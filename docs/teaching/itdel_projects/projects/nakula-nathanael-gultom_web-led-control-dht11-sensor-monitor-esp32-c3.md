---
title: "Web LED Control & DHT11 Sensor Monitor ESP32-C3"
title_en: "Web LED Control & DHT11 Environmental Sensor Monitor (ESP32-C3)"
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
source_ref: "attachment:00003032-deskripsi_proyek_nakula_nathanael_gultom.zip/PROJECT4.md"
---

# Web LED Control & DHT11 Sensor Monitor ESP32-C3

> **English Title**: *Web LED Control & DHT11 Environmental Sensor Monitor (ESP32-C3)*  
> **Student / Author**: [[nakula-nathanael-gultom|Nakula Nathanael Gultom]]  
> **Institution**: Institut Teknologi Del | WA Handle: `nathan`  
> **Category**: `IoT & Hardware` | **Liberal Art Mode**: `[[Quadrivium|Quadrivium-Astronomy]]`  

---

## 1. Deskripsi Proyek (Indonesian)
PROJEK :

Proyek ini mengombinasikan pengontrolan aktuator (LED) dan pemantauan sensor lingkungan (DHT11) berbasis *Internet of Things* (IoT) menggunakan mikrokontroler ESP32-C3 Super Mini. Perangkat dikonfigurasi sebagai *Access Point* (AP) Wi-Fi mandiri yang menjalankan Web Server HTTP pada port 80. Melalui jaringan Wi-Fi ini, pengguna dapat mengakses antarmuka web interaktif berbasis HTML/CSS dari peramban *smartphone* atau laptop untuk:
1. Mematikan dan menyalakan lampu LED (GPIO 8) secara nirkabel melalui tombol sakelar digital.
2. Membaca dan menampilkan data suhu (°C) serta kelembapan udara (%) dari sensor DHT11 (GPIO 4) secara *real-time* dan otomatis tanpa perlu memperbarui (*refresh*) halaman web secara manual.

## 2. Project Description (English Translation)
A full-stack IoT telemetry prototype deploying an asynchronous web server on an ESP32-C3 to monitor live ambient temperature and humidity from a DHT11 sensor while toggling physical relay LEDs over Wi-Fi.

---

## 3. Tujuan Proyek (Indonesian Objectives)
PROJEK :

1. **Pengembangan Embedded Web Server**: Membangun sistem IoT mandiri di mana ESP32-C3 berfungsi sekaligus sebagai pemancar Wi-Fi dan pelayan web (*web server*) tanpa ketergantungan pada internet luar.
2. **Integrasi Sensor & Aktuator**: Menggabungkan pembacaan data kondisi lingkungan (suhu & kelembapan) dan kontrol perangkat keras (LED) dalam satu sistem yang terintegrasi.
3. **Penerapan Komunikasi HTTP**: Mempelajari alur pertukaran data nirkabel dua arah antara peramban web (*client*) dan mikrokontroler (*server*) menggunakan protokol HTTP request (`GET` & respon HTML/JSON).
4. **Antarmuka Pengguna (UI) Interaktif**: Menyediakan tampilan pemantauan dan kendali nirkabel yang responsif, modern, hemat daya, serta ramah pengguna (*user-friendly*).

## 4. Project Objectives (English Translation)
1. Bridge physical sensor telemetry with a modern web dashboard without cloud reliance.
2. Implement bidirectional asynchronous HTTP/WebSocket communication between ESP32 and browser.
3. Deliver a complete IoT edge sensing and actuator control pipeline.

---

## 5. Technical Verification & Delivery Status
- **Repository / Demo**: *Pending submission by student*
- **Delivery Mode**: IoT & Hardware
- **Source Reference**: `attachment:00003032-deskripsi_proyek_nakula_nathanael_gultom.zip/PROJECT4.md`
- **Repository Status**: [Pending Link]
