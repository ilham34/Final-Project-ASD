import data as d
import datetime as dt
from random import randint

def quicksort(array, idx):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)][idx]
    for item in array:
        if item[idx] < pivot:
            low.append(item)
        elif item[idx] == pivot:
            same.append(item)
        elif item[idx] > pivot:
            high.append(item)
    return quicksort(low, idx) + same + quicksort(high, idx)

no1 = quicksort(d.data, 2)
no2 = quicksort(d.data, 3)

for i in no1:
    print(i)
print()
for a in no2:
    print(a)
##user = input("Masukkan lokasi : ")

# NO 2
##tgl = int(input("Masukkan tanggal : "))
##bln = int(input("Masukkan bulan : "))
##tahun = int(input("Masukkan tahun : "))
##jam = int(input("Masukkan jam : "))
##menit = int(input("Masukkan menit : "))

##target = dt.datetime(tahun, bln, tgl, jam, menit)
