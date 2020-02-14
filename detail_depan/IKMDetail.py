import streamlit as st
from datetime import datetime

import utils.display as display
import utils.globalDefine as globalDefine
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import plotly.graph_objects as go
from PIL import Image


def IKMDetail_main(bulan,nama_mpp):
    
    # kl upload di github
    xlsx = pd.ExcelFile('IKM/'+ bulan +'.xlsx')
    # xlsx = pd.ExcelFile('C:/Users/User/.spyder-py3/MockUpDBMppNas/IKM/'+ bulan +'.xlsx')
    df = xlsx.parse(sheet_name = 'Ark1')
    
    #hilangkan index paling kiri
    blankIndex=[''] * len(df)
    df.index=blankIndex
    
    #ambil value masing2 column dalam dataframe. Yg mana dataframeny ambil dari Excel
    category = list(df['Category'])
    interval_nilai = list(df['Interval Nilai'])

    bar_heights = [10, 12, 15, 19, 25, 28, 31, 33, 43, 50, 64, 72, 88, 105, 98,76,67,78,57,80,98,76,54,35,67,87]
    
    bins = [0, 64.99, 76.60, 88.30, 100]
    labels = ['Tidak Baik', 'Kurang Baik', 'Baik', 'Sangat Baik']
    
    colors = {'Tidak Baik': 'red',
              'Kurang Baik': 'yellow',
              'Baik': 'green',
              'Sangat Baik': 'blue'}
    
    # Build dataframe
    df = pd.DataFrame({'y': interval_nilai,
                       'x': category,
                       'label': pd.cut(interval_nilai, bins=bins, labels=labels)})
    
    bars = []
    for label, label_df in df.groupby('label'):
        bars.append(go.Bar(x=label_df.x,
                           y=label_df.y,
                           name=label,
                           marker={'color': colors[label]}))
    
    ab = go.FigureWidget(data=bars)
    ab.update_layout(barmode='group')
    ab.update_layout(title_text='Hasil Indeks Kepuasan Masyarakat di ' + nama_mpp + ' untuk bulan '+ bulan)
    st.plotly_chart(ab)
    
    # kl diupload ke github
    img = Image.open("depan/Permenpan 14 tahun 2017 ttg Survey IKM.jpg")
    # img = Image.open("C:/Users/User/.spyder-py3/MockUpDBMppNas/depan/Permenpan 14 tahun 2017 ttg Survey IKM.jpg")
    st.write("Panduan Survey IKM berdasarkan Permanpan 14 tahun 2017")
    st.image(img,width = 400)
 
    '''
    bins = [0, 20, 40, 80, 200]
    labels = ['Ugly', 'Bad', 'Good', 'Great']

    colors = {'Ugly': 'red',
              'Bad': 'orange',
              'Good': 'lightgreen',
              'Great': 'darkgreen'}
    df = pd.DataFrame({'y': int_interval_nilai,
                   'x': category,
                   'label': pd.cut(int_interval_nilai, bins=bins, labels=labels)})

    bars = []
    for label, label_df in df.groupby('label'):
        bars.append(go.Bar(x=label_df.x,
                           y=label_df.y,
                           name=labels,
                           marker={'color': colors[labels]}))
    '''
    
    '''
    fig = go.Figure(data=[
        go.Bar(name="Nilai IKM", x=category, y=interval_nilai, text = interval_nilai , textposition = 'outside')
        
    ])
    '''
    
    '''
    # Change the bar mode
   
    fig.update_layout(barmode='group')
    fig.update_layout(title_text='Hasil Indeks Kepuasan Masyarakat di ' + bulan, autosize = True, width=1500, height=800)
    
    # st.plotly_chart(fig)
    
    ab = go.FigureWidget(data=bars)
    st.plotly_chart(ab)
    '''
