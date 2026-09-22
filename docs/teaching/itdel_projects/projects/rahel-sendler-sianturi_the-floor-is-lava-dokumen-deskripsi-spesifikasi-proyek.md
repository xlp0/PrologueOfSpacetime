---
title: "THE FLOOR IS LAVA — Dokumen Deskripsi & Spesifikasi Proyek"
title_en: "The Floor is Lava: Interactive Obstacle & Sensor Game"
date: 2026-09-22
author: "Rahel Sendler Sianturi"
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
source_ref: "attachment:00003044-deskripsi proyek Rahel Sendler Sianturi.zip/Proyek 3.md"
---

# THE FLOOR IS LAVA — Dokumen Deskripsi & Spesifikasi Proyek

> **English Title**: *The Floor is Lava: Interactive Obstacle & Sensor Game*  
> **Student / Author**: [[rahel-sendler-sianturi|Rahel Sendler Sianturi]]  
> **Institution**: Institut Teknologi Del  
> **Category**: `IoT & Hardware` | **Liberal Art Mode**: `[[Quadrivium|Quadrivium-Astronomy]]`  

---

## 1. Deskripsi Proyek (Indonesian)
# 🌋 THE FLOOR IS LAVA — Dokumen Deskripsi & Spesifikasi Proyek

> **Tagline:** *"Reach the Exit Before the Lava Gets You!"*  
> **Genre:** 2D Platformer Survival, Vertical Parkour, Time-Attack  
> **Target Platform:** Web App (HTML5 Canvas + Vanilla JS) & Native Desktop (C++17)  
> **Lisensi & Status:** Open Project / Playable Version Available  

---

## 1. 📖 Ringkasan Proyek (Project Overview)

**The Floor is Lava** adalah game aksi-platformer survival 2D bertempo cepat yang menggabungkan presisi parkour vertikal dengan mekanisme ancaman lingkungan dinamis. Pemain ditempatkan dalam skenario darurat ekstrem: lautan lava pijar merambat naik dari dasar lantai secara *real-time*, menelan setiap pijakan yang berada di bawahnya. 

Misi utama pemain adalah melompati serangkaian platform rintangan, mengumpulkan koin emas, menghindari bola api vulkanik, dan mencapai **Pintu Keluar Darurat (Exit Door)** di puncak level sebelum lava menenggelamkan karakter.

Proyek ini dibangun secara independen dengan arsitektur ganda:
1. **Versi Web Canvas (Vanilla JS & HTML5)**: Dapat langsung dijalankan di semua browser modern tanpa instalasi dependensi runtime.
2. **Versi Native C++ (High Performance Engine)**: Menggunakan logika fisika AABB collision deterministik untuk kompilasi desktop native.

---

## 2. 🎨 Karakteristik Visual & Atmosfer Sinematik

Visual dan atmosfer **The Floor is Lava** dirancang dengan kontras dramatis (*high-contrast chiaroscuro*) antara panasnya magma cair dan gelapnya lingkungan sekitar:

| Aspek Visual | Karakteristik & Efek |
| :--- | :--- |
| **Pencahayaan Magma (Volcanic Radiance)** | Dasar layar didominasi cahaya magma pijar berwarna gradien *white-hot core*, jingga menyala, dan merah kirmizi pekat yang memancarkan *under-lighting* ke arah platform atas. |
| **Distorsi Panas (Heat Haze Shimmer)** | Efek gelombang refraksi udara panas yang meliuk-liuk di atas batas permukaan lava, memberikan kesan suhu udara ekstrem yang membiaskan pandangan. |
| **Partikel Bara & Abu (Floating Embers)** | Partikel bara api kecil dan serpihan abu vulkanik hitam yang melayang tersuspensi ke atas mengikuti arus konveksi udara panas. |
| **Tekstur Platform** | Menggabungkan tema interior buatan manusia (meja kelas, pipa pabrik, ban berjalan) dengan batuan alam vulkanik (batu basal gelap, obsidian retak, kristal kuarsa tahan panas). |
| **Peringatan Bahaya (Danger Cue)** | Efek getaran layar mikro (*screen shake*) dan peringatan HUD berkedip merah saat persentase kenaikan lava mendekati posisi ketinggian pemain. |

---

## 3. 🕹️ Mekanika Inti & Gameplay Loop

```
  [Start Level] ──> [Lava Mulai Naik] ──> [Parkour & Lompati Platform]
         ▲                                                │
         │                                                ▼
   [Restart / 'R'] <── [Tersentuh Lava: Game Over]   [Kumpulkan Koin]
                                                          │
                                                          ▼
                                              [Capai Exit Door: CLEARED]
```

### 3.1. Mesin Simulasi Lava (Rising Lava Engine)
- **Kenaikan Dinamis**: Lava bergerak naik secara konstan per detik (`lavaY -= lavaRiseSpeed`).
- **Lava Meter HUD**: Indikator persentase real-time (0% hingga 100%) yang menunjukkan seberapa dekat magma dengan batas atas arena.
- **Insta-Kill Hazard**: Kontak langsung antara hitbox karakter dengan permukaan lava mengakibatkan *Game Over* instan (kecuali dilindungi pelindung khusus).

