import streamlit as st
from englisttohindi.englisttohindi import EngtoHindi
from englisttohindi.englisttohindi import HinditoEng


option = st.selectbox(
    'Select Languages\nभाषा चुने',
    ('English -> हिंदी', 'हिंदी -> English'))

if option == 'English -> हिंदी':
  # message to be translated
  message = st.text_input("Enter the text to be translated from English to Hindi")
   
  # creating a EngtoHindi() object
  res = EngtoHindi(message)
   
  # displaying the translation
  st.write(res.convert)
 
if option == 'हिंदी -> English':
  # message to be translated
  message = st.text_input("हिंदी से अंग्रेजी में अनुवादित होने वाला संदेश दर्ज करें")
   
  # creating a EngtoHindi() object
  res = HinditoEng(message)
   
  # displaying the translation
  st.write(res.convert)

