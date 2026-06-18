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
    ["budi",      "Budi Santoso",               15],
    ["siti",      "Siti Rahayu",                10],
    ["andi",      "Andi Wijaya",                20],
    ["rossevine", "Rossevine Artha Nathasya",   45],
    ["kenneth",   "Kenneth Ansell Hansjaya",    20],
    ["justin",    "Justin Gabriel Kristianto",  30],
    ["theo",      "Theodore Edbert Suryo",      25]
]

# ─────────────────────────────────────────────
#  ARRAY 2D - DATA TRANSAKSI (maks 50 transaksi)
# ─────────────────────────────────────────────
# Kamus Data
# teks     : string/teks yang akan dihitung panjangnya
# hitung   : variabel untuk menyimpan jumlah karakter
# karakter : variabel iterasi untuk setiap karakter dalam teks

transaksi = [None] * MAX_TRANSAKSI
jumlah_transaksi = 0   
id_counter       = 1   

def panjang_teks(teks):
    hitung = 0
    for karakter in str(teks):
        hitung = hitung + 1
    return hitung

# ==============================================
#  FUNGSI MAPPING KARAKTER 
# ==============================================
# Mengubah huruf besar ke kecil. jika input dimasukkan huruf kecil bisa juga masuk ke dalam inputnya meskipun di perintah kodingannya huruf besar.
# Kamus Data
# teks      : teks yang akan diubah menjadi huruf kecil
# h_besar   : string berisi daftar huruf besar
# h_kecil   : string berisi daftar huruf kecil
# hasil     : string yang menampung hasil teks huruf kecil
# karakter  : variabel iterasi untuk setiap karakter pada teks
# ditemukan : boolean untuk menandai apakah karakter adalah huruf besar
# i         : variabel iterasi indeks

def samakan_huruf(teks):
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


# Kamus Data
# teks      : teks yang akan diubah menjadi huruf besar
# h_besar   : string berisi daftar huruf besar
# h_kecil   : string berisi daftar huruf kecil
# hasil     : string yang menampung hasil teks huruf besar
# karakter  : variabel iterasi untuk setiap karakter pada teks
# ditemukan : boolean untuk menandai apakah karakter adalah huruf kecil
# i         : variabel iterasi indeks

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

# ==============================================
#  FUNGSI UTILITAS
# ==============================================
# Kamus Data
# i : variabel iterasi

def bersihkan_layar():

    for i in range(5):
        print("")

# Kamus Data
# judul : teks judul header yang akan dicetak
def cetak_header(judul):

    bersihkan_layar()
    print("=" * 57)
    print("         SISTEM RENTAL KENDARAAN")
    print("=" * 57)
    print("  " + judul)
    print("-" * 57)


# Kamus Data
# nominal : nilai angka/nominal yang akan diformat ke rupiah
# angka   : string dari nilai nominal
# hasil   : string hasil format
# hitung  : variabel untuk menghitung jumlah digit yang sudah diproses
# p_angka : panjang dari string angka
# i       : variabel iterasi untuk membaca angka dari belakang
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

# Kamus Data
# kode : string yang menampung ID transaksi yang baru dibuat
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

# Kamus Data
# prompt        : teks pertanyaan/petunjuk untuk input
# min_val       : nilai minimal yang diperbolehkan
# max_val       : nilai maksimal yang diperbolehkan
# angka_valid   : string berisi karakter angka yang valid
# input_selesai : boolean status perulangan input
# hasil_angka   : variabel penampung nilai angka akhir
# input_teks    : teks yang diinputkan pengguna
# p             : panjang teks input
# semua_angka   : boolean untuk cek apakah input berisi angka semua
# char_dikenal  : boolean untuk cek validitas satu karakter
# nilai_akhir   : angka hasil fkonversi dari string
# i, j          : variabel iterasi

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

