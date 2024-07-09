def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        result = f"The result of the division is {result}"
        return result
    except ZeroDivisionError:
        result = f"Error: Cannot divide by zero."
        return result
    except ValueError:
        result = f"Error: Please enter numeric values only."
        return result
