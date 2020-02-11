import pathlib
import utils.display as udisp
import os
import streamlit as st
import detail_depan.IKMDetail as IKMDetail
import pandas as pd

def write():
    # udisp.title_awesome("Compound Interest Calclator")
    # CalcEngine.calc_main("CI Calculator", "A Compound Interest Calclator")

    # st.write("@avkashchauhan")
    st.title("Indeks Kepuasan Masyarakat")
    
    # kl diupload ke github pake ini
    # path = 'IKM/'
    path = 'C:/Users/User/.spyder-py3/MockUpDBMppNas/IKM/'
    
    
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
    
    # kl diupload ke github pake ini
    # xlsx2 = pd.ExcelFile('daftar mpp.xlsx')
    xlsx2 = pd.ExcelFile('C:/Users/User/.spyder-py3/MockUpDBMppNas/depan/daftar mpp.xlsx')            
    df2 = xlsx2.parse(sheet_name = 'Ark1')
    
    option3 = st.selectbox('Pilih Lokasi MPP', df2['Nama MPP'].unique())
    nama_mpp = str(option3)
     
    #ambil value masing2 column dalam dataframe. Yg mana dataframeny ambil dari Excel
    option1 = st.selectbox('Pilih Bulan', z)
    bulan = str(option1) 
    
    IKMDetail.IKMDetail_main(bulan,nama_mpp)