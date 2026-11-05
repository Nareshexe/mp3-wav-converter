import subprocess
import sys
import shutil
from pathlib import Path
from constants import Constants as ct

INPUT_FOLDER = Path(ct.INPUT_FOLDER)
OUTPUT_FOLDER = Path(ct.OUTPUT_FOLDER)
FFMPEG_PATH = shutil.which("ffmpeg")

if FFMPEG_PATH is None:
    print(
        "ffmpeg is not installed or not found in PATH. Please install ffmpeg to proceed."
    )
    sys.exit(1)
if not INPUT_FOLDER.is_dir():
    print(f"Input folder {INPUT_FOLDER} does not exist. Exiting.")
    sys.exit(1)
MP3_FILES = list(INPUT_FOLDER.glob("*.mp3"))
if not MP3_FILES:
    print(f"No mp3 files found in {INPUT_FOLDER}. Exiting.")
    sys.exit(1)
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

for i in MP3_FILES:
    output_file = OUTPUT_FOLDER / i.with_suffix(".wav").name
    if output_file.exists():
        print(f"Output file {output_file.name} already exists. Skipping conversion.")
        continue
    print(f"Converting {i.name} to wav...")
    command = [FFMPEG_PATH, "-i", str(i), str(output_file)]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Successfully converted {i.name} to {output_file.name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert file: {i.name} with error: {e}")
        print(f"ffmpeg output: {e.stderr}")
    except FileNotFoundError as e:
        print(
            f"ffmpeg not found. Please ensure it is installed and in your PATH. Error: {e}"
        )
