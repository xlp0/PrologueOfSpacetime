# 1. Judul
**TugasKu — Aplikasi Web Pengelola List PR, Kalender & Pengingat Tugas Interaktif**

# 2. Nama
**Dominggo Rajagukguk**

# 3. Deskripsi Produk
**TugasKu** adalah aplikasi web manajemen tugas dan pekerjaan rumah (PR) berbasis *client-side* yang dirancang modern, responsif, dan bebas dependensi eksternal. Aplikasi ini menyediakan tiga tampilan visual utama: **Kalender Bulanan** untuk melihat sebaran jadwal tenggat secara komprehensif, **Daftar PR Dinamis** yang dikelompokkan berdasarkan batas waktu urgensi, dan **Papan Kanban** untuk memantau status pengerjaan (*To Do*, *In Progress*, *Done*). TugasKu dilengkapi fitur *checklist* subtugas terukur, lampiran tautan referensi materi (LMS/Drive), multi-filter pencarian cepat, sistem pengingat deadline kritis berbasis *Web Audio API* & notifikasi peramban, serta fitur pencadangan data cadangan (JSON) yang tersimpan aman di *LocalStorage*.

# 4. Tujuan Produk
Tujuan utama pengembangan produk **TugasKu** meliputi:
* **Mencegah Keterlambatan**: Memberikan peringatan dini dan indikator visual terhadap PR yang mendekati batas waktu pengumpulan (*deadline*).
* **Meningkatkan Manajemen Waktu**: Membantu siswa dan mahasiswa merencanakan jadwal belajar secara terstruktur melalui visualisasi kalender interaktif.
* **Menyederhanakan Tugas Kompleks**: Membantu pengguna memecah tugas-tugas besar menjadi langkah-langkah kecil (*subtasks*) yang lebih terarah dan terukur.
* **Mendorong Produktivitas Mandiri**: Menyediakan sarana pengelolaan tugas belajar yang praktis, cepat, dan aman tanpa bergantung pada koneksi server eksternal.

---

## 🌟 Fitur Utama

### 1. 📅 Tampilan Kalender Interaktif (*Calendar View*)
* **Grid Kalender Bulanan**: Navigasi bulan fleksibel (*Bulan Sebelumnya*, *Hari Ini*, *Bulan Berikutnya*).
* **Chip Tugas Visual**: Tugas ditampilkan langsung pada tanggal jatuh tempo (*due date*) dengan label warna sesuai mata pelajaran.
* **Klik Tanggal & Popover Cepat**: Klik pada sel tanggal mana saja untuk melihat ringkasan tugas di tanggal tersebut atau langsung menambahkan PR baru dengan tanggal yang sudah terisi otomatis.

### 2. 📋 Tampilan Daftar PR Dinamis (*List View*)
* **Pengelompokan Otomatis**: Membagi tugas ke dalam 3 kategori utama:
  * 🔴 **Mendesak & Hari Ini / Terlewat** (*Urgent & Due Today*)
  * 🟡 **Mendatang** (*Upcoming*)
  * 🟢 **Sudah Selesai** (*Completed*)
* **Kartu Tugas Informatif**: Menampilkan subjek, tingkat prioritas (*Tinggi*, *Sedang*, *Rendah*), countdown waktu relatif, dan *progress bar* penyelesaian subtugas.
* **Aksi Cepat**: Centang langsung untuk menyelesaikan tugas, buka modal detail, edit, atau hapus tugas.

### 3. 📊 Papan Kanban (*Kanban Board View*)
* **Visualisasi Alur Kerja**: 3 kolom status:
  * 📝 **Belum Dikerjakan** (*To Do*)
  * ⏳ **Sedang Dikerjakan** (*In Progress*)
  * ✅ **Sudah Selesai** (*Done*)
* **Interaktivitas Cepat**: Pindahkan status tugas antar kolom hanya dengan satu klik atau gunakan kartu ringkas untuk memantau beban kerja.

