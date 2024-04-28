# MEHTA PRADNYATAMA
# A11.2022.14183
# LATIHAN 1

print("|| Python Basic ||")
print("Hello World!")
print("test\n")

print("|| Latihan The Print Function ||")
print("Hello, Python!")
print("Mehta")
print('Mehta')

print("|| Formatting with Special Character ||")
print()
print("Saya sudah sarapan tadi pagi\n dan nanti siang makan lagi") # \n artinya enter
print("Saya sudah sarapan tadi pagi\t dan nanti siang makan lagi") # \t artinya tab
print("nama saya \"Mehta\"")
print("\"")
print("satu.","dua.","tiga.")
print("Nama saya","Mehta", end=" ")
print("Salam")
print("satu","dua","tiga", sep=", ")

print("Latihan 4")
#sebelumnya 
#print("Programming","Essentials","in")
#print("Python")
#diubah menjadi : `Programming***Essentials***in...Python`
print("Programming","Essentials","in", sep="***", end="...")
print("Python"*2)
print("")

print("latihan 5") 
#sebelumnya ada 2 seperti ini didpu
#print("    *    "*2)
#print("   * *   "*2)
#print("  *   *  "*2)
#print(" *     * "*2)
#print("***   ***"*2)
#print("  *   *  "*2)
#print("  *   *  "*2)
#print("  *****  "*2)
#lalu didupilkasi menjadi seperti ini : 
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n"*2)
print()

print("Latihan 6")
print("2"*2) #berisi angka string dan interger
print(2*2) #ini berisi angka interger

print(type("2")) #menjelaskan class string
print(type(2)) #menjelaskan class interger 
print()

print("Latihan 7")
print(5, "mempunyai tipe", type(5)) #ini tipe interger 
print(.5, "mempunyai tipe", type(.5)) #ini tipe float
print()

print("Latihan 8")
print(10_000_00) #float dipashkan dengan "." dan "," diberi "_" agar mudah dibaca
print()

print("Latihan 9")
print("I'm Monty Python")
print()

print("Latihan 10")
print(True) #memberi tahu benar
print(False) #memberi tahu salah

print(4>2)
print(3>4)
print()

print("Latihan 11")
print()

print("Latihan 12") #untuk menampilkan output yang terpisah tiap baris
print('"I\'m"\n""learning""\n"""Python"""')

print("""
"I'm"
""learning""
\"""Python""\"
""")
print()

print("Latihan 13") #ini merupakan operator aritmatika
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3.)
print(2. ** 3)
print()

print(10 / 3)
print(10 // 3)

print(6 / 3.)
print(6 // 3.)

print(-4 + 4)
print(-4. + 8)
print()

print("Latihan 14") #urutan operator 
2 + 3 *5
print(9 % 6 % 2)
print(9 % 6)
print(3 % 2)

print(2 ** 2 ** 3)
print(2 ** 2)
print(2 ** 8)
print((5 * ((25 % 13)+100) / (2 * 13)) // 2)
print()

print("Latihan 15") #variabel
var = 1
print(var)
print()

a=2. #untuk menulis rumus c=\sqrt{a^2+b^2}
b=3.
c=(a**2 + b**2) ** 0.5
print("c = ", c)
print()

print("Latihan 16") #latihan variabel
# Variabel jumlah apel yang dimiliki oleh masing-masing orang
Darjo = 3
Darno = 5
Waginem = 6

# Menampilkan nama variabel dan jumlah apel setiap variabel dalam satu baris, dipisahkan dengan koma
print("Jumlah apel Darjo:", Darjo, ", Jumlah apel Darno:", Darno, ", Jumlah apel Waginem:", Waginem)

# Variabel baru yang berisi penjumlahan seluruh apel yang mereka miliki
totalApel = Darjo + Darno + Waginem
print("Total apel yang dimiliki:", totalApel)

# Mencoba otak-atik dengan operator aritmetik lainnya
# Misalnya, mencari rata-rata apel yang dimiliki
rata_rata_apel = totalApel / 3
print("Rata-rata apel yang dimiliki:", rata_rata_apel)
print()

print("Latihan 17") #latihan a simple converter
kilometer = 12.25
mil = 7.38

miles_to_kilometers = mil * 1.61
kilometers_to_miles = kilometer / 1.61

print(mil, "1 mil adalah", round(miles_to_kilometers, 2), "kilometer")
print(kilometer, "1 kilometer adalah", round(kilometers_to_miles, 2), "mil")
print()

print("Latihan 18") #Latihan operator and Expression
# Menggunakan input() untuk meminta pengguna memasukkan nilai x
x = float(input("Masukkan nilai x1: "))
xx = float(input("Masukkan nilai x2: "))
xxx = float(input("Masukkan nilai x3: "))

# Melengkapi kode untuk menyelesaikan persamaan
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
yy = 3 * xx**3 - 2 * xx**2 + 3 * xx - 1
yyy = 3 * xxx**3 - 2 * xxx**2 + 3 * xxx - 1

print("y1 =", y)
print("y2 =", yy)
print("y3 =", yyy)
print()

print("Latihan 19") #
var = 2
var = 3
print(var) # outputnya angka 3 
print()
print("Nama variabel mana yang ilegal?: ")
print("my_var")
print("m")
print("101")
print("averylongvariablename")
print("m101")
print("m 101")
print("Del")
print("del")  
print("Jadi jawabannya adalah : ")
print("101 karena dimulai dengan angka.")
print("m 101 karena mengandung spasi.")
print("Del karena merupakan kata kunci bawaan dalam Python.")
print("")
print("Apa Outputnya?")
a = '1'
b = "1"
print(a + b)
print("")
print("Apa outputnya?")
a = 6
b = 3
a /= 2 * b
print(a)
print("")

print("Latihan 20") #Latihan Memberi baris comment
#test
print("Hai...") 
#test1
#test2
print("")

print("Latihan 21") #How To Talk To Computer
print("Katakan sesuatu...")
sesuatu = input()
print("mmmmm", sesuatu, " Oke")
print("")

print("Latihan 22")#Latihan Type Casting
angka = float(input("Masukan Angka : "))
print("Pangkat duanya adalah ", angka**2)
print("")

print("Latihan 23")#Latihan Replication
print("+" + 10*"-" + "+")
print(("|" + 10*" " + "|\n") * 5, end="")
print("+" + 10*"-" + "+")
print("")

print("Latihan 24")#Latihan Simple dan output
# Masukkan nilai a dalam float
a = float(input("Masukkan nilai a: "))

# Masukkan nilai b dalam float
b = float(input("Masukkan nilai b: "))

# hitung hasil penambahan disini
penambahan = a + b

# hitung hasil pengurangan disini
pengurangan = a - b

# hitung hasil perkalian disini
perkalian = a * b

# hitung hasil pembagian disini
pembagian = a / b

# Menampilkan hasil
print("Hasil penambahan:", penambahan)
print("Hasil pengurangan:", pengurangan)
print("Hasil perkalian:", perkalian)
print("Hasil pembagian:", pembagian)
print("")

print("Latihan 25")#Operator dan expressions
import math

# Masukkan nilai x
x = float(input("Masukkan nilai x: "))

# Hitung nilai y menggunakan rumus yang diberikan
y = math.sqrt(1 / (x**2 + 1))

# Tampilkan hasil
print("x =", x)
print("y =", y)
print("")

print("\"I'm\"\n \"\"learning\"\"\n \"\"\"Python\"\"\"\n")

