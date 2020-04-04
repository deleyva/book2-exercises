import sqlite3

with sqlite3.connect("blog.db") as conn:
    c = conn.cursor()

    c.execute("""
        CREATE TABLE posts
        (title TEXT, post TEXT)
    """)
    posts = [
        ("Good", "I\'m good."),
        ("Well", "I\'m well."),
        ("Excellent", "I\'m excellent."),
        ("Okay", "I\'m okay."),
    ]

    c.executemany("INSERT INTO posts VALUES(?,?)",posts)