score = 80
if score == 100:
    print("Lulus")
elif score == 80:
    print('lumayan')
else:
    print('Tidak Lulus')

'''
notes:
    ython menganggap setiap nilai kosong (zero) dan null sebagai False. 
    Sebaliknya, nilai yang tidak kosong (non-zero) dan tidak null (non-null) akan bernilai True.
'''
# one liner if
if score == 100: print('Sempurna')
# one liner if else
print('lulus') if score == 100 else print('tidak lulus ki kanda')


lulus = True
kelulusan = ('Tidak lulus','Lulus') [lulus] # one liner if else v2 yang diman di dalam kurung itu param nya (jika kondisi nya salah,jika kondisi nya benar)[kondisi]  
print(kelulusan)

lists = [1,2,3,4,5,6,7,8,9,10]
for i in lists:
    print(i)

for x in range(10):
    print(x)

for v in range(1,10,2):
    print(v)


data = ['aku','belajar','di dicoding']
for i in data:
    print(i)

counter = 1
while counter <= 5:
    print(counter)
    counter+=1


for i in range(1,3):
    for j in range(1,3):
        print(i,j)


for i in range(2):
    print(f'perulanngan luar: {i}')
    for j in range(1,10):
        print(f'perulangan dalam: {j}')
        if j == 2: break

for d in 'Coding Aja':
    if d == ' ':break
    print(d)

for x in range(1,5):
    if x == 2: continue
    for y in range(1,5):
        if y == 2: continue
        print(f'ini nilai x:{x} dan ini nilai y: {y}')

num = [1,2,3,4,5]
# for else -> berguna untuk perulangan yang bersifat pencarian
for item in num:
    if item == 4:print('Angka Di temukan');break
else:
    print('Angka Tidak Di Temukan')
angka = 0
while angka < 3:
    print(angka)
    angka += 1
else:
    print('menjalankan kondisi while yang false')


n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")


f = 3
while f > 5:
    pass # digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.
else:
    print('nilai f tidak memenuhi kondisi')

p = [2,3,4,5]
q = []
for r in p:
    q.append(r**2)
print(q)

# one liner for alias list comprehension
s = [t**2 for t in p]
print(s)


# error exception handling
z = 0
try:
    print(1/z)
except:
    print('Woii Ngotak Dikit mana bisa angka di bagi dengan 0')

# try except lengkap
var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
except NameError:
    print("variable tidak di temukan ki")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")


# raise exception atau membuat error
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)