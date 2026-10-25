#!/bin/bash
# MACOS

cd "$(dirname "$0")"

echo "====================================================="
echo "    EASY YOUTUBE DOWNLOADER - KHỞI ĐỘNG (macOS)"
echo "====================================================="

if ! command -v python3 &> /dev/null; then
    echo "[LỖI] Không tìm thấy Python 3 trên máy Mac của bạn!"
    echo "Bạn có thể cài đặt bằng lệnh: brew install python"
    echo "Hoặc tải từ trang chủ: https://www.python.org/downloads/"
    exit 1
fi

echo "[*] Đang kiểm tra và cập nhật thư viện..."
python3 -m pip install -q -r requirements.txt

python3 downloader.py
