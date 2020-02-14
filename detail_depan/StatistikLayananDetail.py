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


def StatLayananDetail_main(nama_mpp,nama_instansi,bulan,nama_instansi_array):
    
    
    # kl upload di github
    xlsx = pd.ExcelFile('Bulan 2/'+ bulan +'.xlsx')
    # xlsx = pd.ExcelFile('C:/Users/User/.spyder-py3/MockUpDBMppNas/Bulan 2/'+ bulan +'.xlsx')
    df = xlsx.parse(sheet_name = 'Ark1')
    
    
    #hilangkan index paling kiri
    blankIndex=[''] * len(df)
    df.index=blankIndex
    
    #cari nama layanan yang nama instansinya dipilih di selectbox
    nama_layanan_saring = df[df['Category'].isin(nama_instansi_array)]
    nama_layanan = nama_layanan_saring['Nama Layanan']
    
    #ambil value masing2 column dalam dataframe. Yg mana dataframeny ambil dari Excel
    # ambil value kolom tertentu
    booking = list(nama_layanan_saring['Booking'])
    pengunjung_hr_ini = list(nama_layanan_saring['Pengunjung Hari Ini'])
    sudah_terlayani = list(nama_layanan_saring['Sudah Terlayani'])
    tidak_terpanggil = list(nama_layanan_saring['Tidak Terpanggil'])
    
    '''
    # jumlah x
    posisi = np.arange(len(category))
    width = 0.25
    
    #figsize untuk menentukan lebar chartnya
    fig,ax = plt.subplots(figsize = (18,5))
    bar1 = ax.bar(posisi-width,booking,width, color = 'brown')
    bar2 = ax.bar(posisi,pengunjung_hr_ini,width, color = 'blue')
    bar3 = ax.bar(posisi + width,sudah_terlayani, width, color = 'green')
    bar4 = ax.bar(posisi + width + width, tidak_terpanggil, width, color = 'red')
    
    ax.set_ylabel('Jumlah warga')
    ax.set_xlabel('Instansi')
    ax.set_title('Jumlah Warga yang dilayani per Instansi pada bulan ' + bulan)
    ax.set_xticks(posisi + width / 2)
    ax.set_xticklabels(category)
    ax.set_xticklabels(category, rotation = 45)
    
    ax.legend((bar1[0], bar2[0],bar3[0],bar4[0]), ('Booking', 'Pengunjung Hari Ini','Sudah Terlayani','Tidak Terpanggil'))
    
    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='center', va='bottom', rotation = 45)
    
    autolabel(bar1)
    autolabel(bar2)
    autolabel(bar3)
    autolabel(bar4)
    
    plt.tight_layout()
    
    st.pyplot(plt)
    '''
    
    
  
    
    fig = go.Figure(data=[
        go.Bar(name="Booking", x=nama_layanan, y=booking, text = booking , textposition = 'outside'),
        go.Bar(name="Pengunjung yang datang", x=nama_layanan, y=pengunjung_hr_ini, text=pengunjung_hr_ini , textposition = 'outside'),
        go.Bar(name="Yang sudah terlayani", x=nama_layanan, y=sudah_terlayani, text=sudah_terlayani, textposition = 'outside'),
        go.Bar(name="Yang tidak terpanggil", x=nama_layanan, y=tidak_terpanggil, text=tidak_terpanggil, textposition = 'outside')
    ])
    
    # Change the bar mode
   
    fig.update_layout(barmode='group')
    fig.update_layout(title_text='Statistik Pengguna Layanan ' + nama_mpp + ' untuk instansi ' + nama_instansi + ' di ' + bulan, autosize = True, width=1500, height=800)
    
    st.plotly_chart(fig)
    
    '''
    option1 = st.selectbox('Pilih es1', TmbahSemuaEs1['eselon_1'].unique())
    #st.write(option1)
    #convert string ke list
    listOp1 = [option1]
    #menampilkan eselon 2 kebawah yang es 1 nya berasal dari option1
    rslt_Op1 = df2[df2['eselon_1'].isin(listOp1)]
    '''
    
    
    
    
    
