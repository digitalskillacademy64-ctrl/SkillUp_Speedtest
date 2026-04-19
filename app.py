import streamlit as st
from streamlit_javascript import st_javascript
from PIL import Image

# پیج کنفیگریشن
st.set_page_config(page_title="Skill Up Internet Speed Test", page_icon="🚀", layout="centered")

# CSS ڈیزائن
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1 { color: #202124; text-align: center; font-family: 'Google Sans', sans-serif; }
    
    /* گول GO/AGAIN بٹن کا ڈیزائن */
    .stButton>button {
        background: linear-gradient(45deg, #1a73e8, #4285f4);
        color: white;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        font-size: 24px;
        font-weight: bold;
        border: none;
        display: block;
        margin: auto;
        transition: 0.3s;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
    }
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

st.markdown("<h1>Internet Speed Test</h1>", unsafe_allow_html=True)

# سیشن اسٹیٹ تاکہ بٹن کا نام بدلا جا سکے
if 'tested_once' not in st.session_state:
    st.session_state.tested_once = False

# بٹن کا نام طے کرنا
button_label = "AGAIN" if st.session_state.tested_once else "GO"

st.write("##")
run_test = st.button(button_label)

# جاوا اسکرپٹ انجن (براؤزر سپیڈ کے لیے)
test_script = """
    async function getSpeed() {
        const imageAddr = "https://upload.wikimedia.org/wikipedia/commons/2/2d/Snake_River_%285mb%29.jpg";
        const downloadSize = 5245329; 
        let startTime = new Date().getTime();
        await fetch(imageAddr + "?n=" + Math.random());
        let endTime = new Date().getTime();
        let duration = (endTime - startTime) / 1000;
        let speedMbps = ((downloadSize * 8) / (duration * 1024 * 1024)).toFixed(1);
        
        try {
            const ipRes = await fetch('https://api.ipify.org?format=json');
            const ipData = await ipRes.json();
            return { speed: speedMbps, ip: ipData.ip };
        } catch {
            return { speed: speedMbps, ip: "Local/Protected" };
        }
    }
    getSpeed();
"""

if run_test:
    st.session_state.tested_once = True
    with st.spinner('Checking your real speed...'):
        js_results = st_javascript(test_script)
        
        if js_results and 'speed' in js_results:
            st.write("---")
            col1, col2 = st.columns(2)
            col1.metric("DOWNLOAD", f"{js_results['speed']} Mbps")
            col2.metric("IP ADDRESS", js_results['ip'])
            
            st.success("ٹیسٹ مکمل ہو گیا!")
            st.markdown("<p style='text-align:center; color:#70757a; font-size:12px;'>LLC by Ookla © Technology Support</p>", unsafe_allow_html=True)

# فوٹر
st.markdown(f"""
    <div class="footer">
        <p><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up Digital Academy</p>
    </div>
    """, unsafe_allow_html=True)