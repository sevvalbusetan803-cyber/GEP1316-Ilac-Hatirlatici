# İlaç ve Tedavi Saatleri Hatırlatıcı Planlayıcı (GEP1316 - Ara Değerlendirme Ödevi 1)

## Proje Amacı
2030 yılında serbest eczane ve klinik eczacılık ortamında çoklu ilaç kullanan (polifarmasi) hastaların tedavi uyumunu artırmak amacıyla geliştirilmiş komut satırı uygulamasıdır. Eczacının girdiği ilaç adı, açlık/tokluk durumu, günlük doz sıklığı ve ilk doz saatine göre 24 saatlik otomatik doz çizelgesi oluşturur, klinik uyarı notu ekler ve çıktıyı `tedavi_plani.csv` dosyasına aktarır.

## Özellikler
- **Girdi Doğrulama:** Boş ilaç adı, geçersiz açlık/tokluk tercihi, 1-6 dışı veya metin formatında doz sayısı ve hatalı saat formatlarında (`25:90`, `abc`) program çökmeden kullanıcıyı uyarır.
- **Otomatik Doz Hesaplama:** İlk doz saatini baz alarak günlük doz sayısına göre eşit aralıklarla (örneğin günde 3 doz için 8 saat arayla) saatleri hesaplar.
- **Klinik Uyarı Üretimi:** İlacın aç veya tok alınma durumuna göre hastaya özel farmasötik kullanım talimatı atar.
- **CSV Çıktısı:** Hazırlanan planı eczane sistemlerine veya hasta çıktısına uygun şekilde `tedavi_plani.csv` olarak kaydeder.

## Nasıl Çalıştırılır?
1. Bilgisayarınızda Python 3 yüklü olduğundan emin olun.
2. Terminal veya komut satırını açarak proje klasörüne gidin.
3. Aşağıdaki komutu çalıştırın:
   ```bash
   python ilac_hatirlatici.py
