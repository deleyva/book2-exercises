import sqlite3

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    while True:
        answer = input(prompt)
        if answer in set(["1", "2", "3", "4"]):
            operation = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(answer)]

            c.execute(f"SELECT {operation}(num) FROM numbers")

            get = c.fetchone()

            print(f"{operation}: {get[0]}")
        
        elif answer == '5':
            print("Exit")
            break