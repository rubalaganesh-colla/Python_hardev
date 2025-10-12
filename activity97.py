test_dict = {'codingal': 2, 'is': 2, 'best': 3}
print("the orginal dictionary is : " + str(test_dict))
k = 2
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1
print("frecuncy of k is :" + str(res))