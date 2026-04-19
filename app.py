import streamlit as st
from streamlit_javascript import st_javascript
from PIL import Image

# پیج کنفیگریشن
st.set_page_config(page_title="Skill Up Speed Test", page_icon="🚀", layout="centered")

# سپیڈو میٹر اور ڈیزائن (CSS)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        background: #1a73e8; color: white; border-radius: 50%; 
        width: 130px; height: 130px; font-size: 26px; font-weight: bold;
        display: block; margin: auto; border: none; transition: 0.3s;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    .stButton>button:hover { transform: scale(1.05); background: #1765cc; }
    
    /* سپیڈو میٹر اسٹائل */
    .gauge-container {
        width: 300px; height: 150px; border: 12px solid #f1f3f4;
        border-top: 12px solid #34a853; border-radius: 300px 300px 0 0;
        margin: 30px auto; position: relative; text-align: center;
    }
    .speed-val { font-size: 50px; font-weight: bold; color: #202124; margin-top: 30px; }
    .footer { text-align: center; margin-top: 50px; border-top: 1px solid #eee; padding: 20px; color: #5f6368; }
    </style>
    """, unsafe_allow_html=True)

# لوگو
try:
    img = Image.open("logo.jpg")
    st.image(img, width=160)
except:
    pass

st.markdown("<h1 style='text-align:center;'>Skill Up Speed Test</h1>", unsafe_allow_html=True)

# بٹن کی لاجک (GO / AGAIN)
if 'btn_state' not in st.session_state:
    st.session_state.btn_state = "GO"

st.write("##")
run_test = st.button(st.session_state.btn_state)

# جاوا اسکرپٹ: یہ آپ کے موبائل/کمپیوٹر کے براؤزر سے براہ راست ٹیسٹ کرے گا
js_speed_logic = """
    async function getUserInternetSpeed() {
        const start = Date.now();
        // براؤزر کے ذریعے فائل ڈاؤن لوڈ کرنا تاکہ آپ کے انٹرنیٹ کی سپیڈ معلوم ہو سکے
        const response = await fetch('https://upload.wikimedia.org/wikipedia/commons/2/2d/Snake_River_%285mb%29.jpg?nocache=' + Math.random());
        const blob = await response.blob();
        const end = Date.now();
        
        const duration = (end - start) / 1000;
        const bitsLoaded = blob.size * 8;
        const speedMbps = (bitsLoaded / (duration * 1024 * 1024)).toFixed(2);
        
        // آپ کی آئی پی اور لوکل سرور کی معلومات
        const ipRes = await fetch('https://ipapi.co/json/');
        const ipData = await ipRes.json();
        
        return { speed: speedMbps, ip: ipData.ip, provider: ipData.org, city: ipData.city };
    }
    getUserInternetSpeed();
"""

if run_test:
    st.session_state.btn_state = "AGAIN"
    with st.spinner('آپ کے موبائل/کمپیوٹر کی سپیڈ چیک کی جا رہی ہے...'):
        # جاوا اسکرپٹ رزلٹ حاصل کرنا
        res = st_javascript(js_speed_logic)
        
        if res and 'speed' in res:
            # سپیڈو میٹر شو کرنا
            st.markdown(f"""
                <div class="gauge-container">
                    <div class="speed-val">{res['speed']}</div>
                    <div style="color:gray; font-size:18px;">Mbps</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("---")
            col1, col2 = st.columns(2)
            col1.metric("اصلی ڈاؤن لوڈ سپیڈ", f"{res['speed']} Mbps")
            col2.metric("آپ کی آئی پی (IP)", res['ip'])
            
            st.info(f"**ISP:** {res['provider']} | **Location:** {res['city']}")
            st.success("ٹیسٹ مکمل ہو گیا! یہ آپ کے اپنے انٹرنیٹ کنکشن کی سپیڈ ہے۔")

# فوٹر
st.markdown(f"""
    <div class="footer">
        <p><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up Digital Academy</p>
    </div>
    """, unsafe_allow_html=True)