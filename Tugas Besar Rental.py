# ===============================================
#   SISTEM RENTAL KENDARAAN - Tugas Besar Dasprog
# ===============================================
# Fitur:
#   1. Peminjaman & pengembalian kendaraan
#   2. Daftar jenis kendaraan (Mobil, Motor)
#   3. Laporan ketersediaan kendaraan real-time
#   4. Simulasi booking & perhitungan biaya + diskon member
#   5. Sistem pengembalian via ID transaksi


# ─────────────────────────────────────────────
#  KONSTANTA UKURAN ARRAY
# ─────────────────────────────────────────────

MAX_KENDARAAN   = 10
MAX_MEMBER      = 7
MAX_TRANSAKSI   = 50

# ─────────────────────────────────────────────
#  ARRAY 1D & 2D - DATA KENDARAAN
# ─────────────────────────────────────────────

kendaraan = [
    ["M001", "Toyota Avanza",           "Mobil",    350000,     "Ya"    ],
    ["M002", "Honda Brio",              "Mobil",    280000,     "Ya"    ],
    ["M003", "Mitsubishi Xpander",      "Mobil",    450000,     "Ya"    ],
    ["M004", "Toyota Innova",           "Mobil",    500000,     "Tidak" ],
    ["M005", "Toyota Vellfire PHEV",    "Mobil",   1450000,     "Ya"    ],
    ["T001", "Honda Vario 150",         "Motor",     80000,     "Ya"    ],
    ["T002", "Yamaha NMAX",             "Motor",    100000,     "Ya"    ],
    ["T003", "Honda PCX",               "Motor",    110000,     "Ya"    ],
    ["T004", "Yamaha Aerox",            "Motor",     90000,     "Tidak" ],
    ["T005", "BMW S 1000 RR",           "Motor",    940000,     "Ya"    ],
]

# ─────────────────────────────────────────────
#  ARRAY 2D - DATA MEMBER
# ─────────────────────────────────────────────

member = [
    ["budi",      "Budi Santoso",              15],
    ["siti",      "Siti Rahayu",               10],
    ["andi",      "Andi Wijaya",               20],
    ["rossevine", "Rossevine Artha",           45],
    ["kenneth",   "Kenneth Ansell Hansjaya",   20],
    ["justin",    "Justin Gabriel Kristianto", 30],
    ["theo",      "Theodore Edbert Suryo",     25]
]

# ─────────────────────────────────────────────
#  ARRAY 2D - DATA TRANSAKSI (maks 50 transaksi)
# ─────────────────────────────────────────────

transaksi = [None] * MAX_TRANSAKSI
jumlah_transaksi = 0   
id_counter       = 1   

def panjang_teks(teks):
    # Pengganti len()
    hitung = 0
    for karakter in str(teks):
        hitung = hitung + 1
    return hitung

def rata_kiri(teks, panjang):
    # Pengganti {:<} pada format()
    t = str(teks)
    p = panjang_teks(t)
    sisa = panjang - p
    if sisa > 0:
        for i in range(sisa):
            t = t + " "
    return t

def rata_kanan(teks, panjang):
    # Pengganti {:>} pada format()
    t = str(teks)
    p = panjang_teks(t)
    sisa = panjang - p
    spasi = ""
    if sisa > 0:
        for i in range(sisa):
            spasi = spasi + " "
    return spasi + t

def potong_teks(teks, batas):
    # Pengganti slicing string teks[:batas]
    t = str(teks)
    p = panjang_teks(t)
    if p <= batas:
        return t
    hasil = ""
    for i in range(batas):
        hasil = hasil + t[i]
    return hasil

# ══════════════════════════════════════════════
#  FUNGSI MAPPING KARAKTER (TANPA ORD & CHR)
# ══════════════════════════════════════════════

def samakan_huruf(teks):
    # Mengubah huruf besar ke kecil (Pengganti .lower() tanpa ord/chr)
    h_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    h_kecil = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""
    
    for karakter in teks:
        ditemukan = False
        for i in range(26):
            if karakter == h_besar[i]:
                hasil = hasil + h_kecil[i]
                ditemukan = True
        if not ditemukan:
            hasil = hasil + karakter
            
    return hasil

def ubah_huruf_besar(teks):
    h_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    h_kecil = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""
    
    for karakter in teks:
        ditemukan = False
        for i in range(26):
            if karakter == h_kecil[i]:
                hasil = hasil + h_besar[i]
                ditemukan = True
        if not ditemukan:
            hasil = hasil + karakter
            
    return hasil

