import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

try:
    # Verificar si la columna ya existe
    cursor.execute("PRAGMA table_info(Bingo)")
    columnas = [col[1] for col in cursor.fetchall()]
    
    if 'idunidadmonetaria' not in columnas:
        print("✓ Agregando columna idunidadmonetaria a la tabla Bingo...")
        cursor.execute("""
            ALTER TABLE Bingo 
            ADD COLUMN idunidadmonetaria INTEGER
        """)
        conn.commit()
        print("✓ Columna agregada exitosamente")
    else:
        print("✓ La columna idunidadmonetaria ya existe")
    
    # Verificar la estructura final
    cursor.execute("PRAGMA table_info(Bingo)")
    print("\nEstructura final de la tabla Bingo:")
    for col in cursor.fetchall():
        print(f"  - {col[1]} ({col[2]})")
        
except Exception as e:
    print(f"✗ Error: {e}")
finally:
    conn.close()
