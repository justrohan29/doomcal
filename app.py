import streamlit as st

encrypt = st.text_input('Enter Text To Encrypt')
encrypt = encrypt.lower().replace(" ", "")

key = st.slider('Enter Key For Encryption:', 0, 25)

s = ''.join(chr(ord(char) + 5) for char in encrypt)
st.text("Encrypted Text: ")
st.success(s)
