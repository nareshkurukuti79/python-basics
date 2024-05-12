#####################  JSON Files #####################

import json
from pathlib import Path

products = [
    {"Product": "T-Shirt1", "Price": 5.99, "Stock Availability": 15},
    {"Product": "T-Shirt2", "Price": 13.99, "Stock Availability": 8},
    {"Product": "T-Shirt3", "Price": 99.99, "Stock Availability": 4},
    {"Product": "T-Shirt4", "Price": 59, "Stock Availability": 15},
    {"Product": "T-Shirt4", "Price": 100, "Stock Availability": 25},
    {"Product": "T-Shirt5", "Price": 575, "Stock Availability": 98},
]

product_data = json.dumps(products)
print(product_data)
print(type(product_data))


# Writing the above data to a json file
# Path("ecommerce/product.json").write_text(product_data)

# reading from a json file

json_data = Path("ecommerce/product.json").read_text()
# print(json_data)

readable = json.loads(json_data)
print(readable)
