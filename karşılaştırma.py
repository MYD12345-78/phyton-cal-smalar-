# # verilen iki sayısal değerin hangisinin daha küçük veya büyük olduğunu 
# # ya da eşit olup olmadığını bulduran bir program yazalım

x = int(input("bir x sayısı giriniz: "))
y = int(input("bir y sayısı giriniz: "))

# #conditiaul log1

# if x > y:
#     print(f"{x} sayısı {y}  sayısından büyüktür.")
     
# if x < y:
#     print(f"{x} sayısı {y}  sayısından küçüktür.")
    
# if x == y:
#     print(f"{x} sayısı {y}  sayısına eşittir.")

if x > y:
 print(f"{x} sayısı {y}  sayısından büyüktür.")
 
elif x < y:
 print(f"{x} sayısı {y}  sayısından küçüktür.")
 
else:
    print(f"{x} sayısı {y}  sayısına eşittir.")
    
    #if elif else komutları arasında ki ilgiyi anlayabilirsiniz
    #sonda ki iki noktaları unutmamalısınız
    #içerden yazma olayını unutmayınız