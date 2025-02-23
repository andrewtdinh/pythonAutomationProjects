import openpyxl

wb = openpyxl.load_workbook('Automating Worksheets.xlsx')

active_ws = wb.active

print(f"\nActive worksheet: {active_ws.title}")

# ws = wb['Sheet3']
