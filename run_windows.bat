@echo off
chcp 65001 >nul
title Easy YouTube Downloader (Windows)
color 0b

cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [LỖI] Không tìm thấy Python trên máy tính của bạn!
    echo Vui lòng tải và cài đặt Python từ: https://www.python.org/downloads/
    echo (Lưu ý tick chọn "Add python.exe to PATH" khi cài đặt)
    pause
    exit /b
)

echo [*] Đang kiểm tra thư viện cần thiết...
python -m pip install -q -r requirements.txt

python downloader.py

pause
