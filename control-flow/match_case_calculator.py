num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 + num2)
    case "/":
        if (num2 == 0):
            print("Sorry, you can't divide by zero!")
        else:
            print(num1 / num2)
