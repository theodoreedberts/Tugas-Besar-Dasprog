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

transaksi = [None] * MAX_TRANSAKSI
jumlah_transaksi = 0   
id_counter       = 1   

def panjang_teks(teks):
    # Kamus Lokal
    # teks     : string/teks yang akan dihitung panjangnya
    # hitung   : variabel untuk menyimpan jumlah karakter
    # karakter : variabel iterasi untuk setiap karakter dalam teks
    
    # def ini untuk menggantikan len()
    hitung = 0
    for karakter in str(teks):
        hitung = hitung + 1
    return hitung

#Kedua def ini untuk memformat output tabel agar kolom-kolom terlihat rapi dan menjaga lebar tampilan tetap konsisten ketika mencetak daftar kendaraan, member, atau transaksi.
def rata_kiri(teks, panjang):
    # Kamus Lokal
    # teks    : teks yang akan diformat
    # panjang : panjang karakter total yang diinginkan
    # t       : salinan teks dalam bentuk string
    # p       : panjang string t
    # sisa    : jumlah spasi yang perlu ditambahkan
    # i       : variabel iterasi
    t = str(teks)
    p = panjang_teks(t)
    sisa = panjang - p
    if sisa > 0:
        for i in range(sisa):
            t = t + " "
    return t

def rata_kanan(teks, panjang):
    # Kamus Lokal
    # teks    : teks yang akan diformat
    # panjang : panjang karakter total yang diinginkan
    # t       : salinan teks dalam bentuk string
    # p       : panjang string t
    # sisa    : jumlah spasi yang perlu ditambahkan di awal
    # spasi   : string yang menampung spasi tambahan
    # i       : variabel iterasi
    t = str(teks)
    p = panjang_teks(t)
    sisa = panjang - p
    spasi = ""
    if sisa > 0:
        for i in range(sisa):
            spasi = spasi + " "
    return spasi + t

def potong_teks(teks, batas):
    # Kamus Lokal
    # teks  : teks yang akan dipotong
    # batas : batas jumlah karakter maksimal
    # t     : salinan teks dalam bentuk string
    # p     : panjang string t
    # hasil : string yang menampung teks hasil potongan
    # i     : variabel iterasi
    
    # Pengganti slicing string teks[:batas]
    t = str(teks)
    p = panjang_teks(t)
    if p <= batas:
        return t
    hasil = ""
    for i in range(batas):
        hasil = hasil + t[i]
    return hasil

# ==============================================
#  FUNGSI MAPPING KARAKTER 
# ==============================================
# Mengubah huruf besar ke kecil. jika input dimasukkan huruf kecil bisa juga masuk ke dalam inputnya meskipun di perintah kodingannya huruf besar.
def samakan_huruf(teks):
    # Kamus Lokal
    # teks      : teks yang akan diubah menjadi huruf kecil
    # h_besar   : string berisi daftar huruf besar
    # h_kecil   : string berisi daftar huruf kecil
    # hasil     : string yang menampung hasil teks huruf kecil
    # karakter  : variabel iterasi untuk setiap karakter pada teks
    # ditemukan : boolean untuk menandai apakah karakter adalah huruf besar
    # i         : variabel iterasi indeks
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
    # Kamus Lokal
    # teks      : teks yang akan diubah menjadi huruf besar
    # h_besar   : string berisi daftar huruf besar
    # h_kecil   : string berisi daftar huruf kecil
    # hasil     : string yang menampung hasil teks huruf besar
    # karakter  : variabel iterasi untuk setiap karakter pada teks
    # ditemukan : boolean untuk menandai apakah karakter adalah huruf kecil
    # i         : variabel iterasi indeks
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

def bersihkan_layar():
    # Kamus Lokal
    # i : variabel iterasi
    for i in range(5):
        print("")

def cetak_garis(karakter, panjang):
    # Kamus Lokal
    # karakter : karakter yang akan dicetak sebagai garis
    # panjang  : jumlah karakter yang akan dicetak
    # baris    : string untuk menampung karakter garis
    # i        : variabel iterasi
    baris = ""
    for i in range(panjang):
        baris = baris + karakter
    print(baris)

def cetak_header(judul):
    # Kamus Lokal
    # judul : teks judul header yang akan dicetak
    bersihkan_layar()
    cetak_garis("=", 57)
    print("         SISTEM RENTAL KENDARAAN")
    cetak_garis("=", 57)
    print("  " + judul)
    cetak_garis("-", 57)

