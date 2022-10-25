#T.Lehtsalu
#25.10.2022
#Harjutus05

#Duplikaadid

jrk = 1
õpilased = ["Juhan", "Kati", "Maarja", "Mario", "Mario", "Mati"]

for õpilane in õpilased:
    print(f"{jrk}. {õpilane}")
    jrk+=1
    
õpilased.remove("Mario")
print(õpilased)


#Õpilased

jrk = 1
õpilased = ["Juhan", "Kati", "Maarja", "Mario", "Mati"]

for õpilane in õpilased:
    print(f"{jrk}. {õpilane}")
    jrk+=1
remove_õpilane = input("Mario")

if remove_õpilane in õpilane:
    õpilased.remove(remove_õpilane)
    print("Nimekirjast eemaldatud: remove Mario")
else:
    print("Sellist nime pole!")


    
#Nimede lisamine loendisse
  
nimed = []
for i in range(5):
    nimi = input("Lisa nimi: ")
    nimed.append(nimi)
    
print(f"Viimane nimi: {nimi}")
nimed.sort()
print(nimed)