### 3.2. Mesin Fisika 2D Platformer
- **AABB Collision Detection**: Deteksi tumbukan berbasis kotak sumbu (*Axis-Aligned Bounding Box*) dengan pengecekan posisi kaki presisi (*one-way ground checking*).
- **Gravitasi & Inersia**: Kurva gravitasi parabola alami dengan akselerasi jatuh dan redaman friksi horizontal di atas platform.
- **Double Jump & Jump Buffering**: Respons input lompatan responsif dengan toleransi *coyote time* untuk navigasi parkour yang adil dan memuaskan.

---

## 4. 🦹‍♂️ Arketipe Karakter (Character Classes)

Pemain dapat memilih salah satu dari 3 tipe karakter dengan spesialisasi gaya bermain yang berbeda:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   🏃 RUNNER     │    │   🦘 JUMPER     │    │   🛡️ TANK       │
│ Speed: 7.0 px/f │    │ Speed: 5.5 px/f │    │ Speed: 5.0 px/f │
│ Jump: -12.0     │    │ Jump: -14.5     │    │ Jump: -11.0     │
│ Sifat: Lincah   │    │ Sifat: Vertikal │    │ Sifat: Kebal 1x │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

1. **🏃 Runner (Speed Specialist)**:
   - Kecepatan horizontal tertinggi (+40%), akselerasi instan.
   - Sangat efektif untuk level dengan rintangan horizontal panjang dan ban berjalan (*conveyor belt*).
2. **🦘 Jumper (High Leap Specialist)**:
   - Daya dorong vertikal tertinggi (-14.5 jump power), dapat melompati jarak antar platform yang tinggi tanpa bantuan trampolin.
   - Ideal untuk level vertikal terjal dan tebing obsidian.
3. **🛡️ Tank (Lava Shield Specialist)**:
   - Dilengkapi satu lapis perisai panas (*Magma Heat Shield*).
   - Mampu bertahan dari satu kali sentuhan kontak singkat dengan lava sebelum perisai pecah.

---

## 5. 🧱 Ragam Platform & Elemen Interaktif

| Jenis Elemen | Simbol | Perilaku & Interaksi |
| :--- | :---: | :--- |
| **Normal Slate Platform** | 🧱 | Pijakan kokoh standar dari batu alam atau perabot interior tahan panas. |
| **Moving Platform** | ↔️ | Platform dinamis yang bergerak bolak-balik secara horizontal atau vertikal mengikuti fungsi sinus. |
| **Bouncy Trampoline** | 🟩 | Melipatgandakan gaya dorong lompat pemain sebesar $1.8\times$ untuk mencapai area tinggi terpencil. |
| **Crumbling Ledge** | ⏳ | Platform retak yang akan runtuh setelah 0.75 detik diinjak oleh pemain. |
| **Fireball Hazard** | ☄️ | Proyektil magma yang menyembur dari bawah secara periodik dengan lintasan parabola. |
| **Power Switch & Gate** | 🔘 | Saklar mekanik yang membuka pintu gerbang terkunci untuk membuka jalur menuju exit. |
| **Collectible Coin** | 🪙 | Koin emas bernilai skor tambahan yang tersebar di rute-rute berisiko tinggi. |
| **Exit Door** | 🚪 | Pintu besi darurat kedap api di puncak stage; menjadi tujuan akhir penyelesaian level. |

---

## 6. 🗺️ Progresi Level & Dunia (20 Levels, 4 Worlds)

Permainan dirancang dengan 20 level bertingkat yang terbagi ke dalam 4 zona tematik unik:

```
[WORLD 1: The Academy] ──> [WORLD 2: The Factory] ──> [WORLD 3: Magma Core] ──> [WORLD 4: Sky Inferno]
  (Level 1 - 5)              (Level 6 - 10)             (Level 11 - 15)           (Level 16 - 20)
```

### 🏫 World 1: The Abandoned Academy (Level 1 – 5)
- **Setting:** Gedung sekolah bertingkat tua yang retak dan dibanjiri lautan lava dari ruang bawah tanah.
- **Level:** 
  1. *Classroom 🏫* (Tutorial dasar & lompatan pertama)
  2. *Laboratory 🧪* (Pengenalan trampolin bahan kimia)
  3. *Library 📚* (Parkour rak buku tinggi)
  4. *Corridor 🚪* (Platform bergerak horizontal)
  5. *Rooftop 🏫* (Pelarian ke atap dengan kecepatan lava meningkat)

### 🏭 World 2: Industrial Steampower Factory (Level 6 – 10)
- **Setting:** Pabrik peleburan logam dengan mesin uap, piston bertekanan, dan ban berjalan.
- **Level:**
  6. *Conveyor Belt 🏭* (Pijakan bergerak yang mendorong pemain)
  7. *Machine Room ⚙️* (Roda gigi putar dan rintangan sempit)
  8. *Pipe Shaft 💨* (Ventilasi uap vertikal)
  9. *Electric Room ⚡* (Saklar dan platform konduktor)
  10. *Factory Chimney 🏭* (Pendakian cerobong silindris sempit)

