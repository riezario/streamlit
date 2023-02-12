import streamlit as st
import pandas as pd

def calculate_raw_material_requirement(marketing_plan, raw_materials):
    raw_material_requirement = {}
    for product, quantity in marketing_plan.items():
        for raw_material, usage in raw_materials[product].items():
            if raw_material not in raw_material_requirement:
                raw_material_requirement[raw_material] = 0
            raw_material_requirement[raw_material] += usage * quantity
    return raw_material_requirement

def main():
    st.title("Raw Material Calculator")
    
    marketing_plan = {
        "Product A": 100,
        "Product B": 200,
        "Product C": 300
    }
    
    raw_materials = {
        "Product A": {"Raw Material X": 1, "Raw Material Y": 2},
        "Product B": {"Raw Material X": 2, "Raw Material Y": 1, "Raw Material Z": 3},
        "Product C": {"Raw Material Y": 1, "Raw Material Z": 2}
    }
    
    raw_material_requirement = calculate_raw_material_requirement(marketing_plan, raw_materials)
    
    st.write("Marketing Plan:")
    st.write(pd.DataFrame.from_dict(marketing_plan, orient="index", columns=["Quantity"]))
    
    st.write("Raw Material Requirements:")
    st.write(pd.DataFrame.from_dict(raw_material_requirement, orient="index", columns=["Quantity"]))

if __name__ == "__main__":
    main()
