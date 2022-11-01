# T.Lehtsalu
# 01.11.2022
# Funktsioonid

import math

def kuup(a):
    print(f"Kuubi ruumala on {a**3}")
def kera(r):
    print(f"Kera ruumala on {4/3*math.pi*r**3}")
def koonus(r, h):
    print(f"Koonuse ruumala on {(math.pi*r**2*h)/3}")
def silinder(r, h):
    print(f"Silindri ruumala on {round(math.pi*r**2*h)}")

loop = 1
while loop == 1:
    print("************ LEIAME RUUMALA *****************")
    valik = int(input("1. Kuup/n2. Kera/n3. Koonus/n4. Siliner/n5. Välju/nTee valik 1-5: "))
    if valik ==1:
        a = int(input("Lisa kuubi üks külg: "))
        kuup(a)
    elif valik ==2:
        r = int(input("Lisa kera raadius: "))
        kera(r)
    elif valik ==3:
        r = int(input("Lisa koonuse raadius: "))
        h = int(input("Lisa koonuse kõrgus: "))
        koonus(r, h)
    elif valik ==4:
        r = int(input("Lisa silindri raadius: "))
        h = int(input("Lisa silindri kõrgus: "))
        silinder(r, h)
    elif valik ==5:
        loop = 0
    else:
        print("Sellist valikut pole!")





def tevita(nimi="tundmatu",keel="ge"):
    if keel=="et":
        print(f"Tere {nimi}")
    elif keel=="en":
        print(f"Hi {nimi}")
    else:
        print(f"Hallo {nimi}")
 
tevita() 
tevita("Mario","en")
