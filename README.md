# YouTube to MP3 Converter

A simple web app that runs locally on your computer. Paste a YouTube link and download it as an MP3 file instantly. No internet upload, no account required — everything stays on your machine.

---

## 🇬🇧 English Guide

### What You Need Before Starting (One-Time Setup)

#### Step 1 — Install Python

Python is the engine that runs this app. You only need to install it once.

1. Open your browser (Chrome or Edge) and go to: **python.org/downloads**
2. Click the big yellow button that says **"Download Python 3.x.x"**
3. Run the file that was downloaded (it looks like `python-3.x.x-amd64.exe`)
4. **⚠️ Very important:** On the very first screen of the installer, look at the bottom — there is a small checkbox that says **"Add python.exe to PATH"**. Make sure to **tick that box** before doing anything else.
5. Then click **"Install Now"** and wait for it to finish

---

#### Step 2 — Install FFmpeg (Audio Converter Tool)

FFmpeg is a free tool that converts YouTube audio into MP3 format. The app cannot work without it.

1. Open your browser and go to: **ffmpeg.org/download.html**
2. Click on **"Windows"**
3. Click **"Windows builds from gyan.dev"**
4. Find and download the file named **`ffmpeg-release-essentials.zip`**
5. Once downloaded, right-click the `.zip` file and choose **"Extract All..."**
6. Open the extracted folder → open the **`bin`** subfolder inside it
7. You will see a file called **`ffmpeg.exe`** — copy it
8. Paste `ffmpeg.exe` into the project folder (the same folder where `app.py` is)

---

#### Step 3 — Set Up YouTube Cookies (Prevents Download Blocks)

YouTube may block downloads if it thinks you are not logged in. This file proves you are.

1. Open **Google Chrome** (must be Chrome, not Edge or Firefox)
2. Go to **youtube.com** and sign in with your Google account
3. Go to the **Chrome Web Store** and search for: **"Get cookies.txt LOCALLY"**
4. Click **"Add to Chrome"** to install the extension
5. Go back to the YouTube website
6. Click the extension icon at the top-right corner of Chrome (it looks like a puzzle piece 🧩, then find the extension in the list)
7. Click **"Export"** or **"Click here to export cookies"**
8. A file will be downloaded — rename it to exactly: **`www.youtube.com_cookies.txt`** (all lowercase, no spaces)
9. Move that file into the project folder (same folder as `app.py`)

> **Note:** Cookie files expire every 1–3 months. If downloads stop working, repeat this step.

---

#### Step 4 — Install App Libraries (One-Time Only)

1. Open the project folder
2. Click on the address bar at the top of the folder window (the bar that shows the path like `C:\Users\YourName\Project_MP3`)
3. Type **`cmd`** and press **Enter** — a black window will appear
4. In the black window, type the following and press **Enter**:
   ```
   pip install -r requirements.txt
   ```
5. Wait until you see a message like **"Successfully installed..."** — then you are done

---

### How to Use the App (Every Time)

#### Starting the App

1. Go to the project folder
2. Double-click the file named **`start.bat`**
3. A black window will appear showing the text:

   ```
   YouTube to MP3 Converter - กำลังเปิด...
   กรุณารอสักครู่ แล้วเปิดเบราว์เซอร์ไปที่:
      http://127.0.0.1:5000
   ```

4. **Keep this black window open** — do not close it. Closing it will shut down the app.

#### Opening the App in Your Browser

1. Open your browser (Chrome or Edge)
2. Click on the address bar at the top (where you normally type a website address)
3. Type exactly: **`http://127.0.0.1:5000`** and press **Enter**
4. The YouTube to MP3 converter page will appear

#### Downloading a Song

1. Go to **youtube.com** and find the video you want to download
2. Copy the link from the browser's address bar (click on the address bar, then press **Ctrl + A** to select all, then **Ctrl + C** to copy)
3. Go back to the converter page at `http://127.0.0.1:5000`
4. Click inside the input box that says **"วาง Link ที่นี่..."**
5. Press **Ctrl + V** to paste the link
6. Click the red button **"แปลงเป็น MP3 และดาวน์โหลด"**
7. Wait — this may take **10 to 60 seconds** depending on the length of the video and your internet speed
8. The MP3 file will automatically download to your computer when done

#### Closing the App

When you are finished, close the black window (`start.bat` window). The app will shut down.

---

### Troubleshooting

| Problem | What to Do |
|---|---|
| Black window closes immediately after double-clicking `start.bat` | Python is not installed correctly — redo Step 1 |
| Browser shows "This site can't be reached" at `127.0.0.1:5000` | Make sure the black window is still open |
| Download fails or says "blocked" | Your cookie file may have expired — redo Step 3 |
| Nothing happens after clicking the download button | Make sure the link starts with `https://www.youtube.com/` |
| The button unlocks but the file hasn't downloaded yet | Wait a little longer — the file may still be processing |

