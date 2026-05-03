"""
transcribe-url.py — Audio transcription helper for /learn skill.

Takes a short-form video URL (TikTok, IG Reels, IG Posts, YouTube Shorts, X video)
and returns JSON {transcript, publisher, title, url, source-date, duration} on stdout.

INVOCATION (from /learn or manual testing):
    py -3.11 "Optimus Academy/tools/transcribe-url.py" <URL>

Never invoke as `python transcribe-url.py` or `python3 transcribe-url.py`.
Python 3.14 is broken on this machine and sits ahead of 3.11 on PATH.
The yt-dlp module is imported directly; the yt-dlp.exe shim is NOT used.

DEPENDENCIES (verified installed at build time):
    - Python 3.11.9 via py -3.11 launcher
    - openai-whisper 20250625
    - yt-dlp 2026.3.17
    - ffmpeg 8.1 on PATH

NO API KEY required. Whisper runs locally; the only paid API in the larger
/learn pipeline is the existing Anthropic SDK key (used by /learn itself,
not by this script).

EXIT CODES:
    0 — success; stdout has valid JSON
    1 — runtime error during download/transcription; stderr has details
    3 — yt-dlp Python module missing for active interpreter
    4 — ffmpeg missing on PATH
    5 — openai-whisper missing for active interpreter
    6 — wrong Python version (must be 3.11)

UPGRADE PATH (do NOT change without measurement):
    The default Whisper model is "base" — fast, accurate enough for clear
    short-form speech. If accuracy proves insufficient (noisy audio, heavy
    technical jargon, non-native speakers requiring manual transcript
    cleanup more than once per week), swap WHISPER_MODEL to "large".
    Tradeoff: 5-10x slower transcription, ~3 GB model pre-download required.
"""

import os
import sys
import shutil
import json
import tempfile

WHISPER_MODEL = "base"

# Preflight 1: ffmpeg must be on PATH (yt-dlp's audio extraction depends on it)
if shutil.which("ffmpeg") is None:
    print(
        "ERROR: ffmpeg not on PATH. Install ffmpeg and ensure it's in your PATH. "
        "Windows: scoop install ffmpeg or choco install ffmpeg.",
        file=sys.stderr,
    )
    sys.exit(4)

# Preflight 2: yt-dlp must be importable as a Python module (NOT the .exe shim)
try:
    import yt_dlp
except ImportError:
    print(
        "ERROR: yt-dlp Python module not installed for the active Python. "
        "Run: py -3.11 -m pip install yt-dlp",
        file=sys.stderr,
    )
    sys.exit(3)

# Preflight 3: openai-whisper must be importable
try:
    import whisper
except ImportError:
    print(
        "ERROR: openai-whisper Python module not installed for the active Python. "
        "Run: py -3.11 -m pip install openai-whisper",
        file=sys.stderr,
    )
    sys.exit(5)

# Preflight 4: Python version sanity (defensive — should already be 3.11 if invoked correctly)
if sys.version_info[:2] != (3, 11):
    print(
        f"ERROR: this script requires Python 3.11. Active interpreter is "
        f"{sys.version_info.major}.{sys.version_info.minor}. "
        f"Invoke via: py -3.11 \"Optimus Academy/tools/transcribe-url.py\" <URL>",
        file=sys.stderr,
    )
    sys.exit(6)


def transcribe(url: str) -> dict:
    """Download audio for `url`, transcribe with Whisper, return JSON-shaped dict."""
    temp_dir = tempfile.mkdtemp(prefix="optimus-transcribe-")
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(temp_dir, "%(id)s.%(ext)s"),
            "quiet": True,
            "no_warnings": True,
            "noprogress": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "128",
                }
            ],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        audio_id = info.get("id")
        audio_path = os.path.join(temp_dir, f"{audio_id}.mp3")
        if not os.path.exists(audio_path):
            for fname in os.listdir(temp_dir):
                if fname.startswith(audio_id):
                    audio_path = os.path.join(temp_dir, fname)
                    break
        if not os.path.exists(audio_path):
            raise RuntimeError(f"audio file not found after yt-dlp download in {temp_dir}")

        model = whisper.load_model(WHISPER_MODEL)
        result = model.transcribe(audio_path, fp16=False)
        transcript = (result.get("text") or "").strip()

        publisher = (
            info.get("uploader")
            or info.get("channel")
            or info.get("uploader_id")
            or "unknown"
        )
        title = info.get("title") or info.get("description") or "untitled"

        upload_date_raw = info.get("upload_date")
        if upload_date_raw and len(upload_date_raw) == 8:
            source_date = f"{upload_date_raw[:4]}-{upload_date_raw[4:6]}-{upload_date_raw[6:8]}"
        else:
            source_date = "unknown"

        duration_seconds = info.get("duration")
        if duration_seconds is not None:
            mins, secs = divmod(int(duration_seconds), 60)
            duration = f"{mins}:{secs:02d}"
        else:
            duration = "unknown"

        return {
            "transcript": transcript,
            "publisher": publisher,
            "title": title,
            "url": url,
            "source_date": source_date,
            "duration": duration,
        }
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "ERROR: expected exactly one argument (the URL). "
            "Usage: py -3.11 \"Optimus Academy/tools/transcribe-url.py\" <URL>",
            file=sys.stderr,
        )
        return 1

    url = sys.argv[1].strip()
    if not url:
        print("ERROR: empty URL argument.", file=sys.stderr)
        return 1

    try:
        result = transcribe(url)
    except yt_dlp.utils.DownloadError as exc:
        print(f"ERROR: yt-dlp download failed: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"ERROR: transcription failed: {exc.__class__.__name__}: {exc}", file=sys.stderr)
        return 1

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
