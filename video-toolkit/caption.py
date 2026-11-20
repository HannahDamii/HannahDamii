import sys
from faster_whisper import WhisperModel
src, out = sys.argv[1], sys.argv[2]
model = WhisperModel("base.en", device="cpu", compute_type="int8")
segs, _ = model.transcribe(src, word_timestamps=False)
def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(s):02},{int((s%1)*1000):03}"
with open(out, "w") as f:
    for i, s in enumerate(segs, 1):
        f.write(f"{i}\n{ts(s.start)} --> {ts(s.end)}\n{s.text.strip()}\n\n")
print(open(out).read())
