import data as d
import datetime as dt
from random import randint

a = d.data
def quickSort(a,idx):
    if len(a) < 2:
        return a
    low, same, high = [], [], []
    pivot = a[randint(0, len(a) - 1)][idx]
    for i in a:
        if i[idx] < pivot:
            low.append(i)
        elif i[idx] == pivot:
            same.append(i)
        elif i[idx] > pivot:
            high.append(i)
    return quickSort(low,idx) + same + quickSort(high,idx)

no1 = quickSort(a,2)
no2 = quickSort(a,3)

def binSe(a, target,z,x):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid][x] < target:
            low = mid + 1
        elif a[mid][x] > target:
            high = mid - 1
        else:
            if z == 1:
                if mid - 1 < 0:
                    return mid
                if a[mid - 1][x] != target:
                    return mid
                high = mid - 1
            elif z == 2:
                if mid + 1 > (len(a)-1):
                    return mid
                if a[mid + 1][x] != target:
                    return mid
                low = mid + 1
    return False


def cari(awal, akhir, z):
    if awal != False and akhir != False:
        for i in range(awal, akhir + 1):
            print(True, (i, z))
    else:
        print(awal)    

# NO 1
##user = input("Masukkan lokasi : ")
##awal = binSe(no1, user, 1, 2)
##akhir = binSe(no1, user, 2, 2)
##
##cari(awal, akhir, 2)

# NO 2
tgl = int(input("Masukkan tanggal : "))
bln = int(input("Masukkan bulan : "))
tahun = int(input("Masukkan tahun : "))
jam = int(input("Masukkan jam : "))
menit = int(input("Masukkan menit : "))

val = dt.datetime(tahun, bln, tgl, jam, menit)
awal = binSe(no2, val, 1, 3)
akhir = binSe(no2, val, 2, 3)

cari(awal, akhir, 3)
