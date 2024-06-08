def count_uppercase(text):
    uppercase_count = sum (1 for char in text if char.isupper())
    return uppercase_count

text1 = "Ini Adalah Contoh Text"
text2 = "SEMUA HURUF MEMAKAI KAPITAL"
text3 = "semua huruf tidak memakai kapital"

print(f"Jumlah Huruf Besar Dalam Text 1 '{text1}' adalah : {count_uppercase(text1)}")
print(f"Jumlah Huruf Besar Dalam Text 2 '{text2}' adalah : {count_uppercase(text2)}")
print(f"Jumlah Huruf Besar Dalam Text 3 '{text3}' adalah : {count_uppercase(text3)}")