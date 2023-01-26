import streamlit as st

encrypt = input('Enter text to encrypt : ')
encrypt = encrypt.lower().replace(" ", "")
s = ''.join(chr(ord(char) + 5) for char in encrypt)

st.text(s)
