import streamlit as st
import speedtest
from PIL import Image
import os

# پیج سیٹ اپ
st.set_page_config(page_title="Skill Up Internet Speed Test", page_icon="🚀", layout="centered")

# گوگل جیسا کلین اور پروفیشنل ڈیزائن
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stMetric { background-color: #f8f9fa; border: 1px solid #dee2e6; padding: 15px; border-radius: 10px; text-align: center; }
    h1 { color: #202124; font-family: 'Google Sans', Arial, sans-serif; font-size: 32px; margin-bottom: 30px; }
    .stButton>button {
        background: #1a73e8; color: white; border-radius: 4px; 
        padding: 10px 24px; font-size: 16px; border: none;
        display: block; margin: auto; transition: 0.3s;
    }
    .stButton>button:hover { background: #1765cc; box-shadow: 0 1px 3px rgba(60,64,67,0.3); }
    .tech-info { font-size: 12px; color: #70757a; text-align: center; margin-top: 20px; }
    .footer { text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #e8eaed; color: #3c4043; }
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

st.markdown("<h1>Internet Speed Test</h1>", unsafe_allow_html=True)

if 'tested' not in st.session_state:
    st.session_state.tested = False

go_button = st.button("RUN SPEED TEST")

if go_button:
    try:
        with st.spinner('Checking...'):
            # ریئل سپیڈ کے لیے انجن سیٹنگز
            s = speedtest.Speedtest(secure=True)
            s.get_best_server()
            s.download(threads=None) # threads=None خودکار طریقے سے بہترین سپیڈ پکڑتا ہے
            s.upload(threads=None)
            res = s.results.dict()
            
            st.session_state.results = res
            st.session_state.tested = True

        # گوگل اسٹائل ڈسپلے
        st.write("##")
        col1, col2, col3 = st.columns(3)
        col1.metric("DOWNLOAD", f"{res['download'] / 1_000_000:.1f} Mbps")
        col2.metric("UPLOAD", f"{res['upload'] / 1_000_000:.1f} Mbps")
        col3.metric("LATENCY", f"{res['ping']:.0f} ms")

        # ٹیکنیکل تفصیلات (گوگل جیسا ویو)
        st.markdown(f"""
            <div class="tech-info">
                <p><b>Server:</b> {res['server']['name']} | <b>Sponsor:</b> {res['server']['sponsor']}</p>
                <p><b>Your IP:</b> {res['client']['ip']} | <b>Location:</b> {res['client']['country']}</p>
                <p style="font-size: 10px; margin-top:10px;">LLC by Ookla © Technology</p>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error("Connection timed out. Please try again.")

# فکسڈ فوٹر
st.markdown(f"""
    <div class="footer">
        <p><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up Digital Academy</p>
        <p style="font-size: 11px;">Testing performed via high-precision Python engines</p>
    </div>
    """, unsafe_allow_html=True)