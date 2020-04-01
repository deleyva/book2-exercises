import sqlite3

with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()

    c.execute("INSERT INTO inventory VALUES('Ford', 'Focus', 10)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Civic', 11)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Ranger', 12)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Accord', 13)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Avenger', 14)")