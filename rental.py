"""
===============================================
  SISTEM RENTAL KENDARAAN - Tugas Besar Dasprog
===============================================
Fitur:
  1. Peminjaman & pengembalian kendaraan
  2. Daftar jenis kendaraan (Mobil, Motor)
  3. Laporan ketersediaan kendaraan real-time
  4. Simulasi booking & perhitungan biaya + diskon member
  5. Sistem pengembalian via ID transaksi

Batasan:
  - Tidak ada import sama sekali
  - Array 1D dan 2D
  - Fungsi void (pakai variabel global)
  - Pengulangan: if, while, for
  - Searching: Linear Search
  - Sorting: Bubble Sort
  - Tanpa: append, len, lower, strip, dict, dll
===============================================
"""

# ─────────────────────────────────────────────
#  KONSTANTA UKURAN ARRAY
# ─────────────────────────────────────────────

MAX_KENDARAAN   = 8
MAX_MEMBER      = 5
MAX_TRANSAKSI   = 50

# ─────────────────────────────────────────────
#  ARRAY 1D & 2D - DATA KENDARAAN
#
#  Kolom (indeks):
#    0 = ID kendaraan    (string)
#    1 = Nama kendaraan  (string)
#    2 = Jenis           (string: "Mobil" / "Motor")
#    3 = Harga per hari  (int)
#    4 = Tersedia        (string: "Ya" / "Tidak")
# ─────────────────────────────────────────────

kendaraan = [
    ["M001", "Toyota Avanza",      "Mobil", 350000, "Ya"   ],
    ["M002", "Honda Brio",         "Mobil", 280000, "Ya"   ],
    ["M003", "Mitsubishi Xpander", "Mobil", 450000, "Ya"   ],
    ["M004", "Toyota Innova",      "Mobil", 500000, "Tidak"],
    ["T001", "Honda Vario 150",    "Motor",  80000, "Ya"   ],
    ["T002", "Yamaha NMAX",        "Motor", 100000, "Ya"   ],
    ["T003", "Honda PCX",          "Motor", 110000, "Ya"   ],
    ["T004", "Yamaha Aerox",       "Motor",  90000, "Tidak"],
]

# ─────────────────────────────────────────────
#  ARRAY 2D - DATA MEMBER
#
#  Kolom:
#    0 = Nama member  (string, huruf kecil untuk pencocokan)
#    1 = Nama tampil  (string)
#    2 = Diskon (%)   (int: 10, 15, 20)
# ─────────────────────────────────────────────

member = [
    ["budi",    "Budi Santoso",   15],
    ["siti",    "Siti Rahayu",    10],
    ["andi",    "Andi Wijaya",    20],
    ["dewi",    "Dewi Lestari",   15],
    ["kenneth", "Kenneth Ansell", 20],
]

# ─────────────────────────────────────────────
#  ARRAY 2D - DATA TRANSAKSI (maks 50 transaksi)
#
#  Kolom:
#    0  = ID Transaksi   (string)
#    1  = Nama Penyewa   (string)
#    2  = ID Kendaraan   (string)
#    3  = Nama Kendaraan (string)
#    4  = Jenis          (string)
#    5  = Jumlah Hari    (int)
#    6  = Total Bayar    (int)
#    7  = Diskon (%)     (int)
#    8  = Status         (string: "Aktif" / "Selesai")
# ─────────────────────────────────────────────

transaksi = [None] * MAX_TRANSAKSI
jumlah_transaksi = 0   # counter transaksi aktif
id_counter       = 1   # untuk generate ID unik TRX-001, TRX-002, dst


# ══════════════════════════════════════════════
#  FUNGSI UTILITAS
# ══════════════════════════════════════════════

def bersihkan_layar():
    # Cetak banyak baris kosong sebagai pengganti clear screen
    for i in range(10):
        print("")


def cetak_garis(karakter, panjang):
    baris = ""
    for i in range(panjang):
        baris = baris + karakter
    print(baris)


def cetak_header(judul):
    bersihkan_layar()
    cetak_garis("=", 57)
    print("         SISTEM RENTAL KENDARAAN")
    cetak_garis("=", 57)
    print("  " + judul)
    cetak_garis("-", 57)


