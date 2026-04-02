#! /bin/python
# Name:        demo_sqlite.py
# Author:      QA2.0, Pete Behague
# Revision:    v1.0
# Description: This program will demonstrate how to connect to a SQLite database
# file, create a table, insert and query rows using the SQLite3 module/API.
"""
    Create and populate a SQLite database file.
"""

import sys
import pyodbc
import pymssql


def main():
    """ Create, Insert and query all rows in database """
    # Connect into SQLite database file.
    # App can use one of two different packages to access SQL Server database, pyodbc or pymssql:
    db_conn = pyodbc.connect(r"Driver={ODBC Driver 13 for SQL Server};Server=(local);Database=PythonMovies;UID=Fred;PWD=Pa$$w0rd;")
    # db_conn = pymssql.connect(server=r"(local)", database="PythonMovies", user="Fred", password="Pa$$w0rd")
    # Open a cursor to store
    cur = db_conn.cursor()

    # Create a movies table if it doesn't already exist.
    # The "IF object_id..." logic is Microsoft SQL Server specific and won't work for SQLite
    cur.execute("IF object_id('movies', 'U') is null CREATE TABLE movies (id int identity(1, 1) PRIMARY KEY,name TEXT,year INTEGER,rating INTEGER )")
    db_conn.commit()  # Commit Changes to database.

    # Loop and write users favourite movies to database file.
    while True:
        movie = input("Enter name of movie (q=quit): ")
        if movie.lower() == "q":
            break
        year = input(f"Enter year of release for {movie}: ")
        rating = input(f"Enter your rating for {movie} (1-10): ")

        # cur.execute("INSERT INTO movies (name,year,rating) VALUES(?,?,?)", (movie, year, rating))
        cur.execute(f"INSERT INTO movies (name,year,rating) VALUES('{movie}',{year},{rating})")
        print("1 row inserted")

        db_conn.commit()  # Commit Changes to database.

    # Query, fetch and display all rows from database file.
    cur.execute("SELECT * FROM movies")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    db_conn.close()  # Close database connection.
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
