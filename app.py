import streamlit as st
import webbrowser

st.set_page_config(page_title='Two-Term Percentage Calculator')



st.title('Percentage Calculator for Two Term System of CBSE.')
st.subheader('Check you percentage here :)')
t1 = st.slider('Enter your Term 1 Percentage:', 0, 100)



total = st.slider('Enter Percentage you want to achieve:', 0, 100)
o1 = st.slider('Enter term-1 weightage:', 0, 99)
o2 = 100 - o1
#total*100 = (o1*t1+o2*x)
a = total*100
b = o1*t1
c = a-b
vdish = 0


answer = c/o2




if st.button('Get Answer'):
	if t1==total and total==o1 and o1==69:
		st.success("I see you are a man of culture")
	if answer < 0:
		st.write("You need", vdish, "%", "in term 2 reach your goal.")
	elif answer <= 100:
		st.write("You need", answer, "%", "in term 2 reach your goal.")
	else:
		st.error('Required Percentage is above 100. Matlab itna lana impossible hai :(')
		
with st.sidebar:
	
#	if st.button('Check me out'):
#    		webbrowser.open_new_tab('https://just--rohan.blogspot.com/')
	st.write('Made By:   Rohan Singh🙏')
	st.write('Kaksha-Dasvi')
	st.write('Umar-15')
	
	

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
