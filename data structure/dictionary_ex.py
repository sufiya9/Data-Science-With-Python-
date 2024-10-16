my_dict={'name':'sufiya','age':19}
# data retrive formate
print(my_dict['name']) 
print(my_dict.get('age'))

# print(my_dict['address']) it gave the error if dictionary is not available
print(my_dict.get('address'))  #it reture none

# modifying elements from dictionary

my_dict['age']=20
my_dict['address']='lucknow'
print(my_dict)

# removing elements from dictionary
squares={1:1,2:4,3:9,4:16,5:25,6:36,7:49}
print(squares.pop(4))
print(squares.popitem())
print(squares.clear())
del squares

# iterating through a dictionary

squares={1:1,2:4,3:9,4:16,5:25,6:36,7:49}
for i in squares:
    print(i)

for i in squares:
    print(squares[i])

for k,v in squares.items():
    print(k,v)