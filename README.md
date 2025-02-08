# 2048 Oyunu

**2048 Oyunu**, popüler 2048 oyununu temel alan, modern bir Flask uygulaması olarak geliştirilmiş etkileşimli bir projedir.  
Projede farklı cihazlarda çeşitli kontrol seçenekleri sunulmaktadır:

- **Klavye:** Ok tuşları veya WASD tuşları
- **Ekrandaki Butonlar:** Sağ tarafta bulunan WASD butonları
- **Dokunmatik:** Mobil cihazlarda swipe hareketi
- **Fare:** Bilgisayarda fare sürükleme hareketi

## Özellikler

- **Dinamik Oyun Alanı:** Her hamlede oyun tahtası (grid) güncellenir.
- **Kontrol Seçenekleri:** Klavye, ekran üzerindeki butonlar, dokunmatik swipe ve fare sürükleme ile hamle yapılabilir.
- **Oyun Durumu Takibi:** Anlık skor, en yüksek skor (best), Undo ve Restart seçenekleri.
- **Oyun Sonu Geri Bildirimi:** Hamle yapılabilecek alan kalmadığında “Kaybettiniz!” mesajı görüntülenir.

## Kullanılan Teknolojiler

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Oturum Yönetimi:** Flask session (secret key ile imzalanmış)
- **Ortam Değişkenleri Yönetimi:** python-dotenv

## Oyuniçi Görüntüler
![Game Play](https://github.com/kgeckin/game2048/blob/b1b9b5b9a12d8674ccc5d1d7c8ffce061a44b9b9/images/gameplay.png)
