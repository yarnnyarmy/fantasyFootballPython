import pyodbc

# Trusted connection to Sql Server Instance

# Trusted Connection to Named Instance

def connectSql():

    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=BEUDYFUL\\SQLEXPRESS;DATABASE=FantasyFootball;Trusted_Connection=yes;')

    cursor=connection.cursor()
    cursor.execute("SELECT @@VERSION AS version")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.version)
    cursor.close()
    connection.close()
