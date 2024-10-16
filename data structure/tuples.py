# tuple with mix data type
my_tuple= (1, 'hello' ,3.4)
print (my_tuple)

# nested tuple
my_tuple= ('mouse' ,[8,4,6] ,(1,2,4))
print (my_tuple)

# A tuple is also created without using parentheses 
# this is known as tuple packing.
my_tuple= 3,4,6,"apple"
print (my_tuple)

# accessing tuple element using indexing
my_tuple= ('w','r','t','g','q','i')
print (my_tuple[0])
print (my_tuple[5])

# nested tuple
my_tuple=('mouse' ,[8,4,6] ,(1,2,4))
# nested indexing
print (my_tuple[0][3])
print (my_tuple[1][1])

# slicing
my_tuple=('a','s','d','f','g','j','h','k','p','o','i')
# element 2nd to 4th
print(my_tuple[1:4])
# element start to 3th
print(my_tuple[:-7])
# element 7th to last
print(my_tuple[7:])
# element start to end
print(my_tuple[:])

# concatenation 
print((1,2,3)+(4,5,6))

# repeat
print(('repeat',)*3)

my_tuple=('a','e','e','l','o')
print(my_tuple.count('e'))
print(my_tuple.index('l'))
