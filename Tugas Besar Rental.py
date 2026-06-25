# Fitur:
#   1. Peminjaman & pengembalian kendaraan
#   2. Daftar jenis kendaraan (Mobil, Motor)
#   3. Laporan ketersediaan kendaraan real-time
#   4. Simulasi booking & perhitungan biaya + diskon member
#   5. Sistem pengembalian via ID transaksi

kendaraan = [
    [1, "Totoya Calya", "Mobil", 120000, 0, ""],
    [2, "Hondoz XMAX 250", "Motor", 250000, 0, ""],
    [3, "Hondoz PCX 150", "Motor", 85000, 0, ""],
    [4, "Totoya 2020", "Mobil", 250000, 0, ""],
    [5, "Rolls Royce Spectre Series", "Mobil", 22135000, 0, ""],
    [6, "Innova Reborn", "Mobil", 450000, 0, ""],
    [7, "Ferrari SF90","Mobil",4895000,0, ""],
    [8, "Pagani Huayra","Mobil", 4000000,0, ""],
    [9, "Harley Davidson FAT BOY","Motor",2799000,0, ""]
]

def peminjaman():
    print()
    print("=== PEMINJAMAN KENDARAAN ===")
    nama = input("Silahkan masukan nama anda : ")
    print("Pilih Jenis Kendaraan")
    print("1. Mobil")
    print("2. Motor")

    pilih_jenis = int(input("Pilih (1/2) : "))
    if (pilih_jenis == 1):
        jenis = "Mobil"
    else:
        jenis = "Motor"
    cek_ketersediaan(pilih_jenis)
    tersedia = False
    i = 0
    N = 9
    while i < N:
        if (kendaraan[i][2] == jenis) and (kendaraan[i][4] == 0):
            tersedia = True
        i = i + 1

    if (tersedia == False):
        print("Tidak ada", jenis, "yang tersedia saat ini")
        return 
    input_kendaraan = input("Masukkan ID kendaraan : ")

    indeks_kendaraan = cari(9, input_kendaraan, "id")

    if (indeks_kendaraan == -1):
        print("ID kendaraan tidak ditemukan")
        return
    elif (kendaraan[indeks_kendaraan][4] == 1):
        print("Kendaraan sedang tidak tersedia (sudah disewa)")
        return
    elif (kendaraan[indeks_kendaraan][2] != jenis):
        print("Kendaraan", input_kendaraan, "bukan jenis", jenis)
        return
    
    jumlah_hari = int(input("Jumlah hari sewa (1-30): "))
    if jumlah_hari > 0 and jumlah_hari <= 30:
        harga_sewa = kendaraan[indeks_kendaraan][3]
        total_biaya = harga_sewa * jumlah_hari
        kendaraan[indeks_kendaraan][4] = 1
        kendaraan[indeks_kendaraan][5] = nama
        print("")
        print("=== STRUK PEMINJAMAN ===")
        print("Nama        :",nama)
        print("Kendaraan   :", kendaraan[indeks_kendaraan][1])
        print("Jenis       :", kendaraan[indeks_kendaraan][2])
        print("Harga Sewa  : Rp", kendaraan[indeks_kendaraan][3])
        print("Lama sewa   :", jumlah_hari, "hari")
        print("Total Bayar : Rp", total_biaya)
        print("Terima kasih sudah menyewa!")
    else:
        print("Kelebihan hari! Mohon Maaf")
        return
    
def pengembalian():
    print("=== PENGEMBALIAN KENDARAAN ===")
    X = int(input("Masukkan ID Transaksi (ID Kendaraan) yang dikembalikan: "))
    
    N = 9 
    i = 0
    while i < N and kendaraan[i][0] != X:
        i = i + 1
    if i < N:
        ix = i
    else: 
        ix = -1
        
    if ix == -1:
        print("ID Transaksi tidak ditemukan atau salah!")
    else:
        if kendaraan[ix][4] == 0:
            print("Kendaraan ini tersedia (tidak sedang disewa).")
        else:
            nama_peminjam = kendaraan[ix][5]
            kendaraan[ix][4] = 0
            kendaraan[ix][5] = ""
            print(f"Terima kasih {nama_peminjam}! Kendaraan {kendaraan[ix][1]} berhasil dikembalikan.")
def cari(N,X,cari_kendaraan):
    global kendaraan
    if cari_kendaraan == "id":
        i = 0
        while i<N-1 and X not in kendaraan[i][0]:
            i = i + 1
        if X in kendaraan[i][0]:
            ix = i
        else:
            ix = -1
        return ix
    elif cari_kendaraan == "nama":
        i = 0
        while i<N-1 and X not in kendaraan[i][1]:
            i = i + 1
        if X in kendaraan[i][1]:
            ix = i
        else:
            ix = -1
        return ix

def cek_ketersediaan(pilihan):
    print("=== DAFTAR KENDARAAN ===")
    if pilihan == 1:
        i = 0
        N = 9
        while i < N:
            if kendaraan[i][2] == "Mobil":
                if kendaraan[i][4] == 0 or kendaraan[i][4] == "Ya":
                    status = "Tersedia"
                else:
                    status = "Sedang disewa"
                print("ID :", kendaraan[i][0])
                print("Nama :", kendaraan[i][1])
                print("Status :", status)
                print("===============================")
            i = i + 1
    elif pilihan == 2:
        i = 0
        N = 9
        while i < N:
            if kendaraan[i][2] == "Motor":
                if kendaraan[i][4] == 0 or kendaraan[i][4] == "Ya":
                    status = "Tersedia"
                else:
                    status = "Sedang disewa"
                print("ID :", kendaraan[i][0])
                print("Nama :", kendaraan[i][1])
                print("Status :", status)
                print("===============================")
            i = i + 1

def main():
    berjalan = True
    while berjalan == True:
        print()
        print("=== MENU UTAMA ===")
        print("1. Sewa kendaraan")
        print("2. Kembalikan kendaraan")
        print("3. Cek ketersediaan kendaraan")
        print("4. Cari Kendaraan")
        print("5. Keluar")
        pilih_menu = int(input("pilih menu : "))
        if pilih_menu == 1:
            peminjaman()
        elif pilih_menu == 2:
            pengembalian()
        elif pilih_menu == 3:
            print("Pilih Jenis Kendaraan")
            print("1. Mobil")
            print("2. Motor")
            pilihan = int(input("Pilihan : "))
            cek_ketersediaan(pilihan)
        elif pilih_menu == 4:
            print("Cari Berdasarkan")
            print("1. ID")
            print("2. Nama")
            pilihan = int(input("Pilihan : "))
            
            if pilihan == 1:
                x = input("Masukkan ID Kendaraan : ")
                IN = cari(9,x,"id")
            elif pilihan == 2:
                x = input("Masukkan Nama Kendaraan : ")
                IN = cari(9,x,"nama")
            if IN >= 0:
                print("Kendaraan Ditemukan :")
                print("ID :", kendaraan[IN][0])
                print("Nama :", kendaraan[IN][1])
                print("Jenis :", kendaraan[IN][2])
                print("Harga Sewa :", kendaraan[IN][3])
                if kendaraan[IN][4] == 0:
                    status = "Tersedia"
                else:
                    status = "Sedang Disewa"
                print("Status :", status)
            else:
                print("Kendaraan Tidak Ditemukan")
            
        elif pilih_menu == 5:
            print("Program selesai. Terima kasih")
            berjalan = False
        else:
            print("Pilihan menu tidak valid!")
            
if __name__ == '__main__':
    main()
