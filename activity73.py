bill_amount = float(input("Enter the total bill amount: ₹"))
amount_paid = float(input("Enter the amount paid by the customer: ₹"))
if amount_paid < bill_amount:
    due_amount = bill_amount - amount_paid
    print(f"The customer still owes ₹{due_amount:.2f}.")
elif amount_paid > bill_amount:
    change = amount_paid - bill_amount
    print(f"The customer has overpaid. Return ₹{change:.2f} as change.")
else:
    print("The bill is fully paid. No due amount.")