### 🌋 World 3: The Subterranean Magma Core (Level 11 – 15)
- **Setting:** Gua vulkanik alami dengan semburan magma aktif dan kristal kuarsa.
- **Level:**
  11. *Magma Chamber 🌋* (Semburan gelembung lava besar)
  12. *Obsidian Pass 🏔️* (Pijakan rapuh yang runtuh)
  13. *Crystal Grotto 💎* (Platform kristal licin)
  14. *Lava Falls 🌊* (Air terjun magma yang menghalangi jalur)
  15. *Volcano Core 🌋* (Kecepatan lava 2x lipat)

### ☁️ World 4: Sky Inferno & Omega Zenith (Level 16 – 20)
- **Setting:** Struktur mengambang di atas atmosfer kaldera gunung berapi dengan angin kencang dan gravitasi anomal.
- **Level:**
  16. *Cloud Leap ☁️* (Lompatan buta di atas awan asap)
  17. *Storm Citadel ⚡* (Kombinasi kilat dan platform bergerak)
  18. *Gravity Rift 🌀* (Gravitasi rendah dengan jarak lompat melayang)
  19. *Inferno Tower 🔥* (Pendakian menara spiral ekstrem)
  20. *OMEGA LAVA CORE 👑* (Level puncak survival: semua rintangan aktif simultan)

---

## 7. ⌨️ Skema Kontrol (Control Scheme)

| Aksi | Keyboard Utama | Alternatif (Arrow Keys) |
| :--- | :---: | :---: |
| **Bergerak ke Kiri** | `A` | `◄ Left Arrow` |
| **Bergerak ke Kanan** | `D` | `► Right Arrow` |
| **Melompat** | `W` / `Space` | `▲ Up Arrow` |
| **Restart Level Cepat** | `R` | — |
| **Ganti Karakter** | Menu Dropdown HUD | — |
| **Pilih Level** | Dropdown Seleksi Level | — |

---

## 8. 📂 Struktur Repositori & Berkas

```
the-floor-is-lava/
├── index.html              # Antarmuka web, HUD panel, canvas game container
├── README.md               # Ringkasan cepat dan instruksi eksekusi
├── DESKRIPSI_PROYEK.md     # Dokumen komprehensif spesifikasi & arsitektur proyek
├── css/
│   └── style.css           # Styling bertema vulkanik, tombol aksen lava, neon HUD
├── js/
│   ├── app.js              # Inisialisasi DOM, audio controller, modal popup
│   ├── game-engine.js      # Loop game 60 FPS, state manager, level builder (20 levels)
│   ├── platform.js         # Kelas platform (slate, moving, trampolin, crumbling)
│   └── player.js           # Fisika pemain, AABB collision, animasi sprite & kontrol
└── cpp/
    └── main.cpp            # Implementasi native engine C++ berbasis terminal/desktop
```

---

## 9. 🚀 Petunjuk Menjalankan Game

### Menjalankan Versi Web (HTML5 Canvas):
Buka file `index.html` langsung pada browser web (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari):
```text
file:///C:/Users/Lenovo/OneDrive/Desktop/Sendler's/the-floor-is-lava/index.html
```
*Atau jalankan melalui local server:*
```bash
npx serve .
# atau
python -m http.server 8000
```

### Mengompilasi Versi Native C++:
Gunakan compiler C++ modern (GCC/Clang/MSVC):
```bash
cd the-floor-is-lava
g++ -std=c++17 -O2 -o floor_is_lava cpp/main.cpp
./floor_is_lava
```

---

## 10. 🔮 Rencana Pengembangan Mendatang (Roadmap)

- [ ] **Procedural Audio Synthesizer (Web Audio API)**: Efek gemuruh magma (*sub-bass rumble*), desis uap, dan hentakan kaki di atas batu.
- [ ] **Particle Shader Acceleration**: Shader WebGL untuk partikel bara api dinamis dan gelombang fluida lava.
- [ ] **Local High Score Leaderboard**: Penyimpanan rekor waktu tempuh tercepat per level menggunakan `localStorage`.
- [ ] **Level Editor Mode**: Fitur perancangan panggung kustom dengan *drag-and-drop* platform.

## 2. Project Description (English Translation)
An interactive obstacle game turning physical spaces into hazardous lava zones, utilizing sensor detection and visual cues to require players to leap between designated safe zones.

---

## 3. Tujuan Proyek (Indonesian Objectives)
*Tujuan proyek belum diserahkan.*

## 4. Project Objectives (English Translation)
1. Combine physical motion with digital game state mechanics.
2. Implement timing windows and hazard indicators for immersive gameplay.
3. Promote active physical movement through gamified spatial challenges.

---

## 5. Technical Verification & Delivery Status
- **Repository / Demo**: *Pending submission by student*
- **Delivery Mode**: IoT & Hardware
- **Source Reference**: `attachment:00003044-deskripsi proyek Rahel Sendler Sianturi.zip/Proyek 3.md`
- **Repository Status**: [Pending Link]
