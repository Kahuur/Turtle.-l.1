# T.Lehtsalu
# 25.10.2022
# Harjutus06

# Faili avamine
minu_fail = open("poliitikud.txt", "r")

# faili sisu kuvamine
for rida in minu_fail:
    print(rida, end=" ")
 
print()
minu_fail = open("s6pru_l6ustaraamatus.txt", "r")



#reformikad
reformikad = 0
kesikud = 0
erakonnad = []
for i in minu_fail.readlines():
    enimi,pnimi,er,palk=i.split(" ")
    if er=="KE":
        kesikud+=1
    if er=="RE":
        reformikad+=1
    if er not in erakonnad:
        erakonnad.append(er)
              
print(f"Reformikaid kokku: {reformikad}")
print(f"Kesikuid kokku: {kesikud}")
print(f"Erakondi kokku: {len(erakonnad)}")