def format_rupiah(nominal):
    # Kamus Lokal
    # nominal : nilai angka/nominal yang akan diformat ke rupiah
    # angka   : string dari nilai nominal
    # hasil   : string hasil format
    # hitung  : variabel untuk menghitung jumlah digit yang sudah diproses
    # p_angka : panjang dari string angka
    # i       : variabel iterasi untuk membaca angka dari belakang
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
    # Kamus Lokal
    # kode : string yang menampung ID transaksi yang baru dibuat
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
    # Kamus Lokal
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
    # nilai_akhir   : angka hasil konversi dari string
    # i, j          : variabel iterasi
    
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
# Fungsi dari def ini membuang spasi kosong yang tidak sengaja terketik di awal atau di akhir input.
def hapus_spasi(teks):
    # Kamus Lokal
    # teks  : teks yang akan dihapus spasi di awal dan akhirnya
    # p     : panjang teks
    # i     : indeks awal teks yang bukan spasi
    # j     : indeks akhir teks yang bukan spasi
    # hasil : string teks hasil tanpa spasi berlebih
    # k     : variabel iterasi
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

# Ketiga fungsi ini memakai Sequential Search
def cari_kendaraan_by_id(id_cari):
    # Kamus Lokal
    # id_cari : ID kendaraan yang dicari
    # i       : variabel iterasi
    for i in range(MAX_KENDARAAN):
        if kendaraan[i][0] == id_cari:
            return i
    return -1

def cari_member_by_nama(nama_cari):
    # Kamus Lokal
    # nama_cari  : nama member yang dicari
    # nama_lower : nama pencarian yang sudah disamakan menjadi huruf kecil
    # i          : variabel iterasi
    nama_lower = samakan_huruf(nama_cari)
    for i in range(MAX_MEMBER):
        if member[i][0] == nama_lower:
            return i
    return -1

def cari_transaksi_by_id(id_cari):
    # Kamus Lokal
    # id_cari : ID transaksi yang dicari
    # i       : variabel iterasi
    for i in range(jumlah_transaksi):
        if transaksi[i] is not None:
            if transaksi[i][0] == id_cari:
                return i
    return -1

# Theodore
def bubble_sort_kendaraan_by_harga():
    # Kamus Lokal
    # salinan    : list baru yang berisi copy dari data kendaraan
    # i, j, x    : variabel iterasi
    # temp       : variabel sementara untuk menukar elemen (swap)
    # baris_copy : list untuk menampung salinan satu baris kendaraan
    # baris_asli : data baris asli dari array kendaraan
    salinan = []
    for i in range(MAX_KENDARAAN):
        baris_copy = []
        baris_asli = kendaraan[i]
        for x in range(5): 
            baris_copy = baris_copy + [baris_asli[x]]
        salinan = salinan + [baris_copy]
    for i in range(MAX_KENDARAAN - 1):
        for j in range(MAX_KENDARAAN - 1 - i):
            if salinan[j][3] > salinan[j + 1][3]:
                temp           = salinan[j]
                salinan[j]     = salinan[j + 1]
                salinan[j + 1] = temp
    return salinan
# kenneth
def bubble_sort_transaksi_by_total():
    # Kamus Lokal
    # temp_trx   : list baru berisi copy dari data transaksi yang aktif (tidak None)
    # jumlah     : jumlah transaksi riil
    # p, k, x    : variabel iterasi
    # _          : iterasi tak terpakai
    # tem        : variabel sementara untuk menukar elemen (swap)
    # baris_copy : list untuk menampung salinan satu baris transaksi
    # baris_asli : data baris asli dari array transaksi
    temp_trx = []
    for i in range(jumlah_transaksi):
        if transaksi[i] is not None:
            baris_copy = []
            baris_asli = transaksi[i]
            for x in range(9): 
                baris_copy = baris_copy + [baris_asli[x]]
            temp_trx = temp_trx + [baris_copy]
    jumlah = 0
    for _ in temp_trx:
        jumlah = jumlah + 1
    for p in range(0, jumlah - 1, 1):
        for k in range(jumlah - 1, p, -1):
            # descending
            if temp_trx[k][6] > temp_trx[k - 1][6]:
                tem             = temp_trx[k]
                temp_trx[k]     = temp_trx[k - 1]
                temp_trx[k - 1] = tem

    return temp_trx, jumlah


# ==============================================
#  TAMPILKAN KETERSEDIAAN KENDARAAN
# ==============================================

