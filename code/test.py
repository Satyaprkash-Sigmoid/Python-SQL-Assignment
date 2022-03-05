import xlrd
import pandas
import openpyxl

df = pandas.read_excel('/Users/satyaprakash/PycharmProjects/Python_SQL_Assignment/dataFiles/file_Q2.xlsx')
print(df)
# book = xlrd.open_workbook('/Users/satyaprakash/Downloads/file_Q1 copy.xls')
# print("The number of worksheets is {0}".format(book.nsheets))
# print("Worksheet name(s): {0}".format(book.sheet_names()))
# sh = book.sheet_by_index(0)
# print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
# print("Cell D30 is {0}".format(sh.cell_value(rowx=10, colx=5)))
#
# for rx in range(sh.nrows):
#     print(sh.row(rx))