# Fungsi dari def ini membuang spasi kosong yang tidak sengaja terketik di awal atau di akhir input.
# Kamus Data
# teks  : teks yang akan dihapus spasi di awal dan akhirnya
# p     : panjang teks
# i     : indeks awal teks yang bukan spasi
# j     : indeks akhir teks yang bukan spasi
# hasil : string teks hasil tanpa spasi berlebih
# k     : variabel iterasi

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


# ==============================================
#  SEARCHING & SORTING
# ==============================================

def cari_kendaraan_by_id(id_cari): 
    Found = False
    i = 0
    N = MAX_KENDARAAN

    while i < N and not Found :
        if kendaraan[i][0] == id_cari:
            Found = True
        else:
            i = i + 1 
            
    if Found == True:
        ix = i   
    else:
        ix = -1  
    return ix

def cari_member_by_nama(nama_cari):    
    nama_lower = samakan_huruf(nama_cari)
    Found = False
    i = 0
    N = MAX_MEMBER
    
    while i < N and not Found:
        if member[i][0] == nama_lower:
            Found = True
        else:
            i = i + 1  
            
    if Found == True:
        ix = i 
    else:
        ix = -1 
    return ix

def cari_transaksi_by_id(id_cari):    
    Found = False
    i = 0
    N = jumlah_transaksi
    
    while i < N and not Found:
        if transaksi[i] != "":
            if transaksi[i][0] == id_cari:
                Found = True
            else:
                i = i + 1
        else:
            i = i + 1
            
    if Found == True:
        ix = i   
    else:
        ix = -1 
    return ix

def bubble_sort_kendaraan_by_harga():
    salinan = []
    for i in range(MAX_KENDARAAN):
        baris_copy = []
        baris_asli = kendaraan[i]
        for x in range(5): 
            baris_copy = baris_copy + [baris_asli[x]]
        salinan = salinan + [baris_copy]
        
    jumlah = MAX_KENDARAAN
    for p in range(0, jumlah - 1, 1):
        for k in range(jumlah - 1, p, -1):
            if salinan[k][3] < salinan[k - 1][3]:
                temp            = salinan[k]
                salinan[k]      = salinan[k - 1]
                salinan[k - 1]  = temp
                
    return salinan

def bubble_sort_transaksi_by_total():
    temp_trx = []
    for i in range(jumlah_transaksi):
        if transaksi[i] != "":
            baris_copy = []
            baris_asli = transaksi[i]
            for x in range(9): 
                baris_copy = baris_copy + [baris_asli[x]]
            temp_trx = temp_trx + [baris_copy]

    jumlah = 0
    for transaksi_aktif in temp_trx:
        jumlah = jumlah + 1

    for p in range(0, jumlah - 1, 1):
        for k in range(jumlah - 1, p, -1):
            if temp_trx[k][6] > temp_trx[k - 1][6]:
                tem             = temp_trx[k]
                temp_trx[k]     = temp_trx[k - 1]
                temp_trx[k - 1] = tem
    return temp_trx, jumlah


# ==============================================
#  TAMPILKAN KETERSEDIAAN KENDARAAN
# ==============================================
# Kamus Data
# filter_jenis : string untuk filter jenis kendaraan ("Mobil", "Motor", atau "")
# total        : jumlah total kendaraan sesuai filter
# tersedia     : jumlah kendaraan yang tersedia
# i            : variabel iterasi indeks array
# baris        : variabel penampung data kendaraan per baris
# status       : string status ketersediaan kendaraan

def tampilkan_ketersediaan(filter_jenis):
    if filter_jenis == "":
        cetak_header("KETERSEDIAAN SEMUA KENDARAAN")
    else:
        cetak_header("KETERSEDIAAN KENDARAAN - " + filter_jenis)
    
    print("  ID | Nama Kendaraan | Jenis | Harga/Hari | Status")
    print("-" * 57)

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
                status = "Disewa"
            
            print("  " + str(baris[0]) + " | " + str(baris[1]) + " | " + str(baris[2]) + " | " + format_rupiah(baris[3]) + " | " + status)

    print("=" * 57)
    print("  Total: " + str(total) + " unit  |  Tersedia: " + str(tersedia) + "  |  Disewa: " + str(total - tersedia))
    print("=" * 57)

