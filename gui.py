import streamlit as st
import functions as fn

st.set_page_config(layout='wide')
st.title('Finviz Graphs')

for stock, value in fn.dict_create.items():
    try:
        st.subheader(stock + ' - ' + str(value))
        st.image(f'https://finviz.com/chart.ashx?t={stock}')
    except:
        print(str(stock) + "failed download")

