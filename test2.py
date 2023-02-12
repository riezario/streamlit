import streamlit as st
import pandas as pd

@st.cache
def load_data(file):
    data = pd.read_csv(file)
    return data

def main():
    st.title("Rencana Produksi")

    # Load data from CSV file
    products = load_data("products.csv")

    # Create a selectbox for the products
    selected_products = st.multiselect("Pilih produk:", products["Nama Produk"].unique())

    # Filter the products dataframe for the selected products
    selected_products_df = products[products["Nama Produk"].isin(selected_products)]

    # Create an input field for the production plan
    production_plan = {}
    for product in selected_products:
        production_plan[product] = st.number_input(f"Jumlah produk {product}:", value=0)

    # Calculate the raw material needs
    raw_material_needs = {}
    for product, quantity in production_plan.items():
        raw_materials = selected_products_df[selected_products_df["Nama Produk"] == product]["Bahan Baku"].tolist()
        for raw_material in raw_materials:
            if raw_material in raw_material_needs:
                raw_material_needs[raw_material] += quantity
            else:
                raw_material_needs[raw_material] = quantity

    # Calculate the costs
    costs = {}
    for product, quantity in production_plan.items():
        price = selected_products_df[selected_products_df["Nama Produk"] == product]["Harga per Unit"].iloc[0]
        costs[product] = price * quantity

    # Show the results in a table
    st.write("Rencana produksi:")
    st.write(production_plan)
    st.write("Bahan baku yang dibutuhkan:")
    st.write(raw_material_needs)
    st.write("Biaya bahan baku:")
    st.write(costs)

if __name__ == "__main__":
    main()
