import os

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 65536,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-thinking-exp-01-21",
  generation_config=generation_config,
  system_instruction="Sen bir mesaj tespit uzmanısın. Eğer Sana bir mesaj gelirse mesajın duygusunu tespit et ve yorumla. Eğer sana haber metni gelirse bunun özetini çıkar ve bir kaç cümle ile yorumla.", 
)

history=[]



def get_summary(msg_text):
    global history
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(msg_text)
    model_response = response.text
    
    # AI cevabını ve kullanıcı mesajını geçmişe ekle
    history.append({"role": "user", "parts": [msg_text]})
    history.append({"role": "model", "parts": [model_response]})
    
    return model_response    

