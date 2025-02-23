import openpyxl

wb = openpyxl.load_workbook('Automating Worksheets.xlsx')

wb.create_sheet('4th Sheet')

del wb['Third Sheet']

wb.save('Automating Worksheets.xlsx')