# ══════════════════════════════════════════════
#  FUNGSI UTILITAS
# ══════════════════════════════════════════════

def bersihkan_layar():
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
    angka = str(nominal)
    hasil = ""
    hitung = 0
    p_angka = panjang_teks(angka)
    
    for i in range(p_angka - 1, -1, -1):
        if hitung > 0 and hitung % 3 == 0:
            hasil = "." + hasil
        hasil = angka[i] + hasil
        hitung = hitung + 1
    return "Rp " + hasil

def buat_id_transaksi():
    global id_counter
    if id_counter < 10:
        kode = "TRX-00" + str(id_counter)
    elif id_counter < 100:
        kode = "TRX-0" + str(id_counter)
    else:
        kode = "TRX-" + str(id_counter)
    id_counter = id_counter + 1
    return kode
# justin
def input_angka(prompt, min_val, max_val):
    angka_valid = "0123456789"
    input_selesai = False
    hasil_angka = 0
    
    while not input_selesai:
        input_teks = input(prompt)
        p = panjang_teks(input_teks)
        
        if p == 0:
            print("  [!] Input tidak boleh kosong. Masukkan angka.")
        else:
            semua_angka = True
            for i in range(p):
                char_dikenal = False
                for j in range(10):
                    if input_teks[i] == angka_valid[j]:
                        char_dikenal = True
                if not char_dikenal:
                    semua_angka = False
                    
            if not semua_angka:
                print("  [!] Input tidak valid. Masukkan hanya angka.")
            else:
                nilai_akhir = 0
                for i in range(p):
                    for j in range(10):
                        if input_teks[i] == angka_valid[j]:
                            nilai_akhir = (nilai_akhir * 10) + j
                
                if nilai_akhir < min_val:
                    print("  [!] Masukkan angka minimal " + str(min_val) + ".")
                elif nilai_akhir > max_val:
                    print("  [!] Masukkan angka maksimal " + str(max_val) + ".")
                else:
                    hasil_angka = nilai_akhir
                    input_selesai = True
                    
    return hasil_angka

def tekan_enter():
    input("\n  Tekan Enter untuk kembali ke menu...")

def hapus_spasi(teks):
    p = panjang_teks(teks)
    if p == 0:
        return ""
        
    i = 0
    while i < p and teks[i] == " ":
        i = i + 1
        
    j = p - 1
    while j >= 0 and teks[j] == " ":
        j = j - 1
        
    if i > j:
        return ""
        
    hasil = ""
    for k in range(i, j + 1):
        hasil = hasil + teks[k]
    return hasil


# ══════════════════════════════════════════════
#  SEARCHING & SORTING
# ══════════════════════════════════════════════

def cari_kendaraan_by_id(id_cari):
    for i in range(MAX_KENDARAAN):
        if kendaraan[i][0] == id_cari:
            return i
    return -1

def cari_member_by_nama(nama_cari):
    nama_lower = samakan_huruf(nama_cari)
    for i in range(MAX_MEMBER):
        if member[i][0] == nama_lower:
            return i
    return -1

def cari_transaksi_by_id(id_cari):
    for i in range(jumlah_transaksi):
        if transaksi[i] is not None:
            if transaksi[i][0] == id_cari:
                return i
    return -1

# Theodore
def bubble_sort_kendaraan_by_harga():
    salinan = []
    for i in range(MAX_KENDARAAN):
        salinan = salinan + [kendaraan[i][:]]

    for i in range(MAX_KENDARAAN - 1):
        for j in range(MAX_KENDARAAN - 1 - i):
            if salinan[j][3] > salinan[j + 1][3]:
                temp           = salinan[j]
                salinan[j]     = salinan[j + 1]
                salinan[j + 1] = temp
    return salinan

def bubble_sort_transaksi_by_total():
    temp_trx = []
    for i in range(jumlah_transaksi):
        if transaksi[i] is not None:
            temp_trx = temp_trx + [transaksi[i][:]]

    jumlah = 0
    for _ in temp_trx:
        jumlah = jumlah + 1

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
    if filter_jenis == "":
        cetak_header("KETERSEDIAAN SEMUA KENDARAAN")
    else:
        cetak_header("KETERSEDIAAN KENDARAAN - " + filter_jenis)

    k1 = rata_kiri("ID", 6)
    k2 = rata_kiri("Nama Kendaraan", 23)
    k3 = rata_kiri("Jenis", 6)
    k4 = rata_kanan("Harga/Hari", 12)
    print("  " + k1 + "  " + k2 + "  " + k3 + "  " + k4 + "  Status")
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
            
            c1 = rata_kiri(baris[0], 6)
            c2 = rata_kiri(baris[1], 23)
            c3 = rata_kiri(baris[2], 6)
            c4 = rata_kanan(format_rupiah(baris[3]), 12)
            print("  " + c1 + "  " + c2 + "  " + c3 + "  " + c4 + "  " + status)

    cetak_garis("-", 57)
    print("  Total: " + str(total) + " unit  |  Tersedia: " + str(tersedia) +
          "  |  Disewa: " + str(total - tersedia))
    cetak_garis("=", 57)


