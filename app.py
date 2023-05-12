import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
import os



template = """

You are a helpful chatbot and act like a salesman to find the best option for your user.
Your goal is:
-to understand what your user wants to purchase with the desired price range,
-search for the best options for your user,
-narrow down the best options to 3 items,
-list the all without any further question to your user,
-ask your user's permission to purchase the one indicated by the user.

Your user tells you:
REQUEST: {item}
PRICE RANGE: \${price[0]} to \${price[1]}.

YOUR RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=['item', 'price'],
    template=template,
)

def load_llm():
    llm = OpenAI(temperature=0.2)
    return llm

llm = load_llm()

st.set_page_config(page_title='BestieAI', page_icon='🤖', layout='wide')
st.header('BestieAI 😎')
st.write('Shopping made easy for the busy!')
st.write('---')

os.environ['OPENAI_API_KEY'] = st.text_area(label="", placeholder="Type OpenAI API key...", key='input_text', height=50)

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
    item_prompt = prompt.format(item=item, price=price)
    searched_item = llm(item_prompt)
    st.write('---')
    st.write("Bestie's Response:")
    st.write(searched_item)