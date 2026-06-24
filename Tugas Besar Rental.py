data_kendaraan = [
    ["Yamaha NMAX", 100000, "Tersedia"],
    ["Honda Beat", 50000, "Tersedia"],
    ["Toyota Avanza", 350000, "Disewa"],
    ["Honda Brio", 300000, "Tersedia"]
]
def insertionsort(N):
    global data_kendaraan
    for x in range(1, N):
        tem = data_kendaraan[x]
        i = x - 1
        while i >= 0 and tem[0] < data_kendaraan[i][0]:
            data_kendaraan[i+1] = data_kendaraan[i]
            i -= 1
        data_kendaraan[i+1] = tem
    return 
def lihat_kendaraan():
    print("--- DAFTAR KENDARAAN ---")
    N = 0
    for data in data_kendaraan:
        N = N + 1
    insertionsort(N)
    for i in range(N):
        nomor = i + 1
        nama = data_kendaraan[i][0]
        harga = data_kendaraan[i][1]
        status = data_kendaraan[i][2]
        
        print(nomor, ".", nama, "- Rp", harga, "-", status)
        
    print("------------------------")
    print()
# def peminjaman_kendaraan():
def penambahan_kendaraan():
    global data_kendaraan
    print("--- Menambahkan Kendaraan ---")
    nama_kendaraan = input("Masukkan Nama Kendaraan: ")
    harga = int(input("Masukkan Harga Sewa: "))
    status = "Tersedia"
    data_kendaraan += [[nama_kendaraan, harga, status]]
    print("Kendaraan berhasil ditambahkan!")
    print()
    lihat_kendaraan()
def jalankan_rental():
    berjalan = True
    while berjalan == True:
        print("=== Selamat Datang di Rental Kendaraan Mantap ===")
        print("1. Lihat Kendaraan & Statusnya")
        print("2. Peminjaman Kendaraan")
        print("3. Pengembalian Kendaraan")
        print("4. Menambahkan kendaraan")
        print("5. Keluar")
        pilihan = input("Masukkan Pilihan Anda: ")
        if pilihan == "1":
            lihat_kendaraan()
        elif pilihan == "2":
            peminjaman_kendaraan()
        elif pilihan == "3":
            pengembalian_kendaraan()
        elif pilihan == "4":
            penambahan_kendaraan()
        elif pilihan == "5":
            print("Terima Kasih Sudah Menggunakan Jasa Kami")
            berjalan = False
if __name__ == "__main__":
    jalankan_rental()
