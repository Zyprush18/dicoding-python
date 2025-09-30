class kalkulator:
    def __init__(self, angka1,operator,angka2):
        self.angka1 = int(angka1)
        self.operator = operator
        self.angka2 = int(angka2)
    
    def penjumlahan(self):
        return self.angka1 + self.angka2
    
    def pengurangan(self):
        return self.angka1 - self.angka2
    
    def perkalian(self):
        return self.angka1 * self.angka2
    def pembagian(self):
        return self.angka1 / self.angka2

print('============== kalkulator yang sangat sederhana ==================')
angka1 = input('Masukkan Angka pertama: ')
angka2 = input('Masukkan Angka kedua: ')
operator = input('''
operator yang bisa di gunakan:
    1. + -> untuk penjumlahan
    2. - -> untuk pengurangan
    3. * -> untuk perkalian
    4. / -> untuk pembagian            
masukkan operator yang ingin anda gunakan: ''')

calc = kalkulator(angka1,operator,angka2)
if calc.operator == '+':
    print(f'hasil dari penjumlahan angka {calc.angka1} dengan angka {calc.angka2} adalah {calc.penjumlahan()}')
elif calc.operator == '-':
    print(f'hasil dari pengurangan angka {calc.angka1} dengan angka {calc.angka2} adalah {calc.pengurangan()}')
elif calc.operator == '*':
    print(f'hasil dari perkalian angka {calc.angka1} dengan angka {calc.angka2} adalah {calc.perkalian()}')
elif calc.operator == '/':
    print(f'hasil dari pembagian angka {calc.angka1} dengan angka {calc.angka2} adalah {calc.pembagian()}')
else:
    print('Pilih Sesuai Instruksi untuk operator nya blokkk!')

print('arigatou ghozaimasu')