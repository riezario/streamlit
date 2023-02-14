import streamlit as st
import pandas as pd
import numpy as np

st.title("Kebutuhan Bahan Baku")

with st.sidebar:
    st.header("Marketing Plan")
    product_name = st.text_input("Nama Produk")
    production_qty = st.number_input("Jumlah Produksi", min_value=0, step=1)

data = {"Nama Produk": ["Produk A", "Produk B", "Produk C"],
        "Jumlah Produksi": [100, 200, 300]}
df = pd.DataFrame(data)

st.write("Daftar Produk")
st.write(df)
