import streamlit as st
 
text = st.text_input('Enter Text To Encrypt')
s = st.slider('Choose Key For Encryption:', 0, 25)

def encrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

st.success(encrypt(text,s))
