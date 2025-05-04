print("Bugün kaç km bisiklet sürdün?")
#input içinde kullanıcıdan alınan tüm veriler string formatında olur.
km = input()
mil = float(km) * 0.621371192
mil = round(mil, 2)
print(f"Bugün sürdüğün {km} kilometrelik sürüşün karşılığı {mil}")

#round(yuvarlanacak şey, kaç haneye yuvarlanacak)