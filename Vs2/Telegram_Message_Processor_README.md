
# **Telegram Message Processor**  
Bu proje, Telegram mesajlarını çekip, veritabanına kaydeden ve mesajları özetleyerek **summary** tablosuna ekleyen bir sistemdir.  

---

## **Özellikler**  
- Telegram'dan metin mesajlarını, fotoğrafları ve videoları çekme  
- Kullanıcı bilgilerini `users` tablosunda güncelleme veya ekleme  
- Mesajları `messages` tablosuna kaydetme  
- Mesajların özetlerini **summary** tablosuna kaydetme  

---

## **Yapılandırma**  
Öncelikle `.env` dosyasını aşağıdaki gibi yapılandır:  
```env
API_ID=YOUR_TELEGRAM_API_ID
API_HASH=YOUR_TELEGRAM_API_HASH
```

---

## **Gereksinimler**  
- Python 3.x  
- `telethon`  
- `mysql-connector-python`  
- `.env` dosyası için `python-dotenv`  

Gerekli paketleri yüklemek için:  
```bash
pip install telethon mysql-connector-python python-dotenv
```

---

## **Veritabanı Yapısı**  
### `users` Tablosu:  
| Column        | Type        | Description                        |
|---------------|-------------|------------------------------------|
| `id`          | INT         | Birincil anahtar                    |
| `user_name`   | VARCHAR(50) | Kullanıcı adı                       |
| `last_updated`| TIMESTAMP   | Son güncellenme zamanı               |  

### `messages` Tablosu:  
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

### `summary` Tablosu:  
| Column        | Type        | Description                        |
|---------------|-------------|------------------------------------|
| `id`          | INT         | Birincil anahtar                    |
| `msg_id`      | INT         | `messages.id` ile ilişkili           |
| `msg_sum`     | TEXT        | Mesajın özeti                       |  

---

## **Kullanım**  
```bash
python project.py
```

---

## **Proje Yapısı**  
```plaintext
Telegram_Update/
│
├── project.py             # Telegram mesajlarını çekip veritabanına kaydeder
├── gemini_ai.py           # Mesajları işleyip özetler
├── database_connection.py # Veritabanı bağlantı ayarları
├── .env                   # API anahtarları ve veritabanı bilgileri
└── downloads/             # İndirilen fotoğraf ve videoların kaydedildiği klasör
```

---

## **Çalışma Mantığı**  
1. `project.py`, Telegram'dan mesajları çekip `users` ve `messages` tablolarına kaydeder.  
2. Mesajlar işlendiğinde `summary` tablosuna özetleri kaydeder.  
3. Özetleme işlemi için `gemini_ai.py` kullanılır.  

---

## **Katkıda Bulunma**  
Katkıda bulunmak isterseniz:  
1. Fork'layın  
2. Yeni bir dal oluşturun (`git checkout -b feature/new-feature`)  
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)  
4. Dalı push'layın (`git push origin feature/new-feature`)  
5. Pull Request açın  

---

## **Lisans**  
Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.  
