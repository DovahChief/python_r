import  pyodbc

print("hola")

#sqlcmd -S localhost -U SA -P 'Athum117343'

server = 'localhost'
database = 'ejem'
username = 'SA'
password = 'Athum117343'

driver= '{ODBC Driver 13 for SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("select * from usuario")
row = cursor.fetchone()

print(row)