import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from database_connection import db

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

# İstemci başlatma
client = TelegramClient('session_name', api_id, api_hash)

# Oturum açma
with client:
    print("Giriş yapılıyor...")
    client.start()
    print("Giriş başarılı!")
    
    me = client.get_me()  # Kullanıcı bilgilerini al
    print(f"Merhaba, {me.first_name}!")
    
    # Belirli bir mesajı almak
    messages = client.get_messages('bpthaber', limit=5)  # Daha fazla mesaj almak için limit artırılabilir

    # Veritabanı bağlantısını başlat
    database = db.cursor()

    for message in messages:
        if hasattr(message, 'message') and message.message:  # Text içeren mesajları al
            msg_text = message.message  # Mesajın içeriği
            
            # Mesajın veritabanında olup olmadığını kontrol et
            database.execute("SELECT COUNT(*) FROM python WHERE message = %s", (msg_text,))
            exists = database.fetchone()[0]

            if exists == 0:  # Mesaj yoksa ekle
                database.execute("INSERT INTO python (message) VALUES (%s)", (msg_text,))
                print(f"Mesaj eklendi: {msg_text}")

    # Değişiklikleri kaydet ve bağlantıyı kapat
    db.commit()
    print("Mesajlar başarıyla veritabanına eklendi!")
