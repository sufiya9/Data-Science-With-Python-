#fixing c1 using constructor

class Dog:

    def __init__(self,color,breed,gender,age,h=1,w=6):
        print('Dog Created')
        self.color=color
        self.breed=breed
        self.gender=gender
        self.age=age
        self.height=h
        self.weight=w
    def bark(self,sound='bow'):
        print(sound*6)

    def upd_weight(self,new_w):
        self.weight=new_w

tommy=Dog('red','bull Dog','female',5)
tommy.bark()
tommy.upd_weight(6)
print(tommy.age,tommy.weight,tommy.breed)

charlie=Dog('black','german sheperd','male',1,.5,3)
print(charlie.age,charlie.weight,charlie.breed,charlie.height)