### 4. 🔍 Detail PR, Checklist Subtugas & Tautan Materi
* **Modal Detail Komprehensif**: Menampilkan deskripsi lengkap, instruksi pengerjaan dari guru/dosen, serta status tenggat waktu.
* **Checklist Subtugas / Langkah Pengerjaan**: Pecah tugas besar menjadi langkah-langkah kecil. Mencentang seluruh subtugas akan otomatis memperbarui status PR menjadi *Selesai*.
* **Tautan Referensi (LMS & Cloud Links)**: Lampirkan link langsung ke Google Classroom, Google Drive, Canva, GitHub, atau portal e-learning kampus/sekolah.

### 5. ⏰ Pengingat Deadline & Notifikasi Cerdas (*Smart Urgency Engine*)
* **Banner Peringatan Mendesak**: Banner otomatis muncul di bagian atas jika ada PR dengan tenggat < 3 jam atau jatuh tempo hari ini.
* **Audio Chime Sintetis**: Efek suara melodis yang menyenangkan menggunakan **Web Audio API** (tanpa aset file audio eksternal) untuk notifikasi tugas dan suara perayaan saat tugas selesai (*Joyful Arpeggio*).
* **Browser Push Notification**: Integrasi Web Notification API untuk memberikan peringatan desktop saat deadline mendekat.
* **Pusat Notifikasi (Dropdown Hub)**: Ringkasan seluruh tugas yang memerlukan perhatian segera.

### 6. 🔎 Pencarian & Multi-Filter Real-Time
* **Pencarian Cepat**: Filter instan berdasarkan judul tugas, deskripsi, maupun nama mata pelajaran.
* **Filter Terstruktur**: Filter berdasarkan kategori mata pelajaran, tingkat prioritas (*Tinggi / Sedang / Rendah*), dan status pengerjaan.

### 7. 💾 Penyimpanan Data & Ekspor/Impor Cadangan
* **LocalStorage Persistence**: Data tersimpan aman di browser pengguna tanpa memerlukan server backend/database khusus.
* **Ekspor Cadangan (JSON)**: Cadangkan seluruh data tugas ke dalam file `.json` kapan saja.
* **Impor Data (JSON)**: Pulihkan atau pindahkan data tugas ke perangkat/browser lain dengan mudah.
* **Preset Data Otomatis**: Dilengkapi dengan data contoh realistis saat pertama kali dibuka.

### 8. 🎨 UI/UX Modern & Aksesibilitas
* **Tema Gelap & Terang (*Dark/Light Mode*)**: Dukungan perpindahan tema instan dengan palet warna modern berbasis Glassmorphism & efek *ambient glow*.
* **Desain Sepenuhnya Responsif**: Nyaman digunakan di layar *smartphone*, tablet, maupun monitor desktop/laptop.
* **Keyboard Shortcut**:
  * `Ctrl + N` / `Alt + N` : Buka formulir tambah PR baru secara instan.
  * `ESC` : Menutup modal/popover yang sedang terbuka.

---

## 🏗️ Struktur Proyek & Arsitektur Kode

```
ListPR/
├── index.html            # Struktur HTML utama, modal dialog, dashboard & view container
├── README.md             # Dokumentasi lengkap proyek
├── css/
│   ├── style.css         # Variabel desain, sistem tema (dark/light), layout, komponen & kartu
│   └── calendar.css      # Styling khusus komponen kalender, grid, chip tugas & popover
└── js/
    ├── app.js            # Entry point aplikasi, inisialisasi modul, background timer & keybindings
    ├── storage.js        # Manajemen LocalStorage, preset sampel data, ekspor & impor JSON
    ├── taskManager.js    # Logika CRUD tugas, filtering, kalkulasi subtugas & statistik
    ├── calendar.js       # Kontroler tampilan kalender bulanan, navigasi tanggal & render sel
    ├── notifications.js  # Mesin kalkulasi urgensi, Web Audio API chime, & Web Notification
    └── ui.js             # Kontroler UI, render tampilan (List/Kanban), modal dialog & event listener
```

---

## ⚙️ Penjelasan Modul JavaScript

