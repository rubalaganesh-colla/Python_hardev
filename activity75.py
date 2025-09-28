try:
    num1 , num2 = eval( input("Enter two numbers,spearate it  with commas: "))
    result = num1 / num2
    print(" The result is:", result )
except ZeroDivisionError: 
    print("zero division error")
except SyntaxError:
    print("comma missing")
except :
    print("wrong input")
else:
    print("No exceptions occurred.")
finally:
    print("Execution completed.")
    
