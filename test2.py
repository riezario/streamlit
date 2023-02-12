import streamlit as st

st.title("Aplikasi Sederhana Streamlit")

nama = st.text_input("Masukkan nama Anda:", "")

if st.button("Submit"):
    result = f"Hello, {nama}!"
    st.success(result)
