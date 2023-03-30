# IMPORT PYTHON LIBRARIES THAT COULD BE USEFUL IN THE PROJECT
import streamlit as st
import pandas as pd 
import requests
from bs4 import BeautifulSoup


st.title("Web Scrapping App Using Streamlit")
tag=st.selectbox('Choose a topic',['love','humor','life','books','inspirational','reading','friendship','friends','truth'])

#BUTTON TO GENERATE CSV
generate = st.button('Generate CSV')

#ACCESS THE URL 
url =f"https://quotes.toscrape.com/tag/{tag}/"
res = requests.get(url)

# USE BEAUTIFUL SOUP TO ACCESS THE CONTENT ON THE REQUESTED URL
content =  BeautifulSoup(res.content,'html.parser')
quotes = content.find_all('div',class_='quote')

quote_file = []
for quote in quotes:
    text = quote.find('span',class_ ='text').text
    author = quote.find('small',class_ = 'author').text
    link =  quote.find('a')
    st.markdown("""---""")
    st.success(text)
    st.markdown(f"<a href=https://quotes.toscrape.com{link['href']}>{author}</a>",unsafe_allow_html=True)
    st.code(f"https://quotes.toscrape.com{link['href']}")
    quote_file.append([text,author,link['href']])
    
if generate:
    try:
      df = pd.DataFrame(quote_file)
      df.to_csv('Quotes.csv',index=False,header=['Quote','Author','Link'],encoding='cp1252')  
      
    except:
        st.write('Loading ...')
