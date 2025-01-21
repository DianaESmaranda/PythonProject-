def generate_multiplication_table(number, up_to=10):

    print(f"Multiplication Table for {number}:")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")



number = int(input("Enter the number for the multiplication table: "))
up_to = int(input("Enter how many rows you want in the table (default 10): "))


generate_multiplication_table(number, up_to)
