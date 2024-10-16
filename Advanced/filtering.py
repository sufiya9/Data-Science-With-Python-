a=[1,2,3,4,5,6,7,8,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,8,9,]
clean_a=list(filter(lambda i: i !=1,a))
print(clean_a)
clean_a=list(filter(lambda i: i !=4,a))
print(clean_a)
clean_a=list(filter(lambda i: i !=3,a))
print(clean_a)

files=['a.png','b.jpg','c.png','d.jpg','e.png']
jpeg=list(filter(lambda name: name.endswith('.jpg'),files))
png=list(filter(lambda name: name.endswith('.png'),files))
print(jpeg)
print(png)