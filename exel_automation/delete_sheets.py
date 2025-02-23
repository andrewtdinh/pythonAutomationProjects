import openpyxl
import re

wb = openpyxl.load_workbook('Employees.xlsx')

ws_names = wb.sheetnames

pattern = r'^Sheet\d+$'

for ws_name in ws_names:
    if re.search(pattern, ws_name) is not None:
        del wb[ws_name]

wb.save('Employees.xlsx')