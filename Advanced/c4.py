class calculation1:
    def Summation(self,a,b):
        return a+b;
class calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(calculation1,calculation2):
    def divide(self,a,b):
        return a/b;

d= Derived()

print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.divide(10,20))
