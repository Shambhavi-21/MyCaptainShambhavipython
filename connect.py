import sqlite3

def connect(dbname):
    conn = sqlite3.connect("ox.db")
    conn.execute("CREATE TABLE IF NOT EXISTS OXFORD_DISCOVERS (NAME TEXT)")
    print("Table created successfully!")
    conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    insert_sql = "INSERT INTO  OXFORD_DISCOVERS (NAME) VALUES (?)"
    conn.execute(insert_sql, values)

    conn.commit()
    conn.close()

def get_oxford_info(dbname):
    conn = sqlite3.connect(dbname)

    cur = conn.cursor()
    cur.execute("SELECT * OXFORD_DISCOVERS")
    table_data = cur.fetchall()
    for record in table_data:
        print(record)
        
    conn.close()