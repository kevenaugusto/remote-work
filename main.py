import sqlite3

from util.database import check_existence, path as database_path


def main():
    conn = sqlite3.connect(database_path())
    check_existence(conn)


if __name__ == "__main__":
    main()
