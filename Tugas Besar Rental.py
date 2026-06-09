MAX_KENDARAAN = 10
MAX_MEMBER = 6
daftar_kendaraan = [
    # Kenneth
    ["M001", "Toyota Avanza","Mobil", 400000,"Ya"],
    ["M002", "Daihatsu Luxio","Mobil",450000,"Ya"],
    ["M003", "Nissan Serena e-Power","Mobil", 700000,"Ya"],
    ["M004", "Toyota Alphard","Mobil", 890000,"Ya"],
    ["M005", "BMW X5","Mobil",1200000,"Ya"],
    # Theodore
    ["T001", "Honda Vario 150", "Motor", 100000, "Ya"],
    ["T002", "Yamaha NMAX", "Motor", 150000, "Ya"],
    ["T003", "Honda PCX", "Motor", 120000, "Ya"],
    ["T004", "Yamaha Aerox", "Motor", 130000, "Tidak"],
    ["T005", "BMW M 1000 R", "Motor", 950000, "Tidak"]
]

member = [
    #Theodore
    ["Budi", "Budi Santoso", 15],
    ["Siti", "Siti Rahayu", 10],
    ["Andi", "Andi Wijaya", 20],
    ["Justin", "Justin Gabriel Kristianto", 15],
    ["Kenneth", "Kenneth Ansell", 10],
    ["Theo", "Theodore Edbert", 20],
]

# Kenneth
def cari_kendaraan_by_id(id_cari):
    for i in range(MAX_KENDARAAN):
        if daftar_kendaraan[i][0] == id_cari:
            return i
    return -1
def cari_member_by_nama(nama_cari):
    nama_lower = samakan_huruf(nama_cari) # dibuat menyusul
    for i in range(MAX_MEMBER):
        if member[i][0] == nama_lower:
            return i
    return -1

def input_angka(prompt):
    while True:
        nilai = input(prompt)
        valid = True
        for karakter in nilai:
            if karakter < '0' or karakter > '9':
                valid = False
        if valid and nilai != "":
            return int(nilai)
        print("Input harus berupa angka!")

def cek_member():
    hasil_nama_member   = ""
    hasil_diskon_member = 0
    print("\n Apakah Anda Terdaftar sebagai Member?")
    print("[1] Ya")
    print("[2] Tidak")
    pilihan = input_angka("Pilih:",1,2)
    if pilihan == 2:
        return
    nama_input = input("Masukkan nama member: ")
    idx = cari_member_by_nama(nama_input)
    hasil_nama_member = member[idx][1]
    hasil_diskon_member = member[idx][2]
    print("Selamat datang,",hasil_nama_member,"!")
    print("Anda mendapat diskon",str(hasil_diskon_member),"%.")
    return hasil_diskon_member,hasil_nama_member
    


            
# Justin
def proses_peminjaman():
    print("\n==============================================")
    print("             PROSES PEMINJAMAN UNIT           ")
    print("==============================================")
    print(" PILIH JENIS KENDARAAN YANG INGIN DIPINJAM:")
    print(" [1] Mobil")
    print(" [2] Motor")
    print("==============================================")
    
    pilihan = input("Masukkan pilihan jenis (1/2): ")
    
    jenis_terpilih = ""
    if (pilihan == "1"):
        jenis_terpilih = "Mobil"
    elif (pilihan == "2"):
        jenis_terpilih = "Motor"
    else:
        print("Pilihan jenis tidak valid. Kembali ke Menu Utama.")
        return  

    print("\n=========================================================================")
    print("                     DAFTAR KENDARAAN " + jenis_terpilih + " TERSEDIA                 ")
    print("=========================================================================")
    print("ID      | Nama Kendaraan             | Jenis   | Tarif/Hari   | Tersedia")
    print("-------------------------------------------------------------------------")
    
    for i in range(MAX_KENDARAAN):
        id_k   = daftar_kendaraan[i][0]
        nama   = daftar_kendaraan[i][1]
        jenis  = daftar_kendaraan[i][2]
        tarif  = daftar_kendaraan[i][3]
        status = daftar_kendaraan[i][4]
        
        if (jenis == jenis_terpilih and status == "Ya"):
            print(f"{id_k} \t {nama} \t {jenis} \t Rp {tarif} \t {status}")
                
    print("=========================================================================")

#Theodore
def proses_pengembalian():
    print("PENGEMBALIAN KENDARAAN")
    
    if (jumlah_transsaksi == 0):
        print("Belum ada transaksi yang tercatat")
        print()
        return
    
    id_input = input("Masukkan ID Transaksi (contoh: TRX-001): ")
    id_input = hapus_spasi(id_input)

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

    print("  DETAIL TRANSAKSI")
    print("  ID Transaksi  : " + trx[0])
    print("  Nama Penyewa  : " + trx[1])
    print("  Kendaraan     : [" + trx[2] + "] " + trx[3])
    print("  Jenis         : " + trx[4])
    print("  Lama Sewa     : " + str(trx[5]) + " hari")
    print("  Total Bayar   : " + format_rupiah(trx[6]))
    print("  Pengembalian tepat waktu (sistem sederhana, tanpa tanggal).")
    
#Theodore
def menu_utama():
    while True:
        print("MENU UTAMA")
        print("==============================================")
        print(" [1] Peminjaman Kendaraan")
        print(" [2] Pengembalian Kendaraan")
        print(" [3] Ketersediaan Kendaraan")
        print(" [4] Riwayat Transaksi")
        print(" [5] Daftar Kendaraan")
        print(" [6] Cari Kendaraan")
        print(" [0] Keluar")
        print("=============================================")

        pilih = input("Pilih Menu (Nomor): ")

        if (pilih == "1"):
            proses_peminjaman()
        elif (pilih == "2"):
            proses_pengembalian()
        elif (pilih == "3"):
            print("Ketersediaan Kendaraan")
            print(" [1] Semua Kendaraan")
            print(" [2] Mobil")
            print(" [3] Motor")
            pilih_ketersediaan = int(input("Pilih (1, 2, 3): "))
            # akan dibuat setelah di ajarkan searching & sorting
            if (pilih_ketersediaan == 1):
                ketersediaan()
            elif (pilih_ketersediaan == 2):
                tampilkan_mobil()
            elif (pilih_ketersediaan == 3):
                tampilkan_motor()
        elif (pilih == "4"):
            tampilkan_riwayat() 
        elif (pilih == "5"):
            tampilkan_kendaraan_terurut()
        elif (pilih == "6"):
            fitur_cari_kendaraan()
        elif (pilih == "0"):
            bersihkan_layar()
            print("\n  Terima kasih telah menggunakan Sistem Rental Kendaraan.")
            print("  Sampai jumpa!\n")
        else:
            print(" [!] Pilihan tidak valid.")
def main():
    menu_utama()

if __name__=='__main__':
    main()
