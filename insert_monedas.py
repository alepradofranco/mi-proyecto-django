import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Insertar monedas
cursor.execute(
    "INSERT INTO UnidadMonetaria (nombremoneda, tipomoneda, simbolomoneda, tasaconversionmoneda, estadomoneda) VALUES (?, ?, ?, ?, ?)",
    ('Dólar Estadounidense', 'Oficial', '$', 1.00, 1)
)

cursor.execute(
    "INSERT INTO UnidadMonetaria (nombremoneda, tipomoneda, simbolomoneda, tasaconversionmoneda, estadomoneda) VALUES (?, ?, ?, ?, ?)",
    ('Peso Colombiano', 'Oficial', 'COP', 0.00025, 1)
)

conn.commit()

cursor.execute('SELECT * FROM UnidadMonetaria')
print('✓ Monedas agregadas a la BD:')
for row in cursor.fetchall():
    print(f"  ID: {row[0]}, Nombre: {row[1]}, Símbolo: {row[3]}, Activa: {row[5]}")

conn.close()
