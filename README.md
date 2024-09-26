
---

# Auto Create Account Instagram

Proyek ini adalah skrip otomatis untuk membuat akun Instagram secara otomatis menggunakan Python. Skrip ini memanfaatkan API Instagram dan pustaka Python untuk mengotomatisasi proses pendaftaran akun baru, termasuk mengaktifkan otentikasi dua faktor (2FA) secara otomatis.

## Fitur

- Membuat akun Instagram baru secara otomatis.
- Mengisi data profil seperti nama pengguna, email, dan kata sandi.
- Menyesuaikan pengaturan profil akun setelah dibuat.
- Mengaktifkan otentikasi dua faktor (2FA) secara otomatis untuk keamanan tambahan.

## Prasyarat

Sebelum menjalankan skrip ini, pastikan Anda memiliki hal-hal berikut:

- Python 3.x terinstal di sistem Anda.
- Pustaka Python yang diperlukan (tercantum di bawah).
- Koneksi internet aktif.

## Instalasi

1. **Instal pustaka Python yang diperlukan:**

   ```bash
   pkg update && pkg upgrade
   pkg install python3
   ```

 2. **Clone repositori ini:**

    ```bash
    rm -rf Created_AccountIG
    git clone https://github.com/Fajarxyta/Created_AccountIG
    cd Created_AccountIG
    pip3.11 install -r requirements.txt
    ```
## Penggunaan

Jalankan skrip untuk membuat akun Instagram baru dan mengaktifkan 2FA:

```bash
python Main.py
```

Ikuti petunjuk yang muncul di layar untuk menyelesaikan proses pendaftaran dan konfigurasi 2FA. Skrip akan meminta Anda untuk memasukkan kode 2FA yang dikirimkan melalui SMS atau aplikasi autentikator, jika diperlukan.

## Penjelasan 2FA

Otentikasi dua faktor (2FA) adalah metode keamanan tambahan yang memerlukan dua bentuk verifikasi sebelum mengakses akun. Skrip ini secara otomatis mengaktifkan 2FA setelah pembuatan akun untuk meningkatkan keamanan:

- Skrip ini akan mengirimkan permintaan untuk mengaktifkan 2FA melalui antarmuka Instagram.
- Anda akan diminta untuk memasukkan kode yang diterima melalui SMS atau aplikasi autentikator.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan lakukan fork repositori ini dan buat pull request dengan perubahan Anda. Pastikan untuk mengikuti pedoman kontribusi yang ada.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat LICENSE untuk detailnya.

Terima kasih telah menggunakan proyek ini!

---
