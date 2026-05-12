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
        return sum(self.notlar) / len(self.notlar)