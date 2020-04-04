import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    query = """SELECT i.make, i.model, i.quantity, COUNT(o.order_date)
               FROM inventory i
               INNER JOIN orders o
               ON i.model = o.model
               GROUP BY o.model"""

    c.execute(query)

    result = c.fetchall()

    for row in result:
        print(row[0], row[1])
        print("Quantity of", row[2])
        print("Orders", row[3])
        print("__________")