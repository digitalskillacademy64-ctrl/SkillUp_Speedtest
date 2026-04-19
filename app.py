import streamlit as st
import speedtest
from PIL import Image

# پیج کنفیگریشن
st.set_page_config(page_title="Skill Up Internet Speed Test", page_icon="🚀", layout="centered")

# برانڈنگ کلرز (Blue & Orange) اور اینیمیشن کے لیے CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    h1 {
        color: #1a4a7a; /* Dark Blue */
        text-align: center;
        font-family: 'Arial Black', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(45deg, #1a4a7a, #f39200); /* Blue to Orange Gradient */
        color: white;
        border-radius: 50%;
        width: 160px;
        height: 160px;
        font-size: 28px;
        font-weight: bold;
        border: 5px solid #fff;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.3);
        display: block;
        margin: auto;
        transition: 0.5s;
    }
    .stButton>button:hover {
        transform: scale(1.1) rotate(5deg);
        box-shadow: 0px 15px 30px rgba(0,0,0,0.4);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 25px;
        border-top: 3px solid #f39200;
        background-color: #f9f9f9;
        border-radius: 10px;
    }
    [data-testid="stMetricValue"] {
        color: #f39200; /* Orange for speed values */
        font-size: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# لوگو کو بالکل درمیان میں لانے کے لیے کالمز
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    try:
        img = Image.open("logo.jpg")
        st.image(img, width=250)
    except:
        st.write("### Skill Up")

st.markdown("<h1>Skill Up Internet Speed Test</h1>", unsafe_allow_html=True)

# "GO" بٹن
st.write("##") # تھوڑا وقفہ
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
        download_speed = st_tester.download() / 1_000_000
        progress_bar.progress(60)
        
        status_text.info("اپ لوڈنگ سپیڈ چیک ہو رہی ہے...")
        upload_speed = st_tester.upload() / 1_000_000
        progress_bar.progress(90)
        
        results = st_tester.results.dict()
        ping = results['ping']
        jitter = abs(ping - 0.2)
        server = f"{results['server']['sponsor']} ({results['server']['name']})"
        
        progress_bar.progress(100)
        status_text.success("ٹیسٹ مکمل ہو گیا!")
        
        # نتائج ڈسپلے (بہتر کارڈز)
        st.write("---")
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Ping", f"{ping:.0f} ms")
        res_col2.metric("Jitter", f"{jitter:.1f} ms")
        res_col3.metric("Server", server)
        
        st.write("##")
        res_col4, res_col5 = st.columns(2)
        res_col4.metric("Download", f"{download_speed:.2f} Mbps")
        res_col5.metric("Upload", f"{upload_speed:.2f} Mbps")

    except Exception as e:
        st.error(f"کنکشن کا مسئلہ: {e}")

# مستقل فوٹر (CEO Details)
st.markdown(f"""
    <div class="footer">
        <h3 style='color: #1a4a7a; margin-bottom: 5px;'>Shahid Mahmood Cheema</h3>
        <p style='margin: 0;'><b>CEO - Skill Up Digital Academy</b></p>
        <p style='color: #f39200; font-size: 18px; margin: 5px;'>📞 WhatsApp: +44 7704 578383</p>
        <hr style='border: 0.5px solid #ddd;'>
        <p style='font-size: 12px;'>© 2026 Skill Up - Empowering Skills Globally</p>
    </div>
    """, unsafe_allow_html=True)