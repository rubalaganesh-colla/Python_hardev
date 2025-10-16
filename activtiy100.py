import array as arr
array_num = arr.array('i',[1,2,3,4,5])
print("the original array is: " + str(array_num))
print("number of occurence of 3 in the array: " + str(array_num.count(3)))
array_num.reverse()
print("the reversed array is: ")
print(array_num)