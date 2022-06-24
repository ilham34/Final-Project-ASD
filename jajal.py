import data as d
import datetime as dt

#komentar
def cariLurus(wadah, data):
    n = len(wadah)
    l = len(wadah[0])
    t = []
    for i in range(n):
        for j in range(l):
            if wadah[i][j] == data:
                t.append([True, i,j])
    if t == []:
        return False
    else:
        return t
    

user = input("Masukkan lokasi : ")
print(cariLurus(d.data, user))
##print(len(d.data[0]))

# NO 2
tgl = int(input("Masukkan tanggal : "))
bln = int(input("Masukkan bulan : "))
tahun = int(input("Masukkan tahun : "))
jam = int(input("Masukkan jam : "))
menit = int(input("Masukkan menit : "))

val = dt.datetime(tahun, bln, tgl, jam, menit)
print(cariLurus(d.data, val))