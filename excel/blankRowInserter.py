#!python3

# blankRowInserter.py - adds M rows before N row - Usage: blankRowInserter N M filename.xlsx

import openpyxl, os, sys

if len(sys.argv) > 1:
    #Get numbers and fileName from command line
    number = int(sys.argv[1])
    number2 = int(sys.argv[2])
    fileName = str(sys.argv[3])
else:
    print('Please give a number to command line as argument')

# Load workbook, activate sheet 1, you can change this to whatever you want, or ask for input.
wb = openpyxl.load_workbook('/Users/janitiainen/Documents/Koodia/Automate boring stuff/13. excel_worksheets/produceSales.xlsx')
sheet = wb.active

# Insert the rows to the Excel file rows
for i in range(number2):
    sheet.insert_rows(number)

# Get working directory using os, we use this to save the file
workingDir = os.getcwd()

# Save the file to working directory + the filename you gave as argument.
wb.save(workingDir + '/' + fileName)


