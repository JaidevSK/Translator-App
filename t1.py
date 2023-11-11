import streamlit as st
from englisttohindi.englisttohindi import EngtoHindi
 
# message to be translated
message = st.text_input("Enter the text to be translated from English to Hindi")
 
# creating a EngtoHindi() object
res = EngtoHindi(message)
 
# displaying the translation
st.write(res.convert)
