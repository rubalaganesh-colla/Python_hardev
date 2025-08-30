medical_cause=input("did you have a medical cause Y or N:")
if medical_cause == "Y": 
    print("you are allowed")
else:
    atten = int(input("enter attendance of the students:"))
    if atten>=75:
        print("allowed")
    else:
        print("not allowed")