---

### Project Files

```
Project_MP3/
├── app.py                        # Main application code
├── requirements.txt              # Python libraries needed
├── start.bat                     # Double-click this to start the app
├── www.youtube.com_cookies.txt   # Your YouTube login cookies
├── downloads/                    # Downloaded MP3 files are saved here
├── howtouse.txt                  # Thai usage guide
├── git_manualBook.txt            # Git command reference
└── README.md                     # This file
```

---
---

## 🇹🇭 คู่มือภาษาไทย

### สิ่งที่ต้องเตรียมก่อนใช้งานครั้งแรก (ทำแค่ครั้งเดียวตลอดชีพ)

#### ขั้นตอนที่ 1 — ติดตั้ง Python

Python คือโปรแกรมที่ทำให้แอปนี้ทำงานได้ ต้องติดตั้งก่อนเสมอ

1. เปิดเบราว์เซอร์ (Chrome หรือ Edge) แล้วไปที่: **python.org/downloads**
2. กดปุ่มเหลืองใหญ่ที่เขียนว่า **"Download Python 3.x.x"**
3. เปิดไฟล์ที่ดาวน์โหลดมา (จะมีชื่อประมาณ `python-3.x.x-amd64.exe`)
4. **⚠️ สำคัญมาก:** บนหน้าแรกของโปรแกรมติดตั้ง ให้มองที่ **ด้านล่างสุด** จะเห็นช่องเล็กๆ เขียนว่า **"Add python.exe to PATH"** ให้ **คลิกติ๊กถูก** ช่องนี้ก่อนทำอะไรทั้งนั้น
5. จากนั้นกด **"Install Now"** แล้วรอจนเสร็จ

---

#### ขั้นตอนที่ 2 — ติดตั้ง FFmpeg (ตัวแปลงไฟล์เสียง)

FFmpeg คือโปรแกรมช่วยแปลงเสียงจาก YouTube ให้เป็น MP3 โปรแกรมหลักจำเป็นต้องใช้ตัวนี้

1. เปิดเบราว์เซอร์แล้วไปที่: **ffmpeg.org/download.html**
2. คลิกที่หัวข้อ **"Windows"**
3. คลิก **"Windows builds from gyan.dev"**
4. ดาวน์โหลดไฟล์ที่ชื่อว่า **`ffmpeg-release-essentials.zip`**
5. เมื่อดาวน์โหลดเสร็จ คลิกขวาที่ไฟล์ .zip แล้วเลือก **"Extract All..."** หรือ **"แตกไฟล์"**
6. เปิดโฟลเดอร์ที่แตกออกมา แล้วเปิดโฟลเดอร์ย่อยชื่อ **`bin`**
7. จะเห็นไฟล์ชื่อ **`ffmpeg.exe`** ให้คัดลอกไฟล์นี้
8. วาง `ffmpeg.exe` ลงในโฟลเดอร์โปรเจกต์ (โฟลเดอร์เดียวกับที่มีไฟล์ `app.py`)

---

#### ขั้นตอนที่ 3 — เตรียมไฟล์คุกกี้ YouTube (ป้องกันการถูกบล็อก)

YouTube อาจบล็อกการดาวน์โหลดหากไม่ได้ล็อกอิน ไฟล์นี้ช่วยให้โปรแกรมรู้ว่าคุณล็อกอินอยู่

1. เปิด **Google Chrome** (ต้องเป็น Chrome เท่านั้น ไม่ใช่ Edge หรือ Firefox)
2. ไปที่ **youtube.com** แล้วล็อกอินด้วยบัญชี Google ของคุณ
3. ไปที่ **Chrome Web Store** แล้วค้นหาส่วนขยายชื่อ: **"Get cookies.txt LOCALLY"**
4. กด **"Add to Chrome"** เพื่อติดตั้ง
5. กลับมาที่หน้าเว็บ YouTube
6. กดที่ไอคอนส่วนขยายมุมขวาบนของ Chrome (รูปจิ๊กซอว์ 🧩) แล้วหาส่วนขยายนี้ในรายการ
7. กดปุ่ม **"Export"** หรือ **"Click here to export cookies"**
8. ไฟล์จะถูกดาวน์โหลดมา ให้เปลี่ยนชื่อไฟล์เป็น: **`www.youtube.com_cookies.txt`** (ตัวพิมพ์เล็กทั้งหมด ห้ามมีช่องว่าง)
9. ย้ายไฟล์นี้ไปวางในโฟลเดอร์โปรเจกต์ (โฟลเดอร์เดียวกับ `app.py`)

