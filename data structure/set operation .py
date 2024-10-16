# union operation in the set

a={1,2,3,4,5}
b={4,5,6,7,8}
print(a|b)           #or
print(a.union(b))    #or
print(b.union(a))

# intersection operation in set

print(a&b)
print(a.intersection(b))

# difference operation in the set

print(a-b)
print(b-a)
print(a.difference(b))

# symmetric differences in the set

print(a^b)
print(a.symmetric_difference(b))

# is operation in set 

x={3,4,5,7}
y={3,4,5,6,7,8}
print(x.issubset(y))
z={3,4,5,10}
print(x.issubset(z))
n={11,23,87,45}
print(n.isdisjoint(y))
print(y.issuperset(x))

#  use to remove duplicate data

x1=[2,2,3,4,5,6,6,5,4,7,8,9]
xs=(set(x))
xl=list(set(x))
print(x1)
print(xs)
print(xl)