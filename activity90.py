L = [4, 6, 2, 8, 3, 7, 1, 5]
print("original list:", L)
count = 0
for i in L:
    count += i
avg = count / len(L)
print("sum:", count)
print("average:", avg)
L.sort()
print("smallest element is:", L[0])
print("largest element is:", L[-1])