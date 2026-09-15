# Studi_Kasus_4_Irfan

Nama : Muhammad Irfan Nazir
Kelas : B
NIM : 2609116070
Soal : Genap

>> Penjelasan

1. Struktur data

data_produk adalah nested dictionary: key luar = ID produk ("1", "2"), value = dictionary detail produk (nama, harga, stok).
Sudah diisi 2 produk contoh dari awal, jadi program langsung punya data waktu dijalankan.

2. Fungsi bantu validasi

input_angka() → memastikan input berupa angka positif (pakai .isdigit()), kalau salah diminta input ulang terus (loop while True).
input_teks() → memastikan input tidak kosong.
input_id_baru() → cek ID belum dipakai sebelum produk baru ditambahkan (mencegah ID dobel).
input_id_cari() → cek ID benar-benar ada di data sebelum dipakai untuk ubah/hapus.

3. Fungsi CRUD

tambah_data() → minta ID, nama, harga, stok lewat fungsi validasi di atas, lalu simpan sebagai dictionary baru ke data_produk.
tampilkan_data() → cek dulu apakah data kosong, kalau ada isinya di-loop pakai for dan ditampilkan rapi pakai format {:<lebar}.
ubah_data() → tampilkan data lama, lalu tiap field bisa dikosongkan (skip) atau diisi baru; ada pengecekan format khusus untuk harga & stok supaya tidak error kalau salah input.
hapus_data() → minta konfirmasi y/n dulu sebelum data benar-benar dihapus pakai del.

4. Menu utama

tampilkan_menu() cuma nampilin daftar pilihan.
while True di bagian bawah adalah loop utama: terus muter sampai user pilih 5 (break).

>> Hasil Code / Output

1. Menampilkan serta menambahkan data produk
<img width="866" height="752" alt="Screenshot 2026-09-15 202325" src="https://github.com/user-attachments/assets/9f885810-604c-41bf-ba80-6fe580eb916a" />

2. Mengubah serta menambahkan kategori pada produk
<img width="696" height="633" alt="Screenshot 2026-09-15 202430" src="https://github.com/user-attachments/assets/55aabb6f-927f-41ad-87d6-e2cf2213efd2" />

3. Menghapus data produk
<img width="530" height="533" alt="Screenshot 2026-09-15 202501" src="https://github.com/user-attachments/assets/a870daab-9817-4be6-9f27-9410a317fe65" />


