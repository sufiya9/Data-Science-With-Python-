# exiting list to new list 
# 1.loops 
# 2.comprehension (one line expression)
# 3.lambda epression

# comprehension in list
x=[11,5,7,8,4,3,2,6,9]
x2=[i**2 for i in x ]
print(x2)

x=[2,4,6,7,8]
y=[5,4,6,2,8]
z=[i+j for i,j in zip(x,y)]
print(z)

names=['Sufiya Ansari','Ibtisham Raza','Shivani Sachan ']
initials=[i.split()[0][0]+i.split()[-1][0]  for i in names]
print(initials)