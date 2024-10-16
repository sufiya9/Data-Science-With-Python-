# append function(add an item in the list)
fruits=[]

fruits.append('apple')
fruits.append('banana')
fruits.append('mango')
fruits.append('orange')
print("fruits=",fruits)

# insert function(insert an item at a specific index)

fruits.insert(2,'pineapple')
print("fruits=",fruits)

# extend function
dry_fruits=['dates','almonds','cashew','walnuts','raisins']
fruits.extend(dry_fruits)
print(fruits)


# sort function
fruits.sort()
print('fruits=',fruits)

# remove function
fruits.remove('dates')
print('fruits=',fruits)

# fruits.remove('kiwi')
# print('fruits=',fruits)

# reverse function
fruits.sort(reverse=True)
print('fruits=',fruits)



