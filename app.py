import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(page_title="Skill Up Speed Test", layout="centered")

# لوگو اور ٹائٹل
try:
    img = Image.open("logo.jpg")
    st.image(img, width=150)
except:
    pass
st.markdown("<h1 style='text-align:center;'>Skill Up Speed Test</h1>", unsafe_allow_html=True)

# یہ وہ جادوئی کوڈ ہے جو براہ راست آپ کے براؤزر میں چلے گا
speed_test_html = """
<div id="main" style="text-align:center; font-family:sans-serif; padding:20px; border:2px solid #eee; border-radius:15px;">
    <button id="btn" onclick="startTest()" style="background:#1a73e8; color:white; border:none; border-radius:50%; width:120px; height:120px; font-size:24px; cursor:pointer; font-weight:bold; box-shadow:0 4px 10px rgba(0,0,0,0.2);">GO</button>
    
    <div id="results" style="display:none; margin-top:20px;">
        <div style="font-size:50px; font-weight:bold; color:#1a73e8;"><span id="speed">0</span> <small style="font-size:20px; color:#555;">Mbps</small></div>
        <p style="color:#666;">آپ کے کمپیوٹر کی اصل سپیڈ</p>
        <hr style="border:0; border-top:1px solid #eee;">
        <div style="display:flex; justify-content:space-around; font-size:18px;">
            <div><strong>Ping:</strong> <span id="ping">0</span> ms</div>
            <div><strong>IP:</strong> <span id="ip">Checking...</span></div>
        </div>
    </div>
</div>

<script>
async function startTest() {
    const btn = document.getElementById('btn');
    const results = document.getElementById('results');
    const speedEl = document.getElementById('speed');
    const pingEl = document.getElementById('ping');
    const ipEl = document.getElementById('ip');

    btn.innerText = "WAIT...";
    btn.disabled = true;

    try {
        // Ping ٹیسٹ
        const pStart = Date.now();
        await fetch('https://www.google.com/favicon.ico', { mode: 'no-cors' });
        pingEl.innerText = Date.now() - pStart;

        // IP معلوم کرنا
        const ipRes = await fetch('https://api.ipify.org?format=json');
        const ipData = await ipRes.json();
        ipEl.innerText = ipData.ip;

        // اصل سپیڈ ٹیسٹ (آپ کے براؤزر سے فائل ڈاؤن لوڈ کرنا)
        const start = Date.now();
        const response = await fetch('https://upload.wikimedia.org/wikipedia/commons/2/2d/Snake_River_%285mb%29.jpg?nocache=' + Math.random());
        const blob = await response.blob();
        const end = Date.now();
        
        const duration = (end - start) / 1000;
        const mbps = ((blob.size * 8) / (duration * 1024 * 1024)).toFixed(1);

        speedEl.innerText = mbps;
        results.style.display = "block";
        btn.innerText = "AGAIN";
        btn.disabled = false;
    } catch (e) {
        alert("ٹیسٹ کے دوران مسئلہ آیا، دوبارہ کوشش کریں۔");
        btn.innerText = "GO";
        btn.disabled = false;
    }
}
</script>
"""

# HTML کو اسٹریم لٹ میں دکھانا
components.html(speed_test_html, height=400)

st.markdown("<div style='text-align:center; margin-top:30px; color:#888;'>Shahid Mahmood Cheema<br>CEO - Skill Up Digital Academy</div>", unsafe_allow_html=True)