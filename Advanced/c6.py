class Movie:
    def __init__(self,title,rating,year):
       self.title=title
       self.rating=rating
       self.year=year

    def info(self):
        print(f'{self.title}({self.year}) -> {self.rating}')

    # overloading
    def __gt__(self,other):
        if self.rating > other.rating:
            return True
        else:
            return False 
    def __lt__(self,other):
        if self.rating > other.rating:
            return True
        else:
            return False 
        
    def __repr__(self):
        return self.title

m1=Movie('kkkg',4.5,2000)
m2=Movie("liger",1,2022)


print(m1>m2)
print(m2>m1)

movies=[m1,m2]
movies.sort()
print(movies)