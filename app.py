import streamlit as st
import os
from llm import get_llm

st.set_page_config(page_title='BestieAI', page_icon='🤖', layout='wide')
st.header('BestieAI 😎')
st.write('Shopping made easy for the busy!')
st.write('---')

openai_apikey = st.text_area(label="", placeholder="Type your OpenAI API key...", key='api_text', height=10)

st.write('---')

_,_,_,_, col5 = st.columns(5)

with col5:
    st.button('## 📦 Shopping Cart')

st.subheader('🔍 What are you looking for?')

def get_info():
    input_text = st.text_area(label="", placeholder="Type here...", key='input_text', height=50)
    price = st.slider('💲 What is your price range?', 0, 1000, (0, 1000))  
    return input_text, price

item, price = get_info()

if st.button('🔍 Search...'):
    
    response = get_llm(openai_apikey, item, price)
    st.write('---')
    st.write("Bestie's Response:")
    st.write(response)