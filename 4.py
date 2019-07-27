x = str(input("Masukan string: "))
arr = []
x.split()
z= list(x)
param = ['a', 'i', 'u', 'e', 'o']
param2 = ['A', 'I', 'U', 'E', 'O']
print("list condition : " + str(z))
nilai = 0
i = 0

while i < len(z):
    n =0
    while n < len(param):
        if(z[i] == param[n]):
            # print(param[n])
            nilai = nilai+1
        elif (z[i] == param2[n]):
            nilai = nilai+1
        n=n+1
    i=i+1

print("huruf hidup berjumlah : " + str(nilai))
