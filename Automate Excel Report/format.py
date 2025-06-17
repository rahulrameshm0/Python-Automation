from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook('pivot_table.xlsx')
sheet = wb["Report"]

sheet["A1"] = 'Sales Report'
sheet["A2"] = 'June'
sheet["A1"].font = Font('Arial',bold=True, size=20)
sheet["A2"].font = Font('Arial',bold=True, size=20)

wb.save('format.xlsx')