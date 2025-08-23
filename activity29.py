print("enter marks of 5 subjects")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if(a<0 or a>100 or b<0 or b>100 or c<0 or c>100 or d<0 or d>100 or e<0 or e>100):exit
tot = a+b+c+d+e
avg = tot/5
print("Total marks:",tot)
print("Average marks:",avg)

if avg>=91 and avg<=100:
    print("Grade A")
elif avg>=81 and avg<=90:
    print("Grade B")    
elif avg>=71 and avg<=80:
    print("Grade C")
elif avg>=61 and avg<=70:
    print("Grade D")
elif avg>=51 and avg<=60:
    print("Grade E")
elif avg>=0 and avg<=50:
    print("Grade F")
else:
    print("Invalid Input")  


