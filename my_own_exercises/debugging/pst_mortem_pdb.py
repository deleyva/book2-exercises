def add_one_hundred():
    again = 'yes'
    while again == 'yes':
        number = input('Enter a numbeer between 1 and 10: ')
        new_number = (int(number) + 100)
        print(f"{number} plus 100 is {new_number}!")
        again = input("Another round, my friend?")
    print("Goodbye!")

    