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




upperText = "halo python"
print(upperText.upper())

lowerText = 'HALO PYTHON'
print(lowerText.lower())

rstripText = "Python      "
print(rstripText.rstrip()) # menghapus whitespace pada sebelah kanan atau akhir string.

lstripText = '     python is love'
print(lstripText.lstrip()) # menghapus whitespace pada sebelah kiri atau awal string.

stripText = '   halooo    '
print(stripText.strip()) # menghapus whitespace pada sebelah kiri dan kanan  atau awal dan akhir string.

stripText = 'codecodeDicodingcodecode'
print(stripText.strip('code')) #menghilangkan kata code pada bagian samping kiri dan kanan string 

'''
    pada dasarnya strip itu di gunakan ketika kita ingin menghilangkan sebuah kata pada bagian kiri dan kanan dari string.
    jika kita ingin cumn bagian kanan nya doang kita gunkan rstrip dan kalau cumn ingin kiri bisa menggunakan lstrip
'''


startWithText = 'Dicoding Indonesia'
print(startWithText.startswith('Dicoding')) # mengecek apakah kata Dicoding ada pada awal kalimat -> boolean
print(startWithText.endswith('Dicoding')) # mengecek apakah ada kata Dicoding pada akhir kalimat -> boolean


print(' sibuk '.join(['sedang belajar', 'di Dicoding'])) # mengabungkan kalimat sibuk pada akhir kata sebelum kata pada kalimat terakhir
print('Aku sednag belajar di Dicoding'.split()) # ini akan memisahkan string nya menjadi list
print('''aku sangat senang belajar di dicoding indonesia
    karena meterinya menarik
    dan berbobot juga mudah di pahami oleh pemua'''.split('\n')) # kita akan memisahkan string nya menjadi list setiap ada newline atau enter pada baris string tersebut

replaceText = 'ayo belajar coding di DiCoding'
print(replaceText.replace('coding', 'bahasa pemrogramman')) # kita akan mengubah kata coding menjadi bahasa pemrigramman

print('AKU TEXT UPPERCASE'.isupper()) # mengecek apakah text atau string nya itu uppercase
print('AKU TEXT UPPERCASE'.islower()) # mengecek apakah text atau string nya itu lowercase
print('dicoding'.isalpha()) # mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet
print('dicoding123'.isalnum()) # mengembalikan nilai True jika karakter dalam string adalah alfanumerik