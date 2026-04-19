import streamlit as st
from streamlit_javascript import st_javascript
from PIL import Image

# پیج کنفیگریشن
st.set_page_config(page_title="Skill Up Speed Test", page_icon="🚀", layout="centered")

# سپیڈو میٹر اور بٹن کا ڈیزائن (CSS)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        background: linear-gradient(45deg, #1a73e8, #4285f4);
        color: white; border-radius: 50%; width: 130px; height: 130px;
        font-size: 24px; font-weight: bold; border: none; display: block; margin: auto;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2); transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); }
    
    /* سپیڈو میٹر گرافک */
    .gauge-container {
        width: 280px; height: 140px; border: 12px solid #f1f3f4;
        border-top: 12px solid #34a853; border-radius: 280px 280px 0 0;
        margin: 20px auto; position: relative; text-align: center;
    }
    .speed-val { font-size: 48px; font-weight: bold; color: #202124; margin-top: 25px; }
    .footer { text-align: center; margin-top: 50px; border-top: 1px solid #eee; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# لوگو
try:
    img = Image.open("logo.jpg")
    st.image(img, width=160)
except:
    pass

st.markdown("<h1 style='text-align:center;'>Skill Up Speed Test</h1>", unsafe_allow_html=True)

# بٹن کا نام بدلنا
if 'btn_txt' not in st.session_state:
    st.session_state.btn_txt = "GO"

st.write("##")
run_btn = st.button(st.session_state.btn_txt)

# سپیڈ ٹیسٹ لاجک (براؤزر بیسڈ)
js_code = """
    async function test() {
        const start = Date.now();
        const res = await fetch('https://upload.wikimedia.org/wikipedia/commons/2/2d/Snake_River_%285mb%29.jpg?n=' + Math.random());
        const blob = await res.blob();
        const end = Date.now();
        const duration = (end - start) / 1000;
        const mbps = ((blob.size * 8) / (duration * 1024 * 1024)).toFixed(2);
        
        const ipFetch = await fetch('https://ipapi.co/json/');
        const ipData = await ipFetch.json();
        
        return { speed: mbps, ip: ipData.ip, isp: ipData.org };
    }
    test();
"""

if run_btn:
    st.session_state.btn_txt = "AGAIN"
    with st.spinner('ڈیٹا اکٹھا کیا جا رہا ہے...'):
        result = st_javascript(js_code)
        
        if result and 'speed' in result:
            # سپیڈو میٹر ڈسپلے
            st.markdown(f"""
                <div class="gauge-container">
                    <div class="speed-val">{result['speed']}</div>
                    <div style="color:gray;">Mbps</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("---")
            col1, col2 = st.columns(2)
            col1.metric("Download", f"{result['speed']} Mbps")
            col2.metric("Your IP", result['ip'])
            
            st.info(f"**ISP:** {result['isp']}")
            st.success("ٹیسٹ مکمل ہو گیا!")

# فوٹر
st.markdown(f"""
    <div class="footer">
        <p><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up Digital Academy</p>
    </div>
    """, unsafe_allow_html=True)