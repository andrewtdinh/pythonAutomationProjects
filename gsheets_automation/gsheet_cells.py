import gspread

g_client = gspread.service_account('service_account_creds.json')

spread_sheet = g_client.open('gspread_101')

ws = spread_sheet.worksheet('Sheet1')

c = ws.acell('A2')

c_val = c.value

print(f"c val: {c_val}")