print("yaşınızı girin.")
yaş=input()

if yaş:
   
    if (int(yaş)>=18  and int(yaş) <=21 ):
     print("hem kampüse hem hastaneye girebilirsiniz.")
    else:
     print("sadece hastaneyi ziyaret edebilirsiniz.")
else:
    print("hiçbir şey girmediniz.")
    