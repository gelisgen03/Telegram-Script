import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from database_connection import db

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient('session_name', api_id, api_hash)

secilen_kullanici='BtuSksBot'
flag1=0
flag2=0
flag3=0
flag4=0
with client:
    
    print("Giriş yapılıyor...")
    client.start()
    print("Giriş başarılı!")

    messages = client.get_messages(secilen_kullanici, limit=4)  # Son 5 mesajı al
    database = db.cursor()

    for message in messages:
        try:
            # Gönderen kullanıcı adı (olmayan durumlarda "secilen_kullanici")
            msg_username =  secilen_kullanici # (Alternatif) message.sender.username if message.sender else 'Bilinmiyor'
            # Mesaj metni (yoksa boş string olarak ata)
            msg_text = message.message if message.message is not None else ""
            # Mesaj zamanı (varsa)
            msg_time = message.date.strftime('%Y-%m-%d %H:%M:%S') if message.date else None

            # 1. Kullanıcıyı users tablosuna ekle veya güncelle
            database.execute("SELECT id FROM users WHERE user_name = %s", (msg_username,))
            user = database.fetchone()
            if user:
                user_id = user[0]
                database.execute("UPDATE users SET last_updated = NOW() WHERE id = %s", (user_id,))
            else:
                database.execute("INSERT INTO users (user_name, last_updated) VALUES (%s, NOW())", (msg_username,))
                user_id = database.lastrowid  # Yeni eklenen kullanıcının ID'sini al

            # 2. Medya dosyalarını kontrol et ve indir (hata alınırsa None olarak devam et)
            image_path, video_path = None, None

            if message.photo:
                try:
                    image_path = client.download_media(message, file="downloads/photos/")
                    print(f"Fotoğraf indirildi: {image_path}")
                except Exception as e:
                    flag1=1
                    print(f"Fotoğraf indirilirken hata oluştu: {e}")
                    image_path = None

            if message.video:
                try:
                    video_path = client.download_media(message, file="downloads/videos/")
                    print(f"Video indirildi: {video_path}")
                except Exception as e:
                    flag2=1
                    print(f"Video indirilirken hata oluştu: {e}")
                    video_path = None

            # 3. Mesajı messages tablosuna ekle
            database.execute("""
                INSERT INTO messages (
                    user_id, 
                    msg_username, 
                    msg_text, 
                    image_path, 
                    video_path, 
                    msg_time, 
                    insert_time, 
                    status
                )
                VALUES (%s, %s, %s, %s, %s, %s, NOW(), 0)
            """, (user_id, msg_username, msg_text, image_path, video_path, msg_time))
            print(f"Mesaj kaydedildi: {msg_text if msg_text else '[MEDYA]'}")

        except Exception as e:
            flag3=1
            print(f"Mesaj işlenirken hata oluştu: {e}")

    db.commit()
    if flag1+flag2+flag3==0:
        print("Tüm veriler başarıyla veritabanına eklendi!")
    else:
         print("Tüm veriler veritabanına Aktarılamadı !")   
