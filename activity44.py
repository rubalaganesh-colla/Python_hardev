string = input("Enter a string: ")
char = input("Enter a character to find frequency: ")
i=0
count=0
while (i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1
print("Frequency of",char,"is",count)

