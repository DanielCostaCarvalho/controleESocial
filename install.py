import sqlite3

print("Criando a tabela")
conn = sqlite3.connect('controleESocial.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE Empresa (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    nome    VARCHAR,
    enviou1 BOOLEAN,
    enviou2 BOOLEAN,
    enviou3 BOOLEAN,
    passou1 BOOLEAN,
    passou2 BOOLEAN,
    passou3 BOOLEAN,
    obs     VARCHAR,
    cnpj    VARCHAR
);
""")
conn.close()

print('Tabela criada!')
