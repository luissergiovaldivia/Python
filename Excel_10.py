import openpyxl

doc = openpyxl.load_workbook('address1.xlsx')

doc.get_sheet_names()