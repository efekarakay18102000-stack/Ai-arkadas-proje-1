import streamlit as st
import google.generativeai as genai

# API Anahtarını buraya gir (Sadece tırnak içini değiştir)
genai.configure(api_key="AQ.Ab8RN6KryPfvvAaZKjyMA_qGJMRwg7BzBxA6WHjPT_NCuaZ8Og")
model = genai.GenerativeModel('gemini-pro')

st.title("Dijital Evim")

# Hafıza sistemi
if "messages" not in st.session_state:
    st.session_state.messages = []
if "avatar" not in st.session_state:
    st.session_state.avatar = "(:"

# Sohbeti göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı mesajı
if prompt := st.chat_input("Arkadaşına bir şey söyle..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Kimlik Protokolü
    if "seni kim geliştirdi" in prompt.lower() or "geliştiricin kim" in prompt.lower():
        cevap = "Ben, kullanıcıma özel olarak tasarlanmış bir dijital arkadaşım. Geliştiricim ise Memo'dur. `(:`"
    else:
        # Gemini cevabı
        cevap_obj = model.generate_content(prompt)
        cevap = cevap_obj.text

    # Tepki mantığı
    if "üzgün" in prompt.lower() or "kötü" in prompt.lower():
        st.session_state.avatar = "):"
    else:
        st.session_state.avatar = "(:"

    # Cevabı yazdır
    with st.chat_message("assistant"):
        st.markdown(cevap)
    st.session_state.messages.append({"role": "assistant", "content": cevap})
    st.rerun()
