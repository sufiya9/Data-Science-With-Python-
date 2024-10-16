'''
how to run
- open terminal/console  and type
-cd app1
-streamlit run main.py
'''

from random import choices
from sre_constants import MAX_UNTIL
import streamlit as st

st.title('Simple form')
with st.form('Myform'):
    name = st.text_input('Enter your name')
    age=st.number_input('Enter your age',min_value=18,max_value=90)
    message= st.text_area('Enter your thought')
    time=st.time_input('Enter what the time')
    date= st.date_input('Enter the date')
    file=st.file_uploader('Select the file')
    camera=st.camera_input('Grab a photo from webcam')
    sb=st.form_submit_button('Submit')

if sb:
    st.write(name)
    st.write(age)
    st.write(message)
    st.write(time)
    st.write(date)
    st.write(file.name)
    st.write(camera)

with st.form('Another form'):
    color= st.color_picker('select ur color')
    num1=st.select_slider('select a value',[1,5,10,15,20,25])
    num2=st.slider('select another value',min_value=25,max_value=100,step=5)
    gender=st.radio('Gender',['Male','female','other'],horizontal=True)
    education=st.selectbox('select ur highest education',
        ['inetmediate','High-School','Graduate','Master','pade likhe gawar'])
    choices=st.multiselect('select what u are like',
        ['Maggi','Pizza','Spinach','Dry fruits','Noodles','Lichi'])
    is_checked=st.checkbox('agree to our secret terms and conditions',value=True)
    sb2=st.form_submit_button('submit')
    
if sb2:
    st.write(color)
    st.write(num1)
    st.write(num2)
    st.write(gender)
    st.write(education)
    st.write(choices)
    st.write(is_checked)