import sqlite3

from util.database import check_existence


def main():
    conn = sqlite3.connect('db/activities.db')
    check_existence(conn)


if __name__ == "__main__":
    main()
