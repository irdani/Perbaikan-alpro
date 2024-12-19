#kode yang sudah diperbaiki
import math

def hitung_luas_lingkaran(jari_jari):
    """Fungsi untuk menghitung luas lingkaran"""
    luas = math.pi * jari_jari**2
    return luas

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

luas_lingkaran = hitung_luas_lingkaran(jari_jari)
print("Luas lingkaran adalah:", luas_lingkaran)