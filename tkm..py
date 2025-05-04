#İLAYDA MAYDA 352331031

print("TKM OYUNU")
print("...Taş...")
print("...KAĞIT...")
print("...MAKAS...")

oyuncu1=input("oyuncu 1 hamleni yap:")

print("bakmak yok!!!\n\n"*20)

oyuncu2=input("oyuncu 2 hamleni yap:")
if oyuncu1 ==  oyuncu2:
    print("berabere kaldınız")
elif oyuncu1 == "taş" and oyuncu2 == "kağıt":
    print("oyuncu 2 kazandı")
elif oyuncu1 == "taş" and oyuncu2 == "makas":
    print("oyuncu 1 kazandı")
elif oyuncu1 == "kağıt" and oyuncu2 == "makas":
    print("oyuncu 2 kazandı")
elif oyuncu1 == "kağıt" and oyuncu2 == "taş":
    print("oyuncu 1 kazandı")
elif oyuncu1 == "makas" and oyuncu2 == "taş":
    print("oyuncu 2 kazandı")
elif oyuncu1 == "makas" and oyuncu2 == "kağıt":
    print("oyuncu 1 kazandı")
else:
    print("uppps! yanlış bir şey girdiniz.")