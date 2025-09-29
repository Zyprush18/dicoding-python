# fungsi
def f(x):
    return 2*x

print(f(4))

'''
    contoh di atas merupakan implementasi fungsi dari metematika: f(x) = 2x ke fungsi pemrogramman menggunkan python
'''

# docstring fungsi -> membuat fungsi lebih mudah dipahami oleh programmer lain, kita bisa membuat dokumentasi berupa docstring
def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

'''
notes macam macam parameter di python:
    - positional of keyword parameter -> default fungsi dari si python
        contoh:
            def tambah(a,b)
            tambah(b=5,a=2) atau tambah(2,5)
    - positional only -> dimna fungsi ini cumn menerima argumen yang posisi nya sama dengan parameter yang di definisikan dan dia di tandai denga "/" pada akhir parameter nya
        contoh:
            def kurang(a,b, /)
            kurang(5,3) -> argumennya sesuai dengan parameter yang di definisikan
    - keywoard only -> dimna fungsi ini cumn menerima argumen yang sesuai dengan parameter yang di definisikan dan dia di tandai dengan "*" pada awal parameter nya
        contoh:
            def kali(*,a,b)
            kali(b=5,a=3)
    - variadic positional -> Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan menggunakan sintaks *args.
            def JumlahkanSemua(*args)
            JumlahkanSemua(1,2,3,4)
    - variadic keywoard -> Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi.Parameter ini ditentukan dengan menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya).
            def CekInfo(**kwargs)
            JumlahkanSemua(name="admin",address="jalan ini",no=083447)
'''
# lambda fngsi / anonim fungsi
funclambda = lambda x : 2 * x
print(funclambda(3))

nama = 'Dicoding'


# prosedur
def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

greeting("dicoding")