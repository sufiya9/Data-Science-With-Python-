class fruit:
    color='red'
    taste='sweet'

class veg:
    size='small'
    age='fresh'

class GM(fruit,veg):
    name='GM-122'

g=GM()

print(g.name)
print(g.color)
print(g.taste)
print(g.size)
print(g.age)



