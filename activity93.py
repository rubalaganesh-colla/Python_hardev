weather =(1,0,0,0,0,0,0,0,0,1)
sunny = 0
rainy = 1
for i in range(0,10):
    if (weather[i] == 1):
            rainy += 1
    else:
            sunny += 1
if sunny>rainy:
        print("The weather is good")
else:
        print("The weather is bad")