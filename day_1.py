"""
Ubah "Hello World!" menjadi pesan yang ingin Anda sampaikan pada dunia.
"""

print('Hello, World!')


# variable in python
say = 'Ini Variable'
print(say)


# input in pythn
name = input("What your name Bro: ")
print("Hello %s" % name)
print("Yoo {}".format(name))



"""
TODO:
- Buatlah sebuah variabel bernama greeting.
- Assign teks "Saya mulai belajar Python!" pada variabel tersebut. 
"""

greeting  = "Saya mulai belajar Python!"
print(greeting)

# list data type 
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:7:3])
print(x[1:])
print(x[:3])

# set data type
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2) #akan mengabugkan variable set 1 dan variable set 2
print("Union:", union)

intersection = set1.intersection(set2) # akan mengambil nilai yang sama
print("Intersection:", intersection)

# dict data type
profile = {'name': 'Mamang', 'age':19,'isStudent':False}
print(type(profile))
print(profile)
print(profile["name"])
print(profile["isStudent"])
# add data in variable dict
profile['address'] = 'jalan. ke sana sini'
print(profile)
# delete data in variable dict
del profile["isStudent"]
print(profile)

# convet data type
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))
print(dict([[1,2],[3,4]]))