import sqlite3

def single_character_matching_with___underscore_wildcard():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Challenge #16
    query = "SELECT name, sku FROM products WHERE sku LIKE 'USB_-A'"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    single_character_matching_with___underscore_wildcard()