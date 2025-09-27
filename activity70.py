var = 30
while var > 0:
    var = var - 1
    if var % 10 == 0:
        continue
    print(var)
    print("Loop ended")