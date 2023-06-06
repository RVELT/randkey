import random
import string

def sifre_olustur(uzunluk):
    karakteler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakteler)for _ in range(uzunluk))
    return sifre

uzunluk = int(input("Şifrenin uzunluğunu girin: "))
yeni_sifre = sifre_olustur(uzunluk)
print(f"Oluşturulan şifre: {yeni_sifre}")    