# ==============================================
#  CEK MEMBER & HITUNG BIAYA
# ==============================================
# Kamus Data
# pilihan      : pilihan menu member (1=Ya, 2=Tidak)
# selesai      : status loop verifikasi member
# nama_input   : nama member yang dimasukkan pengguna
# idx          : indeks member dalam daftar member, -1 jika tidak ditemukan
# pilih_ulang  : pilihan ulang jika data member tidak ditemukan (0/1)

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

# ==============================================
#  HITUNG BIAYA
# ==============================================
#Kamus Data
# hasil_subtotal    : rumus untuk menghitung tarif per hari berapa
# hasil_potongan    : rumus diskon
# hasil_total       : rumus total dari subtotal dikurangi diskon
def hitung_biaya(harga_per_hari, jumlah_hari, diskon_persen):
    global hasil_subtotal, hasil_potongan, hasil_total
    hasil_subtotal = harga_per_hari * jumlah_hari
    hasil_potongan = (hasil_subtotal * diskon_persen) // 100
    hasil_total    = hasil_subtotal - hasil_potongan


# ==============================================
#  PROSES PEMINJAMAN
# ==============================================
# Kamus Data
# pilihan_jenis  : pilihan jenis kendaraan yang diambil pengguna (1=Mobil, 2=Motor)
# jenis          : jenis kendaraan yang dipilih sebagai string
# ada_tersedia   : flag apakah ada kendaraan tersedia berdasarkan jenis
# kid_input      : input ID kendaraan mentah dari pengguna
# kid            : ID kendaraan dalam huruf besar
# idx_k          : indeks kendaraan dalam daftar kendaraan
# jumlah_hari    : lama sewa dalam hari
# nama_penyewa   : nama penyewa, default "Umum" jika tidak diisi
# diskon         : diskon member dalam persen
# id_trx         : ID transaksi yang dibuat
# konfirm        : pilihan konfirmasi transaksi (1=Ya, 2=Batal)

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
            
    if ada_tersedia == False:
        print("  [!] Tidak ada " + jenis + " yang tersedia saat ini.")
        input("\n  Tekan Enter untuk kembali ke menu...")
        return

    print("\n  Masukkan ID kendaraan (contoh: M001 / T001):")
    kid_input = input("  ID Kendaraan: ")
    kid_input = hapus_spasi(kid_input)

    kid = ubah_huruf_besar(kid_input)
    idx_k = cari_kendaraan_by_id(kid)
    
    if idx_k == -1:
        print(" [!] ID kendaraan tidak ditemukan.")
        input("\n  Tekan Enter untuk kembali ke menu...")
        return

    if kendaraan[idx_k][4] == "Tidak":
        print(" [!] Kendaraan sedang tidak tersedia.")
        input("\n  Tekan Enter untuk kembali ke menu...")
        return

    if kendaraan[idx_k][2] != jenis:
        print("  [!] Kendaraan " + kid + " bukan jenis " + jenis + ".")
        input("\n  Tekan Enter untuk kembali ke menu...")
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
    

    print("=" * 57)
    print("  RINGKASAN BOOKING")
    print("=" * 57)
    print("  ID Transaksi  : " + id_trx)
    print("  Nama Penyewa  : " + nama_penyewa)
    print("  Kendaraan     : [" + kid + "] " + kendaraan[idx_k][1])
    print("  Jenis         : " + kendaraan[idx_k][2])
    print("  Harga/Hari    : " + format_rupiah(kendaraan[idx_k][3]))
    print("  Lama Sewa     : " + str(jumlah_hari) + " hari")
    print("=" * 57)
    print("  Subtotal      : " + format_rupiah(hasil_subtotal))
    if diskon > 0:
        print("  Diskon (" + str(diskon) + "%)    : -" + format_rupiah(hasil_potongan))
    print("  TOTAL BAYAR   : " + format_rupiah(hasil_total))
    print("=" * 57)

    print("  Konfirmasi peminjaman?")
    print("  [1] Ya, Konfirmasi")
    print("  [2] Batal")
    konfirm = input_angka("  Pilih: ", 1, 2)

    if konfirm == 2:
        print("\n  Peminjaman dibatalkan.")
        input("\n  Tekan Enter untuk kembali ke menu...")
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
    input("\n  Tekan Enter untuk kembali ke menu...")