> **หมายเหตุ:** ไฟล์คุกกี้จะหมดอายุทุก 1–3 เดือน ถ้าโหลดไม่ได้ให้ทำขั้นตอนนี้ซ้ำ

---

#### ขั้นตอนที่ 4 — ติดตั้งระบบของโปรแกรม (ทำแค่ครั้งแรก)

1. เปิดโฟลเดอร์โปรเจกต์
2. คลิกที่ **แถบที่อยู่** ด้านบนสุดของหน้าต่างโฟลเดอร์ (แถบที่แสดง `C:\Users\ชื่อ\Project_MP3`)
3. พิมพ์ว่า **`cmd`** แล้วกด **Enter** — หน้าต่างสีดำจะเปิดขึ้น
4. ในหน้าต่างสีดำ พิมพ์คำสั่งนี้แล้วกด **Enter**:
   ```
   pip install -r requirements.txt
   ```
5. รอจนเห็นข้อความ **"Successfully installed..."** แปลว่าเสร็จแล้ว

---

### วิธีใช้งานโปรแกรม (ทำทุกครั้งที่ต้องการโหลดเพลง)

#### เปิดโปรแกรม

1. เข้าไปในโฟลเดอร์โปรเจกต์
2. ดับเบิ้ลคลิกที่ไฟล์ชื่อ **`start.bat`**
3. หน้าต่างสีดำจะเปิดขึ้นและแสดงข้อความว่า:
   ```
   YouTube to MP3 Converter - กำลังเปิด...
   กรุณารอสักครู่ แล้วเปิดเบราว์เซอร์ไปที่:
      http://127.0.0.1:5000
   ```
4. **อย่าปิดหน้าต่างสีดำนี้** — ถ้าปิดโปรแกรมจะหยุดทำงาน

#### เปิดหน้าเว็บโปรแกรมในเบราว์เซอร์

1. เปิดเบราว์เซอร์ (Chrome หรือ Edge)
2. คลิกที่ **แถบที่อยู่** ด้านบน (ช่องที่ใช้พิมพ์ที่อยู่เว็บ)
3. พิมพ์ **`http://127.0.0.1:5000`** แล้วกด **Enter**
4. หน้าเว็บ YouTube to MP3 จะเปิดขึ้นมา

#### ดาวน์โหลดเพลง

1. เปิด **youtube.com** แล้วค้นหาเพลงที่ต้องการ
2. คัดลอกลิงก์จากแถบที่อยู่บนของเบราว์เซอร์ (คลิกที่แถบนั้น กด **Ctrl + A** เพื่อเลือกทั้งหมด แล้ว **Ctrl + C** เพื่อคัดลอก)
3. กลับมาที่หน้าเว็บโปรแกรม `http://127.0.0.1:5000`
4. คลิกในช่องที่เขียนว่า **"วาง Link ที่นี่..."**
5. กด **Ctrl + V** เพื่อวางลิงก์
6. กดปุ่มแดง **"แปลงเป็น MP3 และดาวน์โหลด"**
7. รอสักครู่ — อาจใช้เวลา **10 ถึง 60 วินาที** ขึ้นอยู่กับความยาวเพลงและความเร็วอินเทอร์เน็ต
8. ไฟล์ MP3 จะดาวน์โหลดมาให้อัตโนมัติเมื่อเสร็จ

#### ปิดโปรแกรม

เมื่อใช้งานเสร็จแล้ว ให้ปิดหน้าต่างสีดำ (`start.bat`) โปรแกรมจะหยุดทำงาน

---

### แก้ปัญหาเบื้องต้น

| ปัญหา | วิธีแก้ |
|---|---|
| หน้าต่างสีดำปิดทันทีเมื่อดับเบิ้ลคลิก `start.bat` | Python ติดตั้งไม่สมบูรณ์ — ทำขั้นตอนที่ 1 ใหม่ |
| เบราว์เซอร์เปิด `127.0.0.1:5000` แล้วไม่มีอะไรขึ้น | ตรวจสอบว่าหน้าต่างสีดำยังเปิดอยู่ |
| โหลดไม่ได้ หรือขึ้นว่าถูกบล็อก | ไฟล์คุกกี้หมดอายุ — ทำขั้นตอนที่ 3 ใหม่ |
| กดปุ่มแล้วไม่มีอะไรเกิดขึ้น | ตรวจสอบว่าลิงก์ขึ้นต้นด้วย `https://www.youtube.com/` |
| ปุ่ม unlock แล้วแต่ไฟล์ยังไม่มา | รอต่ออีกสักครู่ ระบบอาจยังประมวลผลอยู่ |

---

*พัฒนาโดย Manapat*
