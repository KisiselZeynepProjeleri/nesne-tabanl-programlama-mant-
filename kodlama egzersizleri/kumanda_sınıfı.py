import random
import time


class Kumanda():
    def __init__(self,tv_durum="kapalı",tv_ses=0,kanal_listesi=["trt"],kanal="trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_aç(self):
        if(self.tv_durum=="açık"):
            print("televizyon zaten açık")
        else:
            print("televizyon açılıyor....")
            self.tv_durum="açık"
    def tv_kapat(self):
        if(self.tv_durum=="kapalı"):
            print("televizyon zaten kapalı..")
        else:
            print("televizyon kanıyor")
            self.tv_durum="kapalı"
    def ses_ayarları(self):
        while True:
            cevap=input("sesi azalt '<'\nSesi Arttır'>'\nÇıkış:'çıkış'")

            if (cevap=='<'):
                if(self.tv_ses!=0):
                    self.tv_ses-=1

                    print(f"SES:{self.tv_ses}")
            elif(cevap=='>'):
                if(self.tv_ses!=31):
                    self.tv_ses+=1
                    print(f"SES:{self.tv_ses}")
            else:
                print(f"Ses güncellendi:{self.tv_ses}")
                break

    def kanal_ekle(self,kanal_ekle):
        print("Kanal Ekleniyor")
        time.sleep(2)#2 saniye bekletiyorum
        self.kanal_listesi.append(self.kanal_ismi)
        print("Kanal Eklendi.....")

    def rastgele_kanal(self):
        rastgele_index=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele_index]
        print(f"şu an ki kanal:{self.kanal}")

    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self)->str:
        return f"TV Durumu:{self.tv_durum}\nKanal Listesi:{self.kanal_listesi}\nŞu an ki Kanal:{self.kanal}"
    
kumanda=Kumanda()    
    

"""Televizyon Uygulaması


1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
"""


while True:

    işlem = input("İşlemi Seçiniz:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor...")
        break

    elif (işlem == "1"):
        kumanda.tv_ac()

    elif (işlem == "2"):
        kumanda.tv_kapat()

    elif (işlem == "3"):
        kumanda.ses_ayarları()

    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif (işlem == "5"):

        print("Kanal Sayısı:",len(kumanda))

    elif (işlem == "6"):
        kumanda.rastgele_kanal()

    elif (işlem == "7"):
        print(kumanda)

    else:
        print("Geçersiz İşlem......")
    
    