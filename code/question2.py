import psycopg2
import xlsxwriter

try:
    conn = psycopg2.connect(host="localhost", database="test", user="satyaprakash", password="Satya@1657", port='5432')
    cursor = conn.cursor()

    query2 = "select emp.empno, emp.ename,dept.dname, CASE WHEN enddate IS NOT NULL then EXTRACT(year FROM age(" \
             "enddate,startdate))*12 + EXTRACT(month FROM age(enddate,startdate)) else EXTRACT(year FROM age(" \
             "'2022-03-04',startdate))*12 + EXTRACT(month FROM age('2022-03-04',startdate)) END *emp.sal " \
             "Compensation,CASE WHEN enddate IS NOT NULL then EXTRACT(year FROM age(enddate,startdate))*12 + EXTRACT(" \
             "month FROM age(enddate,startdate)) else EXTRACT(year FROM age('2022-03-04',startdate))*12 + EXTRACT(" \
             "month FROM age('2022-03-04',startdate)) END Total_Months from emp join jobhist on " \
             "emp.empno=jobhist.empno join dept on dept.deptno=jobhist.deptno; "

    cursor.execute(query2)
    data = cursor.fetchall()
    for i in data:
        print(i)
    workbook_Q1 = xlsxwriter.Workbook(
        '/Users/satyaprakash/PycharmProjects/Python_SQL_Assignment/dataFiles/file_Q2.xlsx')
    worksheet = workbook_Q1.add_worksheet()
    worksheet.write('A1', 'Employee Number')
    worksheet.write('B1', 'Employee Name')
    worksheet.write('C1', 'Department Name')
    worksheet.write('D1', 'Compensation')
    worksheet.write('E1', 'Total Months')

    row = 1
    col = 0
    for num, name, dname, comp, month in (data):
        worksheet.write(row, col, num)
        worksheet.write(row, col + 1, name)
        worksheet.write(row, col + 2, dname)
        worksheet.write(row, col + 3, comp)
        worksheet.write(row, col + 4, month)
        row += 1



except:
    print("There is some Problem in Connection...")
finally:
    conn.close()
    workbook_Q1.close()
