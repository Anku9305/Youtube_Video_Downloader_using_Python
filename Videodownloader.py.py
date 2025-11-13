import yt_dlp

def download_video(url):
    ydl_opts = {
        # Pick only formats that already contain audio + video (progressive download)
        'format': 'bv*+ba/b[ext=mp4][vcodec^=avc1][acodec^=mp4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',  # file name = video title
        'noplaylist': False,             # supports playlist + single video
        'merge_output_format': None,     # no merging step
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    print("🎥 YouTube Video / Short / Playlist Downloader (No FFmpeg needed)")
    url = input("Paste YouTube URL: ").strip()
    if url:
        download_video(url)
        print("\n✅ Download complete! Check your folder — plays directly with sound.")
    else:
        print("❌ Invalid URL, please try again.")

if __name__ == "__main__":
    main()
