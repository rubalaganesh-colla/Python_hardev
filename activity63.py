def total_calc(bill, tip  ):
    tip = bill * tip / 100 
    total = bill + tip 
    return total
bill = int(input("Enter the bill amount: "))
tip = int(input("Enter the tip percentage: "))
amount = total_calc(bill, tip)
print(f"The total amount is: ${amount:.2f}")
