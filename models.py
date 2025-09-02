import sqlite3

DB_NAME = 'hair.db'


# TODO:need to break it into functions

#def get_db_connection():
#    conn = sqlite3.connect(DB_NAME)
#    cur = conn.cursor()
#    return conn

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

# Make a table 
#cur.execute("CREATE TABLE User(Name,Year,Gender)")

cur.execute("""
        INSERT INTO User VALUES
        ('Bruce',2013,'Male'),
        ('Sandy',2000,'Female')
            """)

cur.execute("SELECT * FROM User")
users = cur.fetchall()
print(users)

conn.close()
