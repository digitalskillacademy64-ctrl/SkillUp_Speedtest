import streamlit as st
from streamlit_javascript import st_javascript
from PIL import Image

# پیج سیٹ اپ
st.set_page_config(page_title="Skill Up Speed Test", page_icon="🚀", layout="centered")

# ڈیزائن (CSS)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        background: #1a73e8; color: white; border-radius: 50%; 
        width: 120px; height: 120px; font-size: 24px; font-weight: bold;
        display: block; margin: auto; border: none; transition: 0.3s;
    }
    .gauge-box {
        text-align: center; margin: 20px auto; width: 260px; height: 130px;
        border: 10px solid #f3f3f3; border-top: 10px solid #1a73e8;
        border-radius: 200px 200px 0 0; position: relative;
    }
    .speed-display { font-size: 45px; font-weight: bold; color: #202124; margin-top: 10px; }
    .footer { text-align: center; margin-top: 40px; border-top: 1px solid #eee; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# لوگو
try:
    img = Image.open("logo.jpg")
    st.image(img, width=150)
except:
    pass

st.markdown("<h1 style='text-align:center;'>Skill Up Speed Test</h1>", unsafe_allow_html=True)

if 'label' not in st.session_state:
    st.session_state.label = "GO"

# ٹیسٹ بٹن
run_test = st.button(st.session_state.label)

# جاوا اسکرپٹ اسکرپٹ (اصلی سپیڈ کے لیے)
js_speed_test = """
    async function measure() {
        const start = Date.now();
        // 5MB کی امیج ڈاؤن لوڈ کرنا ریئل سپیڈ کے لیے
        const res = await fetch('https://upload.wikimedia.org/wikipedia/commons/2/2d/Snake_River_%285mb%29.jpg?cache=' + Math.random());
        const blob = await res.blob();
        const end = Date.now();
        const duration = (end - start) / 1000;
        const mbps = ((blob.size * 8) / (duration * 1024 * 1024)).toFixed(2);
        
        // لوکیشن اور آئی پی
        const ipRes = await fetch('https://ipapi.co/json/');
        const ipData = await ipRes.json();
        
        return { speed: mbps, ip: ipData.ip, city: ipData.city, isp: ipData.org };
    }
    measure();
"""

if run_test:
    st.session_state.label = "AGAIN"
    with st.spinner('Checking real speed...'):
        result = st_javascript(js_speed_test)
        
        if result and 'speed' in result:
            st.markdown(f'<div class="gauge-box"></div><div class="speed-display" style="text-align:center;">{result["speed"]} <span style="font-size:20px;">Mbps</span></div>', unsafe_allow_html=True)
            
            st.write("---")
            c1, c2 = st.columns(2)
            c1.metric("YOUR IP", result['ip'])
            c1.metric("LOCATION", result['city'])
            c2.metric("ISP / SERVER", result['isp'])
            c2.metric("STATUS", "Stable")
            
            st.success("ٹیسٹ مکمل ہو گیا! یہ آپ کے براؤزر کی اصل سپیڈ ہے۔")

# فوٹر
st.markdown(f"""
    <div class="footer">
        <p><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up Digital Academy</p>
    </div>
    """, unsafe_allow_html=True)