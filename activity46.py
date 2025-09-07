num=int(input("Enter a number: "))
t=num
numlen=0
while(t>0):    
    numlen=numlen+1
    t=int(t/10)
print(numlen)
if numlen>=4:    
    numlen = int(numlen/2)
    chk = 0
    while numlen > 0:
        rem = num % 10
        if chk == numlen:
            midone = rem
        elif chk == (numlen - 1):
            midtwo = rem
        num = int(num / 10)
        chk = chk + 1
    prod = midone * midtwo
    print(" \n Product of mid digites (" +str(midone)+"*" +str(midtwo)+ ")=", prod)
else:
    print(" \n it is not a more or 4digits")

        
        
        
        
        
        









