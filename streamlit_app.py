# Import dependencies
import streamlit as st
from search import *
from search import search_function

# Page configuration
st.set_page_config(layout = 'wide', 
                   initial_sidebar_state = 'collapsed', 
                   page_title = 'Selamat datang di Tokopaedi')

# Create Header
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
with col1:
    st.image('logo.png', width = 120)

with col2:
    st.header('TokOnline')
    
st.write('---')
    
    
# Input text
# Using for search query
query = st.text_input(label = 'Pencarian',
                      placeholder = 'Cari Produk')

# Create 'Cari' Button
button = st.button('Cari')

# ------------------------------------------------------Create 'Price' filter------------------------------------------------START
st.write('Filter : ')
col1, col2 = st.columns(2)
with col1:
    min_price = st.slider(label='Harga minimal', min_value=0, max_value=150, value=50)

with col2:
    max_price = st.slider(label='Harga maksimal', min_value=151, max_value=300, value=200)

query_price = f'data_detail.price:[{min_price} TO {max_price}]'

    # Configure connection and query 
homedepo_price = search_function(core = solr_homedepo, 
                                 query = query_price, 
                                 rows = 1000000)
# -----------------------------------------------------Create 'Price' filter-----------------------------------------------END

st.write('----')

# -------------------------------------------------------If button clicked-------------------------------------------------START
if button:
    # If search filled
    if query:
        # Create subheader
        st.subheader('Hasil Pencarian : ' + query)
                    # Configure connection and query parameters
        homedepo_product = search_function(core = solr_homedepo, 
                                           query = "data_detail.product_name:" + query, 
                                           rows = 1000000)

         #Get product_name, image_url, and price information fiter by query product_name and price
        product_name = []
        image_url = []
        price = []
        
        for data in homedepo_product:
            if data['data_detail.price'][0] > min_price and data['data_detail.price'][0] < max_price:
                product_name.append(data['data_detail.product_name'])
                image_url.append(data['image_url'])
                price.append(data['data_detail.price'])

        #--------------------------------------Create contents--------------------------------------------START
        if len(product_name) == 0:
            st.warning("Produk tidak ditemukan")
            
        else:
            col1, col2, col3, col4 = st.columns(4)
            
            cols = [col1, col2, col3, col4]
            
            for count, col in enumerate(cols, start = 0):
                try:
                    col.image(image_url[count],
                            caption = f'{price[count]} USD : {product_name[count][:30]} . . .', 
                            width = 150)
                except IndexError:
                    break
                
            for count, col in enumerate(cols, start = 4):
                try:
                    col.image(image_url[count],
                            caption = f'{price[count]} USD : {product_name[count][:30]} . . .', 
                            width = 150)
                except IndexError:
                    break
                
            for count, col in enumerate(cols, start = 8):
                try:
                    col.image(image_url[count],
                            caption = f'{price[count]} USD : {product_name[count][:30]} . . .', 
                            width = 150)
                except IndexError:
                    break
        #--------------------------------------Create contents-------------------------------------END

# ------------------------------------------------------If button clicked--------------------------------------------------END        
    
    
# ------------------------------------------------------If button NOT clicked--------------------------------------------------START        
else:
    # Create subheader
    st.subheader('Produk')
    
    #Get product_name, image_url, and price information filter by price
    product_name = []
    image_url = []
    price = []
    
    for data in homedepo_price:
        product_name.append(data['data_detail.product_name'][0])
        image_url.append(data['image_url'][0])
        price.append(data['data_detail.price'][0])


    #--------------------------------------Create contents--------------------------------------------START
    if len(product_name) == 0:
        st.warning("Produk tidak ditemukan")
        
    else:
        col1, col2, col3, col4 = st.columns(4)
        
        cols = [col1, col2, col3, col4]
        
        for count, col in enumerate(cols, start = 0):
            try:
                col.image(image_url[count],
                        caption = f'{price[count]} USD : {product_name[count][:30]} . . .', 
                        width = 150)
            except IndexError:
                break
            
        for count, col in enumerate(cols, start = 4):
            try:
                col.image(image_url[count],
                        caption = f'{price[count]} USD : {product_name[count][:30]} . . .', 
                        width = 150)
            except IndexError:
                break
            
        for count, col in enumerate(cols, start = 8):
            try:
                col.image(image_url[count],
                        caption = f'{price[count]} USD : {product_name[count][:30]} . . .', 
                        width = 150)
            except IndexError:
                break
    #--------------------------------------Create contents-------------------------------------END

# ------------------------------------------------------If button NOT clicked--------------------------------------------------END
