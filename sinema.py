print("5 yaşından küçük çocuklar giremez.")
print("yaşınızı girin")
yaş=input()

yaş = int(yaş)
if yaş < 5:
    sonuç=5-yaş
    print(f" buraya {sonuç} tane daha doğum günü kutladıktan sonra girebilirsin")
elif 5<= yaş <=8 or yaş >=65:
    print("indirimli tarifeden yararlanacaksınız.")
else:
     print("iyi seyirler.")
