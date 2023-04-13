import sqlite3


def check_existence(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='ACTIVITIES'""")

    if cursor.fetchone() is None:
        create_table(conn)
        check_existence(conn)

    cursor.close()


def create_table(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE "ACTIVITIES" (
            "DATE"	INTEGER NOT NULL,
            "DESCRIPTION"	TEXT NOT NULL,
            "COST"	NUMERIC
        )
    """)

    cursor.close()