def tampilkan_ketersediaan(filter_jenis):
    # Kamus Lokal
    # filter_jenis : string untuk filter jenis kendaraan ("Mobil", "Motor", atau "")
    # k1, k2, k3, k4 : string penampung teks header kolom yang diformat
    # total        : jumlah total kendaraan sesuai filter
    # tersedia     : jumlah kendaraan yang tersedia
    # i            : variabel iterasi
    # baris        : variabel penampung data kendaraan per baris
    # status       : string status kendaraan ("Tersedia" atau "Disewa")
    # c1, c2, c3, c4 : string penampung teks data kolom yang diformat
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


# ==============================================
#  CEK MEMBER & HITUNG BIAYA
# ==============================================

hasil_nama_member   = ""
hasil_diskon_member = 0
hasil_subtotal = 0
hasil_potongan = 0
hasil_total    = 0

def cek_member():
    # Kamus Lokal
    # pilihan      : pilihan menu member (1=Ya, 2=Tidak)
    # selesai      : status loop verifikasi member
    # nama_input   : nama member yang dimasukkan pengguna
    # idx          : indeks member dalam daftar member, -1 jika tidak ditemukan
    # pilih_ulang  : pilihan ulang jika data member tidak ditemukan (0/1)
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
    #Kamus Lokal
    # hasil_subtotal    : rumus untuk menghitung tarif per hari berapa
    # hasil_potongan    : rumus diskon
    # hasil_total       : rumus total dari subtotal dikurangi diskon
    global hasil_subtotal, hasil_potongan, hasil_total
    hasil_subtotal = harga_per_hari * jumlah_hari
    hasil_potongan = (hasil_subtotal * diskon_persen) // 100
    hasil_total    = hasil_subtotal - hasil_potongan


# ==============================================
#  PROSES PEMINJAMAN
# ==============================================
# justin 
def proses_peminjaman():
    # Kamus Lokal
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
    # jika salah input pada ID Kendaraan
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
    # input berapa hari untuk disewa
    jumlah_hari = input_angka("  Jumlah hari sewa (1-30): ", 1, 30)
    # setelah diinput def cek_member akan mengecek datanya
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


# ==============================================
#  PROSES PENGEMBALIAN
# ==============================================
# Theodore
def proses_pengembalian():
    # Kamus Lokal
    # id_input    : input ID transaksi dari pengguna
    # id_cari     : ID transaksi yang sudah disamakan huruf besarnya
    # idx_t       : indeks transaksi dalam array transaksi, -1 jika tidak ditemukan
    # trx         : data transaksi yang ditemukan
    # konfirm     : pilihan konfirmasi pengembalian (1=Ya, 2=Batal)
    # idx_k       : indeks kendaraan terkait dalam array kendaraan
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


# ==============================================
#  RIWAYAT TRANSAKSI 
# ==============================================
# kenneth
def tampilkan_riwayat():
    # Kamus Lokal
    # data_sorted : salinan daftar transaksi yang sudah diurutkan berdasarkan total bayar
    # jml         : jumlah transaksi yang valid dalam daftar transaksi yang disortir
    # t           : baris data transaksi saat dicetak
    # nama_cetak  : nama penyewa yang sudah dipotong agar sesuai lebar kolom
    # kend_awal   : teks kendaraan gabungan ID dan nama kendaraan
    # kend_cetak  : teks kendaraan yang sudah dipotong agar sesuai lebar kolom
    # k1,k2,k3,k4 : teks kolom yang sudah diformat rata kiri/kanan
    # total_aktif : jumlah transaksi status Aktif
    # total_selesai : jumlah transaksi status Selesai
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


# ==============================================
#  DAFTAR KENDARAAN TERURUT 
# ==============================================

def tampilkan_kendaraan_terurut():
    # Kamus Lokal
    # data_sorted    : data kendaraan yang telah diurutkan berdasarkan harga
    # k1, k2, k3, k4 : string penampung teks header kolom yang diformat
    # i              : variabel iterasi
    # baris          : variabel penampung data kendaraan per baris
    # status         : string status kendaraan
    # c1, c2, c3, c4 : string penampung teks data kolom yang diformat
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


# ==============================================
#  CARI KENDARAAN 
# ==============================================

def fitur_cari_kendaraan():
    # Kamus Lokal
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


# ==============================================
#  MENU UTAMA
# ==============================================
# Theodore
def menu_utama():
    # Kamus Lokal
    # program_jalan : boolean untuk menjaga loop menu tetap berjalan
    # pilihan       : input pilihan menu dari user
    # sub           : input pilihan submenu
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


# ==============================================
#  ENTRY POINT
# ==============================================

def main():
    menu_utama()


if __name__ == "__main__":
    main()
