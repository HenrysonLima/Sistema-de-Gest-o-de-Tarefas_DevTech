import pymysql

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "fitlife_db" # nome da base de dados
)

myscursor = mydb.cursor()

myscursor.execute("select * from clientes where id_cliente = 1") # query para ser aplicada na base de dados

myresult = myscursor.fetchall()
resultadoDaQuery = myresult
print(f"Informações achadas do cliente: {resultadoDaQuery}")