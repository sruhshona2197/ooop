class Transport:
    def __init__(self, nomi, tezlik):
        self.nomi = nomi
        self.tezlik = tezlik

class Velosiped(Transport):
    def __init__(self, nomi, tezlik, g_soni):
        super().__init__(nomi, tezlik)
        self.g_soni = g_soni

v = Velosiped('Trek', 30, 21)
print(v.nomi, v.tezlik, v.g_soni)




# 2
class Sozlama:
    til = 'uz'

s1 = Sozlama()
s2 = Sozlama()
Sozlama.til = 'en'
print(s1.til)
print(s2.til)


# 3
class Karta:
    def __init__(self, raqam):
        self.__raqam = raqam

    def __str__(self):
        return f'**** **** **** {self.__raqam[-4:]}'

k = Karta('1234567890123456')
print(k)



# 4
class Parol:
    def __init__(self, uzunlik=8):
        self.uzunlik = uzunlik
        self.kuchli = uzunlik >= 12

p1 = Parol()
p2 = Parol(16)
print(p1.kuchli)
print(p2.kuchli)


# 5
class Yozuvchi:
    def __init__(self, ism):
        self.ism = ism
        self.asarlar = []

    def yoz(self, asar):
        self.asarlar.append(asar)

y = Yozuvchi('Navoiy')
y.yoz('Xamsa')
y.yoz('Farhod va Shirin')
print(len(y.asarlar))



# 6
class Tovar:
    kategoriya = 'Oziq-ovqat'

t1 = Tovar()
t2 = Tovar()
t1.kategoriya = 'Kiyim'
print(Tovar.kategoriya)
print(t1.kategoriya)
print(t2.kategoriya)




# 7
class Test:
    qiymat = 5

print(Test.qiymat)
Test.qiymat = 99
print(Test.qiymat)

# 8
class Config:
    debug = False
    versiya = '1.0'

print(Config.__dict__['debug'])
print(Config.__dict__['versiya'])



# 9
class Box:
    count = 0

b1 = Box()
b2 = Box()
b3 = Box()
print(Box.count)



# 10
class Konteyner:
    def __init__(self):
        self._qiymat = 42

k = Konteyner()
print(k._qiymat)


# 11
class Forma:
    def tavsif(self):
        return 'Forma'

class Rang(Forma):
    def tavsif(self):
        return f'{super().tavsif()} + Qizil'

class Chegara(Rang):
    def tavsif(self):
        return f'{super().tavsif()} + Qalin'

c = Chegara()
print(c.tavsif())



# 12
class Toifa:
    def __init__(self):
        self.elementlar = []

t1 = Toifa()
t2 = Toifa()
t1.elementlar.append('a')
print(len(t1.elementlar))
print(len(t2.elementlar))



# 13
class Kalkulyator:
    def qoshish(self, a, b):
        return a + b

k = Kalkulyator()
print(k.qoshish(3, 7))




#14
class Mahsulot:
    def __init__(self, narx):
        self._narx = narx

    def get_narx(self):
        return f'{self._narx:,} so\'m'

m = Mahsulot(150000)
print(m.get_narx())


# 15
class Shakl:
    def yuza(self):
        return 'Hisoblanmadi'

class Kvadrat(Shakl):
    def __init__(self, t):
        self.t = t

    def yuza(self):
        return self.t ** 2

k = Kvadrat(5)
print(k.yuza())
