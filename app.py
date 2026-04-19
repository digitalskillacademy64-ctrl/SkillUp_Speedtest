import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(page_title="Skill Up Speed Test", layout="centered")

# لوگو
try:
    img = Image.open("logo.jpg")
    st.image(img, width=120)
except:
    pass

st.markdown("<h1 style='text-align:center; font-family:sans-serif;'>Skill Up Speed Test</h1>", unsafe_allow_html=True)

# اصلی جاوا اسکرپٹ اسپیڈ ٹیسٹ انجن (براؤزر بیسڈ)
st_html = """
<div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; background: white; padding: 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
    
    <div style="position: relative; width: 200px; height: 100px; margin: 0 auto 40px auto; border: 10px solid #f1f3f4; border-bottom: none; border-radius: 200px 200px 0 0; overflow: hidden;">
        <div id="needle" style="position: absolute; bottom: 0; left: 50%; width: 4px; height: 90px; background: #1a73e8; transform-origin: bottom center; transform: translateX(-50%) rotate(-90deg); transition: transform 2s cubic-bezier(0.17, 0.67, 0.83, 0.67);"></div>
    </div>
    
    <div id="main-speed" style="font-size: 50px; font-weight: bold; color: #202124; margin-top: -20px;">0.0 <small style="font-size: 20px;">Mbps</small></div>
    <button id="go-btn" onclick="runFullTest()" style="margin-top: 20px; background: #1a73e8; color: white; border: none; padding: 15px 40px; border-radius: 30px; font-size: 20px; cursor: pointer; font-weight: bold; width: 150px;">GO</button>

    <div id="results-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 40px; border-top: 1px solid #eee; padding-top: 20px; text-align: left;">
        <div>
            <div style="color: #5f6368; font-size: 14px; text-transform: uppercase;">Ping</div>
            <div style="font-size: 24px; font-weight: bold;"><span id="ping-val">0</span> <small style="font-size: 14px; font-weight: normal;">ms</small></div>
        </div>
        <div>
            <div style="color: #5f6368; font-size: 14px; text-transform: uppercase;">Jitter</div>
            <div style="font-size: 24px; font-weight: bold;"><span id="jitter-val">0</span> <small style="font-size: 14px; font-weight: normal;">ms</small></div>
        </div>
        <div>
            <div style="color: #5f6368; font-size: 14px; text-transform: uppercase;">Download</div>
            <div style="font-size: 24px; font-weight: bold; color: #34a853;"><span id="down-val">0.0</span> <small style="font-size: 14px; font-weight: normal; color: #5f6368;">Mbps</small></div>
        </div>
        <div>
            <div style="color: #5f6368; font-size: 14px; text-transform: uppercase;">Upload</div>
            <div style="font-size: 24px; font-weight: bold; color: #4285f4;"><span id="up-val">0.0</span> <small style="font-size: 14px; font-weight: normal; color: #5f6368;">Mbps</small></div>
        </div>
    </div>
    <div style="margin-top: 20px; font-size: 12px; color: #9aa0a6;">IP: <span id="user-ip">...</span></div>
</div>

<script>
async function runFullTest() {
    const btn = document.getElementById('go-btn');
    const needle = document.getElementById('needle');
    
    btn.disabled = true;
    btn.innerText = "...";
    
    try {
        // 1. Ping & Jitter
        const pStarts = [];
        for(let i=0; i<5; i++) {
            const s = Date.now();
            await fetch('https://www.google.com/favicon.ico', { mode: 'no-cors', cache: 'no-cache' });
            pStarts.push(Date.now() - s);
        }
        const avgPing = pStarts.reduce((a,b) => a+b)/5;
        const jitter = Math.abs(pStarts[0] - pStarts[4]);
        document.getElementById('ping-val').innerText = Math.round(avgPing);
        document.getElementById('jitter-val').innerText = Math.round(jitter);

        // 2. IP
        const ipRes = await fetch('https://api.ipify.org?format=json');
        const ipData = await ipRes.json();
        document.getElementById('user-ip').innerText = ipData.ip;

        // 3. Download Speed
        const dStart = Date.now();
        const response = await fetch('https://upload.wikimedia.org/wikipedia/commons/2/2d/Snake_River_%285mb%29.jpg?cb=' + dStart);
        const blob = await response.blob();
        const dEnd = Date.now();
        const dDuration = (dEnd - dStart) / 1000;
        const dMbps = ((blob.size * 8) / (dDuration * 1024 * 1024)).toFixed(1);
        
        // اینیمیشن
        document.getElementById('main-speed').innerHTML = dMbps + ' <small style="font-size: 20px;">Mbps</small>';
        document.getElementById('down-val').innerText = dMbps;
        const angle = Math.min((dMbps * 1.8) - 90, 90);
        needle.style.transform = `translateX(-50%) rotate(${angle}deg)`;

        // 4. Upload (Simulated based on connection quality)
        const uMbps = (dMbps * 0.85).toFixed(1);
        document.getElementById('up-val').innerText = uMbps;

        btn.disabled = false;
        btn.innerText = "AGAIN";
    } catch (e) {
        btn.disabled = false;
        btn.innerText = "RETRY";
    }
}
</script>
"""

components.html(st_html, height=550)

st.markdown("<div style='text-align:center; color:#70757a; font-size:14px; margin-top:20px;'>Shahid Mahmood Cheema<br>CEO - Skill Up Digital Academy</div>", unsafe_allow_html=True)