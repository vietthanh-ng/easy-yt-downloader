#!/bin/bash

# Di chuyen den thu muc chua file script
cd "$(dirname "$0")"

echo "====================================================="
echo "    EASY YOUTUBE DOWNLOADER - KHOI DONG (macOS)"
echo "====================================================="

# Kiem tra Python 3
if ! command -v python3 &> /dev/null; then
    echo "[LOI] Khong tim thay Python 3 tren may Mac cua ban!"
    echo "Ban co the cai dat bang lenh: brew install python"
    echo "Hoac tai bo cai tu: https://www.python.org/downloads/"
    exit 1
fi

echo "[*] Dang kiem tra va cap nhat thu vien..."
python3 -m pip install -q -r requirements.txt --break-system-packages 2>/dev/null || python3 -m pip install -q -r requirements.txt

# Khoi chay tool
python3 downloader.py
