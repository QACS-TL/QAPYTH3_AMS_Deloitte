#! /bin/python
# Name:        demo_sqlite.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to connect to a SQLServer database
# file, create a table, insert and query rows using the SQLServer module/API.
"""
    Create and populate a SQLite database file.
"""

import sys
import sqlite3
import os


def main():
    """ Create, Insert and query all rows in database """
    # Prompt user if they want to create or use existing database file.
    if os.path.isfile(r"C:\labs\movies_db.sqlite"):
        response = input("Do you want to use existing SQLite file (y/n)? ")
        if response.lower() == "n":
            os.remove(r"C:\labs\movies_db.sqlite")

    # Connect into SQLite database file.
    db_conn = sqlite3.connect(r"C:\labs\movies_db.sqlite")
    # Open a cursor to store
    cur = db_conn.cursor()

    # Create a movies table if it doesn't already exist.
    cur.execute("""CREATE TABLE IF NOT EXISTS movies
                      ( id      INTEGER PRIMARY KEY
                       ,name    TEXT
                       ,year    INT
                       ,rating  INTEGER ) """)

    # Loop and write users favourite movies to database file.
    while True:
        movie = input("Enter name of movie (q=quit): ")
        if movie.lower() == "q":
            break
        year = input(f"Enter year of release for {movie}: ")
        rating = input(f"Enter your rating for {movie} (1-10): ")

        # cur.execute("""INSERT INTO movies (name,year,rating) VALUES(?,?,?)""", (movie, year, rating))
        cur.execute(f"INSERT INTO movies (name,year,rating) VALUES('{movie}',{year},{rating})")
        print("1 row inserted")

    db_conn.commit()  # Commit Changes to database.

    # Query, fetch and display all rows from database file.
    cur.execute("""SELECT * FROM movies""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    db_conn.close()  # Close database connection.
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
