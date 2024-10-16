from functools import reduce
import operator

x=[1,2,3,4,5,6,7,7,3,4,2,3,5,6]

#multiple all values of x

ans=reduce(operator.mul,x)
print(ans)
ans=reduce(operator.add,x)
print(ans)
ans=reduce(operator.mod,x)
print(ans)
ans=reduce(operator.sub,x)
print(ans)

# same as
# ans=1
# for i in x:
#     ans*=i
# print(ans)

ans2= reduce(lambda i,j : i+i*j+i, x)
print(ans2)