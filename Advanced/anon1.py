f = lambda X : X + X**2

print(f)
ans = f(5)
print(ans)
for i in range (1,10):
    print(f(i))

g = lambda a,b : (a+b) *(b-a) +1
print(g(2,3))
print(g(2,2))
print(g(12,23))
print(g(2,12))