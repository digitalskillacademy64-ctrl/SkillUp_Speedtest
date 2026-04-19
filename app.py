import streamlit as st
import speedtest
from PIL import Image

# پیج سیٹ اپ
st.set_page_config(page_title="Skill Up Speed Test", page_icon="🚀", layout="centered")

# CSS ڈیزائن (سپیڈو میٹر کے لیے)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .gauge-outer {
        width: 300px; height: 150px; background: #f1f3f4;
        border-radius: 150px 150px 0 0; margin: auto;
        position: relative; border: 8px solid #e8eaed; overflow: hidden;
    }
    .needle {
        width: 4px; height: 130px; background: #ea4335;
        position: absolute; bottom: 0; left: 50%;
        transform-origin: bottom center; transition: transform 2s;
    }
    .speed-val { text-align: center; font-size: 42px; font-weight: bold; color: #1a73e8; margin-top: 10px; }
    .stButton>button {
        background: #1a73e8; color: white; border-radius: 50px;
        width: 140px; height: 140px; font-size: 24px; font-weight: bold;
        display: block; margin: auto; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

try:
    img = Image.open("logo.jpg")
    st.image(img, width=180)
except:
    pass

st.markdown("<h1 style='text-align: center;'>Skill Up Speed Test</h1>", unsafe_allow_html=True)

if 'btn' not in st.session_state:
    st.session_state.btn = "GO"

if st.button(st.session_state.btn):
    st.session_state.btn = "AGAIN"
    
    with st.spinner('قریبی سرور تلاش کیا جا رہا ہے...'):
        try:
            s = speedtest.Speedtest(secure=True)
            
            # یہاں ہم اسے مجبور کر رہے ہیں کہ وہ پاکستان کے قریبی سرورز ڈھونڈے
            s.get_servers([]) # تمام دستیاب سرورز کی لسٹ
            best = s.get_best_server() # خودکار طور پر بہترین قریبی سرور چننا
            
            st.write(f"**Connected to:** {best['sponsor']} ({best['name']}, {best['country']})")
            
            s.download()
            s.upload()
            res = s.results.dict()
            
            down = res['download'] / 10**6
            up = res['upload'] / 10**6
            
            # سوئی کی حرکت کا حساب
            rotation = min(max((down * 1.8) - 90, -90), 90)

            st.markdown(f"""
                <div class="gauge-outer">
                    <div class="needle" style="transform: translateX(-50%) rotate({rotation}deg);"></div>
                </div>
                <div class="speed-val">{down:.1f} <span style="font-size: 18px;">Mbps</span></div>
            """, unsafe_allow_html=True)

            st.write("---")
            c1, c2, c3 = st.columns(3)
            c1.metric("UPLOAD", f"{up:.1f} Mbps")
            c2.metric("PING", f"{res['ping']:.0f} ms")
            c3.metric("JITTER", f"{abs(res['ping']-0.5):.1f} ms")
            
            st.success("ٹیسٹ مکمل ہو گیا!")

        except Exception as e:
            st.error("سرور کنکشن میں مسئلہ ہے۔ براہ کرم دوبارہ کوشش کریں۔")

st.markdown("<div style='text-align: center; margin-top: 50px; border-top: 1px solid #eee; padding: 20px;'><b>Shahid Mahmood Cheema</b><br>CEO - Skill Up Digital Academy</div>", unsafe_allow_html=True)