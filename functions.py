import yfinance as yf
import datetime
import pandas as pd
import streamlit as st
import base64
import numpy as np

# NASDAQ = ['ESOA', 'NSYS', 'LINC', 'DXLG', 'LIVE', 'ZEUS', 'RELL', 'RCMT', 'EDRY', 'DLHC', 'BWMX', 'SPWH', 'TSRI',
# 'CRWS', 'LAZY', 'CVLG']

# NYSE = ['ZIM', 'CRC', 'DKS', 'BLDR', 'DDS', 'RYI', 'RS', 'BBW', 'SBSW', 'MLI', 'CLF', 'NUE', 'CMC', 'MATX', 'DHI',
# 'OLN', 'PHM', 'ABC', 'BCC', 'NSP']

# Personal Picks = ['CLFD', 'HDSN']

# NYSEAMERICAN = ['ELA', 'FSI', 'FRD', 'DIT', 'RVP', 'RLGT', 'MHH', 'DPSI']

tickers = ['ESOA', 'NSYS', 'LINC', 'DXLG', 'LIVE', 'ZEUS', 'RELL', 'RCMT', 'EDRY', 'DLHC', 'BWMX', 'SPWH', 'TSRI',
           'CRWS', 'LAZY', 'CVLG', 'ZIM', 'CRC', 'DKS', 'BLDR', 'DDS', 'RYI', 'RS', 'BBW', 'SBSW', 'MLI', 'CLF',
           'NUE', 'CMC', 'MATX', 'DHI', 'OLN', 'PHM', 'ABC', 'BCC', 'NSP', 'CLFD', 'HDSN', 'ELA', 'FSI', 'FRD',
           'DIT', 'RVP', 'RLGT', 'MHH', 'DPSI']

start_date = datetime.datetime.now() - datetime.timedelta(30)


def sma(values_list, window_size=13):
    number_series = pd.Series(values_list)
    windows = number_series.rolling(window_size)
    moving_averages = windows.mean()
    moving_averages_list = moving_averages.tolist()
    return moving_averages_list


def DeM(ticker):
    df = yf.download(ticker, start=start_date)

    window_size = 13
    df['DeMax'] = df['High'] - df['High'].shift(1)
    df['DeMin'] = df['Low'].shift(1) - df['Low']
    df.loc[df['DeMax'] < 0, ['DeMax']] = 0
    df.loc[df['DeMin'] < 0, ['DeMin']] = 0

    # DeM Function
    df['DeMax SMA'] = sma(df['DeMax'], window_size)
    df['DeMin SMA'] = sma(df['DeMin'], window_size)
    DeM_metric = df['DeMax SMA'] / (df['DeMax SMA'] + df['DeMin SMA'])
    df['DeM'] = DeM_metric
    # df.dropna(inplace=True)
    return df.DeM[-2]


def dictionary_create(ticker_list):
    dict_dem = {}
    for ticker in ticker_list:
        dict_dem[ticker] = round(DeM(ticker), 4)
    return dict_dem


def sort_dict(dict1, reverse=False):
    sorted_by_values = sorted(dict1.items(), key=lambda x: x[1], reverse=reverse)
    sorted_by_values = dict(sorted_by_values)
    return sorted_by_values



dict_create = dictionary_create(tickers)
low_sort_dict = sort_dict(dict_create)
high_sort_dict = sort_dict(dict_create, reverse=True)
