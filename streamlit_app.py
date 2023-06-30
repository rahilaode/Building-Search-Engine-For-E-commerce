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

query_price = f'price:[{min_price} TO {max_price}]'

    # Configure connection and query parameters
detail_products = search_function(core = solr_detail_product, 
                                  query = query_price, 
                                  rows = 1000000)

    # Get product_index based on range of prices
product_index_by_price = []
for data in detail_products:
    product_index_by_price.append(data['product_index'][0])
# -----------------------------------------------------Create 'Price' filter-----------------------------------------------END

st.write('---')

# -------------------------------------------------------If button clicked-------------------------------------------------START
if button:
    # If Input search filed
    if query:
        # Create subheader
        st.subheader('Hasil Pencarian : ' + query)

            # Configure connection and query parameters
        homedepo = search_function(core = solr_homedepo, 
                                   query = "title:" + query, 
                                   rows = 1000000)


            # Get product_index, title, and image_url from homedepo based on query and price range
        product_index_by_query_and_price = []
        title = []
        image_url = []
        for data in homedepo:
            if data['product_index'][0] in product_index_by_price:
                product_index_by_query_and_price.append(data['product_index'][0])
                title.append(data['title'][0])
                image_url.append(data['image_url'][0])
        
            # Get price data from detail_products
        price = []
        for index in product_index_by_query_and_price:
            for data in detail_products:
                if data['product_index'][0] == index:
                    price.append(data['price'][0])
        
        #--------------------------------------Create contents--------------------------------------------START
        if len(product_index_by_query_and_price) == 0:
            st.warning("Produk tidak ditemukan")
            
        else:
            col1, col2, col3, col4 = st.columns(4)
            
            cols = [col1, col2, col3, col4]
            
            for count, col in enumerate(cols, start = 0):
                try:
                    col.image(image_url[count],
                            caption = f'{price[count]} USD : {title[count][:30]} . . .', 
                            width = 150)
                except IndexError:
                    break
                
            for count, col in enumerate(cols, start = 4):
                try:
                    col.image(image_url[count],
                            caption = f'{price[count]} USD : {title[count][:30]} . . .', 
                            width = 150)
                except IndexError:
                    break
                
            for count, col in enumerate(cols, start = 8):
                try:
                    col.image(image_url[count],
                            caption = f'{price[count]} USD : {title[count][:30]} . . .', 
                            width = 150)
                except IndexError:
                    break
        #--------------------------------------Create contents-------------------------------------END
        
    # If input search not filled
    else:
        st.warning('Silahkan masukkan pencarian')
    
# ------------------------------------------------------If button clicked--------------------------------------------------END        
    

# If button not clicked
else:
    # Create subheader
    st.subheader('Produk')

    homedepo = search_function(core = solr_homedepo, 
                                query = "title:*", 
                                rows = 1000000)

        # Get product_index, title, and image_url from homedepo based on query and price range
    product_index_by_query_and_price = []
    title = []
    image_url = []
    for data in homedepo:
        if data['product_index'][0] in product_index_by_price:
            product_index_by_query_and_price.append(data['product_index'][0])
            title.append(data['title'][0])
            image_url.append(data['image_url'][0])
    
        # Get price data from detail_products
    price = []
    for index in product_index_by_query_and_price:
        for data in detail_products:
            if data['product_index'][0] == index:
                price.append(data['price'][0])
    
    #--------------------------------------Create contents--------------------------------------------START
    if len(product_index_by_query_and_price) == 0:
        st.warning("Produk tidak ditemukan")
        
    else:
        col1, col2, col3, col4 = st.columns(4)
        
        cols = [col1, col2, col3, col4]
        
        for count, col in enumerate(cols, start = 0):
            try:
                col.image(image_url[count],
                        caption = f'{price[count]} USD : {title[count][:30]} . . .', 
                        width = 150)
            except IndexError:
                break
            
        for count, col in enumerate(cols, start = 4):
            try:
                col.image(image_url[count],
                        caption = f'{price[count]} USD : {title[count][:30]} . . .', 
                        width = 150)
            except IndexError:
                break
            
        for count, col in enumerate(cols, start = 8):
            try:
                col.image(image_url[count],
                        caption = f'{price[count]} USD : {title[count][:30]} . . .', 
                        width = 150)
            except IndexError:
                break
    #--------------------------------------Create contents-------------------------------------END