from ogrenci import Ogrenci
from not_islemleri import (
    not_kontrol,
    sinif_ortalamasi,
    en_basarili_ogrenci
)

ogrenciler = []


while True:
    print("\n=== ÖĞRENCİ NOT TAKİP SİSTEMİ ===")
    print("1 - Öğrenci Ekle")
    print("2 - Öğrencileri Listele")
    print("3 - Sınıf Ortalaması")
    print("4 - En Başarılı Öğrenci")
    print("5 - Öğrenci Ara")
    print("6 - Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        ad = input("Öğrenci adı: ")
        numara = input("Öğrenci numarası: ")

        yeni_ogrenci = Ogrenci(ad, numara)

        not_sayisi = int(input("Kaç adet not girilecek: "))

        for i in range(not_sayisi):
            while True:
                notu = int(input(f"{i + 1}. notu girin: "))

                if not_kontrol(notu):
                    yeni_ogrenci.not_ekle(notu)
                    break
                else:
                    print("Geçersiz not! 0-100 arasında giriniz.")

        ogrenciler.append(yeni_ogrenci)
        print("Öğrenci başarıyla eklendi.")

    elif secim == "2":
        if len(ogrenciler) == 0:
            print("Henüz öğrenci eklenmedi.")
        else:
            print("\n=== ÖĞRENCİ LİSTESİ ===")

            for ogrenci in ogrenciler:
                ogrenci.bilgileri_goster()

    elif secim == "3":
        ortalama = sinif_ortalamasi(ogrenciler)
        print(f"Sınıf Ortalaması: {ortalama:.2f}")

    elif secim == "4":
        ogrenci = en_basarili_ogrenci(ogrenciler)

        if ogrenci is None:
            print("Henüz öğrenci bulunmamaktadır.")
        else:
            print("\n=== EN BAŞARILI ÖĞRENCİ ===")
            ogrenci.bilgileri_goster()

    elif secim == "5":
        aranan_numara = input("Aranacak öğrenci numarası: ")

        bulundu = False

        for ogrenci in ogrenciler:
            if ogrenci.numara == aranan_numara:
                ogrenci.bilgileri_goster()
                bulundu = True
                break

        if not bulundu:
            print("Öğrenci bulunamadı.")

    elif secim == "6":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Hatalı seçim yaptınız!")
