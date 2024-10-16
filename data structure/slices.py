# getting a slice
s="digipodium"
slice1=s[4:7]
print(slice1)

slice2=s[0:4]
print(slice2)

slice3=s[:4]
print(slice3)

slice4=s[4:len(s)]
print(slice4)

slice5=s[4:]
print(slice5)


name="mohammad husain ansari"

# first name
firstname=name[:8]
print(firstname)

# lastname
lastname=name[-6:]
print(lastname)

# middlename
middlename=name[9:-7]
print(middlename)

# even index
even_index=name[::2]
print(even_index)

# odd index
odd_index=name[1::2]
print(odd_index)

# reversing a sequence with slicing
reversed_name=name[::-1]
print(reversed_name)

# dont effect the string
print(name[:])


print(name[::-1][:7][::-1])

# mid alphabets of the name
name="mohammad husain ansari"
midname=name[3:-3]
print(midname)
