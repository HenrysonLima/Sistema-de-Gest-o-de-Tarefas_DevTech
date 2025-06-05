import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "devtech_database" # nome da base de dados
)

myscursor = mydb.cursor()

myscursor.execute("select * from clientes where id_cliente = 1") # query para ser aplicada na base de dados

myresult = myscursor.fetchall()
nome = myresult
print(f"O nome é {nome}")