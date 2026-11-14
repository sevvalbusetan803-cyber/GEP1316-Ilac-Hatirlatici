# Yapay Zekâ Çalışma Günlüğü ve Eleştirel Değerlendirme

**Kullanılan YZ Aracı:** Google Gemini (Büyük Dil Modeli)

## Prompt 1: Problem Analizi ve Veri Yapısı Tasarımı
- **Prompt:** "2030 yılında bir eczacının hastalar için günlük ilaç ve tedavi saatleri planı oluşturacağı komut satırı uygulaması yapmak istiyorum. Her ilaç için ad, açlık/tokluk durumu, günlük doz sayısı ve saatleri tutmak için Python'da nasıl bir veri yapısı kullanmalıyım?"
- **YZ Yanıtı Özeti:** Her ilacı bir sözlük (`dictionary`) olarak tanımlamayı ve tüm ilaçları tek bir ana liste (`list`) içinde saklamayı önerdi.
- **Karar (Kabul / Düzenleme):** **Kabul Edildi.** Sözlük yapısı anahtar-değer eşleşmesi sağladığı için hem ekrana tablo basarken hem de `csv.DictWriter` ile dosyaya yazarken kod okunabilirliğini artırdı.

## Prompt 2: Saat Hesaplama ve Doğrulama Fonksiyonu
- **Prompt:** "Kullanıcıdan '08:00' formatında ilk doz saatini alıp günlük doz sayısına göre diğer doz saatlerini hesaplayan bir Python fonksiyonu yaz. Kullanıcı hatalı saat girerse program çökmesin."
- **YZ Yanıtı Özeti:** `split(":")` ile saati parçalayıp 24 saate bölerek saatleri hesaplayan ve `try-except` kullanan bir fonksiyon üretti.
- **Karar (Düzenleme Yapıldı - Hata Yakalama):** **Düzenlendi.** YZ'nin ilk ürettiği kodda sadece `:` işareti olup olmadığı kontrol ediliyordu; kullanıcı `25:70` yazdığında program hata vermeden kabul ediyordu. Bu eksikliği fark ettim ve `datetime.strptime(saat_metni, "%H:%M")` yöntemini ekleyerek geçersiz saat aralıklarının (24 ve üzeri saat veya 60 ve üzeri dakika) reddedilmesini sağladım.

## Prompt 3: Girdi Doğrulama Döngüsü (Doz Sayısı)
- **Prompt:** "Kullanıcıdan günde kaç kez ilaç alınacağını sorarken harf girilirse veya 0'dan küçük / 6'dan büyük bir sayı girilirse uyarı verip tekrar soran bir doğrulama fonksiyonu oluştur."
- **YZ Yanıtı Özeti:** `while True` döngüsü içinde `.isdigit()` kontrolü ve `1 <= sayi <= 6` aralığını denetleyen `pozitif_tam_sayi_al()` fonksiyonunu verdi.
- **Karar (Kabul Edildi):** **Kabul Edildi.** Negatif sayılarda `-` işareti olduğu için `.isdigit()` otomatik olarak `False` döndürdü ve sıfır bölme hatası (`ZeroDivisionError`) riski ortadan kalktı.

## Prompt 4: Klinik Uyarı Mantığı ve Karar Yapıları
- **Prompt:** "İlacın aç, tok veya fark etmez olmasına göre hastaya farmasötik kullanım uyarısı üreten `if/elif/else` yapısını koda ekle."
- **YZ Yanıtı Özeti:** Aç karnına ilaçlar için yemekten 30-60 dakika önce, tok karnına ilaçlar için yemekten hemen sonra alınması gerektiğine dair standart uyarı metinleri oluşturdu.
- **Karar (Düzenleme Yapıldı):** **Düzenlendi.** Kullanıcının küçük harfle `aç` veya `tok` yazması durumunda koşulun çalışmaması ihtimaline karşı girdi alırken `.strip().capitalize()` metodunu ekleyerek standartlaştırma yaptım.

## Prompt 5: Biçimli Çıktı ve Türkçe Karakter Sorunsuz CSV Kaydı
- **Prompt:** "Oluşturulan ilaç listesini terminalde hizalı bir tablo olarak göster ve `tedavi_plani.csv` dosyasına Türkçe karakterler bozulmadan kaydet."
- **YZ Yanıtı Özeti:** `f-string` hizalama operatörleri (`:<22`) ile tablo görünümü ve `encoding="utf-8"` parametresi ile CSV kaydı önerdi.
- **Karar (Düzenleme Yapıldı):** **Düzenlendi.** Windows Excel'de `.csv` dosyası açıldığında Türkçe karakterlerin (`ş, ğ, ü, ö, ç, İ`) bozuk görünmemesi için kodlamayı `utf-8-sig` ve ayırıcıyı (`delimiter`) Türkiye yerel ayarlarına uygun olan noktalı virgül (`;`) olarak değiştirdim.
