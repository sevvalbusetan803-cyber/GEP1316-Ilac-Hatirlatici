import csv
from datetime import datetime

# Kayıtlı ilaç planlarını tutacak ana liste (İçinde sözlükler barındırır)
ilac_listesi = []


def saat_dogrula(saat_metni):
    """
    Kullanıcının girdiği saatin SS:DD formatında ve geçerli bir saat olup olmadığını kontrol eder.
    Hatalıysa False, doğruysa True döndürür.
    """
    try:
        datetime.strptime(saat_metni, "%H:%M")
        return True
    except ValueError:
        return False


def pozitif_tam_sayi_al(mesaj):
    """
    Kullanıcıdan 1 ile 6 arasında geçerli bir doz sayısı alır.
    Harf veya negatif/sıfır girilirse program çökmeden tekrar sorar.
    """
    while True:
        girdi = input(mesaj).strip()
        if girdi.isdigit():
            sayi = int(girdi)
            if 1 <= sayi <= 6:
                return sayi
            else:
                print("⚠️ Uyarı: Günlük doz sayısı 1 ile 6 arasında olmalıdır!")
        else:
            print("⚠️ Uyarı: Lütfen geçerli bir tam sayı giriniz (Örn: 2).")


def yeni_ilac_ekle():
    """
    Kullanıcıdan hasta/ilaç bilgilerini doğrularak alır ve listeye sözlük olarak ekler.
    """
    print("\n--- YENİ İLAÇ / TEDAVİ PLANI EKLE ---")
    
    # 1. Girdi ve Doğrulama: İlaç Adı (Boş bırakılamaz)
    while True:
        ilac_adi = input("1. İlaç Adı ve Dozu (Örn: Parol 500 mg): ").strip()
        if len(ilac_adi) >= 2:
            break
        print("⚠️ Uyarı: İlaç adı boş bırakılamaz ve en az 2 karakter olmalıdır!")

    # 2. Girdi ve Doğrulama: Açlık/Tokluk Durumu (Karar yapısı ile kontrol)
    while True:
        kullanim_sekli = input("2. Kullanım Şekli (Aç / Tok / Fark Etmez): ").strip().capitalize()
        if kullanim_sekli in ["Aç", "Tok", "Fark etmez"]:
            break
        print("⚠️ Uyarı: Lütfen sadece 'Aç', 'Tok' veya 'Fark etmez' yazınız!")

    # 3. Girdi ve Doğrulama: Günlük Doz Sayısı
    gunluk_doz = pozitif_tam_sayi_al("3. Günde kaç kez alınacak? (1-6): ")

    # 4. Girdi ve Doğrulama: İlk Doz Saati
    while True:
        ilk_saat = input("4. İlk doz saati (SS:DD formatında, örn: 08:00): ").strip()
        if saat_dogrula(ilk_saat):
            break
        print("⚠️ Uyarı: Geçersiz saat formatı! Lütfen SS:DD şeklinde giriniz (Örn: 09:30).")

    # Doz saatlerini otomatik hesaplama (24 saat üzerinden eşit aralıklarla)
    saat_parcalari = ilk_saat.split(":")
    baslangic_saat = int(saat_parcalari[0])
    baslangic_dakika = int(saat_parcalari[1])
    aralik = 24 // gunluk_doz

    doz_saatleri = []
    for i in range(gunluk_doz):
        yeni_saat = (baslangic_saat + i * aralik) % 24
        doz_saatleri.append(f"{yeni_saat:02d}:{baslangic_dakika:02d}")

    # Klinik uyarı notu (Karar yapısı: if / elif / else)
    if kullanim_sekli == "Aç":
        uyari_notu = "Yemeklerden en az 30-60 dakika önce bir bardak su ile alınız."
    elif kullanim_sekli == "Tok":
        uyari_notu = "Mide iritasyonunu önlemek için yemekten hemen sonra alınız."
    else:
        uyari_notu = "Öğün durumundan bağımsız olarak her gün aynı saatte alınız."

    # Veriyi sözlük (dictionary) yapısında saklama
    ilac_kaydi = {
        "ilac_adi": ilac_adi,
        "kullanim_sekli": kullanim_sekli,
        "gunluk_doz": gunluk_doz,
        "doz_saatleri": ", ".join(doz_saatleri),
        "uyari_notu": uyari_notu
    }

    ilac_listesi.append(ilac_kaydi)
    print(f"✅ '{ilac_adi}' tedavi planına başarıyla eklendi!")


def plani_listele_ve_kaydet():
    """
    Kayıtlı tüm ilaçları ekrana tablo biçiminde yazdırır ve CSV dosyasına kaydeder.
    """
    if not ilac_listesi:
        print("\nℹ️ Henüz kayıtlı bir ilaç planı bulunmamaktadır.")
        return

    print("\n" + "=" * 85)
    print(f"{'İLAÇ ADI':<22} | {'DURUM':<12} | {'DOZ':<5} | {'HATIRLATMA SAATLERİ':<25}")
    print("=" * 85)

    for kayit in ilac_listesi:
        print(f"{kayit['ilac_adi']:<22} | {kayit['kullanim_sekli']:<12} | {kayit['gunluk_doz']:<5} | {kayit['doz_saatleri']:<25}")
        print(f"   ↳ Eczacı Notu: {kayit['uyari_notu']}")
        print("-" * 85)

    # Sonuçları .csv dosyasına kaydetme
    dosya_adi = "tedavi_plani.csv"
    with open(dosya_adi, mode="w", newline="", encoding="utf-8-sig") as dosya:
        alan_adlari = ["ilac_adi", "kullanim_sekli", "gunluk_doz", "doz_saatleri", "uyari_notu"]
        yazici = csv.DictWriter(dosya, fieldnames=alan_adlari, delimiter=";")
        yazici.writeheader()
        yazici.writerows(ilac_listesi)

    print(f"💾 Tablo '{dosya_adi}' dosyasına başarıyla kaydedildi.")


def ana_menu():
    """
    Kullanıcı çıkış yapana kadar çalışan ana menü döngüsü.
    """
    print("🏥 ECZANE & KLİNİK TEDAVİ SAATLERİ PLANLAYICI (2030)")
    while True:
        print("\nLütfen yapmak istediğiniz işlemi seçiniz:")
        print("1 - Yeni İlaç / Tedavi Ekle")
        print("2 - Tedavi Planını Görüntüle ve CSV Olarak Kaydet")
        print("3 - Çıkış")

        secim = input("Seçiminiz (1/2/3): ").strip()

        if secim == "1":
            yeni_ilac_ekle()
        elif secim == "2":
            plani_listele_ve_kaydet()
        elif secim == "3":
            print("Sağlıklı günler dileriz. Program sonlandırıldı.")
            break
        else:
            print("⚠️ Geçersiz menü seçimi! Lütfen 1, 2 veya 3 giriniz.")


# Programı başlat
if __name__ == "__main__":
    ana_menu()