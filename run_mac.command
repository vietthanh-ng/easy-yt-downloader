#!/bin/bash
cd "$(dirname "$0")"

echo "====================================================="
echo "    EASY YOUTUBE DOWNLOADER - KHOI DONG (macOS)"
echo "====================================================="

if ! command -v python3 &> /dev/null; then
    echo "[LOI] Khong tim thay Python 3 tren may Mac cua ban!"
    echo "Ban co the cai dat bang lenh: brew install python"
    echo "Hoac tai bo cai tu: https://www.python.org/downloads/"
    read -p "Nhan Enter de thoat..."
    exit 1
fi

python3 downloader.py
