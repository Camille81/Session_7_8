s1 = "hello"
s2 = "world"
print(s1 + s2)
#add a space without modifying s1 and s2
print(s1 + " " + s2)
print(3*s2)
print((10//2)*s1)

#len function gives you the size of the string
print(s1, len(s1))
print(3*s2, len(3*s2))
for c in s2:
    print(c*4, end="")
#or
new_string = ""
for c in s2:
    new_string += c*4
print(new_string)

#in can be used to check if one string is inside another
print("h" in s1)#true
print("d" in s2)#true
print("x" in s1)#false
print("wor" in s2)#true

