print('123'.isdecimal()) # akan mengembalikan nilai true jika karakter dalam string hanya berisi angka atau numeric
print("         ".isspace()) # akan mengembalikan nilai true jika karakter dalam string hanya berisi whitespace(spasi,tab,newline dan karakter whitespace lainnya)
print("Dicoding Indonesia".istitle()) # akan mengembalikan nilai true jika kata di awal nya itu huruf kapital

# format string
text = "coding"
number_text = text.zfill(6) 
print(number_text)

'''
notes:
    Metode zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu. 
    Tujuan dari metode ini adalah membantu untuk memastikan bahwa sebuah angka atau nilai memiliki panjang tetap, 
    terutama ketika ingin menyimpan nilai dalam format yang konsisten.
    pada dasarnya seperti kyk minimal panjang dari si string nya ini berdasarkan parameter yang kita isi di zfillnya,
    jika panjang nya masih kurang dia bakal nambahin angka 0 di depannya sampai panjang nya sesuai dengan parameter yang kita masukkin
'''

print("Mariki coding bersama".rjust(30)) # buat jadi rata kanan -> parameter 30 itu bersifat seperti zfill() ->memastikan string nya panjang nya sesuai dengan parameter yang kita masukkan (panjang nya termasuk value stringnya)
print("Coding Aja".ljust(30)) # kebalikan dari rjust() -> alias buat jadi rata kiri
print("Dicoding".center(10,'-')) # rata kiri kanan dan bersifat zfill(),whitespace nya kita ubah jadi -
print(r"aku anak indonesia \nsehat dan kuat") # raw string-> dia akan menampilkan apapun input atau teks yang di berikan

# multiple
category,color,size = ['shoes','red','M']
print(category)
print(color)
print(size)

name = 'Dicoding Indonesia'
print(f"Hello, saya belajar coding di {name}")

x = 13
y = 3
print(x // y)

x = 1
y = 2
x,y = y,x # contoh code program one liner
print(x)
print(y)