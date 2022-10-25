# T.Lehtsalu
# 25.10.2022
# Harjutus06

# Faili avamine
minu_fail = open("poliitikud.txt", "r")

# faili sisu kuvamine
for rida in minu_fail:
    print(rida, end=" ")


# faili sulgemine
minu_fail.close
