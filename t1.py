import streamlit as st
from englisttohindi.englisttohindi import EngtoHindi

st.title("English to Hindi Translator")


# message to be translated
message = st.text_input("Enter the text to be translated from English to Hindi")

# creating a EngtoHindi() object
res = EngtoHindi(message)

# displaying the translation
st.write("The translated text is:")
st.divider() 
st.write(res.convert)
