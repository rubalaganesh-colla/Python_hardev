def find_first_set_bit_position(n):
    if n == 0:
        return -1
    position = 0
    while (n & 1) == 0:
        n >>= 1
        position += 1
    return position
num = int(input("Enter a number: "))
result = find_first_set_bit_position(num)
if result != -1:
    print(f"The position of the first set bit is: {result}")
else:
    print("No set bits found.")
    
   
   