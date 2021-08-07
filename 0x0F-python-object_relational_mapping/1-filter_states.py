#!/usr/bin/python3
""" this module selects and show the registers in tha tzble states
    of the given database thath starts with 'N'
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # get the connection parameters
    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    db_address = "localhost"

    # Open database connection and create a cursor object
    db = MySQLdb.connect(db_address, db_user, db_pass, db_name)
    cursor = db.cursor()

    # create an execute the SQL sencence
    sql_sentence = 'SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC'
    cursor.execute(sql_sentence)
    results = cursor.fetchall()

    # iterates and print each element in result
    for row in results:
        print(row)
