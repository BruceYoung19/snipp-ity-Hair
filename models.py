import sqlite3
import os

DB_NAME = 'hair.db'

# TODO:Read tables (each table as a function)

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    # TODO : Read database files
    conn.close()

def create_tables():
    try:
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
    
        #Create table - Users
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Firstname TEXT NOT NULL,
                Lastname TEXT NOT NULL,
                Email Text Not NULL UNIQUE
                )
                   ''')

        #Create table - Cuts
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Cuts(
                cut_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cost DECIMAL(10,2) NOT NULL 
                )
                    ''')
    
        #Create table - Style 
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Style(
                sytle_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cost DECIMAL(10,2) NOT NULL,
                description TEXT NOT NULL
                )
                   ''')

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error connect to SQLite: {e}")
    
    finally:
        if conn:
            conn.close()

#TODO - CASE per table, also need to add try
def add_item_db(fname,lname,email):
    #data 

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor() 
    sql_query = "INSERT INTO Users(Firstname,Lastname,email) VALUES (?,?,?)"
    cur.execute(sql_query, (fname,lname,email))

    conn.commit()
    conn.close()

def read_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    select_query = "SELECT * FROM Users"
    data = cur.execute(select_query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

#Testing the functions
#create_tables()
#add_item_db()
