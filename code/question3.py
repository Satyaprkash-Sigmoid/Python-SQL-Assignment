import xlrd
import pandas
import openpyxl
import psycopg2

df = pandas.read_excel('/Users/satyaprakash/PycharmProjects/Python_SQL_Assignment/dataFiles/file_Q2.xlsx')

try:
    conn = psycopg2.connect(host="localhost", database="test", user="satyaprakash", password="Satya@1657", port='5432')
    cursor = conn.cursor()
    insert_query = "Insert into newTable (empno, ename, dname, compensation, months) values (%s,%s,%s,%s,%s)"
    for index, row in df.iterrows():
        cursor.execute(insert_query,(row['Employee Number'], row['Employee Name'], row['Department Name'], row['Compensation'], row['Total Months']))
    conn.commit()
except:
    print("Connection Error")
finally:
    conn.close()


