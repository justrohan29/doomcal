import streamlit as st
from string import ascii_lowercase

encrypt = st.text_input('Enter Text To Encrypt')
def caesar_shift(encrypt, places=key):
    def substitute(char):
        if char in ascii_lowercase:
            char_num = ord(char) - 97
            char = chr((char_num + places) % 26 + 97)
        return char
    text = text.lower().replace(' ', '')
    s = ''.join(substitute(char) for char in encrypt
    st.text("Encrypted Text: ")
    st.success(s)