# ==============================================
#  PROSES PENGEMBALIAN
# ==============================================
# Kamus Data
# id_input    : input ID transaksi dari pengguna
# id_cari     : ID transaksi yang sudah disamakan huruf besarnya
# idx_t       : indeks transaksi dalam array transaksi, -1 jika tidak ditemukan
# trx         : data transaksi yang ditemukan
# konfirm     : pilihan konfirmasi pengembalian (1=Ya, 2=Batal)
# idx_k       : indeks kendaraan terkait dalam array kendaraan

def proses_pengembalian():
    cetak_header("PENGEMBALIAN KENDARAAN")

    if jumlah_transaksi == 0:
        print("  Belum ada transaksi yang tercatat.")
        input("\n  Tekan Enter untuk kembali ke menu...")
        return

    id_input = input("  Masukkan ID Transaksi (contoh: TRX-001): ")
    id_input = hapus_spasi(id_input)

    id_cari = ubah_huruf_besar(id_input)
    idx_t = cari_transaksi_by_id(id_cari)

    if idx_t == -1:
        print("  [!] ID Transaksi tidak ditemukan.")
        input("\n  Tekan Enter untuk kembali ke menu...")
        return

    trx = transaksi[idx_t]

    if trx[8] == "Selesai":
        print("  [!] Transaksi ini sudah pernah dikembalikan.")
        input("\n  Tekan Enter untuk kembali ke menu...")
        return

    print("=" * 57)
    print("  DETAIL TRANSAKSI")
    print("=" * 57)
    print("  ID Transaksi  : " + trx[0])
    print("  Nama Penyewa  : " + trx[1])
    print("  Kendaraan     : [" + trx[2] + "] " + trx[3])
    print("  Jenis         : " + trx[4])
    print("  Lama Sewa     : " + str(trx[5]) + " hari")
    print("  Total Bayar   : " + format_rupiah(trx[6]))
    print("=" * 57)
    print("  Pengembalian tepat waktu (sistem sederhana).")
    print("=" * 57)

    print("  Konfirmasi pengembalian?")
    print("  [1] Ya, Kembalikan")
    print("  [2] Batal")
    konfirm = input_angka("  Pilih: ", 1, 2)

    if konfirm == 2:
        print("\n  Pengembalian dibatalkan.")
        input("\n  Tekan Enter untuk kembali ke menu...")
        return

    transaksi[idx_t][8] = "Selesai"

    idx_k = cari_kendaraan_by_id(trx[2])
    if idx_k != -1:
        kendaraan[idx_k][4] = "Ya"

    print("\n  Kendaraan [" + trx[2] + "] " + trx[3] + " berhasil dikembalikan.")
    print("  Status kendaraan kini: Tersedia")
    input("\n  Tekan Enter untuk kembali ke menu...")


# ==============================================
#  RIWAYAT TRANSAKSI 
# ==============================================
# Kamus Data
# data_sorted   : list/array baru menampung data transaksi terurut omset terbesar
# jml           : variabel penampung jumlah riil transaksi yang valid (bukan None)
# i             : variabel iterasi indeks untuk looping
# t             : variabel penampung data satu baris transaksi yang sedang diproses
# total_aktif   : counter hitung jumlah transaksi status "Aktif"
# total_selesai : counter hitung jumlah transaksi status "Selesai"

