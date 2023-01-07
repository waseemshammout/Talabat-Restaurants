import pyodbc as db

conn = db.connect('Driver={SQL Server};Server=DESKTOP-PDC6CGI\SQLEXPRESS;Database=SIS;Trusted_Connection=yes')
cursor = conn.cursor()
cursor.execute('Select * from TB_1214 ')

for row in cursor.fetchall():
    print(row[1])