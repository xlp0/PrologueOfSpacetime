# JUDUL : Blink LED ESP32-C3 Super Mini
# NAMA : NAKULA NATHANAEL GULTOM
# DESKRIPSI PROJEK :

Proyek ini adalah implementasi dasar mikrokontroler ESP32-C3 Super Mini untuk mengontrol indikator lampu LED bawaan (*on-board LED*) yang terhubung pada pin GPIO 8. Program mengeksekusi logika *Active LOW* di mana LED akan menyala saat sinyal `LOW` dikirimkan dan mati saat sinyal `HIGH` dikirimkan secara bergantian dengan interval jeda (*delay*) 1 detik. Selain itu, status aktivasi LED ditransmisikan secara *real-time* ke Serial Monitor pada kecepatan transmisi 115200 bps untuk pemantauan eksekusi kode.

# TUJUAN PROJEK :

1. **Memahami Dasar Sistem Tertanam**: Mempelajari alur pemrograman mikrokontroler ESP32-C3 Super Mini menggunakan arsitektur C/C++ pada Arduino IDE.
2. **Penguasaan Digital I/O**: Memahami konfigurasi pin Output digital, manipulasi status sinyal `HIGH` dan `LOW`, serta karakteristik *Active LOW* pada hardware.
3. **Penggunaan Serial Debugging**: Melatih penggunaan komunikasi serial (*Serial Monitor*) untuk keperluan validasi dan proses penelusuran kesalahan (*debugging*) program.
4. **Pengujian Perangkat Keras**: Mengonfirmasi bahwa board ESP32-C3 dan port komunikasi USB/CDC berfungsi dengan baik sebelum melangkah ke proyek IoT yang lebih kompleks.
