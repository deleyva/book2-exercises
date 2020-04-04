import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    query = "SELECT model, COUNT(order_date) FROM orders GROUP BY model"

    c.execute(query)

    results = c.fetchall()

    for row in results:
        print(row[0], row[1])