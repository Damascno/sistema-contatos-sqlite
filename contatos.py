import sqlite3

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT
)
''')

cursor.executemany('''
INSERT INTO contatos (nome, email, telefone)
VALUES (?, ?, ?)
''', [
    ('João', 'joao@email.com', '123-456-7890'),
    ('Maria', 'maria@email.com', '987-654-3210'),
    ('Carlos', 'carlos@email.com', '555-555-5555')
])

conn.commit()

cursor.execute('SELECT * FROM contatos')
contatos = cursor.fetchall()

for contato in contatos:
    print(contato)

cursor.execute('''
UPDATE contatos
SET telefone = ?
WHERE id = ?
''', ('999-999-9999', 2))

conn.commit()

cursor.execute('''
DELETE FROM contatos
WHERE id = ?
''', (1,))

conn.commit()

conn.close()
