import streamlit as st
import speedtest
from PIL import Image
import os

# پیج کنفیگریشن
st.set_page_config(page_title="Skill Up Internet Speed Test", page_icon="🚀", layout="centered")

# برانڈنگ کلرز اور اسٹائلنگ
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
    .stButton>button:hover { transform: scale(1.1) rotate(5deg); }
    .footer {
        text-align: center; margin-top: 50px; padding: 25px;
        border-top: 3px solid #f39200; background-color: #f9f9f9; border-radius: 10px;
    }
    [data-testid="stMetricValue"] { color: #f39200; font-size: 40px; }
    </style>
    """, unsafe_allow_html=True)

# لوگو سیٹ اپ
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(current_dir, "logo.jpg")
        img = Image.open(logo_path)
        st.image(img, width=250)
    except:
        st.write("### Skill Up")

st.markdown("<h1>Skill Up Internet Speed Test</h1>", unsafe_allow_html=True)

st.write("##")
go_button = st.button("GO")

if go_button:
    try:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.info("بہترین سرور تلاش کیا جا رہا ہے...")
        st_tester = speedtest.Speedtest()
        st_tester.get_best_server()
        progress_bar.progress(30)
        
        status_text.info("ڈاؤن لوڈنگ سپیڈ چیک ہو رہی ہے...")
        st_tester.download()
        progress_bar.progress(60)
        
        status_text.info("اپ لوڈنگ سپیڈ چیک ہو رہی ہے...")
        st_tester.upload()
        progress_bar.progress(90)
        
        # نتائج حاصل کرنا (یہاں ہم نے تبدیلی کی ہے تاکہ سپیڈ درست آئے)
        results = st_tester.results.dict()
        download_speed = results['download'] / 1_000_000  # Mbps میں تبدیلی
        upload_speed = results['upload'] / 1_000_000      # Mbps میں تبدیلی
        ping = results['ping']
        server = f"{results['server']['sponsor']} ({results['server']['name']})"
        
        progress_bar.progress(100)
        status_text.success("ٹیسٹ مکمل ہو گیا!")
        
        st.write("---")
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Ping", f"{ping:.0f} ms")
        res_col2.metric("Server", server)
        res_col3.metric("Status", "Online")
        
        st.write("##")
        res_col4, res_col5 = st.columns(2)
        res_col4.metric("Download", f"{download_speed:.2f} Mbps")
        res_col5.metric("Upload", f"{upload_speed:.2f} Mbps")

    except Exception as e:
        st.error("نیٹ ورک کا مسئلہ ہے یا سرور مصروف ہے۔ دوبارہ کوشش کریں۔")

# فوٹر
st.markdown(f"""
    <div class="footer">
        <h3 style='color: #1a4a7a; margin-bottom: 5px;'>Shahid Mahmood Cheema</h3>
        <p style='margin: 0;'><b>CEO - Skill Up Digital Academy</b></p>
        <p style='color: #f39200; font-size: 18px; margin: 5px;'>📞 WhatsApp: +44 7704 578383</p>
        <hr style='border: 0.5px solid #ddd;'>
        <p style='font-size: 12px;'>© 2026 Skill Up - Empowering Skills Globally</p>
    </div>
    """, unsafe_allow_html=True)