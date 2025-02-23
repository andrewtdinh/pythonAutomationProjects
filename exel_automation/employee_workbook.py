import openpyxl

wb = openpyxl.load_workbook('Employees.xlsx')

names = ['Avery Prada', 'Junn Patel', 'Andrew Dang', 'Jen Belosi']

for name in names:
    wb.create_sheet(name)

wb.save('Employees.xlsx')