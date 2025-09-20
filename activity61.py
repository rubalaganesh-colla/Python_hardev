def convert_number(num):
    hexadecimal = hex(num)
    binary = bin(num)
    octal = oct(num)
    return hexadecimal, binary, octal
decimal_number = int(input("Enter a decimal number: "))
hexadecimal, binary, octal = convert_number(decimal_number)
print(f"Hexadecimal: {hexadecimal}")
print(f"Binary: {binary}")
print(f"Octal: {octal}")