#!/bin/bash

# Di chuyển đến thư mục chứa script
cd "$(dirname "$0")"

echo "====================================================="
echo "    EASY YOUTUBE DOWNLOADER - KHỞI ĐỘNG (macOS)"
echo "====================================================="

# Kiểm tra Python 3
if ! command -v python3 &> /dev/null; then
    echo "[LỖI] Không tìm thấy Python 3 trên máy Mac của bạn!"
    echo "Bạn có thể cài đặt bằng lệnh: brew install python"
    echo "Hoặc tải từ trang chủ: https://www.python.org/downloads/"
    exit 1
fi

# Tự động cài đặt thư viện cần thiết
echo "[*] Đang kiểm tra và cập nhật thư viện..."
python3 -m pip install -q -r requirements.txt

# Khởi chạy tool
python3 downloader.py
