import subprocess
from pathlib import Path
from constants import Constants as ct

INPUT_FOLDER = Path(ct.INPUT_FOLDER)
OUTPUT_FOLDER = Path(ct.OUTPUT_FOLDER)

MP3_FILES = list(INPUT_FOLDER.glob("*.mp3"))

print(len(MP3_FILES))

for i in MP3_FILES:
    print(i)
