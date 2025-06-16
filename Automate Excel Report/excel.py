import pandas as pd
df = pd.read_excel('supermarket_sales.xlsx')

df = df[['Gender', 'Product line', 'Total']]
# print(product_head)
pivot_table = df.pivot_table(index="Gender", columns="Product line", values="Total", aggfunc="sum").round(0)

pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)
print(pivot_table)

