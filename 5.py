# data_1 = [['a','b','c','d'],['g','e','f']]
# data_2 = [['g','h','i','j'],['a','c','e','b','d'],['g','e','f']]
# tes1 = sorted(data_1, key=len)
# tes2 = sorted(data_2, key=len)
#
# z = sorted(tes1[0])
# new = []
# i = 0
# while i <= len(tes1)-1:
#     z = sorted(tes1[i])
#     new.append(z)
#     i = i + 1
# print(new)
#
# new2 = []
# i2 = 0
# while i2 <= len(tes2)-1:
#     z2 = sorted(tes2[i2])
#     new2.append(z2)
#     i2 = i2 + 1
# print(new2)

data = str(input("masukan kalimat mu: "))
r = data.split()

i = 0
arr=[]
while i <= len(r)-1:
    z = ''.join(r[i])
    # print(z)
    t = ','.join(z)
    list = t.split (",")
    arr.append(list)

    i=i+1

d = 0
kosongan = []
while d <= len(arr)-1:
    m = sorted(arr[d])
    kosongan.append(m)
    d=d+1

kosongan = sorted(kosongan, key=len)
print(kosongan)
# t = list(r[0])
# i = 0
# arr = []
# while i <= len(r)-1:
#     arr1 = []
#     split_ = r[i].split()
#     indexin = list(str(r[i]))
#     indexin.sort()
#     join_dulu = ','.join(indexin)
#     arr1.append(join_dulu)
#     arr.append(arr1)
#
#     i = i +1
# print(arr)


# new = []
# n = 0
# while n <= len(arr)-1:
#     z = sorted(arr[n])
#     new.append(z)
#     n = n + 1
# print("hasil sorting adalah : " + str(new))
