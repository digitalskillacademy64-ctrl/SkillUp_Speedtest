import streamlit as st
import speedtest
from PIL import Image

st.set_page_config(page_title="Skill Up Speed Test", page_icon="🚀")

# سیشن اسٹیٹ بٹن کے نام کے لیے
if 'label' not in st.session_state:
    st.session_state.label = "GO"

# ڈیزائن
st.markdown("""
    <style>
    .stButton>button {
        background: #1a73e8; color: white; border-radius: 50%; 
        width: 150px; height: 150px; font-size: 24px; margin: auto; display: block;
    }
    </style>
    """, unsafe_allow_html=True)

try:
    img = Image.open("logo.jpg")
    st.image(img, width=200)
except:
    st.write("### Skill Up")

if st.button(st.session_state.label):
    st.session_state.label = "AGAIN"
    with st.spinner('Testing...'):
        s = speedtest.Speedtest(secure=True)
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        
        st.metric("Download", f"{res['download']/10**6:.1f} Mbps")
        st.metric("Upload", f"{res['upload']/10**6:.1f} Mbps")
        st.write(f"**IP:** {res['client']['ip']} | **Server:** {res['server']['name']}")
        st.caption("LLC by Ookla © Technology")