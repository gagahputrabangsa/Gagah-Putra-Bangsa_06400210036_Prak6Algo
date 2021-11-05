from math import *
print("@@@@@   @@@@@@   @@@@@   @@@@@@   @    @")
print("@       @    @   @       @    @   @    @")
print("@ @@@   @@@@@@   @ @@@   @@@@@@   @@@@@@")
print("@   @   @    @   @   @   @    @   @    @")
print("@@@@@   @    @   @@@@@   @    @   @    @\n")

def kecepatan(awal,percepatan,jarak):
    a=(sqrt(awal**2 + (2*percepatan*(jarak))))
    print("kecepatan awal=",awal,"percepatan=",percepatan,"jarak=",jarak,"hasil=",a)
    return a
    
awal=int(input("kecepatan awal= "))
percepatan=int(input("percepatan= "))
jarak=int(input("jarak ="))
kecepatan(awal,percepatan,jarak)