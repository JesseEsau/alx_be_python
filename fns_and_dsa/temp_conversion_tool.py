FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


def convert_to_celsius(fahrenheit):
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

match unit:
    case "c":
        print(
            f"{temperature}{chr(176)}C is {convert_to_fahrenheit(temperature)}{chr(176)}F")
    case "f":
        print(
            f"{temperature}{chr(176)}F is {convert_to_celsius(temperature)}{chr(176)}C")
    case _:
        print("invalid input")
