"""
Easy YouTube Downloader (Cross-platform for Windows, macOS, Linux)
Hỗ trợ tải Video Full HD, 4K, Playlist và tách nhạc MP3 tốc độ cao.
"""

import os
import sys
import shutil
import platform
import subprocess

def ensure_dependencies():
    """Tự động kiểm tra và cài đặt thư viện thiếu nếu máy người dùng chưa có."""
    required = {
        "yt_dlp": "yt-dlp",
        "colorama": "colorama",
        "imageio_ffmpeg": "imageio-ffmpeg"
    }
    missing = []
    for mod, pkg in required.items():
        try:
            __import__(mod)
        except ImportError:
            missing.append(pkg)

    if missing:
        print(f"[*] Đang tự động cài đặt thư viện cần thiết: {', '.join(missing)}...")
        cmd = [sys.executable, "-m", "pip", "install", "-q"] + missing
        try:
            subprocess.check_call(cmd)
            print("[OK] Cài đặt thư viện hoàn tất!\n")
        except subprocess.CalledProcessError:
            try:
                subprocess.check_call(cmd + ["--break-system-packages"])
                print("[OK] Cài đặt thư viện hoàn tất!\n")
            except Exception:
                pass

# Tự động đảm bảo môi trường đầy đủ trước khi chạy
ensure_dependencies()

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR_TITLE = Fore.CYAN + Style.BRIGHT
    COLOR_SUCCESS = Fore.GREEN + Style.BRIGHT
    COLOR_WARN = Fore.YELLOW + Style.BRIGHT
    COLOR_ERR = Fore.RED + Style.BRIGHT
    COLOR_RESET = Style.RESET_ALL
except ImportError:
    COLOR_TITLE = ""
    COLOR_SUCCESS = ""
    COLOR_WARN = ""
    COLOR_ERR = ""
    COLOR_RESET = ""

def get_ffmpeg_path():
    """Tìm đường dẫn ffmpeg trên hệ thống hoặc qua thư viện imageio-ffmpeg."""
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg

    try:
        import imageio_ffmpeg
        bundled_ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
        if bundled_ffmpeg and os.path.exists(bundled_ffmpeg):
            return bundled_ffmpeg
    except ImportError:
        pass

    script_dir = os.path.dirname(os.path.abspath(__file__))
    local_ffmpeg_win = os.path.join(script_dir, "ffmpeg.exe")
    local_ffmpeg_unix = os.path.join(script_dir, "ffmpeg")
    if os.path.exists(local_ffmpeg_win):
        return local_ffmpeg_win
    if os.path.exists(local_ffmpeg_unix):
        return local_ffmpeg_unix

    return None

def open_folder(folder_path):
    """Mở thư mục chứa file đã tải tùy theo hệ điều hành."""
    current_os = platform.system()
    try:
        if current_os == "Windows":
            os.startfile(folder_path)
        elif current_os == "Darwin":  # macOS
            subprocess.run(["open", folder_path])
        else:  # Linux
            subprocess.run(["xdg-open", folder_path])
    except Exception:
        pass

def print_banner():
    """In giao diện tiêu đề."""
    os_name = "macOS" if platform.system() == "Darwin" else platform.system()
    print(COLOR_TITLE + "=" * 65)
    print(COLOR_TITLE + f"       EASY YOUTUBE DOWNLOADER (Đa nền tảng - {os_name})")
    print(COLOR_TITLE + "=" * 65)
    print("  * Tải Video chất lượng cao (1080p, 2K, 4K)")
    print("  * Tải danh sách phát (Playlist) theo khoảng tập")
    print("  * Tách nhạc MP3 chất lượng 320kbps")
    print(COLOR_TITLE + "=" * 65 + "\n")

