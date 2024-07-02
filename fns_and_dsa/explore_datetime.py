from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print(
        f"Current date and time: {current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}")


number_of_days = int(
    input("Enter the number of days to add to the current date: "))


def calculate_future_date():
    current_date = datetime.now()
    to_be_added = timedelta(days=number_of_days)
    future_date = current_date + to_be_added
    print(
        f"Future date: {future_date.year}-{future_date.month}-{future_date.day}")
