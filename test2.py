# memasukkan pustaka streamlit
import streamlit as st

# meminta pengguna untuk memasukkan jumlah produk yang akan diproduksi
jumlah_produk = st.number_input("Masukkan jumlah produk yang akan diproduksi: ")

# meminta pengguna untuk memasukkan jumlah bahan baku per produk
jumlah_bahan_baku = st.number_input("Berapa banyak bahan baku yang digunakan per produk? ")

# membuat list untuk menyimpan informasi bahan baku
bahan_baku = []

# meminta pengguna untuk memasukkan informasi bahan baku
for i in range(bahan_baku):
    nama_bahan_baku = st.text_input(f"Masukkan nama bahan baku {i+1}: ")
    jumlah_bahan_baku_per_produk = st.number_input(f"Masukkan jumlah bahan baku per produk: ")
    harga_bahan_baku = st.number_input(f"Masukkan harga bahan baku per satuan: ")
    bahan_baku.append((nama_bahan_baku, jumlah_bahan_baku_per_produk, harga_bahan_baku))

# menghitung kebutuhan bahan baku dan biaya total
total_biaya = 0
for bahan in bahan_baku:
    nama_bahan_baku, jumlah_bahan_baku_per_produk, harga_bahan_baku = bahan
    kebutuhan_bahan_baku = jumlah_produk * jumlah_bahan_baku_per_produk
    biaya = kebutuhan_bahan_baku * harga_bahan_baku
    total_biaya += biaya

# menampilkan hasil
st.write("Kebutuhan Bahan Baku:")
for bahan in bahan_baku:
    nama_bahan_baku, jumlah_bahan_baku_per_produk, harga_bahan_baku = bahan
    st.write(f"- {nama_bahan_baku}: {jumlah_produk * jumlah_bahan_baku_per_produk}")
st.write(f"Total Biaya: {total_biaya}")
