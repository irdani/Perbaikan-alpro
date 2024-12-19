#kode yang sudah diperbaiki
def hitung_jumlah(n):
    jumlah = 0
    for i in range(1, n+1):
        jumlah += i
    return jumlah

n = int(input("masukkan nilai n: "))

hasil = hitung_jumlah(n)
print("Jumlah bilangan dari 1 hingga", n , "adalah", hasil)
