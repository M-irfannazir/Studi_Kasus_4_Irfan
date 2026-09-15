# Program Pengelolaan Data Produk Toko Serba Ada

# Variabel (tempat penyimpanan utama)
data_produk = {
    "1": {"nama": "Buku Tulis", "harga": 5000, "stok": 100},
    "2": {"nama": "Pensil", "harga": 2000, "stok": 50}
}


# Fungsi bantu (Validasi input)

def input_angka(teks):
    while True:
        nilai = input(teks)
        if nilai.isdigit() and int(nilai) > 0:
            return int(nilai)
        else:
            print("Input tidak valid! Harap masukkan angka lebih dari 0.\n")


def input_teks(teks, nama_field):
    while True:
        nilai = input(teks).strip()
        if nilai != "":
            return nilai
        else:
            print(f"{nama_field} tidak boleh kosong! Coba lagi.\n")


def input_id_baru(teks):
    while True:
        id_produk = input(teks).strip()
        if id_produk == "":
            print("ID produk tidak boleh kosong! Coba lagi.\n")
        elif id_produk in data_produk:
            print("ID produk sudah dipakai! Gunakan ID lain.\n")
        else:
            return id_produk


def input_id_cari(teks):
    while True:
        id_produk = input(teks).strip()
        if id_produk in data_produk:
            return id_produk
        else:
            print("ID produk tidak ditemukan! Coba lagi.\n")


# Fungsi CRUD

def tambah_data():
    print("\n=== TAMBAH PRODUK BARU ===")
    id_baru = input_id_baru("Masukkan ID produk: ")
    nama = input_teks("Masukkan nama produk: ", "Nama produk")
    harga = input_angka("Masukkan harga produk: ")
    stok = input_angka("Masukkan stok produk: ")

    data_produk[id_baru] = {"nama": nama, "harga": harga, "stok": stok}

    print(f"\nBerhasil menambahkan produk: {data_produk[id_baru]}")
    print("DATA PRODUK SETELAH DITAMBAHKAN")
    tampilkan_data()


def tampilkan_data():
    print("\n=== DAFTAR DATA PRODUK ===")

    # Conditional statement: cek apakah dictionary masih kosong
    if len(data_produk) == 0:
        print("Belum ada data produk.")
    else:
        print(f"{'ID':<8}{'Nama':<20}{'Harga':<12}{'Stok':<8}{'Kategori'}")
        print("-" * 60)
        # Looping (for) untuk menampilkan setiap produk satu per satu
        for id_produk, detail in data_produk.items():
            kategori = detail.get("kategori", "-")
            print(f"{id_produk:<8}{detail['nama']:<20}{detail['harga']:<12}{detail['stok']:<8}{kategori}")


def ubah_data():
    print("\n=== UBAH DATA PRODUK ===")

    if len(data_produk) == 0:
        print("Belum ada produk yang bisa diubah.")
        return

    tampilkan_data()
    id_cari = input_id_cari("\nMasukkan ID produk yang ingin diubah: ")
    produk = data_produk[id_cari]
    print(f"Data lama: {produk}")
    print("(Kosongkan input lalu tekan 'ENTER' jika tidak ingin mengubah field tersebut)")

    nama_baru = input(f"Nama baru [{produk['nama']}]: ").strip()
    harga_baru = input(f"Harga baru [{produk['harga']}]: ").strip()
    stok_baru = input(f"Stok baru [{produk['stok']}]: ").strip()
    kategori_baru = input(f"Kategori baru [{produk.get('kategori', '-')}]: ").strip()

    # Conditional statement untuk masing-masing field, tidak crash walau input salah
    if nama_baru != "":
        produk["nama"] = nama_baru

    if harga_baru != "":
        if harga_baru.isdigit() and int(harga_baru) > 0:
            produk["harga"] = int(harga_baru)
        else:
            print("Harga tidak valid, harga lama tetap dipakai.")

    if stok_baru != "":
        if stok_baru.isdigit() and int(stok_baru) > 0:
            produk["stok"] = int(stok_baru)
        else:
            print("Stok tidak valid, stok lama tetap dipakai.")

    if kategori_baru != "":
        produk["kategori"] = kategori_baru

    print(f"\nData berhasil diubah menjadi: {produk}")
    tampilkan_data()
    




def hapus_data():
    print("\n=== HAPUS DATA PRODUK ===")

    if len(data_produk) == 0:
        print("Belum ada data yang bisa dihapus.")
        return

    tampilkan_data()
    id_cari = input_id_cari("\nMasukkan ID produk yang ingin dihapus: ")
    data_terhapus = data_produk[id_cari]

    # Konfirmasi sebelum menghapus, dengan validasi looping (y/n)
    while True:
        konfirmasi = input(f"Yakin ingin menghapus {data_terhapus}? (y/n): ").strip().lower()
        if konfirmasi in ["y", "n"]:
            break
        else:
            print("Masukkan 'y' untuk ya atau 'n' untuk tidak.")

    if konfirmasi == "y":
        del data_produk[id_cari]
        print("Produk berhasil dihapus.")
        tampilkan_data()
    else:
        print("Penghapusan dibatalkan.")


# MENU UTAMA (Looping while sampai user pilih KELUAR)

def tampilkan_menu():
    print("\n========================================")
    print("   SISTEM PENGELOLAAN DATA PRODUK")
    print("=" * 40)
    print("1. Tambah Produk Baru")
    print("2. Lihat Semua Produk")
    print("3. Ubah Data & Tambah Kategori Produk")
    print("4. Hapus Produk")
    print("5. Keluar")
    print("=" * 40)


print("Selamat Datang di toko Serba Ada")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ").strip()

    # Conditional statement untuk validasi & pengecekan menu
    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan sistem ini!")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih angka 1-5.")