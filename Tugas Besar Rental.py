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
    [8, "Pagani Huayra", 4000000,0],
    [9, "Harley Davidson FAT BOY","Motor",3024244]
]
def peminjaman(jenis_kendaraan):
    print("Peminjaman Kendaraan")

    print("Pilih Jenis Kendaraan")
    print("1. Mobil")
    print("2. Motor")

    pilih_jenis = int(input("Pilih (1/2) : "))
    if (pilih_jenis == 1):
        jenis = "Mobil"
    else:
        jenis = "Motor"
    
    cek_ketersediaan(jenis)

    

    
def pengembalian(jenis_kendaraan,N):
    global kendaraan
    i = 0
    while i < N and kendaraan[i][0] != X:
        i = i + 1
        if kendaraan[i][0] == X:
            ix = i
        else:
            ix = -1
    return ix
def cek_ketersediaan():
    
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
        jenis_kendaraan = input("masukan jenis kendaraan : ") 
            
        if pilih_menu == 1:
            peminjaman(jenis_kendaraan)
        elif pilih_menu == 2:
            pengembalian(jenis_kendaraan)
        elif pilih_menu == 3:
            cek_ketersediaan()
        elif pilih_menu == 4:
            berjalan = False
            
if __name__ == '__main__':
    main()
