def check_age(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age < 18:
            return "Minor"
        elif age < 65:
            return "Adult"
        else:
            return "Senior"
    except ValueError as ex:
        return f"Error: {ex}"
userinput_age = int(input("Enter your age: "))
print(check_age(userinput_age))
