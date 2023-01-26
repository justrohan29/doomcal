import streamlit as st

def encrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 
encrypt = st.text_input('Enter Text To Encrypt')
key = st.slider('Choose Key For Encryption:', 0, 25)

st.success(encrypt(text,s))
