import psycopg2
import xlsxwriter
import logging


class FirstQuery:
    def solution(self, query1):
        try:
            conn = psycopg2.connect(host="localhost", database="test", user="satyaprakash", password="Satya@1657",
                                    port='5432')
            cursor = conn.cursor()

            cursor.execute(query1)
            data = cursor.fetchall()

            workbook_Q1 = xlsxwriter.Workbook(
                '/Users/satyaprakash/PycharmProjects/Python_SQL_Assignment/dataFiles/file_Q1.xlsx')
            worksheet = workbook_Q1.add_worksheet()
            worksheet.write('A1', 'Employee Number')
            worksheet.write('B1', 'Employee Name')
            worksheet.write('C1', 'Manager Name')
            row = 1
            col = 0
            for num, name, mgr in (data):
                worksheet.write(row, col, num)
                worksheet.write(row, col + 1, name)
                worksheet.write(row, col + 2, mgr)
                row += 1
        except:
            logging.error("Error in connection")
        finally:
            conn.close()
            workbook_Q1.close()
            logging.info("No issues")


if __name__ == '__main__':
    query1 = "select t1.empno,t1.ename, t2.ename from emp t1 left join emp as t2 on t1.mgr=t2.empno;"
    ob = FirstQuery()
    ob.solution(query1)
