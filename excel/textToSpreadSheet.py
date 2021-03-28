#!python3

# Open text files - add the contents to spread sheet.

import os, openpyxl
from pathlib import Path

# Open a file and read its contents.
print("Give a path to text file you want to read. Let's read 2 files.")

path1 = input()
path2 = input()

opFile = open(path1)
opFile2 = open(path2)

fileRows = opFile.readlines()
fileRows2 = opFile2.readlines()

# Save txt files lines to Excel workbook, first column and rows.
workBook = openpyxl.Workbook()
sheet = workBook.active

for i in range(len(fileRows)):
    sheet.cell(column=1, row= i + 1).value = fileRows[i]
    sheet.row_dimensions[i + 1].height = 30     # Lets make the row height taller.

for i in range(len(fileRows2)):
    sheet.cell(column=2, row= i + 1).value = fileRows2[i]

workBook.save('/Users/janitiainen/Desktop/testi.xlsx')
