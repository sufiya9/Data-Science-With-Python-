def calc_area_v2(w,h):
    area=w*h
    return area

# display 
print(calc_area_v2(18,40))
print(calc_area_v2(10,67))

# storing return value in a variable
ans=calc_area_v2(10,56)
print(ans)

# using return values in a expression
ans= calc_area_v2(3,6)+calc_area_v2(20,30)
print(ans)
