# 2048 Oyunu

## Genel Bilgiler
Projede farklı cihazlarda çeşitli kontrol seçenekleri sunulmaktadır:

- **Klavye:** Ok tuşları veya WASD tuşları
- **Ekrandaki Butonlar:** Sağ tarafta bulunan WASD butonları
- **Dokunmatik:** Mobil cihazlarda swipe hareketi
- **Fare:** Bilgisayarda fare sürükleme hareketi

Bu repoda her iki versiyon da 2048 oyununun dinamik yapısını ve çeşitli kontrol seçeneklerini içermektedir. Hangi versiyonun kullanılacağı, geliştirme amacı veya kullanım senaryosuna göre tercih edilebilir.

Her iki uygulama da kullanıcıya etkileşimli bir oyun deneyimi sunmak üzere tasarlanmıştır. İyi eğlenceler!

### Oyuniçi Görüntüler

![Game Play](https://github.com/kgeckin/game2048/blob/b1b9b5b9a12d8674ccc5d1d7c8ffce061a44b9b9/images/gameplay.png)

**Oyunu oynayabilmek için:**  
[Flask Versiyonu (canlı demo)](https://web.itu.edu.tr/~geckin19/)

Bu repoda iki farklı **2048 Oyunu** uygulaması bulunmaktadır:

- **Flask Versiyonu:** Python Flask kullanılarak geliştirilen etkileşimli 2048 oyunu.
- **JavaScript Versiyonu:** Sunucu tarafı olmadan, tamamen HTML, CSS ve JavaScript kullanılarak oluşturulmuş 2048 oyunu.

---

## Flask Versiyonu

**2048 Oyunu**, popüler 2048 oyununu temel alan, modern bir Flask uygulaması olarak geliştirilmiş etkileşimli bir projedir.  

### Özellikler

- **Dinamik Oyun Alanı:** Her hamlede oyun tahtası (grid) güncellenir.
- **Kontrol Seçenekleri:** Klavye, ekran üzerindeki butonlar, dokunmatik swipe ve fare sürükleme ile hamle yapılabilir.
- **Oyun Durumu Takibi:** Anlık skor, en yüksek skor (best), Undo ve Restart seçenekleri.
- **Oyun Sonu Geri Bildirimi:** Hamle yapılabilecek alan kalmadığında “Kaybettiniz!” mesajı görüntülenir.

### Kullanılan Teknolojiler

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Oturum Yönetimi:** Flask session
- **Ortam Değişkenleri Yönetimi:** python-dotenv

---

## Pure JavaScript Versiyonu

Bu versiyonda, oyunun tüm mantığı ve arayüzü, **HTML, CSS ve JavaScript** kullanılarak tamamen istemci tarafında geliştirilmiştir. Flask veya başka bir backend teknolojisi kullanılmamaktadır.

### Özellikler

- **Dinamik Oyun Alanı:** Her hamlede oyun tahtası (grid) güncellenir.
- **Kontrol Seçenekleri:** Klavye (WSAD ve ok tuşları), ekrandaki WASD butonları, dokunmatik swipe ve fare sürükleme ile hamle yapılabilir.
- **Skor Yönetimi:** Anlık skor ve en yüksek skor, CryptoJS kütüphanesi kullanılarak HMAC doğrulaması ile güvenli bir şekilde saklanır.
- **Undo ve Restart Seçenekleri:** Son hamleyi geri alabilir veya oyunu sıfırlayabilirsiniz.
- **Kullanıcı Etkileşimi:** Fare sürükleme sırasında yön göstergesi (drag indicator) ile hamle yönünüz görsel olarak desteklenir.

### Kullanılan Teknolojiler

- **Frontend:** HTML, CSS, JavaScript
- **Güvenlik:** CryptoJS (HMAC doğrulaması ile en yüksek skorun doğrulanması)




