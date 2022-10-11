#T.Lehtsalu
#11.10.22
#Harjutus02
import math

#kütusekulu
# 400km, 24liitrit


#arvusüsteemid
#bin hex

#kasutaja sisesta minutid
#leian tunnid
#leian minutid
#väljastan tulemuse
minutid = int(input("sisesta minutid: "))
h = minutid//60
m = minutid%60
print("vastus on:",h,":",m)


#ajateisendus
# täisarvuline jagamine //
#jääk %

print(72%60)




#hypotenuus
a,b = 16,9
c = round(math.sqrt(pow(a,2)+pow(b,2)),2)
print("Hüpotenuus on",c)
#18,36


#rulluisutajad
#11,96

#Pitsa
#4,73?


#toote hind
hind = 36.75
ale = 0.4
kogus = 3
summa = round((hind-(hind*ale))*kogus,2)
print(kogus,"toote hind on",summa,"€")


#kolmnurga ümbermõõt
a,b,c = 30,30,30
p=a+b+c
print("Kolmnurga ümbermõõt on:",p)