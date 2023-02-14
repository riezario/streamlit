import streamlit as st
import pandas as pd
import numpy as np

st.title("Kebutuhan Bahan Baku")

# Inisialisasi session state
if "products" not in st.session_state:
    st.session_state.products = pd.DataFrame({"Nama Produk": [], "Jumlah Produksi": []})

with st.sidebar:
    st.header("Marketing Plan")
    product_name = st.text_input("Nama Produk")
    production_qty = st.number_input("Jumlah Produksi", min_value=0, step=1)
    if st.button("Tambahkan"):
        new_product = pd.DataFrame({"Nama Produk": [product_name], "Jumlah Produksi": [production_qty]})
        st.session_state.products = pd.concat([st.session_state.products, new_product], ignore_index=True)

st.write("Daftar Produk")
st.write(st.session_state.products)
