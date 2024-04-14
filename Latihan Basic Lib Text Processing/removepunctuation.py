import string

kalimat = "Ini &adalah [contoh] kalimat? {dengan} tanda. baca?!!"
translator = str.maketrans("", "", string.punctuation)
hasil = kalimat.translate(translator)
hasil = hasil.replace("  ", " ")  # Mengganti dua spasi berturut-turut dengan satu spasi
hasil = hasil.strip()  # Menghapus spasi ekstra di awal dan akhir kalimat
print(hasil)
