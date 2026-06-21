import streamlit as st
import google.generativeai as genai
import os

# Secrets'tan anahtarı al
api_key = st.secrets["GOOGLE_API_KEY"]

# Anahtarı kütüphaneye tanımla
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
import streamlit as st
import google.generativeai as genai

# Anahtarı kasadan al
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# BAŞLIK KISMI
st.title("Dijital Evim")
st.subheader("Merhaba, ben Perryn!") # Yapay zekanın adı
st.caption("Geliştiren: Efekarakaya") # Geliştirici bilgisi

# Hafıza sistemi
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sohbeti göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ... (baş kısımlar aynı kalacak)

# Kullanıcı girişi
if prompt := st.chat_input("Arkadaşına bir şey söyle..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini cevabı (Hata almamak için metin kontrolü ekliyoruz)
    try:
        response = model.generate_content(prompt)
        # Cevabın boş olup olmadığını kontrol et
        if response.text:
            cevap = response.text
        else:
            cevap = "Üzgünüm, şu an bir cevap üretemiyorum."
    except Exception as e:
        cevap = f"Bir hata oluştu: {e}"
    
    with st.chat_message("assistant"):
        st.markdown(cevap)
    st.session_state.messages.append({"role": "assistant", "content": cevap})
    

    # Gemini cevabı
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
        
