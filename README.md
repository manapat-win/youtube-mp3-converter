# YouTube to MP3 Converter

A simple web app that runs locally on your computer, letting you paste a YouTube link and download it as an MP3 file. No cloud upload, no account needed — everything stays on your machine.

---

## What You Need Before Starting (One-Time Setup)

### 1. Install Python

Python is the programming language that powers this app.

1. Go to **python.org/downloads** in your browser
2. Click the big yellow **"Download Python 3.x.x"** button
3. Run the downloaded installer
4. **Important:** On the first screen of the installer, check the box at the bottom that says **"Add python.exe to PATH"** before clicking Install Now

### 2. Install FFmpeg

FFmpeg is a separate tool that converts video audio into MP3 format. The app cannot work without it.

1. Go to **ffmpeg.org/download.html**
2. Click **Windows** → then **"Windows builds from gyan.dev"**
3. Download the file named `ffmpeg-release-essentials.zip`
4. Extract (unzip) the downloaded file
5. Open the extracted folder, then open the `bin` subfolder
6. Copy the file named **`ffmpeg.exe`**
7. Paste it into this project folder (same folder as `app.py`)

### 3. Set Up YouTube Cookies (Lets the App Download Without Being Blocked)

YouTube may block downloads if you are not signed in. This file proves you are logged in.

1. Open **Google Chrome** and go to **youtube.com** — sign in with your Google account
2. Install the Chrome extension: **"Get cookies.txt LOCALLY"** (search for it in the Chrome Web Store)
3. While on the YouTube website, click the extension icon (top-right corner of Chrome)
4. Click **"Export"** or **"Click here to export cookies"**
5. Rename the downloaded file to exactly: `www.youtube.com_cookies.txt`
6. Move that file into this project folder (same folder as `app.py`)

> **Note:** Cookie files expire every 1–3 months. If downloads stop working, repeat this step.

### 4. Install App Dependencies (One-Time)

1. Open this project folder
2. Click the address bar at the top of the folder window, type `cmd`, and press Enter
3. In the black window that appears, type this command and press Enter:
   ```
   pip install -r requirements.txt
   ```
4. Wait until you see "Successfully installed..."

---

## How to Use the App (Every Time)

### Start the App

**Easy way:** Double-click `start.bat` in this folder

**Manual way:** Open CMD in this folder and run:
```
python app.py
```

### Download a Song

1. Open your browser (Chrome or Edge) and go to:
   ```
   http://127.0.0.1:5000
   ```
2. Go to YouTube and copy the video link (the URL in the browser's address bar)
3. Paste the link into the input box on the app page
4. Click **"แปลงเป็น MP3 และดาวน์โหลด"**
5. Wait 10–60 seconds (depends on your internet speed) — the MP3 file will download automatically

> **Important:** Keep the black CMD window open while using the app. Closing it shuts down the app.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Page at 127.0.0.1:5000 won't load | Make sure the CMD window is still open and `python app.py` is running |
| Download fails / blocked | Your cookie file may have expired — redo Step 3 above |
| "start.bat" closes instantly | Python may not be installed correctly — redo Step 1 |
| Nothing happens after clicking the button | Check that the YouTube link starts with `https://www.youtube.com/` |

---

## Project Structure

```
Project_MP3/
├── app.py                        # Main application code
├── requirements.txt              # Python packages needed
├── start.bat                     # Easy launcher (double-click to start)
├── www.youtube.com_cookies.txt   # Your YouTube login cookies
├── downloads/                    # Downloaded MP3 files are saved here
├── วิธีใช้งาน.txt                # Thai usage guide
├── คำสั่งต่างๆ.txt               # Git command reference
└── README.md                     # This file
```

---

*Developed by Manapat*
