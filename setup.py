import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, " \
"name TEXT, " \
"sku TEXT, " \
"price NUMBER )")




cursor.execute("INSERT INTO products (product_id, name, sku, price) " \
" VALUES (201, 'USB-C Hub', 'USB1-A', 34.50)")
cursor.execute("INSERT INTO products (product_id, name, sku, price) " \
" VALUES (202, 'USB-C Hub Pro', 'USB2-A', 34.50)")
cursor.execute("INSERT INTO products (product_id, name, sku, price) " \
" VALUES (203, 'USB Flash Drive', 'USB10-A', 19.99)")
cursor.execute("INSERT INTO products (product_id, name, sku, price) " \
" VALUES (204, 'Wireless Mouse', 'MOU1-B', 19.99)")
cursor.execute("INSERT INTO products (product_id, name, sku, price) " \
" VALUES (205, 'Mechanical Keyboard', 'KEY1-B', 89.00)")

conn.commit()
conn.close()