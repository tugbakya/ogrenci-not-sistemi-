def not_kontrol(notu):
    if 0 <= notu <= 100:
        return True
    else:
        return False


def sinif_ortalamasi(ogrenciler):
    if len(ogrenciler) == 0:
        return 0

    toplam = 0

    for ogrenci in ogrenciler:
        toplam += ogrenci.ortalama_hesapla()

    return toplam / len(ogrenciler)


def en_basarili_ogrenci(ogrenciler):
    if len(ogrenciler) == 0:
        return None

    en_iyi = ogrenciler[0]

    for ogrenci in ogrenciler:
        if ogrenci.ortalama_hesapla() > en_iyi.ortalama_hesapla():
            en_iyi = ogrenci

    return en_iyi
