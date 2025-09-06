num = int(input("Enter a number: "))

rev = 0

temp = num

while temp > 0:
	rem = temp % 10
	rev = rem + (rev * 10)
	temp = temp // 10

# display the result
if rev == num:
	print("\nIt is a Palindrome Number")
else:
	print("\nIt is not a Palindrome Number")