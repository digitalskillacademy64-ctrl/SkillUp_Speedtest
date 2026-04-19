import streamlit as st
from streamlit_javascript import st_javascript
from PIL import Image

# پیج کنفیگریشن
st.set_page_config(page_title="Skill Up Speed Test", page_icon="🚀", layout="centered")

# سپیڈو میٹر اور ڈیزائن کے لیے CSS
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1 { color: #202124; text-align: center; font-family: 'Google Sans', sans-serif; }
    
    /* سپیڈو میٹر ڈیزائن */
    .speed-gauge {
        width: 300px; height: 150px;
        border: 15px solid #f3f3f3;
        border-top: 15px solid #1a73e8;
        border-radius: 50% 50% 0 0;
        margin: auto;
        position: relative;
        transition: transform 1s ease-in-out;
    }
    .speed-value {
        text-align: center; font-size: 48px; font-weight: bold; color: #1a73e8; margin-top: -40px;
    }
    .unit { font-size: 18px; color: #70757a; }
    
    .stButton>button {
        background: #1a73e8; color: white; border-radius: 50px;
        padding: 10px 40px; font-size: 20px; font-weight: bold;
        display: block; margin: auto; border: none;
    }
    .footer { text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# لوگو
try:
    img = Image.open("logo.jpg")
    st.image(img, width=180)
except:
    pass

st.markdown("<h1>Skill Up Speed Test</h1>", unsafe_allow_html=True)

if 'button_label' not in st.session_state:
    st.session_state.button_label = "GO"

st.write("##")
run_test = st.button(st.session_state.button_label)

# جاوا اسکرپٹ اسکرپٹ: یہ آپ کے براؤزر سے ریئل ڈیٹا ڈاؤن لوڈ کرے گا
test_script = """
    async function measureSpeed() {
        const start = Date.now();
        // 5MB کی فائل ڈاؤن لوڈ کر کے چیک کرنا تاکہ سپیڈ درست آئے
        const response = await fetch('https://upload.wikimedia.org/wikipedia/commons/2/2d/Snake_River_%285mb%29.jpg?cache=' + Math.random());
        const blob = await response.blob();
        const end = Date.now();
        
        const duration = (end - start) / 1000;
        const sizeInBits = blob.size * 8;
        const speedMbps = (sizeInBits / (duration * 1024 * 1024)).toFixed(2);
        
        // IP اور سرور کی تفصیلات
        const ipRes = await fetch('https://api.ipify.org?format=json');
        const ipData = await ipRes.json();
        
        return { speed: speedMbps, ip: ipData.ip };
    }
    measureSpeed();
"""

if run_test:
    st.session_state.button_label = "AGAIN"
    with st.spinner('Checking your actual internet speed...'):
        # براؤزر کے اندر ٹیسٹ چلانا
        results = st_javascript(test_script)
        
        if results and 'speed' in results:
            # سپیڈو میٹر ویو
            st.markdown(f"""
                <div class="speed-gauge"></div>
                <div class="speed-value">{results['speed']} <span class="unit">Mbps</span></div>
            """, unsafe_allow_html=True)
            
            st.write("---")
            col1, col2 = st.columns(2)
            col1.metric("Download Speed", f"{results['speed']} Mbps")
            col2.metric("Your IP", results['ip'])
            
            st.success("ٹیسٹ مکمل ہو گیا! یہ آپ کے براؤزر کی اصل سپیڈ ہے۔")
            st.caption("LLC by Ookla Technology Support")

# فوٹر
st.markdown(f"""
    <div class="footer">
        <p><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up Digital Academy</p>
    </div>
    """, unsafe_allow_html=True)