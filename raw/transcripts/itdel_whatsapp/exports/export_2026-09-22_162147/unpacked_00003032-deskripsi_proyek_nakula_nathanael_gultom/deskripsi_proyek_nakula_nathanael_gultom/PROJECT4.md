# JUDUL : Web LED Control & DHT11 Sensor Monitor ESP32-C3
# NAMA : NAKULA NATHANAEL GULTOM
# DESKRIPSI PROJEK :

Proyek ini mengombinasikan pengontrolan aktuator (LED) dan pemantauan sensor lingkungan (DHT11) berbasis *Internet of Things* (IoT) menggunakan mikrokontroler ESP32-C3 Super Mini. Perangkat dikonfigurasi sebagai *Access Point* (AP) Wi-Fi mandiri yang menjalankan Web Server HTTP pada port 80. Melalui jaringan Wi-Fi ini, pengguna dapat mengakses antarmuka web interaktif berbasis HTML/CSS dari peramban *smartphone* atau laptop untuk:
1. Mematikan dan menyalakan lampu LED (GPIO 8) secara nirkabel melalui tombol sakelar digital.
2. Membaca dan menampilkan data suhu (°C) serta kelembapan udara (%) dari sensor DHT11 (GPIO 4) secara *real-time* dan otomatis tanpa perlu memperbarui (*refresh*) halaman web secara manual.

# TUJUAN PROJEK :

1. **Pengembangan Embedded Web Server**: Membangun sistem IoT mandiri di mana ESP32-C3 berfungsi sekaligus sebagai pemancar Wi-Fi dan pelayan web (*web server*) tanpa ketergantungan pada internet luar.
2. **Integrasi Sensor & Aktuator**: Menggabungkan pembacaan data kondisi lingkungan (suhu & kelembapan) dan kontrol perangkat keras (LED) dalam satu sistem yang terintegrasi.
3. **Penerapan Komunikasi HTTP**: Mempelajari alur pertukaran data nirkabel dua arah antara peramban web (*client*) dan mikrokontroler (*server*) menggunakan protokol HTTP request (`GET` & respon HTML/JSON).
4. **Antarmuka Pengguna (UI) Interaktif**: Menyediakan tampilan pemantauan dan kendali nirkabel yang responsif, modern, hemat daya, serta ramah pengguna (*user-friendly*).
