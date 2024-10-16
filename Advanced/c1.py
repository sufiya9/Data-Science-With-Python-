class Dog:
    breed= ""
    age=0
    color=""
    weight=0
    height=0
    gender=""

    def bark(self):
        print('🐕bow'*4)

    def wag(self):
        print('wags tails')
    
    def eat(self,food):
        print(f'dog {food} kha raha h')

charlie= Dog() # calling the constructor
charlie.age=3
charlie.breed='street dog'
charlie.color='black'
charlie.weight=10
charlie.height=1
charlie.gender='male'
sheru= Dog()
sheru.age=6
sheru.breed='husky'
sheru.color='gray'
sheru.weight=7
sheru.height=2
sheru.gender='female'
jinny=Dog()
jinny.age=10
jinny.breed='bull dog'
jinny.color='white'
jinny.weight=7
jinny.height=3
jinny.gender='female'

jinny.bark()
jinny.eat('fish')
charlie.eat('dog-food')
sheru.eat('bachi hui roti')
sheru.eat('bachi hui dall')
sheru.bark()
charlie.bark()