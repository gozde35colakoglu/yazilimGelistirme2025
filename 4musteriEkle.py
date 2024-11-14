#müşteri ekleme fonsiyonu
def musteriEkle(ad,soyad):
    print("müşteri adi:",ad)
    print("müşteri soyadi:",soyad)
#musteriEkle("gözde","colakoglu") buraya kadar çalıştırırsan ekranda müsteri adi gözde musteri soyadi: çolakoğlu olarak görürsün
#müşteriyi ekrandan giriş yaparak öğrenelim
ad=input("müşteri adi giriniz:")
soyad=input("müsteri soyadı giriniz:")
musteriEkle(ad,soyad)