# ══════════════════════════════════════════════
#  CEK MEMBER & HITUNG BIAYA
# ══════════════════════════════════════════════

hasil_nama_member   = ""
hasil_diskon_member = 0
hasil_subtotal = 0
hasil_potongan = 0
hasil_total    = 0

def cek_member():
    global hasil_nama_member, hasil_diskon_member
    hasil_nama_member   = ""
    hasil_diskon_member = 0
    print("\n  Apakah Anda terdaftar sebagai member?")
    print("  [1] Ya")
    print("  [2] Tidak")
    pilihan = input_angka("  Pilih: ", 1, 2)
    if pilihan == 2:
        return
    selesai = False 
    while selesai == False:
        nama_input = input("  Masukkan nama member: ")
        nama_input = hapus_spasi(nama_input)
        idx = cari_member_by_nama(nama_input)
        if idx != -1:
            hasil_nama_member   = member[idx][1]
            hasil_diskon_member = member[idx][2]
            print("  Selamat datang, " + hasil_nama_member + "!")
            print("  Anda mendapat diskon " + str(hasil_diskon_member) + "%.")
            selesai = True
        else:
            print("  [!] Nama member tidak ditemukan.")
            print("  [1] Coba ketik ulang nama member")
            print("  [0] Keluar (Lanjut tanpa diskon)")
            pilih_ulang = input_angka("  Pilih: ", 0, 1)
            if pilih_ulang == 0:
                print("  Lanjut peminjaman tanpa diskon member.")
                selesai = True 

def hitung_biaya(harga_per_hari, jumlah_hari, diskon_persen):
    global hasil_subtotal, hasil_potongan, hasil_total
    hasil_subtotal = harga_per_hari * jumlah_hari
    hasil_potongan = (hasil_subtotal * diskon_persen) // 100
    hasil_total    = hasil_subtotal - hasil_potongan


# ══════════════════════════════════════════════
#  PROSES PEMINJAMAN
# ══════════════════════════════════════════════
# justin 
def proses_peminjaman():
    global jumlah_transaksi

    cetak_header("PEMINJAMAN KENDARAAN")
    tampilkan_ketersediaan("")

    print("\n  Pilih Jenis Kendaraan:")
    print("  [1] Mobil")
    print("  [2] Motor")
    pilihan_jenis = input_angka("  Pilih: ", 1, 2)
    if pilihan_jenis == 1:
        jenis = "Mobil"
    else:
        jenis = "Motor"

    tampilkan_ketersediaan(jenis)

    ada_tersedia = False
    for i in range(MAX_KENDARAAN):
        if kendaraan[i][2] == jenis and kendaraan[i][4] == "Ya":
            ada_tersedia = True
    if not ada_tersedia:
        print("  [!] Tidak ada " + jenis + " yang tersedia saat ini.")
        tekan_enter()
        return

    print("\n  Masukkan ID kendaraan (contoh: M001 / T001):")
    kid_input = input("  ID Kendaraan: ")
    kid_input = hapus_spasi(kid_input)

    kid = ubah_huruf_besar(kid_input)
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

    jumlah_hari = input_angka("  Jumlah hari sewa (1-30): ", 1, 30)

    cek_member()
    nama_penyewa = hasil_nama_member
    diskon       = hasil_diskon_member
    if nama_penyewa == "":
        nama_input = input("  Nama penyewa: ")
        nama_penyewa = hapus_spasi(nama_input)
        if nama_penyewa == "":
            nama_penyewa = "Umum"

    hitung_biaya(kendaraan[idx_k][3], jumlah_hari, diskon)
    id_trx = buat_id_transaksi()
    
    # kenneth
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

    print("  Konfirmasi peminjaman?")
    print("  [1] Ya, Konfirmasi")
    print("  [2] Batal")
    konfirm = input_angka("  Pilih: ", 1, 2)

    if konfirm == 2:
        print("\n  Peminjaman dibatalkan.")
        tekan_enter()
        return

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
    kendaraan[idx_k][4] = "Tidak"

    print("\n  Booking berhasil!")
    print("  Simpan ID Transaksi Anda: " + id_trx)
    tekan_enter()