def main():
    import yt_dlp

    ffmpeg_path = get_ffmpeg_path()
    
    while True:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        print_banner()

        if not ffmpeg_path:
            print(COLOR_WARN + "[LƯU Ý] Chưa phát hiện FFmpeg trên máy.")
            print(COLOR_WARN + "Video 1080p+ có thể không gộp được âm thanh.")
            print("Khuyên dùng: pip install imageio-ffmpeg hoặc brew install ffmpeg (trên Mac)\n")
        else:
            print(COLOR_SUCCESS + f"[OK] Đã kết nối bộ xử lý FFmpeg: {os.path.basename(ffmpeg_path)}\n")

        url = input(">>> Dán link YouTube (Video / Playlist / Shorts): ").strip()
        if not url:
            continue
        url = url.strip('"\'')

        print("\n" + "-" * 50)
        print("Chọn định dạng tải về:")
        print("  [1] 1080p Full HD (Chuẩn MP4 - Khuyên dùng)")
        print("  [2] 720p HD (Chuẩn MP4 - Nhẹ, tải nhanh)")
        print("  [3] Tốt nhất có thể (Best Quality - Lên đến 2K/4K/8K)")
        print("  [4] Chỉ tải âm thanh MP3 (Nhạc, Podcast)")
        print("-" * 50)
        choice = input("Nhập lựa chọn (1/2/3/4) [Mặc định: 1]: ").strip() or "1"

        playlist_items = None
        if "list=" in url:
            print("\n" + COLOR_TITLE + "[Phát hiện Playlist Danh Sách Phát]")
            print("  [1] Tải toàn bộ playlist")
            print("  [2] Chọn khoảng tập muốn tải (ví dụ: 1-50 hoặc 1-100)")
            pl_choice = input("Lựa chọn (1 hoặc 2) [Mặc định: 1]: ").strip() or "1"
            if pl_choice == "2":
                playlist_items = input("Nhập khoảng tập (ví dụ 1-50): ").strip()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, "downloads")
        os.makedirs(output_dir, exist_ok=True)

        out_template_default = os.path.join(output_dir, "%(title)s.%(ext)s")
        out_template_playlist = os.path.join(output_dir, "%(playlist_title)s", "%(playlist_index)03d - %(title)s.%(ext)s")

        ydl_opts = {
            "outtmpl": {
                "default": out_template_default,
                "playlist": out_template_playlist,
            },
            "windowsfilenames": True,
            "nooverwrites": True,
            "ignoreerrors": True,
        }

        if ffmpeg_path:
            ydl_opts["ffmpeg_location"] = ffmpeg_path

        if playlist_items:
            ydl_opts["playlist_items"] = playlist_items

        if choice == "1":
            ydl_opts["format"] = "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
            ydl_opts["merge_output_format"] = "mp4"
        elif choice == "2":
            ydl_opts["format"] = "bestvideo[height<=720]+bestaudio/best[height<=720]"
            ydl_opts["merge_output_format"] = "mp4"
        elif choice == "3":
            ydl_opts["format"] = "bestvideo+bestaudio/best"
            ydl_opts["merge_output_format"] = "mp4"
        elif choice == "4":
            ydl_opts["format"] = "bestaudio/best"
            ydl_opts["postprocessors"] = [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }]

        print("\n" + COLOR_TITLE + "=" * 65)
        print("Đang tiến hành tải, xin vui lòng đợi...")
        print(COLOR_TITLE + "=" * 65 + "\n")

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("\n" + COLOR_SUCCESS + "[THÀNH CÔNG] Quá trình tải đã hoàn tất!")
            print(COLOR_SUCCESS + f"File được lưu tại: {output_dir}")
            open_folder(output_dir)
        except Exception as e:
            print("\n" + COLOR_ERR + f"[LỖI] Có sự cố xảy ra: {e}")

        print("\n" + "-" * 50)
        cont = input("Bạn có muốn tải tiếp link khác không? (Y/N) [Y]: ").strip().upper()
        if cont == "N":
            print("\nCảm ơn bạn đã sử dụng công cụ! Tạm biệt.")
            break

if __name__ == "__main__":
    main()
