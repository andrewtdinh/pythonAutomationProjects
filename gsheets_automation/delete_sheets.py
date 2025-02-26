import gspread
import re

g_client = gspread.service_account('service_account_creds.json')

spread_sheet = g_client.open_by_key('18BdSkWlJkP1akC2WYO4X-6Xi8WKdPT2lwEFRLQnp1-w')

all_ws = spread_sheet.worksheets()

pattern = r'^Sheet\d+$'

for ws in all_ws:
    if re.search(pattern, ws.title) is not None:
        spread_sheet.del_worksheet(ws)