# ══════════════════════════════════════════════
#  PROSES PENGEMBALIAN
# ══════════════════════════════════════════════
# Theodore
def proses_pengembalian():
    cetak_header("PENGEMBALIAN KENDARAAN")

    if jumlah_transaksi == 0:
        print("  Belum ada transaksi yang tercatat.")
        tekan_enter()
        return

    id_input = input("  Masukkan ID Transaksi (contoh: TRX-001): ")
    id_input = hapus_spasi(id_input)

    id_cari = ubah_huruf_besar(id_input)
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
    print("  Pengembalian tepat waktu (sistem sederhana).")
    cetak_garis("=", 57)

    print("  Konfirmasi pengembalian?")
    print("  [1] Ya, Kembalikan")
    print("  [2] Batal")
    konfirm = input_angka("  Pilih: ", 1, 2)

    if konfirm == 2:
        print("\n  Pengembalian dibatalkan.")
        tekan_enter()
        return

    transaksi[idx_t][8] = "Selesai"

    idx_k = cari_kendaraan_by_id(trx[2])
    if idx_k != -1:
        kendaraan[idx_k][4] = "Ya"

    print("\n  Kendaraan [" + trx[2] + "] " + trx[3] + " berhasil dikembalikan.")
    print("  Status kendaraan kini: Tersedia")
    tekan_enter()


# ══════════════════════════════════════════════
#  RIWAYAT TRANSAKSI 
# ══════════════════════════════════════════════

def tampilkan_riwayat():
    cetak_header("RIWAYAT TRANSAKSI")

    if jumlah_transaksi == 0:
        print("  Belum ada transaksi yang tercatat.")
        tekan_enter()
        return

    data_sorted, jml = bubble_sort_transaksi_by_total()

    k1 = rata_kiri("ID Trx", 10)
    k2 = rata_kiri("Nama Penyewa", 14)
    k3 = rata_kiri("Kendaraan", 18)
    k4 = rata_kanan("Total Bayar", 12)
    print("  " + k1 + "  " + k2 + "  " + k3 + "  " + k4 + "  Status")
    cetak_garis("-", 57)

    for i in range(jml):
        t = data_sorted[i]
        nama_cetak = potong_teks(t[1], 14)
        kend_awal  = "[" + t[2] + "] " + t[3]
        kend_cetak = potong_teks(kend_awal, 18)
        
        c1 = rata_kiri(t[0], 10)
        c2 = rata_kiri(nama_cetak, 14)
        c3 = rata_kiri(kend_cetak, 18)
        c4 = rata_kanan(format_rupiah(t[6]), 12)
        
        print("  " + c1 + "  " + c2 + "  " + c3 + "  " + c4 + "  " + t[8])

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
#  DAFTAR KENDARAAN TERURUT 
# ══════════════════════════════════════════════

def tampilkan_kendaraan_terurut():
    cetak_header("DAFTAR KENDARAAN (Urut Harga Termurah)")

    data_sorted = bubble_sort_kendaraan_by_harga()

    k1 = rata_kiri("ID", 6)
    k2 = rata_kiri("Nama Kendaraan", 23)
    k3 = rata_kiri("Jenis", 6)
    k4 = rata_kanan("Harga/Hari", 12)
    print("  " + k1 + "  " + k2 + "  " + k3 + "  " + k4 + "  Status")
    cetak_garis("-", 57)

    for i in range(MAX_KENDARAAN):
        baris  = data_sorted[i]
        if baris[4] == "Ya":
            status = "Tersedia"
        else:
            status = "Disewa  "
            
        c1 = rata_kiri(baris[0], 6)
        c2 = rata_kiri(baris[1], 23)
        c3 = rata_kiri(baris[2], 6)
        c4 = rata_kanan(format_rupiah(baris[3]), 12)
            
        print("  " + c1 + "  " + c2 + "  " + c3 + "  " + c4 + "  " + status)

    cetak_garis("=", 57)
    tekan_enter()


# ══════════════════════════════════════════════
#  CARI KENDARAAN 
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
        found_in = False
        
        panjang_nama = panjang_teks(nama_lower)
        panjang_kata = panjang_teks(kata_lower)
        
        if panjang_nama >= panjang_kata:
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
# Theodore
def menu_utama():
    program_jalan = True
    while program_jalan:
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
            program_jalan = False
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
