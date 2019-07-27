import math
string = ""
bar = 1

x = int(input("Masukkan angka :"))

# Looping Baris
while bar <= x:
	kol = x
	# Looping Kolom
	while kol > 0:
            if(kol == 1):
                string = string + " * "
            elif(kol == x):
                string =string + " * "
            elif(bar == math.ceil(x/2)):
                string = string + " * "
            else:
                string = string + " = "
            kol = kol - 1

	string = string + "\n"
	bar = bar + 1
print (string)
