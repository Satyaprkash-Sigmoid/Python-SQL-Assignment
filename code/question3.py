import xlrd
import pandas
import openpyxl
import psycopg2
import logging


class ThirdQuery:
    def solution(self, insert_query):
        df = pandas.read_excel('/Users/satyaprakash/PycharmProjects/Python_SQL_Assignment/dataFiles/file_Q2.xlsx')
        try:
            conn = psycopg2.connect(host="localhost", database="test", user="satyaprakash", password="Satya@1657",
                                    port='5432')
            cursor = conn.cursor()

            for index, row in df.iterrows():
                cursor.execute(insert_query, (
                row['Employee Number'], row['Employee Name'], row['Department Name'], row['Compensation'],
                row['Total Months']))
            conn.commit()
        except:
            logging.error("Error in connection")
        finally:
            conn.close()
            logging.info("No issues")


if __name__ == '__main__':
    insert_query = "Insert into newTable (empno, ename, dname, compensation, months) values (%s,%s,%s,%s,%s)"
    ob = ThirdQuery()
    ob.solution(insert_query)
