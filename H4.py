# T.Lehtsalu
# 17.10.2022
# Harjutus04
import random

#ruutude ja kuupide tabel
number=1
for i in range (1,11):
    print(number,end="  ")
    print(number**2,end="  ")
    print(number**3,end="  ")
    print()
    number+=1

#pank
kontoraha = 10000
intress = 0.05 #5%
aastad = 6
x=1
for i in range (aastad):
    print(f"Sul on raha pangas {x} aastat")
    print(f"arvel on{kontoraha}")
    kontoraha+=kontoraha*intress
    x+=1

#arvamismäng
loop = 1

while loop==1:
    arv = random.randint(1,10)
    print(arv) #testimiseks
    for i in range(3):
        pakkumine = int(input("Arva arv 1-10: "))
        if pakkumine==arv:
            print("LETS GOOOO")
            break
        else:
            print("Better luck next time buddy")
    loop = int(input("Jätka 1/0: "))
print("Game over")
        

#korrutustabel
arv = 5
for i in range(10):
    print(f"{arv} x {i} = {arv*i}")


#paarisjapaaritu
for i in range(1,10):
    if i%2==0:
        print(f"{i} paaris ")
    else:
        print(f"{i} paaritu")
    
    

#loto
for i in range(5):
    print(random.randint(0,9),end="")

# Jalgpalli meeskond

sugu = input("\nTeie sugu: ")
if sugu=="mees":
    vanus = int(input("Teie vanus: "))
    if 16<=vanus<=18:
        print("Kõlbate tiimi")
else:
    print("Headaega")

#tärnid

print()
x=1
for i in range (5):
    print("* "*5)
    
print()
for i in range (5):
    print("* "*x)
    x+=1
    
print()
y=5
for i in range (5):
    print("* "*y)
    y-=1


# müük
hind = float(input("Sisesta toote hind: "))
if hind>10:
    print("soodustus 20%")
if hind<10:
    print("soodustus 10%")

# juubel
sp = "5.6.2000"
vanus = 2022-int(sp.split(".")[2])
if vanus%5==0:
    print("juubel")
else:
    print("ei ole juubel")

# matem
a,b = 10,20
tehe = input("Vali tehe (+ - * /): ")
if tehe=="+":
    vastus = a + b
elif tehe=="-":
    vastus = a - b

else:
    vastus = "n/a"
print(f"{a} {tehe} {b} = {vastus}")
# ruut
a,b = 10,20
if a==b:
    print(f"{a} ja {b} teevad kokku ruudu")
else:
    print(f"{a} ja {b} teevad kokku ristküliku")
 
 