def format_rupiah(nominal):
    # Konversi nominal ke string rupiah tanpa library
    # Contoh: 350000 -> "Rp 350.000"
    angka = str(nominal)
    hasil = ""
    hitung = 0
    for i in range(len(angka) - 1, -1, -1):
        if hitung > 0 and hitung % 3 == 0:
            hasil = "." + hasil
        hasil = angka[i] + hasil
        hitung = hitung + 1
    return "Rp " + hasil


def buat_id_transaksi():
    global id_counter
    # Format: TRX-001, TRX-002, ...
    if id_counter < 10:
        kode = "TRX-00" + str(id_counter)
    elif id_counter < 100:
        kode = "TRX-0" + str(id_counter)
    else:
        kode = "TRX-" + str(id_counter)
    id_counter = id_counter + 1
    return kode


def input_angka(prompt, min_val, max_val):
    # Input integer dengan validasi range, kembalikan nilai valid
    while True:
        try:
            nilai = int(input(prompt))
            if nilai < min_val:
                print("  [!] Masukkan angka minimal " + str(min_val) + ".")
            elif nilai > max_val:
                print("  [!] Masukkan angka maksimal " + str(max_val) + ".")
            else:
                return nilai
        except ValueError:
            print("  [!] Input tidak valid. Masukkan angka.")


def tekan_enter():
    input("\n  Tekan Enter untuk kembali ke menu...")


def samakan_huruf(teks):
    # Mengubah huruf besar ke kecil secara manual tanpa .lower()
    hasil = ""
    for karakter in teks:
        kode = ord(karakter)
        if 65 <= kode <= 90:       # A-Z -> a-z
            hasil = hasil + chr(kode + 32)
        else:
            hasil = hasil + karakter
    return hasil


def hapus_spasi(teks):
    # Hapus spasi di awal dan akhir tanpa .strip()
    # Hapus dari depan
    i = 0
    while i < len(teks) and teks[i] == " ":
        i = i + 1
    teks = teks[i:]
    # Hapus dari belakang
    j = len(teks) - 1
    while j >= 0 and teks[j] == " ":
        j = j - 1
    return teks[:j + 1]


# ══════════════════════════════════════════════
#  SEARCHING - LINEAR SEARCH
# ══════════════════════════════════════════════

def cari_kendaraan_by_id(id_cari):
    """
    Linear search kendaraan berdasarkan ID.
    Kembalikan indeks array, atau -1 jika tidak ditemukan.
    """
    for i in range(MAX_KENDARAAN):
        if kendaraan[i][0] == id_cari:
            return i
    return -1


def cari_member_by_nama(nama_cari):
    """
    Linear search member berdasarkan nama (tidak case-sensitive).
    Kembalikan indeks array, atau -1 jika tidak ditemukan.
    """
    nama_lower = samakan_huruf(nama_cari)
    for i in range(MAX_MEMBER):
        if member[i][0] == nama_lower:
            return i
    return -1


def cari_transaksi_by_id(id_cari):
    """
    Linear search transaksi berdasarkan ID transaksi.
    Kembalikan indeks array, atau -1 jika tidak ditemukan.
    """
    for i in range(jumlah_transaksi):
        if transaksi[i] is not None:
            if transaksi[i][0] == id_cari:
                return i
    return -1


# ══════════════════════════════════════════════
#  SORTING - BUBBLE SORT
# ══════════════════════════════════════════════

def bubble_sort_kendaraan_by_harga():
    """
    Bubble sort kendaraan berdasarkan harga per hari (kolom 3), ascending.
    Mengurutkan salinan array supaya data asli tidak berubah.
    """
    # Buat salinan array kendaraan
    salinan = []
    for i in range(MAX_KENDARAAN):
        salinan = salinan + [kendaraan[i][:]]   # copy tiap baris

    # Bubble sort ascending berdasarkan harga (indeks 3)
    for i in range(MAX_KENDARAAN - 1):
        for j in range(MAX_KENDARAAN - 1 - i):
            if salinan[j][3] > salinan[j + 1][3]:
                # Tukar
                temp           = salinan[j]
                salinan[j]     = salinan[j + 1]
                salinan[j + 1] = temp

    return salinan


