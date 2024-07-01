def perform_operation(num1, num2, operation):

    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                print("can't divide by zero")
            else:
                result = num1 / num2
    return float(result)


print(perform_operation(5, 6, "add"))

#  if operation == "add":
# result = num1 + num2
# elif operation == "subtract":
#  result = num1 - num2
# elif operation == "multiply":
#   result = num1 * num2
# elif operation == "divide" and num2 != 0:
#   result = num1 / num2
