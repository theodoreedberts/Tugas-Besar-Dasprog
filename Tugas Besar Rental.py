# Fitur:
#   1. Peminjaman & pengembalian kendaraan
#   2. Daftar jenis kendaraan (Mobil, Motor)
#   3. Laporan ketersediaan kendaraan real-time
#   4. Simulasi booking & perhitungan biaya + diskon member
#   5. Sistem pengembalian via ID transaksi
kendaraan = [
    [1, "Totoya Calya", "Mobil", 120000, 0],
    [2, "Hondoz XMAX 250", "Motor", 250000, 0],
    [3, "Hondoz PCX 150", "Motor", 85000, 0],
    [4, "Totoya 2020", "Mobil", 250000, 0],
    [5, "Rolls Royce Spectre Series", "Mobil", 22135000, 0],
    [6, "Innova Reborn", "Mobil", 450000, 0],
    [7, "Ferrari SF90","Mobil",4895000,0],
    [8, "Pagani Huayra","Mobil", 4000000,0],
    [9, "Harley Davidson FAT BOY","Motor",3024244,0]
]

def cari_kendaraan_by_id(id_dicari):
    # Ubah input menjadi angka karena ID di list berupa angka
    id_dicari = int(id_dicari)
    
    indeks = 0
    for data in kendaraan:
        if data[0] == id_dicari:
            return indeks
        indeks = indeks + 1
    return -1

def peminjaman(nama):
    print("Peminjaman Kendaraan")

    print("Pilih Jenis Kendaraan")
    print("1. Mobil")
    print("2. Motor")

    pilih_jenis = int(input("Pilih (1/2) : "))
    if (pilih_jenis == 1):
        jenis = "Mobil"
    else:
        jenis = "Motor"
    
    cek_ketersediaan()

    tersedia = False
    for i in range(len(kendaraan)):
        if (kendaraan[i][2] == jenis) and (kendaraan[i][4] == 0):
            tersedia = True

    if (tersedia == False):
        print("Tidak ada", jenis, "yang tersedia saat ini")
        return 

    print(" Masukkan ID kendaraan : ")
    input_kendaraan = input("ID Kendaraan: ")

    indeks_kendaraan = cari_kendaraan_by_id(input_kendaraan)

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
    
    # Hitung total biaya
    harga_sewa = kendaraan[indeks_kendaraan][3]
    total_biaya = harga_sewa * jumlah_hari
    
    # Ubah status kendaraan menjadi 1 (disewa)
    kendaraan[indeks_kendaraan][4] = 1
    
    print("")
    print("=== STRUK PEMINJAMAN ===")
    print("Nama        :",nama)
    print("Kendaraan   :", kendaraan[indeks_kendaraan][1])
    print("Jenis       :", kendaraan[indeks_kendaraan][2])
    print("Harga Sewa  : Rp", kendaraan[indeks_kendaraan][3])
    print("Lama sewa   :", jumlah_hari, "hari")
    print("Total Bayar : Rp", total_biaya)
    print("Terima kasih sudah menyewa!")
    
def sorting(N,X):
    global kendaraan
    i = 0
    while i < N and kendaraan[i][0] != X:
        i = i + 1
        if kendaraan[i][0] == X:
            ix = i
        else:
            ix = -1
    return ix
def pengembalian(nama):
    print("=== PENGEMBALIAN KENDARAAN ===")
    input_id = input("Masukkan ID kendaraan yang ingin dikembalikan : ")
    
    indeks = cari_kendaraan_by_id(input_id)
    
    if indeks == -1:
        print("ID kendaraan tidak ditemukan.")
    else:
        # Cek apakah memang sedang disewa (status 1)
        if kendaraan[indeks][4] == 1:
            # Ubah status kembali ke 0 (Tersedia)
            kendaraan[indeks][4] = 0
            print("Kendaraan", kendaraan[indeks][1], "berhasil dikembalikan.")
            print("Terima kasih!",nama)
        else:
            print("Kendaraan", kendaraan[indeks][1], "tidak sedang disewa (masih ada di rental).")
def cari():
    print("")

def cek_ketersediaan():
    print("")
    print("--- DAFTAR KENDARAAN ---")
    print("Pilih Jenis Kendaraan")
    print("1. Mobil")
    print("2. Motor")
    pilihan = int(input("Pilihan : "))
    if pilihan == 1:
        for mobil in kendaraan:
            if mobil[2] == "Mobil":
                if mobil[4] == 0 or mobil[4] == "Ya":
                    status = "Tersedia"
                else:
                    status = "Sedang disewa"
                print("ID :", mobil[0])
                print("Nama :", mobil[1])
                print("Status :", status)
                print("------------------------------")
    elif pilihan == 2:
        for motor in kendaraan:
            if motor[2] == "Motor":
                if motor[4] == 0 or motor[4] == "Ya":
                    status = "Tersedia"
                else:
                    status = "Sedang disewa"
                print("ID :", motor[0])
                print("Nama :", motor[1])
                print("Status :", status)
                print("------------------------------")

def main():
    berjalan = True
    while berjalan == True:
        print("\n--- MENU UTAMA ---")
        print("1. Sewa kendaraan")
        print("2. Kembalikan kendaraan")
        print("3. Cek ketersediaan kendaraan")
        print("4. Keluar")
        nama = input("Silahkan masukan nama anda : ")
        pilih_menu = int(input("pilih menu : "))
        if pilih_menu == 1:
            peminjaman(nama)
        elif pilih_menu == 2:
            pengembalian(nama)
        elif pilih_menu == 3:
            cek_ketersediaan()
        elif pilih_menu == 4:
            print("Program selesai. Terima kasih")
            berjalan = False
        else:
            print("Pilihan menu tidak valid!")
            
if __name__ == '__main__':
    main()
