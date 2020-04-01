import sqlite3

with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()

    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()

    for r in rows:
        print(f"La marca {r[0]} tiene {r[2]} coches del modelo {r[1]}")

    c.execute("UPDATE inventory SET quantity = 9 WHERE model ='Civic'")
    c.execute("UPDATE inventory SET quantity = 2 WHERE model = 'Accord'")

    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    print("_----------____--------")
    for r in rows:
        print(f"La marca {r[0]} tiene {r[2]} coches del modelo {r[1]}")

