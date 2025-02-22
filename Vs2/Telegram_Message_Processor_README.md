
# **Telegram Message Processor ⚙️**  
* Bu projede hedef kullanıcının mesaj verileri, Python kullanılarak Telegram API'sinden alınmaktadır. Daha sonra projeye Entegre edilen Gemini API sayesinde mesajlar işlenir ve hem orijinal mesaj hemde işlenmiş mesajlar MySql database aktarılır.
* Gelen mesaj eğer normal yazışma mesajı işe duygu tespiti yapılır, eğer bir haber metni ise haber özetlenir ve haber hakkında kısa yorum yapılır.
* Vs1 ve Vs2 ön çalışmaları içerir.
* ✅ En güncel versiyon için Vs3 Klasörüne Bakınız.
    ## Önemli Not 🗒️:
    * Her Kullanıcı `.env` dosyasını mesaj çekeceği hesaba ve kendi Gemini API Key'ine göre oluşturmalıdır !
---

## **Özellikler ✨**  
- Telegram'dan metin mesajı, fotoğraf ve video çekme  
- Kullanıcı bilgilerini `users` tablosunda güncelleme veya ekleme  
- Orijinal Mesajları `messages` tablosuna kaydetme  
- İşlenmiş Mesajları (Gemini tarafından yapılan özetler ve yorumlar) `summary` tablosuna kaydetme  

---

## **Yapılandırma 📐**  
Öncelikle `.env` dosyasını aşağıdaki gibi yapılandırın:  
```env
API_ID=YOUR_TELEGRAM_API_ID
API_HASH=YOUR_TELEGRAM_API_HASH
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## **Gereksinimler 💥**  
- Python 3.x  
- `telethon`  
- `mysql-connector-python`  
- `.env` dosyası için `python-dotenv`  

Gerekli paketleri yüklemek için 📥 :  
```terminal
pip install telethon
pip install mysql-connector-python
pip install python-dotenv
pip install -U google-generativeai (güncel versiyonu kontrol edin)
```

---

## **Veritabanı Yapısı 🗃️**  
### 1️⃣ `users` Tablosu:  
| Column        | Type        | Description                        |
|---------------|-------------|------------------------------------|
| `id`          | INT         | Birincil anahtar                    |
| `user_name`   | VARCHAR(50) | Kullanıcı adı                       |
| `last_updated`| TIMESTAMP   | Son güncellenme zamanı               |  

### 2️⃣ `messages` Tablosu:  
| Column        | Type        | Description                        |
|---------------|-------------|------------------------------------|
| `id`          | INT         | Birincil anahtar (AUTO_INCREMENT)   |
| `user_id`     | INT         | `users.id` ile ilişkili             |
| `msg_username`| VARCHAR(50) | Mesajı gönderen kullanıcı adı       |
| `msg_text`    | TEXT        | Mesaj içeriği                       |
| `image_path`  | VARCHAR(255)| Fotoğraf yolu                       |
| `video_path`  | VARCHAR(255)| Video yolu                          |
| `msg_time`    | DATETIME    | Mesajın gönderildiği zaman          |
| `insert_time` | TIMESTAMP   | Mesajın veritabanına eklendiği zaman|
| `status`      | TINYINT     | Özetleme durumu                     |  

### 3️⃣ `summary` Tablosu:  
| Column        | Type        | Description                        |
|---------------|-------------|------------------------------------|
| `id`          | INT         | Birincil anahtar                    |
| `msg_id`      | INT         | `messages.id` ile ilişkili           |
| `msg_sum`     | TEXT        | Mesajın özeti                       |  

### ⏺️ Şablon:
![NewDatabaseStructure](https://github.com/user-attachments/assets/f827489c-fb63-4897-9b5d-ff067331a264)

---

## **Kullanım 🌟**  
```terminal
python project.py
```

---

## **Proje Yapısı 🏛️**  
```plaintext
./
│
├── project.py             # Telegram mesajları çekilir, gemini fonksiyonu çağrılır, tüm veriler veritabanına kaydedilir
├── gemini_ai.py           # Mesajları işlenip özetlernir 
├── database_connection.py # Veritabanı bağlantı ayarlarları
├── .env                   # API anahtarları ve veritabanı bilgileri
└── downloads/             # İndirilen fotoğraf ve videoların kaydedildiği klasör
```

---

## **Çalışma Mantığı ℹ️**  
1. `project.py`, Telegram'dan mesajları çekip `users` ve `messages` tablolarına kaydeder.  
2. `gemini_ai.py` dosyasındaki `get_summary()` fonksiyonu sayesinde Mesajlar işlenir 
3.  İşlenen mesajlar `summary` tablosuna kaydedilir. 

---

## **Katkıda Bulunma ➕**  
Katkıda bulunmak isterseniz:  
1. Fork'layın  
2. Yeni bir dal oluşturun (`git checkout -b feature/new-feature`)  
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)  
4. Dalı push'layın (`git push origin feature/new-feature`)  
5. Pull Request açın  

---

## **Teşekkürler 🌷**  
Sofware Developer `SULEYMAN ASIM GELISGEN`

  
