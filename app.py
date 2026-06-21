import streamlit as st
import google.generativeai as genai

# 1. Sayfa Yapılandırması
st.set_page_config(page_title="Dijital Evim", page_icon="🤖")

# 2. Güvenli API Anahtarı Tanımlama
# Streamlit secrets üzerinden anahtarı çekiyoruz
try:
    api_key = st.secrets["general"]["API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("API anahtarı bulunamadı! Lütfen .streamlit/secrets.toml dosyanı kontrol et.")
    st.stop()

# 3. Model Başlatma
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. Arayüz
st.title("Dijital Evim")
st.subheader("Merhaba, ben Perryn!")
st.caption("Geliştiren: Efekarakaya")

# 5. Hafıza (Session State) Başlatma
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# 6. Geçmişi Ekrana Yazdırma
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7. Kullanıcı Girişi ve Yanıt
if prompt := st.chat_input("Arkadaşına bir şey söyle..."):
    # Kullanıcı mesajını kaydet ve göster
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Modelden yanıt al
    with st.chat_message("assistant"):
        with st.spinner("Düşünüyorum..."):
            try:
                response = st.session_state.chat_session.send_message(prompt)
                cevap = response.text
                st.markdown(cevap)
                # Asistan yanıtını kaydet
                st.session_state.messages.append({"role": "assistant", "content": cevap})
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}")
    
