import random 

print("TKM OYUNU")
print("...Taş...")
print("...KAĞIT...")
print("...MAKAS...")

p1 = input("oyuncu 1: taş, kağıt ya da makas yaz-->").lower()

x= random.randint(1,3)
if x == 1:
    bilg="taş"
elif x == 2:
    bilg="kağıt"
else:
    bilg="makas"
    
print(f"bilgisayar {bilg} oynadı.")

if x ==  bilg:
    print("berabere kaldınız")
elif x == "taş" and bilg == "kağıt":
    print("bilgisayar kazandı")
elif x == "taş" and bilg == "makas":
    print("oyuncu 1 kazandı")
elif x == "kağıt" and bilg == "makas":
    print("oyuncu 2 kazandı")
elif x == "kağıt" and bilg == "taş":
    print("oyuncu 1 kazandı")
elif x == "makas" and bilg == "taş":
    print("oyuncu 2 kazandı")
elif x == "makas" and bilg == "kağıt":
    print("oyuncu 1 kazandı")
else:
    print("uppps! yanlış bir şey girdiniz.")