def bubble_sort_transaksi_by_total():
    """
    Bubble sort transaksi berdasarkan total bayar (kolom 6), descending.
    Hanya transaksi yang sudah terisi (tidak None).
    """
    # Kumpulkan transaksi valid ke array sementara
    temp_trx = []
    for i in range(jumlah_transaksi):
        if transaksi[i] is not None:
            temp_trx = temp_trx + [transaksi[i][:]]

    jumlah = 0
    for _ in temp_trx:
        jumlah = jumlah + 1

    # Bubble sort descending berdasarkan total bayar (indeks 6)
    for i in range(jumlah - 1):
        for j in range(jumlah - 1 - i):
            if temp_trx[j][6] < temp_trx[j + 1][6]:
                temp           = temp_trx[j]
                temp_trx[j]     = temp_trx[j + 1]
                temp_trx[j + 1] = temp

    return temp_trx, jumlah


# ══════════════════════════════════════════════
#  TAMPILKAN KETERSEDIAAN KENDARAAN
# ══════════════════════════════════════════════

def tampilkan_ketersediaan(filter_jenis):
    """
    Tampilkan tabel ketersediaan.
    filter_jenis: "" = semua, "Mobil", atau "Motor"
    """
    if filter_jenis == "":
        cetak_header("KETERSEDIAAN SEMUA KENDARAAN")
    else:
        cetak_header("KETERSEDIAAN KENDARAAN - " + filter_jenis)

    print("  {:<6}  {:<23}  {:<6}  {:>12}  {}".format(
        "ID", "Nama Kendaraan", "Jenis", "Harga/Hari", "Status"
    ))
    cetak_garis("-", 57)

    total    = 0
    tersedia = 0

    for i in range(MAX_KENDARAAN):
        baris = kendaraan[i]
        if filter_jenis == "" or baris[2] == filter_jenis:
            total = total + 1
            if baris[4] == "Ya":
                status   = "Tersedia"
                tersedia = tersedia + 1
            else:
                status = "Disewa  "
            print("  {:<6}  {:<23}  {:<6}  {:>12}  {}".format(
                baris[0], baris[1], baris[2],
                format_rupiah(baris[3]), status
            ))

    cetak_garis("-", 57)
    print("  Total: " + str(total) + " unit  |  Tersedia: " + str(tersedia) +
          "  |  Disewa: " + str(total - tersedia))
    cetak_garis("=", 57)


# ══════════════════════════════════════════════
#  CEK MEMBER & DISKON
# ══════════════════════════════════════════════

# Variabel global untuk menyimpan hasil cek member
hasil_nama_member   = ""
hasil_diskon_member = 0

def cek_member():
    """
    Fungsi void: hasil disimpan ke hasil_nama_member & hasil_diskon_member.
    """
    global hasil_nama_member, hasil_diskon_member
    hasil_nama_member   = ""
    hasil_diskon_member = 0

    print("\n  Apakah Anda terdaftar sebagai member?")
    print("  [1] Ya")
    print("  [2] Tidak")
    pilihan = input_angka("  Pilih: ", 1, 2)

    if pilihan == 2:
        return

    nama_input = input("  Masukkan nama member: ")
    nama_input = hapus_spasi(nama_input)

    idx = cari_member_by_nama(nama_input)
    if idx == -1:
        print("  [!] Nama tidak ditemukan. Lanjut tanpa diskon.")
        return

    hasil_nama_member   = member[idx][1]
    hasil_diskon_member = member[idx][2]
    print("  Selamat datang, " + hasil_nama_member + "!")
    print("  Anda mendapat diskon " + str(hasil_diskon_member) + "%.")


# ══════════════════════════════════════════════
#  HITUNG BIAYA
# ══════════════════════════════════════════════

hasil_subtotal = 0
hasil_potongan = 0
hasil_total    = 0

def hitung_biaya(harga_per_hari, jumlah_hari, diskon_persen):
    """
    Fungsi void: hasil disimpan ke global hasil_subtotal, potongan, total.
    """
    global hasil_subtotal, hasil_potongan, hasil_total
    hasil_subtotal = harga_per_hari * jumlah_hari
    hasil_potongan = (hasil_subtotal * diskon_persen) // 100
    hasil_total    = hasil_subtotal - hasil_potongan


# ══════════════════════════════════════════════
#  PROSES PEMINJAMAN
# ══════════════════════════════════════════════

