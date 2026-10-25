# Easy YouTube Downloader (Đa Nền Tảng)

Công cụ tải video YouTube, Shorts, Playlist và tách nhạc MP3 tốc độ cao, hỗ trợ chạy mượt trên **Windows** và **macOS**.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Powered by yt-dlp](https://img.shields.io/badge/Engine-yt--dlp-red.svg)](https://github.com/yt-dlp/yt-dlp)

---

## Tính Năng Nổi Bật

- **Tải Video Đa Độ Phân Giải:** Hỗ trợ chuẩn **1080p Full HD**, **720p HD**, hoặc chất lượng gốc cao nhất (**2K / 4K / 8K**).
- **Tách Nhạc MP3:** Tự động tách âm thanh chất lượng cao 320kbps từ video âm nhạc hoặc podcast.
- **Hỗ Trợ Danh Sách Phát (Playlist):**
  - Tải toàn bộ danh sách phát chỉ bằng 1 liên kết.
  - Tùy chọn tải theo khoảng tập (ví dụ: chỉ tải từ tập `1-50` hoặc `10-20`).
- **Tốc Độ Vượt Trội:** Kết nối trực tiếp tới máy chủ CDN của Google/YouTube, tải tối đa băng thông đường truyền mạng.
- **Tự Động Ghép File (Remux):** Tự động hợp nhất luồng hình ảnh và âm thanh thành file `.mp4` chuẩn chỉnh không lỗi lệch tiếng.
- **Tự Động Mở Thư Mục:** Sau khi tải xong, tự động mở thư mục chứa video trên Windows Explorer hoặc macOS Finder.

---

## Khởi Động Nhanh (1-Click - Không Cần Dòng Lệnh)

Dành cho người dùng muốn sử dụng ngay mà không cần thao tác với dòng lệnh:

- **Trên Windows:** Nhấp đúp chuột vào file **`run_windows.bat`**.
- **Trên macOS:** Nhấp đúp chuột vào file **`run_mac.command`** trong Finder.

> **Lưu ý:** Hệ thống đã tích hợp sẵn cơ chế tự động cài đặt thư viện thiếu. Khi mở lần đầu, tool sẽ tự chuẩn bị mọi thứ trong vài giây mà bạn không cần phải tự gõ bất kỳ câu lệnh nào.

---

## Cấu Trúc Dự Án

```text
easy-yt-downloader/
├── downloader.py         # Mã nguồn chính chạy trên mọi hệ điều hành
├── run_windows.bat       # Khởi động nhanh 1-click cho người dùng Windows
├── run_mac.command       # Khởi động nhanh 1-click cho người dùng macOS (Finder)
├── run_mac.sh            # Script khởi chạy qua Terminal trên macOS/Linux
├── requirements.txt      # Danh sách thư viện phụ thuộc
├── .gitignore            # Bỏ qua các file rác và video đã tải khi push lên Git
├── README.md             # Tài liệu hướng dẫn sử dụng
└── LICENSE               # Giấy phép mã nguồn mở MIT
```

---

## Hướng Dẫn Cài Đặt Bằng Dòng Lệnh (Dành Cho Lập Trình Viên)

Nếu bạn muốn chạy thông qua Terminal / Command Prompt:

### 1. Dành cho Windows
```powershell
# Di chuyển vào thư mục dự án
cd easy-yt-downloader

# Cài đặt thư viện (nếu cần)
pip install -r requirements.txt

# Khởi chạy tool
python downloader.py
```

### 2. Dành cho macOS / Linux
```bash
# Di chuyển vào thư mục dự án
cd easy-yt-downloader

# Cấp quyền thực thi và chạy
chmod +x run_mac.command
./run_mac.command
```

> **Gợi ý trên macOS:** Khuyên dùng `ffmpeg` thông qua Homebrew (`brew install ffmpeg`) để tối ưu hiệu năng ghép video. Nếu máy chưa có Homebrew, tool sẽ tự động sử dụng bộ chuyển mã đi kèm qua `imageio-ffmpeg`.

---

## Hướng Dẫn Thao Tác

Khi màn hình công cụ hiện lên:
1. **Dán link:** Copy link video hoặc playlist từ trình duyệt -> Chuột phải (hoặc `Ctrl + V` / `Cmd + V`) vào cửa sổ tool -> Nhấn **Enter**.
2. **Chọn chất lượng:**
   - Nhập `1`: Tải chuẩn **1080p Full HD (MP4)** *(Khuyên dùng)*.
   - Nhập `2`: Tải chuẩn **720p HD (MP4)** *(Dung lượng nhẹ)*.
   - Nhập `3`: Tải chất lượng tối đa (**2K / 4K / 8K**).
   - Nhập `4`: Chỉ lấy file âm thanh **MP3 (320kbps)**.
3. **Nếu là Playlist:**
   - Chọn `1`: Tải tất cả các video trong playlist.
   - Chọn `2`: Nhập khoảng tập bạn muốn (ví dụ: `1-50`).
4. **Xem kết quả:** Video tải về sẽ tự động được lưu vào thư mục `downloads/` ngay trong thư mục dự án.

---

## Câu Hỏi Thường Gặp (FAQ)

<details>
<summary><b>1. Video 1080p có bị mất tiếng không?</b></summary>
Hoàn toàn không. Công cụ tự động kích hoạt FFmpeg để ghép luồng hình và âm thanh vào chuẩn container MP4 tiêu chuẩn, tương thích với mọi thiết bị di động, máy tính và TV.
</details>

<details>
<summary><b>2. Có tải được video Shorts hoặc từ các nền tảng khác không?</b></summary>
Có. Ngoài YouTube thông thường và Shorts, công cụ còn hỗ trợ tải video/audio từ Facebook, TikTok, Instagram, SoundCloud, Vimeo, Bilibili...
</details>

<details>
<summary><b>3. Làm sao để tải các tập tiếp theo của một playlist mà không bị tải trùng?</b></summary>
Công cụ đã bật sẵn tính năng chống ghi đè (`nooverwrites=True`). Những video đã có trong thư mục sẽ tự động được bỏ qua, giúp tiết kiệm thời gian và băng thông.
</details>

---

## Đóng Góp (Contributing)

Mọi đóng góp nhằm cải thiện công cụ đều rất được hoan nghênh! Hãy mở một **Issue** hoặc tạo một **Pull Request** trên GitHub.

## Bản Quyền (License)

Dự án được phân phối dưới giấy phép [MIT License](LICENSE). Tự do sử dụng, chỉnh sửa và chia sẻ.
