import statistics

print('Statistika Data Tunggal')

#UNTUK MENGISI DATA PISAHKAN DENGAN SPASI BUKAN KOMA CONTOH (4 2 5 5 6 6)
data = list(map(int, input("Data: ").split()))

mean = statistics.mean(data)

median = statistics.median(data)

modus = statistics.multimode(data)

print("\nHasil Perhitungan:")
print("Data  :", data)
print("Mean  :", mean)
print("Median:", median)
print("Modus :", modus)