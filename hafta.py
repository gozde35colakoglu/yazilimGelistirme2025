#listeler=["yönetim","bilisim","sistemleri"]
#demetler=("yönetim","bilisim","sistemleri")
#print(dir(listeler))
#print(dir(demetler))
#sözlükler (dictionary)
#sözlükler={"isim":"ali","soyisim":"yilmaz
#listelerede veri yapısı index kullanıyorduk
#listelerde de index kullanıyoruz ama sözlüklerde key kullanıyoruz
# 0 1 2
liste=[15,14,12]
liste[0]
#key value
#associative array
sozlukler={anahtar1:deger1,anahtar2:deger2}
sozlukler["anahtar1"]
gunler={0:"pazartesi",1:"salı",2:"çarşamba",3:"perşembe",4:"cuma"}
musteriler={"gozde colakoglu":{"dogum yeri":"izmir","meslek":"iş analisti"},
            "ayşe yilmaz":{"dogum yeri":"istanbul","meslek":"sporcu"}}

print(musteriler["gozde colakoglu"])
k=musteriler.keys()
for i in k:
    print(i)

v=musteriler.values()
for i in v:
    print(i)

#module

musteri_adi="gozde"
musteri_soyadi="colakoglu"
urunler=["civata","vida","kablo"]
         def karHesapla ()
