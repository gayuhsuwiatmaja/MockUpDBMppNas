import pathlib
import utils.display as udisp
import os
import streamlit as st
import detail_depan.StatistikLayanan as StatistikLayanan
import pandas as pd

def write():
    #udisp.title_awesome("Statistik Pengguna Layanan di lingkungan MPP Kota Bogor")
    st.title("Statistik Pengguna Layanan per Instansi")
    
    # path ini dipake utk upload ke github
    # path = 'Bulan/'
    
    path = 'C:/Users/User/.spyder-py3/MockUpDBMppNas/Bulan/'
   
    
    #dapatkan semua file xlsx dlm sebuah folder
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.xlsx' in file:
                files.append(os.path.join(r, file))  
                
    #dapatkan semua nama files yang ekstensi xlsx
    z = []
    for f in files:
        base=os.path.basename(f)
        a = os.path.splitext(base)[0]
        z.append(a) 
    
    # dipake jika diupload ke github
    # xlsx = pd.ExcelFile('daftar mpp.xlsx')   

    xlsx = pd.ExcelFile('C:/Users/User/.spyder-py3/MockUpDBMppNas/depan/daftar mpp.xlsx')         
    df = xlsx.parse(sheet_name = 'Ark1')
    
    '''
    #hilangkan index paling kiri
    blankIndex=[''] * len(df)
    df.index=blankIndex
    '''
    
    #ambil value masing2 column dalam dataframe. Yg mana dataframeny ambil dari Excel
    # category = list(df['Category'])         
    # option1 = st.selectbox('Pilih es1', TmbahSemuaEs1['eselon_1'].unique())
    option2 = st.selectbox('Pilih Lokasi MPP', df['Nama MPP'].unique())        
    nama_mpp = str(option2)
           
    option1 = st.selectbox('Pilih Bulan', z)
    bulan = str(option1)
    # st.write("Statistik Pengguna Layanan")
    StatistikLayanan.StatLayanan_main(bulan,nama_mpp)

    # st.write("@avkashchauhan")