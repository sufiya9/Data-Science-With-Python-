# count the total n0 0f a item in the list
x=[1,1,1,1,1,1,3,4,5,6,7,87,90,65,44,4,5,6,3,3,3]
print("total number of 1 = ",x.count(1))
print("total number of 3 = ",x.count(3))
print("total number of 90 = ",x.count(90))
print("total number of 89 = ",x.count(89))

# index function( return the first index value )
movies=['RRR','DDLJ','Dr Strange','3 idiots','KKKG','baby','gangubai']
print(movies.index("Dr Strange"))
# print(movies.index("puspa"))

# copy function
blockbuster=movies.copy()
print('blockbuster=',blockbuster)

# clear function
blockbuster.clear()
print('blockbuster=',blockbuster)

# pop function

print("after poping=",movies.pop())
print("after poping index 2=",movies.pop(2))
print("after poping index 3=",movies.pop(3))
print("after poping unavailable index =",movies.pop(8))