def proses_peminjaman():
    global jumlah_transaksi

    cetak_header("PEMINJAMAN KENDARAAN")
    tampilkan_ketersediaan("")

    # Pilih jenis
    print("\n  Pilih Jenis Kendaraan:")
    print("  [1] Mobil")
    print("  [2] Motor")
    pilihan_jenis = input_angka("  Pilih: ", 1, 2)
    if pilihan_jenis == 1:
        jenis = "Mobil"
    else:
        jenis = "Motor"

    tampilkan_ketersediaan(jenis)

    # Cek ada yang tersedia
    ada_tersedia = False
    for i in range(MAX_KENDARAAN):
        if kendaraan[i][2] == jenis and kendaraan[i][4] == "Ya":
            ada_tersedia = True
    if not ada_tersedia:
        print("  [!] Tidak ada " + jenis + " yang tersedia saat ini.")
        tekan_enter()
        return

    # Input ID kendaraan
    print("\n  Masukkan ID kendaraan (contoh: M001 / T001):")
    kid_input = input("  ID Kendaraan: ")
    kid_input = hapus_spasi(kid_input)

    # Ubah ke huruf besar manual
    kid = ""
    for karakter in kid_input:
        kode = ord(karakter)
        if 97 <= kode <= 122:
            kid = kid + chr(kode - 32)
        else:
            kid = kid + karakter

    idx_k = cari_kendaraan_by_id(kid)

    if idx_k == -1:
        print(" [!] ID kendaraan tidak ditemukan.")
        tekan_enter()
        return

    if kendaraan[idx_k][4] == "Tidak":
        print(" [!] Kendaraan sedang tidak tersedia.")
        tekan_enter()
        return

    if kendaraan[idx_k][2] != jenis:
        print("  [!] Kendaraan " + kid + " bukan jenis " + jenis + ".")
        tekan_enter()
        return

    # Input jumlah hari
    jumlah_hari = input_angka("  Jumlah hari sewa (1-30): ", 1, 30)

    # Cek member
    cek_member()
    nama_penyewa = hasil_nama_member
    diskon       = hasil_diskon_member

    # Jika bukan member, input nama manual
    if nama_penyewa == "":
        nama_input = input("  Nama penyewa: ")
        nama_penyewa = hapus_spasi(nama_input)
        if nama_penyewa == "":
            nama_penyewa = "Umum"

    # Hitung biaya
    hitung_biaya(kendaraan[idx_k][3], jumlah_hari, diskon)
    id_trx = buat_id_transaksi()

    # Tampilkan ringkasan
    cetak_garis("-", 57)
    print("  RINGKASAN BOOKING")
    cetak_garis("-", 57)
    print("  ID Transaksi  : " + id_trx)
    print("  Nama Penyewa  : " + nama_penyewa)
    print("  Kendaraan     : [" + kid + "] " + kendaraan[idx_k][1])
    print("  Jenis         : " + kendaraan[idx_k][2])
    print("  Harga/Hari    : " + format_rupiah(kendaraan[idx_k][3]))
    print("  Lama Sewa     : " + str(jumlah_hari) + " hari")
    cetak_garis("-", 57)
    print("  Subtotal      : " + format_rupiah(hasil_subtotal))
    if diskon > 0:
        print("  Diskon (" + str(diskon) + "%)    : -" + format_rupiah(hasil_potongan))
    print("  TOTAL BAYAR   : " + format_rupiah(hasil_total))
    cetak_garis("=", 57)

    # Konfirmasi
    print("  Konfirmasi peminjaman?")
    print("  [1] Ya, Konfirmasi")
    print("  [2] Batal")
    konfirm = input_angka("  Pilih: ", 1, 2)

    if konfirm == 2:
        print("\n  Peminjaman dibatalkan.")
        tekan_enter()
        return

    # Simpan transaksi ke array 2D
    transaksi[jumlah_transaksi] = [
        id_trx,
        nama_penyewa,
        kid,
        kendaraan[idx_k][1],
        kendaraan[idx_k][2],
        jumlah_hari,
        hasil_total,
        diskon,
        "Aktif"
    ]
    jumlah_transaksi = jumlah_transaksi + 1

    # Update status kendaraan
    kendaraan[idx_k][4] = "Tidak"

    print("\n  Booking berhasil!")
    print("  Simpan ID Transaksi Anda: " + id_trx)
    tekan_enter()


