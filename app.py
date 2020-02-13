import streamlit as st

import utils.display as udisp


import depan.HlmnDpnStatLayanan
import depan.HlmnDpnStatLayananDetail
import depan.IKM
import depan.Rekap

MENU = {
    "Statistik Pengguna Layanan per Instansi" : depan.HlmnDpnStatLayanan,
    "Statistik Pengguna Layanan per Jenis Layanan" : depan.HlmnDpnStatLayananDetail,
    "Indeks Kepuasan Masyarakat" : depan.IKM,
    "Peta Rekapitulasi MPP Nasional" : depan.Rekap
}

def main():
    st.sidebar.title("Silahkan Pilih Menu...")
    menu_selection = st.sidebar.radio("Silahkan Pilih...", list(MENU.keys()))
    max_width_str = f"max-width: 100%;"
    st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)
    
    menu = MENU[menu_selection]
    udisp.render_page(menu)
        

if __name__ == "__main__":
    main()
