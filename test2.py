import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Input produk dan bahan baku
products = ['Product 1', 'Product 2', 'Product 3']
raw_materials = ['Raw Material 1', 'Raw Material 2', 'Raw Material 3', 'Raw Material 4']

# Input jumlah produksi produk
production_plan = [100, 200, 300]

# Input harga bahan baku
raw_material_prices = [10, 20, 30, 40]

# Input jumlah bahan baku per produk
raw_material_usage = [[10, 20, 30, 40], [20, 30, 40, 50], [30, 40, 50, 60]]

# Perhitungan biaya kebutuhan bahan baku
costs = []
for usage in raw_material_usage:
    cost = 0
    for i in range(len(usage)):
        cost += usage[i] * raw_material_prices[i]
    costs.append(cost)

# Buat data frame dari input
data = {'Product': products, 'Production Plan': production_plan, 'Cost': costs}
df = pd.DataFrame(data)

# Tampilkan laporan
pdf_pages = PdfPages('Production Report.pdf')
plt.figure(figsize=[15, 5])
plt.bar(df['Product'], df['Cost'])
plt.xlabel('Product')
plt.ylabel('Cost')
plt.title('Production Report')
pdf_pages.savefig()
pdf_pages.close()
