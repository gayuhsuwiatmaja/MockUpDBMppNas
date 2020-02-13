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
import os
import folium
from folium import IFrame
from statistics import mean
import branca


def RekapDetail_main(bulan):
    
    # kl di github pake ini:
    path2 = 'statrekap/'
    # path2 = 'C:/Users/User/.spyder-py3/MockUpDBMppNas/statrekap/'
     
    #dapatkan semua file xlsx dlm sebuah folder
    files2 = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path2):
        for file in f:
            if '.xlsx' in file:
                files2.append(os.path.join(r, file))  
                
    #dapatkan semua nama files yang ekstensi xlsx
    z2 = []
    for f in files2:
        base2 =os.path.basename(f)
        a2 = os.path.splitext(base2)[0]
        z2.append(a2) 
        
    # kl di github
    xlsx2 = pd.ExcelFile('statrekap/'+ bulan +'.xlsx')
    # xlsx2 = pd.ExcelFile('C:/Users/User/.spyder-py3/MockUpDBMppNas/statrekap/'+ bulan +'.xlsx')
    df2 = xlsx2.parse(sheet_name = 'bulan')
    
    
    
    #hilangkan index paling kiri
    blankIndex=[''] * len(df2)
    df2.index=blankIndex
    
    # ambil value masing2 column dalam dataframe. Yg mana dataframeny ambil dari Excel
    nama_mpp2 = list(df2['nama_mpp'])
    lat2 = list(df2['lat'])
    long2 = list(df2['long'])
    # jml_instansi = list(df2['jml_instansi'])
    # jml_layanan = list(df2['jml_layanan'])
    # tot_booking = list(df2['total_booking'])
    # tot_pengunjung = list(df2['total_pengunjung'])
    # tot_sdh_terlayani = list(df2['total_sudah_terlayani'])
    # tot_tdk_terpanggil = list(df2['total_tidak_terpanggil'])
    # tot_hasil_survey = list(df2['hasil_survey_IKM'])
    
    def fancy_html(row):
        i = row
        
        nama_mpp2 = df2['nama_mpp'].iloc[i]
        jml_instansi = df2['jml_instansi'].iloc[i]
        jml_layanan = df2['jml_layanan'].iloc[i]
        tot_booking = df2['total_booking'].iloc[i]
        tot_pengunjung = df2['total_pengunjung'].iloc[i]
        tot_sdh_terlayani = df2['total_sudah_terlayani'].iloc[i]
        tot_tidak_terpanggil = df2['total_tidak_terpanggil'].iloc[i]
        tot_hasil_survey = df2['hasil_survey_IKM'].iloc[i]
        
        left_col_colour = "#2A799C"
        right_col_colour = "#C5DCE7"
    
        html3 = """<!DOCTYPE html>
            <html>
            
            <head>
            <h4 style="margin-bottom:0"; width="700px">Rekap Statistik pada bulan {} di {}</h4>""".format(bulan,nama_mpp2) +"""
            
            </head>
                <table style="height: 126px; width: 350px;">
            <tbody>
            <tr>
            <td style="width: 200px;background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Jumlah Instansi</span></td>
            <td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(jml_instansi) + """
            </tr>
            <tr>
            <td style="width: 200px;background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Jumlah Layanan</span></td>
            <td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(jml_layanan) + """
            </tr>
            <tr>
            <td style="width: 200px;background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Total yang sudah booking</span></td>
            <td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(tot_booking) + """
            </tr>
            <tr>
            <td style="width: 200px;background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Total pengunjung yang membutuhkan layanan</span></td>
            <td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(tot_pengunjung) + """
            </tr>
            <tr>
            <td style="width: 200px;background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Total pengunjung yang sudah terlayani</span></td>
            <td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(tot_sdh_terlayani) + """
            </tr>
            <tr>
            <td style="width: 200px;background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Total Pengunjung yang tidak terlayani</span></td>
            <td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(tot_tidak_terpanggil) + """
            </tr>
            <tr>
            <td style="width: 200px;background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Hasil Survey IKM</span></td>
            <td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(tot_hasil_survey) + """
            </tr>
            </tbody>
            </table>
            </html>
            """
        
        return html3
    
    m3 = folium.Map(location=(mean(lat2),mean(long2)), zoom_start=5, control_scale=True, width='100%', tiles='OpenStreetMap')
    
    for i in range(len(df2)):
        html4 = fancy_html(i)
     
        iframe = branca.element.IFrame(html=html4,width=400,height=300)
        popup = folium.Popup(iframe,parse_html=True)
        
        folium.Marker(location = (lat2[i],long2[i]),popup=popup,icon=folium.Icon(color='green'),tooltip = nama_mpp2[i]).add_to(m3)
    
    st.markdown(m3._repr_html_(), unsafe_allow_html=True)
