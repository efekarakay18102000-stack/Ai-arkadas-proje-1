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

# Kullanıcı girişi
if prompt := st.chat_input("Arkadaşına bir şey söyle..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini cevabı
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
        
