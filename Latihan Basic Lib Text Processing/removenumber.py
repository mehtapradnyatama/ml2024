import re

kalimat = "Berikut ini adalah 5 negara dengan pendidikan terbaik di dunia adalah Korea Selatan, Jepang, Singapura, Hong Kong, dan Finlandia."

hasil = re.sub(r"\d+|adalah", "", kalimat)
hasil = re.sub(r"\s+", " ", hasil)  # Menghapus spasi ganda yang mungkin tersisa
hasil = hasil.strip()  # Menghapus spasi ekstra di awal dan akhir kalimat
print(hasil)
