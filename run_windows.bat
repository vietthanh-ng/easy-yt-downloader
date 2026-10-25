@echo off
chcp 65001 >nul
title Easy YouTube Downloader (Windows)
color 0b

cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo =====================================================================
    echo [LỖI] Máy tính của bạn chưa cài đặt Python!
    echo =====================================================================
    echo Đang tự động mở trang web chính thức để bạn tải Python...
    start https://www.python.org/downloads/
    echo.
    echo * LƯU Ý QUAN TRỌNG: Khi cài đặt, hãy nhớ tick chọn ô:
    echo   "[X] Add python.exe to PATH" ở góc dưới cùng!
    echo =====================================================================
    pause
    exit /b
)

python downloader.py

pause
