import openpyxl

wb = openpyxl.load_workbook('my_workbook.xlsx')

ws = wb.active

ws['A1'] = 'Andrew was here'

wb.save('my_workbook.xlsx')