# Octal to Decimal conversion in Python

octal_string = input("Enter an octal number: ")
decimal_value = 0
power = 0

# Iterate through the octal string from right to left
for digit_char in reversed(octal_string):
    # Check if the character is a valid octal digit (0-7)
    if '0' <= digit_char <= '7':
        digit = int(digit_char)
        decimal_value += digit * (8 ** power)
        power += 1
    else:
        print("Invalid octal number entered.")
        exit(1)  # Indicate an error

print("Decimal equivalent:", decimal_value)