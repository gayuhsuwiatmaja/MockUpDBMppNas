import streamlit as st

import utils.display as udisp


import depan.HlmnDpnStatLayanan
import depan.HlmnDpnStatLayananDetail
import depan.IKM


MENU = {
    "Statistik Pengguna Layanan per Instansi" : depan.HlmnDpnStatLayanan,
    "Statistik Pengguna Layanan per Jenis Layanan" : depan.HlmnDpnStatLayananDetail,
    "Indeks Kepuasan Masyarakat" : depan.IKM,
}

def main():
    st.sidebar.title("Silahkan Pilih Menu...")
    menu_selection = st.sidebar.radio("Silahkan Pilih...", list(MENU.keys()))

    menu = MENU[menu_selection]
    udisp.render_page(menu)
        

if __name__ == "__main__":
    main()