# ══════════════════════════════════════════════
#  PROSES PENGEMBALIAN
# ══════════════════════════════════════════════

def proses_pengembalian():
    cetak_header("PENGEMBALIAN KENDARAAN")

    if jumlah_transaksi == 0:
        print("  Belum ada transaksi yang tercatat.")
        tekan_enter()
        return

    id_input = input("  Masukkan ID Transaksi (contoh: TRX-001): ")
    id_input = hapus_spasi(id_input)

    # Ubah ke huruf besar
    id_cari = ""
    for karakter in id_input:
        kode = ord(karakter)
        if 97 <= kode <= 122:
            id_cari = id_cari + chr(kode - 32)
        else:
            id_cari = id_cari + karakter

    idx_t = cari_transaksi_by_id(id_cari)

    if idx_t == -1:
        print("  [!] ID Transaksi tidak ditemukan.")
        tekan_enter()
        return

    trx = transaksi[idx_t]

    if trx[8] == "Selesai":
        print("  [!] Transaksi ini sudah pernah dikembalikan.")
        tekan_enter()
        return

    # Tampilkan detail
    cetak_garis("-", 57)
    print("  DETAIL TRANSAKSI")
    cetak_garis("-", 57)
    print("  ID Transaksi  : " + trx[0])
    print("  Nama Penyewa  : " + trx[1])
    print("  Kendaraan     : [" + trx[2] + "] " + trx[3])
    print("  Jenis         : " + trx[4])
    print("  Lama Sewa     : " + str(trx[5]) + " hari")
    print("  Total Bayar   : " + format_rupiah(trx[6]))
    cetak_garis("-", 57)
    print("  Pengembalian tepat waktu (sistem sederhana, tanpa tanggal).")
    cetak_garis("=", 57)

    # Konfirmasi
    print("  Konfirmasi pengembalian?")
    print("  [1] Ya, Kembalikan")
    print("  [2] Batal")
    konfirm = input_angka("  Pilih: ", 1, 2)

    if konfirm == 2:
        print("\n  Pengembalian dibatalkan.")
        tekan_enter()
        return

    # Update status transaksi
    transaksi[idx_t][8] = "Selesai"

    # Update status kendaraan via linear search
    idx_k = cari_kendaraan_by_id(trx[2])
    if idx_k != -1:
        kendaraan[idx_k][4] = "Ya"

    print("\n  Kendaraan [" + trx[2] + "] " + trx[3] + " berhasil dikembalikan.")
    print("  Status kendaraan kini: Tersedia")
    tekan_enter()


# ══════════════════════════════════════════════
#  RIWAYAT TRANSAKSI (diurutkan bubble sort by total bayar)
# ══════════════════════════════════════════════

def tampilkan_riwayat():
    cetak_header("RIWAYAT TRANSAKSI")

    if jumlah_transaksi == 0:
        print("  Belum ada transaksi yang tercatat.")
        tekan_enter()
        return

    # Gunakan bubble sort untuk menampilkan transaksi terurut
    data_sorted, jml = bubble_sort_transaksi_by_total()

    print("  {:<10}  {:<14}  {:<18}  {:>12}  {}".format(
        "ID Trx", "Nama Penyewa", "Kendaraan", "Total Bayar", "Status"
    ))
    cetak_garis("-", 57)

    for i in range(jml):
        t = data_sorted[i]
        nama_pendek    = t[1]
        kend_pendek    = "[" + t[2] + "] " + t[3]
        print("  {:<10}  {:<14}  {:<18}  {:>12}  {}".format(
            t[0],
            nama_pendek[:14],
            kend_pendek[:18],
            format_rupiah(t[6]),
            t[8]
        ))

    cetak_garis("-", 57)
    total_aktif   = 0
    total_selesai = 0
    for i in range(jumlah_transaksi):
        if transaksi[i][8] == "Aktif":
            total_aktif   = total_aktif + 1
        else:
            total_selesai = total_selesai + 1
    print("  Total: " + str(jumlah_transaksi) +
          "  |  Aktif: " + str(total_aktif) +
          "  |  Selesai: " + str(total_selesai))
    cetak_garis("=", 57)
    tekan_enter()


# ══════════════════════════════════════════════
#  DAFTAR KENDARAAN TERURUT (bubble sort by harga)
# ══════════════════════════════════════════════

