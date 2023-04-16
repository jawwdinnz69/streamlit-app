import gui
import streamlit as st
import functions as fn


st.header("Stocks with the lowest DeMarker value")


for stock, value in fn.low_sort_dict.items():
    try:
        st.subheader(stock + ' - ' + str(value))
        st.image(f'https://finviz.com/chart.ashx?t={stock}')
    except:
        print(str(stock) + "failed download")
