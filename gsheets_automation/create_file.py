import gspread

gc = gspread.service_account('service_account_creds.json')

spread_sheet = gc.create('gspread 201')

ws = spread_sheet.sheet1
ws.update([["Andrew", "Dinh", "was here"]], "A1:C3")

spread_sheet.share("andrewdinh74@gmail.com", perm_type="user", role="writer")