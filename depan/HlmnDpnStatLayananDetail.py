import pathlib
import utils.display as udisp
import os
import pandas as pd
import streamlit as st
import detail_depan.StatistikLayananDetail as StatistikLayananDetail

def write():
    #udisp.title_awesome("Statistik Pengguna Layanan di lingkungan MPP Kota Bogor")
    st.title("Statistik Pengguna Layanan per Jenis Layanan")
    
    # path ini dipake utk upload ke github
    path = 'Bulan 2/'
    
    # path = 'C:/Users/User/.spyder-py3/MockUpDBMppNas/Bulan 2/'
    
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
    # utk dapat nama instansi pemberi layanan
    xlsx = pd.ExcelFile('Bulan 2/desember 2019.xlsx')
    df = xlsx.parse(sheet_name = 'Ark1')
    # utk dapat nama mpp
    xlsx2 = pd.ExcelFile('depan/daftar mpp.xlsx')            
    df2 = xlsx2.parse(sheet_name = 'Ark1')
    
    # utk dapat nama instansi pemberi layanan
    # xlsx = pd.ExcelFile('C:/Users/User/.spyder-py3/MockUpDBMppNas/Bulan 2/desember 2019.xlsx')
    # df = xlsx.parse(sheet_name = 'Ark1')
    #utk dapat nama mpp
    # xlsx2 = pd.ExcelFile('C:/Users/User/.spyder-py3/MockUpDBMppNas/depan/daftar mpp.xlsx')            
    # df2 = xlsx2.parse(sheet_name = 'Ark1')
    
    
    #hilangkan index paling kiri
    blankIndex=[''] * len(df)
    df.index=blankIndex
    
    #ambil value masing2 column dalam dataframe. Yg mana dataframeny ambil dari Excel
    # category = list(df['Category'])         
    # option1 = st.selectbox('Pilih es1', TmbahSemuaEs1['eselon_1'].unique())
    option3 = st.selectbox('Pilih Lokasi MPP', df2['Nama MPP'].unique())
    nama_mpp = str(option3)
    
    option2 = st.selectbox('Pilih Instansi', df['Category'].unique())
    nama_instansi = str(option2)     
    nama_instansi_array = [option2]      
    
    option1 = st.selectbox('Pilih Bulan', z)
    bulan = str(option1)
    # st.write("Statistik Pengguna Layanan")
    # StatistikLayanan.StatLayanan_main(bulan)
    StatistikLayananDetail.StatLayananDetail_main(nama_mpp,nama_instansi,bulan,nama_instansi_array)
    st.info('Silahkan klik tombol fullscreen-enter di pojok kanan atas grafik untuk melihat grafik dengan lebih jelas')
    # st.write("@avkashchauhan")
    
    
    '''
    # hilangkan index paling kiri
    # blankIndex=[''] * len(df)
    # df.index=blankIndex
    '''
    
    # ambil value masing2 column dalam dataframe. Yg mana dataframeny ambil dari Excel
    # category = list(df['Category'])         
    # option1 = st.selectbox('Pilih es1', TmbahSemuaEs1['eselon_1'].unique())
        
