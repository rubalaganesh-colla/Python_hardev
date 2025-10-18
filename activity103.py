numbers1 = [1,2,3,4,5]
numbers2 = [6,7,8,9,10]
result = map(lambda x, y:x+ y, numbers1 , numbers2)
print("Final Result:")
print(list(result))
nums = [1,2,3,4,5]
def sq(n):
    return n*n  
square = list(map(sq, nums))
print("square of in list")
print(square)