"""Auto-caption a video: python3 -I caption.py input.mp4 output.srt"""
import subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

src, out = sys.argv[1], sys.argv[2]
# Decode audio with ffmpeg (avoids PyAV version issues) -> 16 kHz mono float32
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                     check=True, capture_output=True).stdout
audio = np.frombuffer(raw, np.float32)
model = WhisperModel("base.en", device="cpu", compute_type="int8")
segs, _ = model.transcribe(audio)

def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(s):02},{int(round((s % 1) * 1000)) % 1000:03}"

with open(out, "w") as f:
    for i, s in enumerate(segs, 1):
        f.write(f"{i}\n{ts(s.start)} --> {ts(s.end)}\n{s.text.strip()}\n\n")
print(open(out).read())
