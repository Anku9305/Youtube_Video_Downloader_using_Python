# YouTube Video Downloader (Python + yt-dlp)

Simple command‑line YouTube downloader built with Python and [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

It can download:

- Single **videos**
- **Shorts**
- **Playlists** (optional, you can choose whether to download the full playlist)

The script also includes logic to handle some recent YouTube changes that can cause `HTTP Error 403: Forbidden` by retrying with safer fallback formats.

---

## Requirements

- **Python 3.8+** (recommended)
- `yt-dlp` Python package

Install `yt-dlp`:

```bash
pip install -U yt-dlp
```

If you have multiple Python versions, you may need:

```bash
python -m pip install -U yt-dlp
```

---

## How to Run

From the project folder:

```bash
python Videodownloader.py
```

Then:

1. Paste a YouTube URL (video / short / playlist).
2. Choose whether to download **all videos** if it is a playlist (`Y/n` question).
3. Wait for the download to finish. Files will appear in the **current folder** with the video title as the filename.

---

## Error Handling & 403 Fix

The script:

- First tries a **normal best‑quality MP4 download** (video + audio).
- If YouTube returns **HTTP 403** for the stream, it automatically **retries with safer fallback formats** that avoid some problematic streaming types.
- Prints clear error messages if something still goes wrong.

Keeping `yt-dlp` **up to date** is important because YouTube changes often:

```bash
python -m pip install -U yt-dlp
```

---

## Notes

- Downloads go to the same folder where you run the script.
- Playlist downloads can be large; make sure you have enough disk space.
- This project is for **personal/educational use**. Respect YouTube’s Terms of Service and copyright rules.

