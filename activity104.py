s1 = {1,2,3}
s2 = {'b', 'c', 'd'}
s3 = list(zip(s1, s2))
print(s3,"\n")
list1 = [1,2,3]
list2 = ['a','b','c']
for x,y in zip(list1, list2[::-1]):
    print(x,y)
stocks = {'AAPL', 'GOOG', 'MSFT'}
price = {150, 2800, 300}
new_dict = {stocks:price for stocks,
                       price in zip(stocks,(stocks,price))}
print('\n{}'.format(new_dict))


