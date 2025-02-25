import gspread

g_client = gspread.service_account('service_account_creds.json')

spread_sheet = g_client.open_by_key('18BdSkWlJkP1akC2WYO4X-6Xi8WKdPT2lwEFRLQnp1-w')

products = ['Binge Cherries', 'Rockit Apples', 'Main Blueberries']

for product in products:
    spread_sheet.add_worksheet(title=product, rows=100, cols=100)

spread_sheet.worksheets()