def tampilkan_kendaraan_terurut():
    cetak_header("DAFTAR KENDARAAN (Urut Harga Termurah)")

    data_sorted = bubble_sort_kendaraan_by_harga()

    print("  {:<6}  {:<23}  {:<6}  {:>12}  {}".format(
        "ID", "Nama Kendaraan", "Jenis", "Harga/Hari", "Status"
    ))
    cetak_garis("-", 57)

    for i in range(MAX_KENDARAAN):
        baris  = data_sorted[i]
        if baris[4] == "Ya":
            status = "Tersedia"
        else:
            status = "Disewa  "
        print("  {:<6}  {:<23}  {:<6}  {:>12}  {}".format(
            baris[0], baris[1], baris[2],
            format_rupiah(baris[3]), status
        ))

    cetak_garis("=", 57)
    tekan_enter()


# ══════════════════════════════════════════════
#  CARI KENDARAAN (linear search by nama)
# ══════════════════════════════════════════════

def fitur_cari_kendaraan():
    cetak_header("CARI KENDARAAN")

    kata = input("  Masukkan kata kunci nama kendaraan: ")
    kata = hapus_spasi(kata)
    kata_lower = samakan_huruf(kata)

    cetak_garis("-", 57)
    print("  Hasil pencarian untuk: \"" + kata + "\"")
    cetak_garis("-", 57)

    ditemukan = False
    for i in range(MAX_KENDARAAN):
        nama_lower = samakan_huruf(kendaraan[i][1])
        # Cek apakah kata_lower ada di dalam nama_lower (manual substring search)
        found_in = False
        panjang_nama = len(nama_lower)
        panjang_kata = len(kata_lower)
        for j in range(panjang_nama - panjang_kata + 1):
            cocok = True
            for k in range(panjang_kata):
                if nama_lower[j + k] != kata_lower[k]:
                    cocok = False
            if cocok:
                found_in = True

        if found_in:
            ditemukan = True
            if kendaraan[i][4] == "Ya":
                status = "Tersedia"
            else:
                status = "Disewa  "
            print("  [" + kendaraan[i][0] + "] " + kendaraan[i][1] +
                  " | " + kendaraan[i][2] +
                  " | " + format_rupiah(kendaraan[i][3]) +
                  " | " + status)

    if not ditemukan:
        print("  Tidak ditemukan kendaraan dengan kata kunci tersebut.")

    cetak_garis("=", 57)
    tekan_enter()


# ══════════════════════════════════════════════
#  MENU UTAMA
# ══════════════════════════════════════════════

def menu_utama():
    while True:
        cetak_header("MENU UTAMA")
        print("  [1]  Peminjaman Kendaraan")
        print("  [2]  Pengembalian Kendaraan")
        print("  [3]  Ketersediaan Kendaraan")
        print("  [4]  Riwayat Transaksi")
        print("  [5]  Daftar Kendaraan (Urut Harga)")
        print("  [6]  Cari Kendaraan")
        print("  [0]  Keluar")
        cetak_garis("-", 57)

        pilihan = input("  Pilih menu: ")

        if pilihan == "1":
            proses_peminjaman()
        elif pilihan == "2":
            proses_pengembalian()
        elif pilihan == "3":
            cetak_header("KETERSEDIAAN KENDARAAN")
            print("\n  Filter:")
            print("  [1] Semua Kendaraan")
            print("  [2] Mobil Saja")
            print("  [3] Motor Saja")
            sub = input_angka("  Pilih: ", 1, 3)
            if sub == 1:
                tampilkan_ketersediaan("")
            elif sub == 2:
                tampilkan_ketersediaan("Mobil")
            else:
                tampilkan_ketersediaan("Motor")
            tekan_enter()
        elif pilihan == "4":
            tampilkan_riwayat()
        elif pilihan == "5":
            tampilkan_kendaraan_terurut()
        elif pilihan == "6":
            fitur_cari_kendaraan()
        elif pilihan == "0":
            bersihkan_layar()
            print("\n  Terima kasih telah menggunakan Sistem Rental Kendaraan.")
            print("  Sampai jumpa!\n")
            break
        else:
            print("  [!] Pilihan tidak valid.")
            tekan_enter()


# ══════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════

def main():
    menu_utama()


if __name__ == "__main__":
    main()
