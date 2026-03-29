number1 = float(input("Enter your number1: "))
opr = input("Enter your operator: (+,-,*,/): ")
number2 = float(input("Enter your number2: "))
if number1 < 0 or number2 < 0:
    print("Invalid input, only positive numbers are allowed")
    exit()
match opr:
    case "+":
        print("Result: " + str(number1 + number2))
    case "-":
        print("Result: " + str(number1 - number2))   
    case "*":
        print("Result: " + str(number1 * number2))
    case "/":
        if number2 == 0:
            print("Error: Division by zero is not allowed")
        print("Result: " + str(number1 / number2))      
    case _:
        print("Invalid operator")
        