import streamlit as st

# Daftar produk yang tersedia
produk_tersedia = {
    "Produk A": {"Bahan Baku 1": 10, "Bahan Baku 2": 5, "Bahan Baku 3": 2, "Harga": 1000},
    "Produk B": {"Bahan Baku 1": 5, "Bahan Baku 2": 8, "Bahan Baku 3": 1, "Harga": 1500},
    "Produk C": {"Bahan Baku 1": 3, "Bahan Baku 2": 6, "Bahan Baku 3": 4, "Harga": 2000},
}

# Meminta pengguna untuk memasukkan nama produk
nama_produk = st.selectbox("Pilih produk yang akan diproduksi:", list(produk_tersedia.keys()))

# Meminta pengguna untuk memasukkan jumlah produk yang akan diproduksi
jumlah_produk = int(st.number_input("Masukkan jumlah produk yang akan diproduksi: "))

# Mengambil informasi produk yang dipilih oleh pengguna
informasi_produk = produk_tersedia[nama_produk]

# Menghitung kebutuhan bahan baku dan biaya total
total_biaya = 0
st.write("Kebutuhan Bahan Baku:")
for bahan_baku, jumlah_bahan_baku in informasi_produk.items():
    if bahan_baku == "Harga":
        continue
    kebutuhan_bahan_baku = jumlah_bahan_baku * jumlah_produk
    biaya = kebutuhan_bahan_baku * informasi_produk["Harga"]
    total_biaya += biaya
    st.write(f"- {bahan_baku}: {kebutuhan_bahan_baku}")

# Menampilkan hasil
st.write(f"Total Biaya: {total_biaya}")
