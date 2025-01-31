#[]
s = "abcdefghijklmopqrstuvwxyz"
print(s)
print(s[1:4], s[6:9])
print(s[:4], s[6:])
print(s[1:10:2])
print(s[::-1])
print("racecar"[::-1])

# how to replace a letter
s= "cat"
s = "r" + s[1:]
print(s)

s = "seven" #I want to change it se7en
s = s[:2] + "7" + s[3:]
print(s)
