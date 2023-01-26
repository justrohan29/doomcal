import streamlit as st

st.title('Python based Encryption and Decryption')


sel = st.selectbox('Select:', ['Encryption', 'Decryption'])

if sel=="Encryption":
    text = st.text_input('Enter Text To Encrypt')
    s = st.slider('Choose Key For Encryption:', 0, 25)
    
    def encrypt(text,s):
        result = ""
     
        for i in range(len(text)):
            char = text[i]
     
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
                
            elif (char.isspace()):
                result += chr((ord(char) + 0 - 0) % 26 + 26)
     
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
     
        return result
    
    st.text("Encrypted Text: ")
    st.success(encrypt(text,s))
    
else:
    text2 = st.text_input('Enter Text To Encrypt')
    s2 = st.slider('Choose Key For Encryption:', 0, 25)
    
    def encrypt2(text2,s2):
        result = ""
     
        for i in range(len(text2)):
            char2 = text2[i]
     
            if (char2.isupper()):
                result += chr((ord(char2) - s2-65) % 26 + 65)
                
            elif (char2.isspace()):
                result += chr((ord(char2) - 0 - 0) % 26 + 26)
     
            else:
                result += chr((ord(char2) - s2 - 97) % 26 + 97)
     
        return result
    
    st.text("Encrypted Text: ")
    st.success(encrypt2(text2,s2))
    
    
with st.sidebar:
        st.write("Made By:   Rohan Singh🙏")
	st.write("Class-11C")
	st.write("Age-16")
	
	

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
