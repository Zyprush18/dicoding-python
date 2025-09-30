# OOP (Object Oriented Programming)
print('===================== Mobil =======================')
class Mobil:
    # attribute kelas
    warna = 'biru'


# object
avanza1 = Mobil()
print(avanza1.warna)

avanza2 = Mobil()
print(avanza2.warna)

# mengubah value dari attribute kelas warna
Mobil.warna = 'merah'
print(avanza1.warna)
print(avanza2.warna)

'''
    hasil dari mengubah value attribute kelas warna pada class mobil itu merupakan kelmahan dari attribute jenis kelas tersebut
    oleh karena itu kita bisa menggunakan attribute instance yang namanya class constructor untuk menaganani nya.

    class constructor adalah sebuah fungsi khusus dalam Python yang digunakan untuk menentukan nilai awal atau kondisi awal dari suatu kelas.
'''

print('\n===================== Motor =======================')
class Motor:
    # attribute instance
    def __init__(self,warna,merek,max_kecepatan):
        self.warna = warna
        self.merek = merek
        self.max_kecepatan = max_kecepatan

motr1 = Motor('biru','Yamaha', 300)
motor2 = Motor('abu-abu','Honda', 150)
print(motr1.warna)
print(motr1.merek)
print(motr1.max_kecepatan)

print(motor2.warna)
print(motor2.merek)
print(motor2.max_kecepatan)


# ubah attribute motor nya
motr1.warna = 'hitam'

print(motr1.warna)
print(motor2.warna)

'''
    ketika kita menggunakan attribute instance kemudian kita melakukan perubahan pada atrribute warna,contohnya:
        Motor.warna = 'biru'
    hal tersebut tidak akan berfungsi alias object apapun yang makai kelas tersebut dan memakai attribute warna tersebut tidak akan berubah menjadi biru.
    Hal ini karena pada kelas yang kita buat tidak memiliki atribut kelas, sedangkan sintaks Mobil.warna = "Hitam" bertujuan untuk mengubah jenis atribut kelas. 
'''

print('\n=============== decorator =================')

# decorator
def mydecoraor(func):
    def wrapper():
        print('sebelum fungsi di eksekusi')
        func()
        print('sesudah fungsi di eksekusi')
    return wrapper

# dekorasi dengan decorator
@mydecoraor
def sayHello():
    print('Hello World!')
    
sayHello()

'''
    Dekorator adalah fungsi dalam Python yang mengembalikan fungsi lain, biasanya diawali dengan sintaks "@" di awal. 
    Dekorator sangat berguna untuk menambahkan fungsionalitas tambahan pada suatu fungsi atau metode tanpa harus mengubah kode asli dari fungsi tersebut.
'''



print('\n================= Mobil Sport =================')
class MobilSportNoNos:
    # attribute instance
    def __init__(self,warna,merek,kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    # metode dari objek (object method)
    def tambah_kecepatan(self):
        self.kecepatan += 10

    def kurang_kecepatan(self):
        self.kecepatan -= 10

    # metode secara statis (statis method)
    @staticmethod
    def klakson():
        print('prit prit prit')
    
    # metode dari kelas (class method)
    @classmethod
    def Rem(*args):
        print(args)
        print('mobil berhenti')

supra = MobilSportNoNos('biru','supra',100)
print('sebelum tambah keceptan,kecepatan berada pada kecepatan: ',supra.kecepatan) # belum menambah kecepatan

supra.tambah_kecepatan() # menambah kecepatan
print('sesudah menambah keceptan,kecepatan berada pada kecepatan: ',supra.kecepatan) 

# memangil static method
MobilSportNoNos.klakson()
'''
    Static method adalah fungsi atau method pada sebuah kelas yang bersifat statis. 
    Artinya, metode atau fungsi ini bersifat independen dan tidak terikat pada instance kelas. 
    Metode ini dapat dianggap seperti kita membuat fungsi seperti biasa, tetapi didefinisikan dalam kelas sehingga ini menjadi perilaku untuk kelas tersebut. 
'''

# memanggil class method
MobilSportNoNos.Rem()
'''
    Metode terakhir adalah class method yang termasuk jenis metode cukup spesial dalam Python. 
    Jika object method identik dengan parameter self yang merujuk pada objek, class method juga memerlukan sebuah parameter yang merujuk pada kelas.
    Penamaan cls merupakan kesepakatan bersama dari programmer Python untuk memudahkan pembacaan kode. Anda dapat mengganti namanya, tidak harus cls.
    Ini adalah parameter wajib dalam menggunakan dekorator @classmethod.

    Pada contoh kode di atas, fungsi Rem() menggunakan variadic positional parameter, yakni *args untuk melihat argumen yang diterima oleh fungsi tersebut. 
    Perhatikan lebih baik output-nya, kode di atas menerima sebuah parameter, 
    yakni kelas MobilSport walaupun ketika pemanggilan fungsi Rem() kita tidak memberikan argumen apa pun.
    Ini membuktikan bahwa ketika Anda menggunakan class method, Python akan secara otomatis menambahkan kelas tersebut sebagai argumen pertama.
'''


# inheritance (pewarisan)
print('\n============== Inheritance ===================')
class MobilSportNos(MobilSportNoNos):
    def Nos(self):
        self.kecepatan += 60

    #override / menimpa method yang sudh ada pada class mobil sport no nos 
    def tambah_kecepatan(self):
        self.kecepatan += 30

    # super -> ini kayak kita ingin menimpa method yang sudah ada pada class induk cumn kita tidak ingin merubah code yang sudah ad
    def kurang_kecepatan(self):
        super().kurang_kecepatan()
        print('Kecepatan Anda menurun')

# class mobil sport no nos
supra_bapak = MobilSportNoNos('merah','Yamaha', 900)
print(supra_bapak.kecepatan)
supra_bapak.tambah_kecepatan()
print(supra_bapak.kecepatan)

# class monil sport nos -> inheritance dari class mobil sport no nos
supra_kakek = MobilSportNos('biru','Ducati', 1000)
print(supra_kakek.warna)
print(supra_kakek.merek)
print(supra_kakek.kecepatan) # belum nyalain nos
supra_kakek.tambah_kecepatan() # menambahkan keceptan mengguanakan method yang telh di override
print(supra_kakek.kecepatan)
supra_kakek.Nos() # menyalakan nos / menambah kecepatan
print(supra_kakek.kecepatan)
supra_kakek.kurang_kecepatan()
print(supra_kakek.kecepatan)
