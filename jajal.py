import data as d

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
