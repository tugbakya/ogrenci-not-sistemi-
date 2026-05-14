class Ogrenci:
    def __init__(self, ad, numara):
        self.ad = ad
        self.numara = numara
        self.notlar = []

    def not_ekle(self, notu):
        self.notlar.append(notu)

    def ortalama_hesapla(self):
        if len(self.notlar) == 0:
            return 0

        toplam = sum(self.notlar)
        ortalama = toplam / len(self.notlar)
        return ortalama

    def harf_notu(self):
        ortalama = self.ortalama_hesapla()

        if ortalama >= 85:
            return "AA"
        elif ortalama >= 70:
            return "BB"
        elif ortalama >= 50:
            return "CC"
        else:
            return "FF"

    def bilgileri_goster(self):
        print("---------------------------")
        print(f"Öğrenci Adı: {self.ad}")
        print(f"Numara: {self.numara}")
        print(f"Notlar: {self.notlar}")
        print(f"Ortalama: {self.ortalama_hesapla():.2f}")
        print(f"Harf Notu: {self.harf_notu()}")
        print("---------------------------")