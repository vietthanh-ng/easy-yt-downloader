#!/bin/bash
# Tu dong chuyen den thu muc chua file script
cd "$(dirname "$0")"

echo "====================================================="
echo "    EASY YOUTUBE DOWNLOADER - KHOI DONG (macOS)"
echo "====================================================="

# 1. Kiem tra Python 3
if ! command -v python3 &> /dev/null; then
    echo "[LOI] Khong tim thay Python 3 tren may Mac cua ban!"
    echo "Ban co the cai dat bang lenh: brew install python"
    echo "Hoac tai bo cai tu: https://www.python.org/downloads/"
    read -p "Nhan Enter de thoat..."
    exit 1
fi

# 2. Tu dong tao moi truong ao (.venv) de tranh loi externally-managed-environment tren macOS
if [ ! -d ".venv" ]; then
    echo "[*] Dang khoi tao moi truong rieng biet (.venv)..."
    python3 -m venv .venv
fi

# 3. Kich hoat moi truong ao
source .venv/bin/activate

# 4. Cai dat thu vien vao moi truong ao
echo "[*] Dang kiem tra va cap nhat thu vien can thiet..."
pip install -q -r requirements.txt

# 5. Khoi chay tool
python downloader.py
