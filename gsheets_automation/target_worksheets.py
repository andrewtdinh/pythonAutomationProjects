import gspread

g_client = gspread.service_account('service_account_creds.json')

spread_sheet = g_client.open('gspread_101')

active_ws = spread_sheet.sheet1

print(f'Active worksheet: {active_ws.title}')

ws = spread_sheet.worksheet('Sheet2')
ws.update_title('2nd sheet')

