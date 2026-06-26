# 🚗 Simulasi Sistem Manajemen Sewa Kendaraan

Sebuah program berbasis CLI (Command Line Interface) menggunakan bahasa pemrograman Python untuk mensimulasikan sistem manajemen penyewaan kendaraan (Mobil dan Motor). Program ini dirancang dengan struktur array dua dimensi serta menerapkan konsep dasar algoritma pencarian (*searching*) dan perulangan.

## ✨ Fitur Utama

* **Sewa Kendaraan:** Memproses peminjaman kendaraan berdasarkan jenis (Mobil/Motor) dan ID kendaraan, menghitung total biaya sewa berdasarkan durasi hari, serta mencetak struk peminjaman.
* **Pengembalian Kendaraan:** Memproses pengembalian kendaraan yang sedang disewa untuk mengubah statusnya kembali menjadi tersedia.
* **Cek Ketersediaan Kendaraan:** Menampilkan daftar seluruh mobil atau motor beserta status ketersediaannya saat ini (*Tersedia* atau *Sedang disewa*).
* **Cari Kendaraan:** Mencari informasi mendetail mengenai kendaraan tertentu berdasarkan **ID** maupun **Nama Kendaraan**.

---

## 📊 Struktur Data (Kamus Data)

Data kendaraan disimpan dalam bentuk array dua dimensi (`list` di dalam `list`) dengan format indeks sebagai berikut:

| Indeks Kolom | Nama Kolom | Tipe Data | Keterangan |
| :---: | :--- | :---: | :--- |
| **0** | ID Kendaraan | `int` | Identifikasi unik kendaraan |
| **1** | Nama Kendaraan | `str` | Merk dan tipe kendaraan |
| **2** | Jenis Kendaraan | `str` | Mobil / Motor |
| **3** | Harga Sewa | `int` | Tarif sewa per hari (Rp) |
| **4** | Status Ketersediaan | `int` | `0` = Tersedia, `1` = Sedang disewa |
| **5** | Nama Peminjam | `str` | Menyimpan nama penyewa saat ini |
