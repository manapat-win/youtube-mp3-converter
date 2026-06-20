from flask import Flask, request, render_template_string, send_file
import yt_dlp
import os
import glob
import time

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# เพิ่ม JavaScript เล็กน้อยสำหรับทำปุ่ม Loading 
HTML_PAGE = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube to MP3 Converter</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f2f5; margin: 0; }
        .container { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; width: 100%; max-width: 400px; }
        h2 { color: #333; margin-top: 0; }
        input[type="text"], input[type="number"] { width: 90%; padding: 12px; margin: 10px 0; border: 1px solid #ccc; border-radius: 6px; font-size: 16px; box-sizing: border-box; }
        button { background-color: #ff0000; color: white; border: none; padding: 14px 20px; font-size: 16px; border-radius: 6px; cursor: pointer; width: 90%; font-weight: bold; transition: 0.3s; margin-top: 15px; }
        button:hover { background-color: #cc0000; }
        button:disabled { background-color: #999; cursor: not-allowed; }
        .label-text { font-size: 14px; color: #555; text-align: left; display: block; margin-left: 5%; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>YouTube to MP3 🎵</h2>
        <form action="/convert" method="post" onsubmit="showLoading()">
            <label class="label-text">ลิงก์ YouTube:</label>
            <input type="text" name="url" placeholder="วาง Link ที่นี่..." required>
            
            <label class="label-text">ลำดับเพลง (ระบบจะเติมเลขหน้าไฟล์เพื่อเล่นในรถตามลำดับ):</label>
            <input type="number" name="track_num" value="1" min="1" required>
            
            <button id="submitBtn" type="submit">แปลงเป็น MP3 และดาวน์โหลด</button>
        </form>
    </div>

    <script>
        function showLoading() {
            const btn = document.getElementById('submitBtn');
            btn.innerText = 'กำลังแปลงไฟล์... กรุณารอสักครู่ ⏳';
            btn.disabled = true; // ป้องกันการกดเบิ้ล
            
            // ปลดล็อคปุ่มกลับมาเหมือนเดิมหลังจากผ่านไป 10 วินาที (เผื่อไว้กรณีโหลดเสร็จหรือเกิด Error)
            setTimeout(() => {
                btn.innerText = 'แปลงเป็น MP3 และดาวน์โหลด';
                btn.disabled = false;
            }, 10000);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/convert', methods=['POST'])
def convert():
    url = request.form['url']
    track_num = request.form.get('track_num', '1').zfill(2) # แปลงเลข 1 ให้เป็น 01

    # 1. เคลียร์ไฟล์ .mp3 เก่าๆ ทั้งหมดที่มีอยู่ในโฟลเดอร์ทิ้งก่อน
    for old_file in glob.glob(f"{DOWNLOAD_FOLDER}/*.mp3"):
        try:
            os.remove(old_file)
        except:
            pass

    # 2. ตั้งค่าการดาวน์โหลด (ใส่ track_num นำหน้าชื่อไฟล์ และอ้างอิงไฟล์คุกกี้)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_FOLDER}/{track_num}_%(title)s.%(ext)s',
        'cookiefile': 'www.youtube.com_cookies.txt',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            # 🌟 เพิ่มคำสั่งบรรทัดนี้: บังคับฝังข้อมูล Metadata ลงในไฟล์เสียง
            {'key': 'FFmpegMetadata', 'add_metadata': True},
        ],
        # 🌟 เพิ่มคำสั่งบรรทัดนี้: บังคับให้ตัวแปร track_num ฝังลงไปในช่อง Track Number ของ ID3 Tag
        'parse_metadata': f':%(track_number)s',
        'noplaylist': True
    }

    try:
        # 3. เริ่มกระบวนการดาวน์โหลดและแปลงไฟล์
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)
            
            # 4. หาไฟล์ที่แปลงเสร็จแล้วส่งให้ผู้ใช้ดาวน์โหลด
            downloaded_files = glob.glob(f"{DOWNLOAD_FOLDER}/*.mp3")
            if downloaded_files:
                return send_file(downloaded_files[0], as_attachment=True)
            else:
                return "เกิดข้อผิดพลาด: ไม่พบไฟล์หลังจากดาวน์โหลด", 500
    except Exception as e:
        return f"เกิดข้อผิดพลาดในการโหลด: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)