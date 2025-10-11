s1 = {2,5,9,}
s2 = {1,2,3,4,5}
s3 = list(zip(s1,s2))
print(s3,"\n")
list1 = [10,20,30,40,50]
list2 = [600,700,800,900,100]
for x , y in zip(list1,list2[::-1]):
    print(x,y)