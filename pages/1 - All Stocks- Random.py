import streamlit as st
import functions as fn

# https://jawwdinnz69-streamlit-app-gui-lromwn.streamlit.app/

st.title('Finviz Graphs')

for stock, value in fn.dict_create.items():
    try:
        st.subheader(stock + ' - ' + str(value))
        st.image(f'https://finviz.com/chart.ashx?t={stock}')
    except:
        print(str(stock) + "failed download")

