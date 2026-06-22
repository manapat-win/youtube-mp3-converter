from flask import Flask, request, render_template_string, send_file
import yt_dlp
import os
import glob

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube to MP3 Converter</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f2f5; margin: 0; }
        .container { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; width: 100%; max-width: 450px; }
        h2 { color: #333; margin-top: 0; }
        input[type="text"] { width: 90%; padding: 12px; margin: 10px 0; border: 1px solid #ccc; border-radius: 6px; font-size: 16px; box-sizing: border-box; }
        button { background-color: #ff0000; color: white; border: none; padding: 14px 20px; font-size: 16px; border-radius: 6px; cursor: pointer; width: 90%; font-weight: bold; transition: 0.3s; margin-top: 15px; }
        button:hover { background-color: #cc0000; }
        button:disabled { background-color: #999; cursor: not-allowed; }
        .label-text { font-size: 14px; color: #555; text-align: left; display: block; margin-left: 5%; margin-top: 10px; }
        .hint { font-size: 12px; color: #aaa; margin: 6px 0 0 0; }
    </style>
</head>
<body>
    <div class="container">
        <h2>YouTube to MP3 🎵</h2>
        <form action="/convert" method="post" onsubmit="return showLoading()">
            <label class="label-text">ลิงก์ YouTube:</label>
            <input type="text" name="url" id="urlInput" placeholder="วาง Link ที่นี่..." required>
            <p class="hint">คัดลอกลิงก์จาก YouTube แล้ววางในช่องนี้</p>
            <button id="submitBtn" type="submit">แปลงเป็น MP3 และดาวน์โหลด</button>
        </form>
    </div>

    <script>
        function showLoading() {
            const url = document.getElementById('urlInput').value.trim();
            if (!url) return false;
            const btn = document.getElementById('submitBtn');
            btn.innerText = 'กำลังแปลงไฟล์... กรุณารอสักครู่ ⏳';
            btn.disabled = true;
            setTimeout(() => {
                btn.innerText = 'แปลงเป็น MP3 และดาวน์โหลด';
                btn.disabled = false;
            }, 15000);
            return true;
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
    url = request.form.get('url', '').strip()
    if not url:
        return "กรุณาใส่ลิงก์ YouTube", 400

    for old_file in glob.glob(os.path.join(DOWNLOAD_FOLDER, '*.mp3')):
        try:
            os.remove(old_file)
        except OSError:
            pass

    cookies_file = 'www.youtube.com_cookies.txt'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {'key': 'FFmpegMetadata', 'add_metadata': True},
        ],
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }

    if os.path.exists(cookies_file):
        ydl_opts['cookiefile'] = cookies_file

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)

        downloaded_files = glob.glob(os.path.join(DOWNLOAD_FOLDER, '*.mp3'))
        if downloaded_files:
            return send_file(downloaded_files[0], as_attachment=True)
        return "เกิดข้อผิดพลาด: ไม่พบไฟล์หลังจากดาวน์โหลด กรุณาลองใหม่อีกครั้ง", 500
    except yt_dlp.utils.DownloadError as e:
        return f"ดาวน์โหลดไม่สำเร็จ: ลิงก์อาจไม่ถูกต้อง หรือวิดีโอถูกจำกัดการเข้าถึง<br><small>{str(e)}</small>", 500
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)