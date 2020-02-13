import pathlib
import utils.display as udisp
import os
import streamlit as st
import detail_depan.RekapDetail as RekapDetail
import pandas as pd

def write():
    # udisp.title_awesome("Compound Interest Calclator")
    # CalcEngine.calc_main("CI Calculator", "A Compound Interest Calclator")

    # st.write("@avkashchauhan")
    st.title("Peta Rekapitulasi MPP Nasional")
    
    # kl diupload ke github pake ini
    # path = 'statrekap/'
    path = 'C:/Users/User/.spyder-py3/MockUpDBMppNas/statrekap/'
    
    
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
    
     
    #ambil value masing2 column dalam dataframe. Yg mana dataframeny ambil dari Excel
    option1 = st.selectbox('Pilih Bulan', z)
    bulan = str(option1) 
    
    RekapDetail.RekapDetail_main(bulan)
    