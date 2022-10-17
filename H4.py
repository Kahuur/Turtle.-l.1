# T.Lehtsalu
# 17.10.2022
# Harjutus04

# Jalgpalli meeskond


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