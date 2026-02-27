import yt_dlp
from yt_dlp.utils import DownloadError


def download_video(url: str, download_playlist: bool = True) -> None:
    """
    Download a YouTube video/short or playlist using yt_dlp.

    Tries a normal `best` MP4 download first. If YouTube returns a 403
    for the stream (SABR issue), it retries once with a more conservative
    format selection that avoids some problematic streaming formats.

    :param url: YouTube video/short/playlist URL
    :param download_playlist: If True and URL is a playlist, download all videos.
    """
    base_opts = {
        "outtmpl": "%(title)s.%(ext)s",  # file name = video title
        "noplaylist": not download_playlist,
        "quiet": False,
        "retries": 5,
        "fragment_retries": 5,
    }

    # First attempt: let yt_dlp pick a good format (mp4 when possible)
    primary_opts = {
        **base_opts,
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "merge_output_format": "mp4",
    }

    try:
        with yt_dlp.YoutubeDL(primary_opts) as ydl:
            ydl.download([url])
        return
    except DownloadError as err:
        # If it's not a 403 error, re-raise so the caller can see it
        if "403" not in str(err):
            raise
        print("\nGot HTTP 403 for normal formats, retrying with safer fallback formats...")

    # Second attempt: avoid some m3u8/DASH formats that are more likely
    # to hit SABR/403 issues. Stick to non-HLS MP4 where possible.
    fallback_opts = {
        **base_opts,
        "format": (
            "bestvideo[ext=mp4][protocol!=m3u8]+bestaudio[ext=m4a]/"
            "best[ext=mp4][protocol!=m3u8]/"
            "best[protocol!=m3u8]/"
            "worst"
        ),
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(fallback_opts) as ydl:
        ydl.download([url])


def ask_yes_no(prompt: str, default: bool = True) -> bool:
    """Simple Y/n prompt that returns a bool."""
    suffix = " [Y/n]: " if default else " [y/N]: "
    while True:
        answer = input(prompt + suffix).strip().lower()
        if not answer:
            return default
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")


def main() -> None:
    print("YouTube Video / Short / Playlist Downloader (No FFmpeg needed)")

    url = input("Paste YouTube URL (or press Enter to exit): ").strip()
    if not url:
        print("No URL entered. Exiting.")
        return

    download_playlist = ask_yes_no(
        "If this is a playlist, download ALL videos?", default=True
    )

    try:
        download_video(url, download_playlist=download_playlist)
        print("\nDownload complete! Check your folder for the files.")
    except DownloadError as e:
        print(f"\nError while downloading: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()