| Berkas | Fungsi & Tanggung Jawab Utama |
| :--- | :--- |
| **`js/storage.js`** | Mengatur persistensi data ke `localStorage`, menyediakan sampel PR dinamis berbasis tanggal saat ini, serta menangani fungsi ekspor/impor file cadangan JSON. |
| **`js/taskManager.js`** | Mengelola *state* data tugas (tambah, perbarui, hapus, centang selesai, toggle subtugas), menghitung persentase progres, dan memfilter data berdasarkan parameter pencarian. |
| **`js/notifications.js`** | Menghitung selisih waktu jatuh tempo (*diff hours/minutes*), menentukan kategori urgensi (*Critical*, *Today*, *Tomorrow*, *Overdue*), memutar audio sintetis via Web Audio API, dan memicu notifikasi desktop. |
| **`js/calendar.js`** | Mengatur perhitungan kalender Gregorian (42 sel per bulan, penyesuaian hari Senin–Minggu), meletakkan kartu PR ke dalam tanggal yang sesuai, serta interaksi klik tanggal. |
| **`js/ui.js`** | Mengontrol seluruh pembaruan DOM: perpindahan tab (*Calendar, List, Kanban*), pengelolaan modal (form & detail PR), dropdown notifikasi, feedback Toast, dan pergantian tema gelap/terang. |
| **`js/app.js`** | Titik mula aplikasi (*entry point*) yang menginisialisasi semua modul saat `DOMContentLoaded`, menjalankan interval *ticker* per menit untuk memperbarui countdown waktu secara real-time, dan mengikat pintasan keyboard global. |

---

## 📊 Skema Data Tugas (*Task Data Schema*)

Setiap objek tugas (*Task*) disimpan dalam format JSON dengan struktur berikut:

```json
{
  "id": "task_1727000000000_abc12",
  "title": "PR Matematika: Kalkulus Integral & Luas Daerah",
  "subject": "Matematika",
  "subjectColor": "#06b6d4",
  "description": "Selesaikan latihan Bab 5 halaman 142 nomor 1 sampai 8.",
  "dueDate": "2026-09-25",
  "dueTime": "23:59",
  "priority": "Tinggi",
  "status": "in_progress",
  "reminderOffset": 120,
  "subtasks": [
    { "id": "sub_1", "text": "Kerjakan no 1 - 4", "completed": true },
    { "id": "sub_2", "text": "Kerjakan no 5 - 8", "completed": false }
  ],
  "links": [
    { "title": "Google Classroom", "url": "https://classroom.google.com" }
  ],
  "createdAt": "2026-09-20T10:00:00.000Z",
  "completedAt": null
}
```

---

## 🚀 Cara Menjalankan Aplikasi

1. Buka berkas **`index.html`** langsung di peramban web modern apa pun (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari, Opera).
2. Atau gunakan ekstensi **Live Server** di VS Code.

---

## ⌨️ Pintasan Keyboard (*Keyboard Shortcuts*)

| Tombol | Aksi |
| :--- | :--- |
| `Ctrl + N` atau `Alt + N` | Buka modal untuk menambah PR baru |
| `Escape (ESC)` | Tutup modal dialog / popover tanggal yang sedang aktif |

---

## 💡 Teknologi yang Digunakan

* **HTML5**: Struktur semantik, dialog modal terstandarisasi, aksesibilitas form.
* **CSS3**: CSS Custom Properties (*variables*), CSS Grid Layout, Flexbox, Glassmorphism, Micro-animations, Dark/Light Mode.
* **Vanilla JavaScript (ES6+)**: Modular Object Pattern, Web Audio API, Web Notification API, Web Storage API (`localStorage`), FileReader API.
* **SVG Icons**: Ikon vektor independen tanpa dependensi font eksternal.

---

## 📄 Lisensi
Proyek ini dibuat untuk tujuan edukasi dan manajemen produktivitas belajar siswa serta mahasiswa. Bebas digunakan dan dikembangkan lebih lanjut.
