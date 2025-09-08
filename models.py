import sqlite3
import os

DB_NAME = 'hair.db'

# TODO:need to break it into functions
# TODO:Read tables (each table as a function)

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    # TODO : Read database files
    conn.close()

def create_tables():
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
    conn.close()

def add_item_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    conn.close()

create_tables()
