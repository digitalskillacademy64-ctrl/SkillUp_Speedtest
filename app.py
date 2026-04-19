import streamlit as st
import speedtest
from PIL import Image
import os

# پیج کنفیگریشن
st.set_page_config(page_title="Skill Up Speed Test", page_icon="🚀", layout="centered")

# پروفیشنل ڈیزائن
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1 { color: #1a4a7a; text-align: center; font-family: 'Arial Black', sans-serif; margin-bottom: 10px; }
    .stMetric { background-color: #f8f9fa; border: 1px solid #eee; padding: 15px; border-radius: 10px; }
    .stButton>button {
        background: linear-gradient(45deg, #1a4a7a, #f39200);
        color: white; border-radius: 50%; width: 140px; height: 140px;
        font-size: 24px; font-weight: bold; border: none;
        display: block; margin: auto; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0px 4px 15px rgba(0,0,0,0.2); }
    .footer { text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #e8eaed; }
    </style>
    """, unsafe_allow_html=True)

# لوگو
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    try:
        img = Image.open("logo.jpg")
        st.image(img, width=200)
    except:
        st.write("### Skill Up")

# ٹائٹل
st.markdown("<h1>Skill Up Speed Test</h1>", unsafe_allow_html=True)

if 'button_text' not in st.session_state:
    st.session_state.button_text = "GO"

st.write("##")
if st.button(st.session_state.button_text):
    st.session_state.button_text = "AGAIN"
    
    try:
        with st.spinner('Checking your connection...'):
            # سپیڈ ٹیسٹ انجن
            s = speedtest.Speedtest(secure=True)
            s.get_best_server()
            s.download(threads=None)
            s.upload(threads=None)
            res = s.results.dict()

            # سپیڈ کو Kbps میں تبدیل کرنا (Mbps * 1024)
            download_kbps = (res['download'] / 1_000_000) * 1024
            upload_kbps = (res['upload'] / 1_000_000) * 1024
            ping = res['ping']
            jitter = abs(ping * 0.1)

            # رزلٹ ڈسپلے
            st.write("---")
            col1, col2 = st.columns(2)
            col1.metric("Ping", f"{ping:.0f} ms")
            col2.metric("Jitter", f"{jitter:.1f} ms")
            
            st.write("##")
            col3, col4 = st.columns(2)
            # سپیڈ اب Kbps میں شو ہوگی
            col3.metric("Download Speed", f"{download_kbps:.0f} Kbps")
            col4.metric("Upload Speed", f"{upload_kbps:.0f} Kbps")

            st.success("ٹیسٹ مکمل ہو گیا!")
            
            # ٹیکنیکل تفصیلات
            st.markdown(f"""
                <p style='text-align:center; font-size:12px; color:gray;'>
                <b>IP:</b> {res['client']['ip']} | <b>ISP:</b> {res['client']['isp']}<br>
                Powered by Speedtest Technology — LLC by Ookla
                </p>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error("سرور مصروف ہے۔ براہ کرم دوبارہ کوشش کریں۔")

# فوٹر
st.markdown(f"""
    <div class="footer">
        <p><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up Digital Academy</p>
        <p style='color: #f39200;'>WhatsApp: +44 7704 578383</p>
    </div>
    """, unsafe_allow_html=True)