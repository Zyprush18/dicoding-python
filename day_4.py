import array
import numpy as np
import sys

# membuat array menggunakan library array
x = array.array("i",[1,2,3,4,5]) # membuat array bertipe integer dengan menyatakan "i" sebelum array
print(x)


"""
    Selepas berakhirnya semester genap, para guru dari SMA Dicoding perlu merekap semua nilai ujian akhir semester. 
    Salah satunya adalah guru matematika, guru tersebut perlu merekap nilai dari seluruh siswa yang ada di kelas IPA 1. 
    Guru tersebut membuat program menggunakan Python untuk mempermudah proses rekap nilai.
"""

nilai = [90,100,20,10,50,60,70,54,23,40]
print(nilai)
print(nilai[0])

"""
notes:
    dalam Python kita dapat mendeklarasikan array menggunakan dua cara. 
    Pertama dengan memanfaatkan list dan kedua menggunakan library Python.
"""

# default value in list
lists = [0 for i in range(10)]
print(lists)

# mengubah nilai dari default list/array
for i in range(10):
    lists[i] = i

print(lists)


# array sekuensial
var_arr = [1,2,3,4]
result_array = 0
for i in range(len(var_arr)):
    current_array = var_arr[i]
    next_index = i + 1 # agar si indeks nya di increment

    if next_index < len(var_arr):
        next_array = var_arr[next_index]
    else:
        next_array = None
    

    print(f'current value array : {current_array} and next value array: {next_array}')

    result_array += var_arr[i] 

print(result_array)
rata_rata = result_array / len(var_arr)
print(f'rata rata dari value array di atas adalah: {rata_rata}')

# latihan array -> mencari nilai terbesar (two pointer)
data_arry = [1,7,2,89,3,34,90,100,3004,4,2,5,8,100000]
left_pointer = data_arry[0]
for i in range(1,len(data_arry)):
    right_pointer = data_arry[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(f'nilai terbesar yang ada di dalam array tersebut adalah {left_pointer}')


# matrix
matrix_manual = [[1,2,3],[4,5,6],[7,8,9]] # array atau list di samping mirip dengan matrix dengan ordo 3x3
print(matrix_manual)

# buat matrix makai library numpy
matriks = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriks)


# mengecek ukuran memory yang di gunakan
print('ukuran memory matriks list adalah: ',sys.getsizeof(matrix_manual) * len(matrix_manual))
print('ukuran memori matriks numpy adalah: ', matriks.size * matriks.itemsize)

# deklarasi nilai default matriks menggunakan nested list dan nested for
matrics = [[0 for i in range(5)] for i in range(5)]
print(matrics)

# operasi matrix di kalikan dengan konstanta (nested list)
var_mat = [[5,0],[1,-2]]
def_mat = [[0 for i in range(2)] for i in range(2)]

for v in range(len(var_mat)):
    for w in range(len(var_mat[0])):
        def_mat[v][w] = var_mat[v][w] * 2

print("Ini adalah hasil dari perkalian matrix dengan nilai konstanta menggunakan nested list: ",def_mat)

# operasi matrix di kalikan dengan konstanta (library numpy)
mat_np = np.array([[5,0],[1,-2]]) * 2
print("Ini adalah hasil dari perkalian matrix dengan nilai konstanta menggunakan numpy: ",mat_np)

