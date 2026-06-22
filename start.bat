@echo off
chcp 65001 >nul
echo ============================================
echo   YouTube to MP3 Converter - กำลังเปิด...
echo ============================================
echo.
echo ** ปิดหน้าต่างนี้ = ปิดโปรแกรม **
echo.

start /b cmd /c "timeout /t 2 /nobreak >nul & start http://127.0.0.1:5000"
python app.py
