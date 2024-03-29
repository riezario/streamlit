import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

st.title("Kebutuhan RAW MATERIAL")

# Inisialisasi session state
if "products" not in st.session_state:
    st.session_state.products = pd.DataFrame({"Customer": [" "], "Produk": [" "], "Count": [" "], "Jenis": [" "], "Quantity": [1], "Harga": [1], "Total Amount": [1], "key": [0]})

with st.sidebar:
    st.header("Marketing Plan")
    customer_name = st.text_input("Nama Customer")
    product_name = st.text_input("Nama Produk")
    count = st.text_input("Count")
    jenis = st.selectbox("Jenis", options=["A", "B", "C"])
    quantity = st.number_input("Quantity", min_value=1, step=1)
    harga = st.number_input("Harga", min_value=0.0, step=0.01)
    if st.button("Tambahkan"):
        total_amount = quantity * harga
        new_product = pd.DataFrame({"Customer": [customer_name], "Produk": [product_name], "Count": [count], "Jenis": [jenis], "Quantity": [quantity], "Harga": [harga], "Total Amount": [total_amount]})
        st.session_state.products = pd.concat([st.session_state.products, new_product], ignore_index=True)

st.write("Daftar Produk")
st.write(st.session_state.products[1:].reset_index(drop=True))
total_amount = st.session_state.products["Total Amount"].sum()
st.write(f"Total Amount: {total_amount:.2f}") 

if st.button("Hitung Jumlah Produk"):
    if st.session_state.products.empty:
        st.warning("Belum ada produk yang ditambahkan.")
        st.stop()
    product_sum = st.session_state.products.groupby(['Produk']).sum().reset_index()
    table_html = product_sum.to_html()
    st.components.v1.html(table_html, height=500, scrolling=True)

