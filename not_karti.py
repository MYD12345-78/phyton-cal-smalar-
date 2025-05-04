
not_defteri = float(input("sınavdan aldığın not ne?"))
if 0 <= not_defteri <= 100:

 if not_defteri >=90 :
     print("A aldın")
 elif not_defteri >=80 :
     print("B aldın ")
 elif  not_defteri >=70 :
     print("C aldın")
 elif not_defteri >=60 :
     print ("D aldın")
 elif not_defteri >=50 :
    print ("E aldın")
 else :
  print("F ile kaldın")
else:
    print("bu bir sınav notu değil!!")