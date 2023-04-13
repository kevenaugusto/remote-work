import json
import sqlite3


def create_query() -> str:
    with open('settings/config.json', 'r') as config:
        return json.load(config)['database']['table']['create']


def generic_query(key: str) -> str:
    with open('settings/config.json', 'r') as config:
        return json.load(config)['database']['generic_queries'][key]


def path() -> str:
    with open('settings/config.json', 'r') as config:
        return json.load(config)['database']['path']


def check_existence(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute(generic_query('find_table'))

    if cursor.fetchone() is None:
        create_table(conn)
        check_existence(conn)

    cursor.close()


def create_table(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute(create_query())
    cursor.close()
