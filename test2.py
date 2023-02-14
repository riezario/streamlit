import streamlit as st
import pandas as pd

st.title("Kebutuhan Bahan Baku")

# Inisialisasi session state
if "products" not in st.session_state:
    st.session_state.products = pd.DataFrame({"Customer": [], "Produk": [], "Count": [], "Jenis": [], "Quantity": [], "Harga": []})

with st.sidebar:
    st.header("Marketing Plan")
    customer_name = st.text_input("Nama Customer")
    product_name = st.text_input("Nama Produk")
    count = st.number_input("Count", min_value=0, step=1)
    jenis = st.selectbox("Jenis", options=["A", "B", "C"])
    quantity = st.number_input("Quantity", min_value=0, step=1)
    harga = st.number_input("Harga", min_value=0.0, step=0.01)
    if st.button("Tambahkan"):
        new_product = pd.DataFrame({"Customer": [customer_name], "Produk": [product_name], "Count": [count], "Jenis": [jenis], "Quantity": [quantity], "Harga": [harga]})
        st.session_state.products = pd.concat([st.session_state.products, new_product], ignore_index=True)

st.write("Daftar Produk")
st.write(st.session_state.products)
