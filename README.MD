# Ne Jowo (.nj) Programming Language v2.1.0

<p align="center">
  <img src="assets/ne-jowo-logo.jpg" width="400" alt="Logo Ne Jowo">
</p>

Bahasa pemrograman kustom berbasis **Token-Transpiler Python** dengan cita rasa kearifan lokal (Bahasa Jawa). Versi **v2.1.0 (Color Update)** ini menghadirkan fitur pewarnaan teks otomatis di terminal CLI tanpa memerlukan pustaka tambahan, menjadikannya lebih interaktif dan estetik saat dijalankan di Termux.

## 🚀 Fitur Unggulan v2.1.0
- **Auto ANSI Colors**: Perintah `aturaken` otomatis mencetak warna hijau cerah, teks sambutan berwarna cyan, dan pesan eror sistem otomatis berwarna merah menyala.
- **Indentation Free**: Tidak perlu pusing mengatur spasi tabulasi (*indentation*) yang ketat seperti pada Python asli.
- **Blok "wis_rampung"**: Penanda akhir logika yang terstruktur dan sangat ramah bagi pemula yang baru belajar pemrograman.
- **Auto Safe-Input**: Fitur `nyuwun_angka` dilengkapi penanganan eror otomatis agar program tidak langsung *crash* jika pengguna salah memasukkan teks biasa.

## 📚 Kamus Sintaks Terupdate

| Sintaks Ne Jowo | Arti / Padanan Python | Fungsi Visual |
| :--- | :--- | :--- |
| `aturaken "teks"` | `print("teks")` | Mencetak output teks otomatis berwarna **Hijau Terang** |
| `gadhah` | `=` | Operator memasukkan nilai data ke variabel |
| `nyuwun_input` | `input()` | Meminta input data teks (String) |
| `nyuwun_angka` | `int(input())` | Meminta input data angka (Integer) dengan fitur anti-crash |
| `yen ... banjur` | `if ... :` | Membuka kondisi percabangan logika |
| `utawa_yen ... banjur`| `elif ... :` | Membuka kondisi alternatif |
| `utawa` | `else:` | Logika akhir jika semua kondisi di atas salah |
| `mbaleni ... banjur` | `while ... :` | Membuka blok perulangan loop |
| `wis_rampung` | *(Mengurangi Tab)* | Menutup blok logika `yen` maupun `mbaleni` |

### Operasi Matematika & Perbandingan
- `ditambah` (+) | `dikurangi` (-) | `diping` (*) | `diporo` (/)
- `podo_karo` (==) | `luwih_akeh` (>) | `luwih_sithik` (<)

## 💻 Contoh Kode Berwarna (`examples/game_warna.nj`)
```text
# Berkas program Ne Jowo v2.1.0
aturaken "=== TES SISTEM ==="

angka_rahasia gadhah 10
yen angka_rahasia podo_karo 10 banjur
    aturaken "Angkane bener lan teks iki bakal mawa warna ijo!"
utawa
    aturaken "Angkane luput!"
wis_rampung
```

## 🛠️ Cara Instalasi lan Nganggo ing Termux
```bash
git clone https://github.com/NarzX/Ne-Jowo
cd Ne-Jowo
bash install.sh
```
Jalankan berkas kode program `.nj` Anda cukup dengan mengetik perintah ringkas:
```bash
nj examples/game_warna.nj
```

## 📄 Lisensi
Proyek open-source ini dilindungi sepenuhnya oleh hukum hak cipta terbuka di bawah naungan [MIT License](LICENSE).
