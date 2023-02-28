while True:
    type = input("* , + , / ")
    
    first_number = input("Enter First Number ")
    second_number = input("Enter Second Number ")

    if type == '*':
        result = float(first_number) * float(second_number)
    elif type == '+':
        result = float(first_number) + float(second_number)
    elif type == '/':
        result = float(first_number) / float(second_number)
    else:
        print("Invalid operator")
        continue

    print("Result:",result) 
