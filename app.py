import streamlit as st
import speedtest
from PIL import Image
import os

# پیج کنفیگریشن
st.set_page_config(page_title="Skill Up Internet Speed Test", page_icon="🚀", layout="centered")

# CSS (پہلے والی ہی ہے)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    h1 { color: #1a4a7a; text-align: center; font-family: 'Arial Black', sans-serif; }
    .stButton>button {
        background: linear-gradient(45deg, #1a4a7a, #f39200);
        color: white; border-radius: 50%; width: 160px; height: 160px;
        font-size: 28px; font-weight: bold; border: 5px solid #fff;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.3); display: block; margin: auto; transition: 0.5s;
    }
    .footer { text-align: center; margin-top: 50px; padding: 25px; border-top: 3px solid #f39200; background-color: #f9f9f9; border-radius: 10px; }
    [data-testid="stMetricValue"] { color: #f39200; font-size: 40px; }
    </style>
    """, unsafe_allow_html=True)

# لوگو
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    try:
        img = Image.open("logo.jpg")
        st.image(img, width=250)
    except:
        st.write("### Skill Up")

st.markdown("<h1>Skill Up Internet Speed Test</h1>", unsafe_allow_html=True)
st.write("##")
go_button = st.button("GO")

if go_button:
    try:
        status_text = st.empty()
        status_text.info("سپیڈ ٹیسٹ انجن لوڈ ہو رہا ہے...")
        
        # یہاں ہم نے تبدیلی کی ہے تاکہ کنکشن فیل نہ ہو
        s = speedtest.Speedtest(secure=True) 
        
        status_text.info("بہترین سرور تلاش کیا جا رہا ہے...")
        s.get_best_server()
        
        status_text.info("ڈاؤن لوڈنگ سپیڈ (Mbps)...")
        s.download(threads=1) # تھریڈ کم کرنے سے ایرر کے چانس کم ہوتے ہیں
        
        status_text.info("اپ لوڈنگ سپیڈ (Mbps)...")
        s.upload(threads=1)
        
        results = s.results.dict()
        
        status_text.success("ٹیسٹ مکمل ہو گیا!")
        
        st.write("---")
        res_col1, res_col2 = st.columns(2)
        res_col1.metric("Download", f"{results['download'] / 1_000_000:.2f} Mbps")
        res_col2.metric("Upload", f"{results['upload'] / 1_000_000:.2f} Mbps")
        
        st.metric("Ping", f"{results['ping']:.0f} ms", delta_color="inverse")

    except Exception as e:
        st.error(f"سرور ابھی جواب نہیں دے رہا۔ براہ کرم 10 سیکنڈ بعد دوبارہ 'GO' دبائیں۔")
        # یہ لائن صرف آپ کی معلومات کے لیے ہے تاکہ پتا چلے اصل مسئلہ کیا ہے
        # st.write(f"Technical Detail: {e}")

# فوٹر
st.markdown(f"""
    <div class="footer">
        <h3 style='color: #1a4a7a; margin-bottom: 5px;'>Shahid Mahmood Cheema</h3>
        <p style='margin: 0;'><b>CEO - Skill Up Digital Academy</b></p>
        <p style='color: #f39200; font-size: 18px; margin: 5px;'>📞 WhatsApp: +44 7704 578383</p>
    </div>
    """, unsafe_allow_html=True)