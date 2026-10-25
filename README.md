#  Easy YouTube Downloader (Đa Nền Tảng)

Công cụ tải video YouTube, Shorts, Playlist và tách nhạc MP3 tốc độ cao, hỗ trợ chạy mượt trên **Windows** và **macOS** .

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Powered by yt-dlp](https://img.shields.io/badge/Engine-yt--dlp-red.svg)](https://github.com/yt-dlp/yt-dlp)

---

##  Tính Năng Nổi Bật

-  **Tải Video Đa Độ Phân Giải:** Hỗ trợ chuẩn **1080p Full HD**, **720p HD**, hoặc chất lượng gốc cao nhất (**2K / 4K / 8K**).
-  **Tách Nhạc MP3:** Tự động tách âm thanh chất lượng cao 320kbps từ video âm nhạc hoặc podcast.
-  **Hỗ Trợ Danh Sách Phát (Playlist):**
  - Tải toàn bộ danh sách phát chỉ bằng 1 liên kết.
  - Tùy chọn tải theo khoảng tập (ví dụ: chỉ tải từ tập `1-50` hoặc `10-20`).
-  **Tốc Độ Vượt Trội:** Kết nối trực tiếp tới máy chủ CDN của Google/YouTube, tải tối đa băng thông đường truyền mạng.
-  **Tự Động Ghép File (Remux):** Tự động hợp nhất luồng hình ảnh và âm thanh thành file `.mp4` chuẩn chỉnh không lỗi lệch tiếng.
-  **Tự Động Mở Thư Mục:** Sau khi tải xong, tự động mở thư mục chứa video trên Windows Explorer hoặc macOS Finder.

---

## 📂 Cấu Trúc Dự Án

```text
easy-yt-downloader/
├── downloader.py         # Mã nguồn chính chạy trên mọi hệ điều hành
├── run_windows.bat       # File chạy nhanh 1-click cho người dùng Windows
├── run_mac.sh            # File chạy nhanh 1-click cho người dùng macOS
├── requirements.txt      # Danh sách thư viện cần thiết (yt-dlp, imageio-ffmpeg, colorama)
├── .gitignore            # Bỏ qua các file rác và video đã tải khi push lên Git
├── README.md             # Tài liệu hướng dẫn sử dụng
└── LICENSE               # Giấy phép mã nguồn mở MIT
```

---

##  Hướng Dẫn Cài Đặt & Sử Dụng

### 1. Dành cho người dùng Windows

#### Cách 1: Chạy nhanh (Khuyên dùng)
1. Tải hoặc `git clone` mã nguồn về máy:
   ```bash
   git clone https://github.com/YOUR_USERNAME/easy-yt-downloader.git
   cd easy-yt-downloader
   ```
2. Nhấp đúp chuột vào file **`run_windows.bat`**.
3. File `.bat` sẽ tự động kiểm tra, cài đặt thư viện cần thiết và khởi chạy công cụ.

#### Cách 2: Chạy bằng Terminal
```powershell
pip install -r requirements.txt

python downloader.py
```

---

### 2. Dành cho người dùng macOS

#### Cách 1: Chạy qua Script
1. Mở ứng dụng **Terminal** trên máy Mac.
2. Di chuyển vào thư mục dự án và cấp quyền thực thi (chỉ cần làm lần đầu):
   ```bash
   chmod +x run_mac.sh
   ./run_mac.sh
   ```

#### Cách 2: Chạy trực tiếp với Python 3
```bash
pip3 install -r requirements.txt

python3 downloader.py
```

> [!TIP]
> **Khuyên dùng trên macOS:** Bạn nên cài đặt `ffmpeg` thông qua Homebrew để tối ưu hóa hiệu năng ghép video:
> ```bash
> brew install ffmpeg
> ```
> *(Nếu máy chưa có Homebrew hoặc ffmpeg, công cụ sẽ tự động sử dụng bộ chuyển mã đi kèm qua `imageio-ffmpeg`)*.

---

## 📖 Hướng Dẫn Thao Tác

Khi màn hình công cụ hiện lên:
1. **Dán link:** Copy link video hoặc playlist từ trình duyệt $\rightarrow$ Chuột phải (hoặc `Ctrl + V` / `Cmd + V`) vào cửa sổ tool $\rightarrow$ Nhấn **Enter**.
2. **Chọn chất lượng:**
   - Nhập `1`: Tải chuẩn **1080p Full HD (MP4)** *(Mặc định)*.
   - Nhập `2`: Tải chuẩn **720p HD (MP4)** *(Dung lượng nhẹ)*.
   - Nhập `3`: Tải chất lượng tối đa (**2K / 4K / 8K**).
   - Nhập `4`: Chỉ lấy file âm thanh **MP3 (320kbps)**.
3. **Nếu là Playlist:**
   - Chọn `1`: Tải tất cả các video trong playlist.
   - Chọn `2`: Nhập khoảng tập bạn muốn (ví dụ: `1-50`).
4. **Xem kết quả:** Video tải về sẽ tự động được lưu vào thư mục `downloads/` ngay trong thư mục dự án.

---

##  Câu Hỏi Thường Gặp (FAQ)

<details>
<summary><b>1. Video 1080p có bị mất tiếng không?</b></summary>
Hoàn toàn không. Công cụ tự động kích hoạt FFmpeg để ghép luồng hình và âm thanh vào chuẩn container MP4 tiêu chuẩn, tương thích với mọi thiết bị di động, máy tính và TV.
</details>

<details>
<summary><b>2. Có tải được video Shorts hoặc video riêng tư không?</b></summary>
- Video Shorts: Hỗ trợ 100%.
- Video riêng tư / giới hạn độ tuổi: Cần bổ sung cookies trình duyệt nếu YouTube yêu cầu đăng nhập.
</details>

<details>
<summary><b>3. Làm sao để tải các tập tiếp theo của một playlist mà không bị tải trùng?</b></summary>
Công cụ đã bật sẵn tính năng chống ghi đè (`nooverwrites=True`). Những video đã tải trong thư mục sẽ tự động được bỏ qua, giúp tiết kiệm thời gian và băng thông.
</details>

---

##  Đóng Góp (Contributing)

Mọi đóng góp nhằm cải thiện công cụ đều rất được hoan nghênh! Hãy mở một **Issue** hoặc tạo một **Pull Request** trên GitHub.

## 📄 Bản Quyền (License)

Dự án được phân phối dưới giấy phép [MIT License](LICENSE). Tự do sử dụng, chỉnh sửa và chia sẻ.
