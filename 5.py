data_1 = [['a','b','c','d'],['g','e','f']]
data_2 = [['g','h','i','j'],['a','c','e','b','d'],['g','e','f']]
tes1 = sorted(data_1, key=len)
tes2 = sorted(data_2, key=len)
# z = sorted(tes1, key=tes1.lower)
z = sorted(tes1[0])
# print(z)
# # print(tes1)
# print(tes2)
new = []
i = 0
while i <= len(tes1)-1:
    z = sorted(tes1[i])
    new.append(z)
    i = i + 1
print(new)

new2 = []
i2 = 0
while i2 <= len(tes2)-1:
    z2 = sorted(tes2[i2])
    new2.append(z2)
    i2 = i2 + 1
print(new2)
