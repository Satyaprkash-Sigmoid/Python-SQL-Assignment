import psycopg2
import xlsxwriter

try:
    conn = psycopg2.connect(host="localhost", database="test", user="satyaprakash", password="Satya@1657", port='5432')
    cursor = conn.cursor()
    query4 = 'select t1.dname,t2.deptno,sum(t1.compensation) from newtable t1 join dept t2 on t1.dname=t2.dname group ' \
             'by t1.dname,t2.deptno; '
    cursor.execute(query4)
    data = cursor.fetchall()
    # for i in data:
    #     print(i)

    workbook_Q4 = xlsxwriter.Workbook(
        '/Users/satyaprakash/PycharmProjects/Python_SQL_Assignment/dataFiles/file_Q4.xlsx')
    worksheet = workbook_Q4.add_worksheet()
    worksheet.write('A1', 'Department name')
    worksheet.write('B1', 'Department Number')
    worksheet.write('C1', 'Compensation')

    row = 1
    col = 0
    for name, number, comp in (data):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, number)
        worksheet.write(row, col + 2, comp)
        row += 1
except:
    print("Connection Error...")
finally:
    conn.close()
    workbook_Q4.close()
