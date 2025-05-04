print ("istediğiniz herhangi bir sayı giriniz")
sayı=float(input())
if sayı != int(sayı):
    print("bu bir tam sayı değil!!")
else:
 if sayı % 2 == 0:
     print( "çift")
 else:
     print ( "tek")
  
