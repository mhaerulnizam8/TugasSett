# Daftar kata spam menggunakan set
kata_spam = {"promo", "diskon", "hadiah", "gratis", "menang"}

# Input email dari user
email = input("Masukkan isi email: ")

# Ubah email menjadi huruf kecil lalu pecah menjadi kata-kata
kata_email = set(email.lower().split())

# Cari kata yang cocok
spam_terdeteksi = kata_spam.intersection(kata_email)

# Cek hasil
if spam_terdeteksi:
    print("Email kemungkinan SPAM")
    print("Kata spam ditemukan:", spam_terdeteksi)
else:
    print("Email bukan spam")
