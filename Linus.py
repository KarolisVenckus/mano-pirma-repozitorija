First_number = input("Type in a number: ")
Second_number = input("Type in a second number: ")
Third_number = input("Type in a third number: ")
Biggest_number = 0
if int(First_number) > int(Biggest_number):
    Biggest_number = First_number
if int(Second_number) > int(Biggest_number):
    Biggest_number = Second_number
if int(Third_number) > int(Biggest_number):
    Biggest_number = Third_number
print(f"The highest number is {Biggest_number}")
