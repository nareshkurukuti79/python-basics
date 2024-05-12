####################  SQLite DataBase ################

import sqlite3
import json
from pathlib import Path

products = json.loads(Path("ecommerce/products.json")).read_text()

print(products)
print(type(products))

# writing to a database

with sqlite3.connect("products-db.sqlite3") as connection:
    command = "INSERT INTO Products VALUES (?, ?, ?)"

    for product in products:
        connection.execute(command, product.values())

    connection.commit()


# Reading from a database

with sqlite3.connect("products-db.sqlite3") as connection:
    command = "SELECT * FROm Products"
    connection.execute(command)

    cursor = connection.execute(command)

    for data_row in cursor:
        print(data_row)
