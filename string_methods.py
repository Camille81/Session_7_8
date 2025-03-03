from os.path import split

print(dir("hello"))

print(help("hi".capitalize))

print("I like to go to school". capitalize())
print("IS THIS SUPPOSED TO WORK?".capitalize())
print("hello".center(40, "*")) # nothing, "*" or "-"
print("gmail.com".find(".")) #if doesn't find -> -1
s = "i see a cat who like to cat while i cat on a cat"
#find all occurrences
poz = 0
while True:
    poz = s.find("cat", poz)
    if poz == -1:
        break
    print("fund cat on position", poz)
    poz += 1

#lower
s = "I SEE A LOT OF THINGS"
print(s.lower())

#replace - replace x with y
s = "i see a cat who likes to eat a rat, what a good cat"
print(s.replace("c", "r"))
print(s.replace("cat", "lion"))
s = "hello, kind sir!"
print(s.replace(",", ""))

#split
s = "i like to go shopping"
print(s.split())
splitted = s.split()
print("XX".join(splitted)) #join

#upper
s = "i see a lot of things"
print(s.upper())
print(s.upper().capitalize())

#tittle
s = "i like the mountains"
print(s.title())


