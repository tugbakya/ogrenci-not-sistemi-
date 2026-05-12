from ogrenci import Ogrenci

ogrenciler = []

while True:
    print("\n1- Öğrenci Ekle")
    print("2- Öğrencileri Listele")
    print("3- Çıkış")

    secim = input("Seçim: ")

    if secim == "1":
        ad = input("Öğrenci adı: ")
        numara = input("Numara: ")

        yeni_ogrenci = Ogrenci(ad, numara)

        not_sayisi = int(input("Kaç not girilecek: "))

        for i in range(not_sayisi):
            notu = int(input("Not gir: "))
            yeni_ogrenci.not_ekle(notu)

        ogrenciler.append(yeni_ogrenci)

    elif secim == "2":
        for ogrenci in ogrenciler:
            print("----------------")
            print("Ad:", ogrenci.ad)
            print("Numara:", ogrenci.numara)
            print("Ortalama:", ogrenci.ortalama_hesapla())

    elif secim == "3":
        print("Program kapandı.")
        break

    else:
        print("Hatalı seçim!")