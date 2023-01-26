import streamlit as st

encrypt = st.text_input('Enter Text To Encrypt')
encrypt = encrypt.lower().replace(" ", "")
s = ''.join(chr(ord(char) + 5) for char in encrypt)

st.success(s)
