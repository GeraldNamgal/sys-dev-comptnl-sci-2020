#!/usr/bin/env python3

# Sharer: Gerald Arocena
# Coder: Bianca Cordazzo
# Listener: Gerald Arocena and Bianca Cordazzo

import sqlite3

db = sqlite3.connect('test_db.sqlite')  # Create a connection to the database
cursor = db.cursor() 
cursor.execute("DROP TABLE IF EXISTS candidates")  # TODO: Don't exactly understand why sometimes need this?

cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_init TEXT, 
               party TEXT NOT NULL)''')

db.commit()

with open("candidates.txt") as candidates:
    next(candidates)  # jump over the header

    for line in candidates:
        line = line.strip('\n')
        values = line.split(sep="|")

        cursor.execute('''INSERT INTO candidates
        (id, first_name, last_name, middle_init, party)
        VALUES (?, ?, ?, ?, ?)''',
                       (int(values[0]), values[1], values[2], values[3], values[4]))

        db.commit()

# Demo
cursor.execute("SELECT * FROM candidates")
# # all_rows = cursor.fetchall()
# # print(all_rows)
for i in cursor:
    print(i)
