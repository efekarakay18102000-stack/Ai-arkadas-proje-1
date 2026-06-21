import streamlit as st
import google.generativeai as genai

# Anahtarı doğrudan koda yazdık, secrets kullanmıyoruz
genai.configure(api_key="AIzaSyAQ.Ab8RN6LlvUjpMlglsDV6OJf6oTGtysdJGA3JqsYKVeLjPXaRMA")

model = genai.GenerativeModel('gemini-1.5-flash')

# Başlık ve bilgiler
st.title("Dijital Evim")
st.subheader("Merhaba, ben Perryn!")
st.caption("Geliştiren: Efekarakaya")

# Hafıza sistemi
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sohbeti göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı girişi
if prompt := st.chat_input("Arkadaşına bir şey söyle..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = model.generate_content(prompt)
        cevap = response.text
    except Exception as e:
        cevap = f"Bir hata oluştu: {e}"
    
    with st.chat_message("assistant"):
        st.markdown(cevap)
    st.session_state.messages.append({"role": "assistant", "content": cevap})
        
