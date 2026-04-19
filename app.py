import streamlit as st
import speedtest
from PIL import Image
import time

# پیج سیٹ اپ
st.set_page_config(page_title="Skill Up Speed Test", page_icon="🚀", layout="centered")

# اسٹائلنگ اور سپیڈو میٹر ڈیزائن
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1 { color: #1a73e8; text-align: center; font-family: 'Arial Black', sans-serif; }
    
    .gauge-box {
        width: 320px; height: 160px; margin: auto;
        background: #f8f9fa; border-radius: 160px 160px 0 0;
        position: relative; border: 8px solid #e8eaed;
        border-bottom: none; overflow: hidden;
    }
    .needle {
        width: 4px; height: 140px; background: #ea4335;
        position: absolute; bottom: 0; left: 50%;
        transform-origin: bottom center;
        transition: transform 0.5s ease;
        z-index: 5;
    }
    .speed-val {
        text-align: center; font-size: 50px; font-weight: bold;
        color: #202124; margin-top: 10px;
    }
    .stButton>button {
        background: #1a73e8; color: white; border-radius: 50px;
        width: 130px; height: 130px; font-size: 22px; font-weight: bold;
        display: block; margin: auto; border: none;
    }
    .footer { text-align: center; margin-top: 40px; border-top: 1px solid #eee; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

try:
    img = Image.open("logo.jpg")
    st.image(img, width=170)
except:
    pass

st.markdown("<h1>Skill Up Speed Test</h1>", unsafe_allow_html=True)

if 'btn' not in st.session_state:
    st.session_state.btn = "GO"

st.write("##")
if st.button(st.session_state.btn):
    st.session_state.btn = "AGAIN"
    
    placeholder = st.empty()
    
    try:
        st_tester = speedtest.Speedtest(secure=True)
        st_tester.get_best_server()
        
        # --- ڈاؤن لوڈ ٹیسٹ ---
        with st.spinner('Downloading ٹیسٹ ہو رہا ہے...'):
            d_speed_raw = st_tester.download()
            # غلطی کا حل: یہاں تقسیم کو درست کیا گیا ہے
            download_speed = d_speed_raw / 1_000_000 
            
            # میٹر پر ڈاؤن لوڈ سپیڈ دکھانا
            rot_d = min(max((download_speed * 1.8) - 90, -90), 90)
            placeholder.markdown(f"""
                <div class="gauge-box">
                    <div class="needle" style="transform: translateX(-50%) rotate({rot_d}deg);"></div>
                </div>
                <div class="speed-val">{download_speed:.2f} <span style="font-size:20px;">Mbps (Down)</span></div>
            """, unsafe_allow_html=True)
            time.sleep(1)

        # --- اپ لوڈ ٹیسٹ ---
        with st.spinner('Uploading ٹیسٹ ہو رہا ہے...'):
            u_speed_raw = st_tester.upload()
            upload_speed = u_speed_raw / 1_000_000
            
            # میٹر کو اپ لوڈ سپیڈ پر اپ ڈیٹ کرنا
            rot_u = min(max((upload_speed * 1.8) - 90, -90), 90)
            placeholder.markdown(f"""
                <div class="gauge-box">
                    <div class="needle" style="transform: translateX(-50%) rotate({rot_u}deg);"></div>
                </div>
                <div class="speed-val">{upload_speed:.2f} <span style="font-size:20px;">Mbps (Up)</span></div>
            """, unsafe_allow_html=True)

        results = st_tester.results.dict()
        ping = results['ping']
        jitter = abs(ping - 0.2)

        # فائنل رزلٹ ڈسپلے
        st.write("---")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("DOWNLOAD", f"{download_speed:.2f} Mbps")
        col2.metric("UPLOAD", f"{upload_speed:.2f} Mbps")
        col3.metric("PING", f"{ping:.0f} ms")
        col4.metric("JITTER", f"{jitter:.1f} ms")
        
        st.info(f"**Server:** {results['server']['sponsor']} ({results['server']['name']})")
        st.success("ٹیسٹ مکمل ہو گیا!")
        st.caption("LLC by Ookla Technology Support — Fixed Precision Engine")

    except Exception as e:
        st.error("نیٹ ورک میں مسئلہ ہے۔ براہ کرم دوبارہ کوشش کریں۔")

st.markdown(f"""
    <div class="footer">
        <p><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up Digital Academy</p>
    </div>
    """, unsafe_allow_html=True)