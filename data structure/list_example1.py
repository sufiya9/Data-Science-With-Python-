x=[2,4,6,8]
x2=[]
for i in x:
    s=i**2
    x2.append(s)
print(x2)
print(x)


x=[2,4,6,8]
y=[5,6,8,3]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)


# exiting list to new list 
# 1.loops 
# 2.comprehension (one line expression)
# 3.lambda epression
    
names=['Sufiya Ansari','Ibtisham Raza','Shivani Sachan']
initials=[]
for name in names:
    parts=name.split()
    initials.append(parts[0][0]+parts[-1][0])
print(initials)