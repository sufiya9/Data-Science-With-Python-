x= [1,2,3,4,5,6,7,8,9,1,2,3,4,5]
# x2=map(lambda i : i**2,x)
# print(x2)
# # for i in x2:
# #      print(i)
# # print(list(x2))
x2=list(map(lambda i: i**2, x))

x3=tuple(map(lambda i : i**3,x)) #tuple with x cube
print(x2)
print(x3)

y=['apple','banana','cherry']
z=['pie','shake','jam']

words=set(map(lambda a,b : a+'-'+b, y,z))
print(words)

# single line input with multiple
numbers =list(map(int,input('enter 10 numbers ;').split()))
print(numbers)

