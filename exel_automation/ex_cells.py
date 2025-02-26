import openpyxl

from delete_sheets import ws_names

wb = openpyxl.load_workbook('my_workbook.xlsx')

ws = wb['Sheet']

c = ws['A1']

c_val = c.value

print(c_val)

rev_content = c_val[::-1]

ws['A2'] = rev_content

wb.save('my_workbook.xlsx')

print(ws['A2'].value)
