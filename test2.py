# memasukkan pustaka streamlit
import streamlit as st

# membuat list untuk menyimpan informasi produk
produk = ["Produk A", "Produk B", "Produk C", "Produk D"]

# membuat list untuk menyimpan informasi bahan baku
bahan_baku = ["Bahan A", "Bahan B", "Bahan C", "Bahan D"]

# meminta pengguna untuk memilih produk yang akan diproduksi
pilihan_produk = st.selectbox("Pilih produk yang akan diproduksi:", produk)

# meminta pengguna untuk memasukkan jumlah produk yang akan diproduksi
jumlah_produk = int(st.number_input("Masukkan jumlah produk yang akan diproduksi: "))

# meminta pengguna untuk memilih bahan baku yang akan digunakan
pilihan_bahan_baku = st.multiselect("Pilih bahan baku yang akan digunakan:", bahan_baku)

# membuat list untuk menyimpan informasi bahan baku yang akan digunakan
bahan_baku_digunakan = []

# meminta pengguna untuk memasukkan informasi bahan baku
for bahan in pilihan_bahan_baku:
    jumlah_bahan_baku_per_produk = float(st.number_input(f"Berapa banyak bahan {bahan} yang digunakan per produk? "))
    harga_bahan_baku = float(st.number_input(f"Berapa harga bahan {bahan} per satuan? "))
    bahan_baku_digunakan.append((bahan, jumlah_bahan_baku_per_produk, harga_bahan_baku))

# menghitung kebutuhan bahan baku dan biaya total
total_biaya = 0
for bahan in bahan_baku_digunakan:
    nama_bahan_baku, jumlah_bahan_baku_per_produk, harga_bahan_baku = bahan
    kebutuhan_bahan_baku = jumlah_produk * jumlah_bahan_baku_per_produk
    biaya = kebutuhan_bahan_baku * harga_bahan_baku
    total_biaya += biaya

# menampilkan hasil
st.write("Informasi Produk:")
st.write(f"- Nama Produk: {pilihan_produk}")
st.write(f"- Jumlah Produk: {jumlah_produk}")
st.write("Kebutuhan Bahan Baku:")
