import gspread

g_client = gspread.service_account('service_account_creds.json')

spread_sheet = g_client.open('gspread_101')

ws = spread_sheet.sheet1

ws.update([['Hello Googlesheets!']], 'A2')