import sqlite3

database = 'livrariazinha.db'

conn = sqlite3.connect(database)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE if not exists tb_cliente
(CPF char(3) primary key,
nome varchar(40),
idade int)""")

# cursor.execute("""
# INSERT INTO tb_cliente values ('06944402130', 'Esther', 32)
# """)

l = cursor.execute("select * from tb_cliente")
print(l.fetchall())

conn.commit()
cursor.close()
conn.close()
