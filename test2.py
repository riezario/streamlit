import streamlit as st
import pandas as pd
import base64
from io import BytesIO
import weasyprint

st.title("Kebutuhan Bahan Baku")

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

if st.button("Hitung Jumlah Produk"):
    product_sum = st.session_state.products.groupby(['Produk']).sum().reset_index()
    st.write(product_sum)
    pdf = product_sum.to_html().encode("UTF-8")
    io = BytesIO()
    weasyprint.HTML(string=pdf).write_pdf(io)
    b64 = base64.b64encode(io.getvalue()).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="laporan.pdf">Download PDF</a>'
    st.markdown(href, unsafe_allow_html=True)
