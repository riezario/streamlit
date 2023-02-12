# memasukkan pustaka prettytable
from prettytable import PrettyTable

# meminta pengguna untuk memasukkan jumlah produk yang akan diproduksi
jumlah_produk = int(input("Masukkan jumlah produk yang akan diproduksi: "))

# meminta pengguna untuk memasukkan jumlah bahan baku per produk
jumlah_bahan_baku = int(input("Berapa banyak bahan baku yang digunakan per produk? "))

# membuat list untuk menyimpan informasi bahan baku
bahan_baku = []

# meminta pengguna untuk memasukkan informasi bahan baku
for i in range(jumlah_bahan_baku):
    nama_bahan_baku = input("Masukkan nama bahan baku: ")
    jumlah_bahan_baku_per_produk = int(input("Masukkan jumlah bahan baku per produk: "))
    harga_bahan_baku = int(input("Masukkan harga bahan baku per satuan: "))
    bahan_baku.append((nama_bahan_baku, jumlah_bahan_baku_per_produk, harga_bahan_baku))

# membuat tabel
tabel = PrettyTable()
tabel.field_names = ["Nama Bahan Baku", "Jumlah Bahan Baku", "Harga Bahan Baku", "Biaya Bahan Baku"]

# menghitung kebutuhan bahan baku dan biaya total
total_biaya = 0
for bahan in bahan_baku:
    nama_bahan_baku, jumlah_bahan_baku_per_produk, harga_bahan_baku = bahan
    kebutuhan_bahan_baku = jumlah_produk * jumlah_bahan_baku_per_produk
    biaya = kebutuhan_bahan_baku * harga_bahan_baku
    total_biaya += biaya
    tabel.add_row([nama_bahan_baku, kebutuhan_bahan_baku, harga_bahan_baku, biaya])

# menambahkan baris total biaya
tabel.add_row(["Total", "", "", total_biaya])

# menampilkan tabel
print(tabel)
