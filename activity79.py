def calculate_age(birth_date):
    """
    Calculate age based on the given birth date.
    :param birth_date: A datetime object representing the date of birth.
    :return: Age in years.
    """
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
def main():
    try:
        birth_date_input = input("Enter your date of birth (YYYY-MM-DD): ")
        birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
        age = calculate_age(birth_date)
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
if __name__ == "__main__":
    main()