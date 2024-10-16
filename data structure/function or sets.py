# initialize my set
my_set={1,3}
print(my_set)

# add an item
my_set.add(2)
print(my_set)

# add multiple item
my_set.update([2,3,4])
print(my_set)
my_set.update([4,5],{1,6,8})
print(my_set)

# removing item from sets

# initialize my_set
my_set={1,3,4,5,6}
print(my_set)

# discard an element
my_set.discard(4)
print(my_set)

# remove an element
my_set.remove(6)
print(my_set)

# pops the random item in the sets
my_set.pop()
print(my_set)

# clear all set and give empty set 
my_set.clear()
print(my_set)