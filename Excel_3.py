from openpyxl import Workbook

wb = Workbook()

ws = wb.active

ws1 = wb.create_sheet("Mihojas") # insert at the end (default)