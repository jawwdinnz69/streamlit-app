import streamlit as st

st.set_page_config(layout='wide')

st.title('Description of Strategy')

st.subheader('Exchanges used: NYSE, NYSEAMERICAN, NASDAQ')

general_msg = """
From Investopedia 'Perception and Cost of NYSE and NASDAQ':

The NYSE and the Nasdaq have different images among companies and investors. Whether a stock trades on the Nasdaq or the NYSE is not necessarily a determining factor for investors. It is, however, for companies that care about how each exchange is perceived.

The Nasdaq is known for technology and innovation, and it is home to digital, biotechnology, and other companies at the cutting edge. As such, stocks listed on the Nasdaq are considered growth-oriented and more volatile. In contrast, companies that list on the NYSE are perceived as more stable and well-established. The NYSE draws blue chips and industrials, some of which have been in business for generations.

However, these perceptions may not be as relevant today as they were in the past. Many corporate giants are listed on the Nasdaq. Think Apple, Google, Microsoft, Meta (formerly Facebook), Amazon, and Intel. Also, the NYSE is trying to appeal to younger or smaller firms with its direct listings (a less-expensive option than an IPO).

Still, the listing requirements for the Nasdaq are more favorable to new companies. The Nasdaq Stock Market has three tiers: Nasdaq Global Select Market, Nasdaq Global Market, and Nasdaq Capital Market...
Given the lower cost of entry, it’s understandable why growth companies with less initial capital might prefer the Nasdaq.
"""
st.write(general_msg)

msg_NYSE = """Different metrics were used for each exchange as it was determined that each exchange performed 
differently under the same metrics. For NYSE the assumption was that value and well-established blue chip stocks dominate the exchange.  Therefore Market Cap filter was excluded.
For NYSE, we filtered off of metrics such as: 
1. roe_median > 0.2 
2. price-to-sales < 1 
3. revenue_cagr_10 > 0.01 
4. roic_5yr_avg > 0.2
Initial Universe = 40 stocks
List of 20 Stocks filtered off historical relative strength (2018-2023) based on stock CAGR performance:

['ZIM', 'CRC', 'DKS', 'BLDR', 'DDS', 'RYI', 'RS', 'BBW', 'SBSW', 'MLI', 'CLF', 'NUE', 'CMC', 'MATX', 'DHI','OLN', 'PHM', 'ABC', 'BCC', 'NSP']
"""
st.subheader('NYSE Metrics')
st.write(msg_NYSE)

msg_NASDAQ = """For NASDAQ we filtered off of different criteria than the NYSE.  We restricted market cap to only 
small caps as we believe that the growth tech industry is very competitive and smaller firms can eventually compete 
with the larger companies or get acquired. 
1. market_cap < 500,000,000 
2. price-to-sales < 1 
3. roic_5yr_cagr > 0.12 
4. revenue_cagr_10 > 0.012

Initial Universe = 37 stocks

List of 15 Stocks filtered off historical relative strength (2018-2023) based on stock CAGR performance:
Some stocks were removed due to acquisition/privatization/delisting

['ESOA', 'NSYS', 'LINC', 'DXLG', 'ZEUS', 'RELL', 'RCMT', 'EDRY', 'DLHC', 'BWMX', 'SPWH', 'TSRI','CRWS', 'LAZY', 'CVLG']
"""

st.subheader('NASDAQ Metrics')
st.write(msg_NASDAQ)

msg_NYSEAMERICAN = """For NYSEAMERICAN we filtered off of similar criteria as NASDAQ as NYSEAMERICAN is also for growth statups:
1. roe_median > 0.085   
2. price-to-sales < 1
3. roic_5yr_cagr > 0.085
4. revenue_cagr_10 > 0.02

Initial Universe = 8 stocks

List of all Stocks filtered off historical relative strength (2018-2023) based on stock CAGR performance:

['ELA', 'FSI', 'FRD', 'DIT', 'RVP', 'RLGT', 'MHH', 'DPSI']
"""

st.subheader('NYSEAMERICAN Metrics')
st.write(msg_NYSEAMERICAN)

msg_personal = """
I also have two personal picks that I have relatively high conviction in for a 5-10 year timespan:

1. HDSN
2. CLFD

In the All Stocks, Lowest DeMarker, and Highest DeMarker pages we can filter off the technical indicator DeMarker to 
find relatively oversold stocks within the combined list.  We can also filter off the highest to determine which ones 
are overbought which maybe useful when considering to sell.

"""

st.subheader('Personal Picks')
st.write(msg_personal)