def tampilkan_riwayat():
    cetak_header("RIWAYAT TRANSAKSI")
    if jumlah_transaksi == 0:
        print("  Belum ada transaksi yang tercatat.")
        input("\n  Tekan Enter untuk kembali ke menu...")
        return

    data_sorted, jml = bubble_sort_transaksi_by_total()

    print("  ID Trx | Nama Penyewa | Kendaraan | Total Bayar | Status")
    print("=" * 57)

    for i in range(jml):
        t = data_sorted[i]
        print("  " + str(t[0]) + " | " + str(t[1]) + " | [" + str(t[2]) + "] " + str(t[3]) + " | " + format_rupiah(t[6]) + " | " + str(t[8]))

    print("=" * 57)
    
    total_aktif   = 0
    total_selesai = 0
    for i in range(jumlah_transaksi):
        if transaksi[i][8] == "Aktif":
            total_aktif   = total_aktif + 1
        else:
            total_selesai = total_selesai + 1
            
    print("  Total: " + str(jumlah_transaksi) + "  |  Aktif: " + str(total_aktif) + "  |  Selesai: " + str(total_selesai))
    print("=" * 57)
    input("\n  Tekan Enter untuk kembali ke menu...")

# ==============================================
#  DAFTAR KENDARAAN TERURUT 
# ==============================================
# Kamus Data
# data_sorted  : list/array baru yang menampung hasil urutan dari fungsi bubble sort
# i            : variabel iterasi indeks untuk looping
# baris        : variabel penampung data satu baris kendaraan saat dicetak
# status       : string untuk mengubah tanda "Ya"/"Tidak" menjadi teks "Tersedia"/"Disewa"

def tampilkan_kendaraan_terurut(): 
    cetak_header("DAFTAR KENDARAAN (Urut Harga Termurah)")

    data_sorted = bubble_sort_kendaraan_by_harga()

    print("  ID | Nama Kendaraan | Jenis | Harga/Hari | Status")
    print("=" * 57)

    for i in range(MAX_KENDARAAN):
        baris  = data_sorted[i]
        
        if baris[4] == "Ya":
            status = "Tersedia"
        else:
            status = "Disewa"
            
        print("  " + str(baris[0]) + " | " + str(baris[1]) + " | " + str(baris[2]) + " | " + format_rupiah(baris[3]) + " | " + status)

    print("=" * 57)
    input("\n  Tekan Enter untuk kembali ke menu...")

# ==============================================
#  CARI KENDARAAN 
# ==============================================
# Kamus Data
# kata         : kata kunci input pencarian
# kata_lower   : kata kunci yang diubah menjadi huruf kecil
# ditemukan    : boolean status apakah kendaraan ditemukan
# i, j, k      : variabel iterasi
# nama_lower   : nama kendaraan yang diubah menjadi huruf kecil
# found_in     : boolean kecocokan kata pada string nama
# panjang_nama : panjang string nama kendaraan
# panjang_kata : panjang string kata kunci
# cocok        : boolean kecocokan per karakter
# status       : string status ketersediaan kendaraan

def fitur_cari_kendaraan():
    cetak_header("CARI KENDARAAN")

    kata = input("  Masukkan kata kunci nama kendaraan: ")
    kata = hapus_spasi(kata)
    kata_lower = samakan_huruf(kata)

    print("=" * 57)
    print("  Hasil pencarian untuk: \"" + kata + "\"")
    print("=" * 57)

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

    print("=" * 57)
    input("\n  Tekan Enter untuk kembali ke menu...")

# ==============================================
#  MENU UTAMA
# ==============================================
# Kamus Data
# program_jalan : boolean untuk menjaga loop menu tetap berjalan
# pilihan       : input pilihan menu dari user
# sub           : input pilihan submenu

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
        print("=" * 57)
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
            input("\n  Tekan Enter untuk kembali ke menu...")
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
            input("\n  Tekan Enter untuk kembali ke menu...")
def main():
    menu_utama()
if __name__ == "__main__":
    main()
