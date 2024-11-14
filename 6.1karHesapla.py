def gelirHesapla(finans, kira, pazar):
    gelir = finans + kira + pazar
    return gelir

def giderHesapla(finans, muh, maas):
    gider = finans + muh + maas  # gider hesaplanmalı
    return gider  # gider döndürülmeli

def karHesapla(gelir, gider):
    kar = gelir - gider
    if kar > 0:
        print("şirket kardadır")
    elif kar < 0:
        print("şirket zarardır")
    else:
        print("şirket karı sıfırdır")

# Kullanıcıdan giriş almak için ana akış
finans_gelir = int(input("finans gelir: "))
kira_gelir = int(input("kira gelir: "))
pazar_gelir = int(input("pazar gelir: "))
finans_gider = int(input("finans gider: "))
muh_gider = int(input("muh gider: "))
maas_gider = int(input("maas gider: "))

gelir = gelirHesapla(finans_gelir, kira_gelir, pazar_gelir)
gider = giderHesapla(finans_gider, muh_gider, maas_gider)
karHesapla(gelir, gider)