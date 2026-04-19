import streamlit as st
import speedtest
from PIL import Image
import time

# پیج کنفیگریشن
st.set_page_config(page_title="Skill Up Speed Test", page_icon="🚀", layout="centered")

# سپیڈو میٹر اور اینیمیشن کے لیے CSS
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1 { color: #1a73e8; text-align: center; font-family: 'Arial Black', sans-serif; }
    
    /* سپیڈو میٹر ڈیزائن */
    .gauge {
        width: 300px; height: 150px; margin: auto;
        background: #f1f3f4; border-radius: 150px 150px 0 0;
        position: relative; border: 10px solid #e8eaed;
        border-bottom: none; overflow: hidden;
    }
    .needle {
        width: 4px; height: 130px; background: #ea4335;
        position: absolute; bottom: 0; left: 50%;
        transform-origin: bottom center;
        transition: transform 2s cubic-bezier(0.4, 0, 0.2, 1);
        z-index: 5;
    }
    .speed-display {
        text-align: center; font-size: 45px; font-weight: bold;
        color: #202124; margin-top: 10px; font-family: 'Courier New', monospace;
    }
    
    .stButton>button {
        background: #1a73e8; color: white; border-radius: 50px;
        width: 140px; height: 140px; font-size: 24px; font-weight: bold;
        display: block; margin: auto; border: none; transition: 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover { transform: scale(1.05); background: #1765cc; }
    .footer { text-align: center; margin-top: 40px; border-top: 1px solid #eee; padding: 20px; color: #70757a; }
    </style>
    """, unsafe_allow_html=True)

# لوگو لوڈ کرنا
try:
    img = Image.open("logo.jpg")
    st.image(img, width=180)
except:
    pass

st.markdown("<h1>Skill Up Speed Test</h1>", unsafe_allow_html=True)

if 'btn_label' not in st.session_state:
    st.session_state.btn_label = "GO"

st.write("##")
if st.button(st.session_state.btn_label):
    st.session_state.btn_label = "AGAIN"
    
    with st.spinner('ڈیٹا اکٹھا کیا جا رہا ہے...'):
        try:
            # سپیڈ ٹیسٹ انجن
            st_tester = speedtest.Speedtest(secure=True)
            st_tester.get_best_server()
            
            # ٹیسٹ رن کرنا
            st_tester.download()
            st_tester.upload()
            results = st_tester.results.dict()
            
            # ڈیٹا پروسیسنگ (Mbps میں)
            download_speed = results['download'] / 10**6
            upload_speed = results['upload'] / 10**6
            ping = results['ping']
            jitter = abs(ping - 0.2)
            server_info = f"{results['server']['sponsor']} ({results['server']['name']})"

            # سپیڈو میٹر اینیمیشن (سپیڈ کے حساب سے سوئی گھمانا)
            # 0 Mbps = -90deg, 100+ Mbps = 90deg
            rotation = min(max((download_speed * 1.8) - 90, -90), 90)

            st.markdown(f"""
                <div class="gauge">
                    <div class="needle" style="transform: translateX(-50%) rotate({rotation}deg);"></div>
                </div>
                <div class="speed-display">{download_speed:.1f} <span style="font-size: 20px;">Mbps</span></div>
            """, unsafe_allow_html=True)

            st.write("---")
            
            # دیگر رزلٹ
            col1, col2, col3 = st.columns(3)
            col1.metric("UPLOAD", f"{upload_speed:.1f} Mbps")
            col2.metric("PING", f"{ping:.0f} ms")
            col3.metric("JITTER", f"{jitter:.1f} ms")
            
            st.info(f"**Server:** {server_info}")
            st.success("ٹیسٹ مکمل ہو گیا!")
            st.caption("LLC by Ookla Technology Support — Precision Engine")

        except Exception as e:
            st.error("سرور سے رابطہ نہیں ہو سکا۔ براہ کرم دوبارہ کوشش کریں۔")

# فوٹر
st.markdown(f"""
    <div class="footer">
        <p><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up Digital Academy</p>
    </div>
    """, unsafe_allow_html=True)