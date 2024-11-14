def gelirHesapla(finans,kira,pazar):
    gelir = finans + kira + pazar
    return gelir
def giderHesapla(finans,muh,maas):
    return gider
def karHesapla(gelir,gider):
    kar=gelir-gider
    if (kar>0):
        print("şirket kardadır")
    elif(kar<0):
        print("şirket zarardır")
    else:
        print("şirket karı sıfırdır")
gelir=gelirHesapla(450,650,850)
gider=giderHesapla(75,150,1050)
karHesapla(gelir,gider)