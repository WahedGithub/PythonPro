import openpyxl

wb = openpyxl.workbook.Workbook() # with this the Sheet will get created 

wb.save("Sample.xlsx")