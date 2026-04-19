import streamlit as st
import speedtest
from PIL import Image
import os

# پیج کنفیگریشن
st.set_page_config(page_title="Skill Up by Kar e Kamal", page_icon="🚀", layout="centered")

# پروفیشنل ڈیزائن
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1 { color: #1a4a7a; text-align: center; font-family: 'Arial Black', sans-serif; margin-bottom: 0px; }
    h3 { color: #f39200; text-align: center; margin-top: 0px; font-size: 18px; }
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

# اکیڈمی کا نام اور ٹائٹل
st.markdown("<h1>Skill Up by Kar e Kamal</h1>", unsafe_allow_html=True)
st.markdown("<h3>Digital Learning Institution</h3>", unsafe_allow_html=True)

if 'button_text' not in st.session_state:
    st.session_state.button_text = "GO"

st.write("##")
if st.button(st.session_state.button_text):
    st.session_state.button_text = "AGAIN"
    
    try:
        with st.spinner('براہ کرم انتظار کریں، آپ کا انٹرنیٹ چیک کیا جا رہا ہے...'):
            # سپیڈ ٹیسٹ انجن
            s = speedtest.Speedtest(secure=True)
            s.get_best_server()
            s.download(threads=None)
            s.upload(threads=None)
            res = s.results.dict()

            # ڈیٹا نکالنا
            download = res['download'] / 1_000_000
            upload = res['upload'] / 1_000_000
            ping = res['ping']
            jitter = abs(ping * 0.1) # Jitter کا تخمینہ

            # رزلٹ ڈسپلے
            st.write("---")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Ping", f"{ping:.0f} ms")
            col2.metric("Jitter", f"{jitter:.1f} ms")
            col3.metric("Download", f"{download:.1f} Mbps")
            col4.metric("Upload", f"{upload:.1f} Mbps")

            st.success("ٹیسٹ مکمل ہو گیا!")
            
            # ٹیکنیکل تفصیلات
            st.markdown(f"""
                <p style='text-align:center; font-size:12px; color:gray;'>
                <b>IP:</b> {res['client']['ip']} | <b>ISP:</b> {res['client']['isp']}<br>
                Powered by Speedtest Technology — LLC by Ookla
                </p>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error("نیٹ ورک ٹائم آؤٹ۔ براہ کرم دوبارہ کوشش کریں۔")

# فوٹر
st.markdown(f"""
    <div class="footer">
        <p><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up by Kar e Kamal</p>
        <p style='color: #f39200;'>WhatsApp: +44 7704 578383</p>
    </div>
    """, unsafe_allow_html=True)