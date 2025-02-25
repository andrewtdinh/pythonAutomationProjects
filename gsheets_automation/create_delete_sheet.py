import gspread

g_client = gspread.service_account('service_account_creds.json')

spread_sheet = g_client.open('gspread_101')

spread_sheet.add_worksheet(title="new_ws", rows=100, cols=100)

ws = spread_sheet.worksheet('2nd sheet')

spread_sheet.del_worksheet(ws)