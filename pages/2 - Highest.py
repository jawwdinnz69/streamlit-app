import streamlit as st
import functions as fn

st.header('Stocks with the Highest DeMarker Value')

for stock, value in fn.high_sort_dict.items():
    try:
        st.subheader(stock + ' - ' + str(value))
        st.image(f'https://finviz.com/chart.ashx?t={stock}')
    except:
        print(str(stock) + "failed download")