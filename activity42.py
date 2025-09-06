n=int(input("Enter a number: "))
sum =  0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit 
    temp//= 10
if n%sum==0:
    print(n, "It is an harshad number ")
else:
    print(n, "It is not a  harshad number ")



