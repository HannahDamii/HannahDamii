# Instagram video editing toolkit

Tools Claude uses to edit my Reels in Claude Code cloud sessions
(environment: **HannahDamii video editing**). Its setup script installs
them at the start of each session.

| Tool | What it does | Install | Status |
|---|---|---|---|
| FFmpeg | cutting, audio, resizing, burning in captions | preinstalled | tested ✅ |
| Remotion | animated titles (React → MP4) | `npm i remotion@4 @remotion/cli@4 react@18 react-dom@18` in a project | tested ✅ |
| HyperFrames | animated graphics/overlays (HTML → MP4) | `npm i -g hyperframes@0.9.72` | tested ✅ |
| Whisper (faster-whisper) | auto captions | `pip install faster-whisper` | installed; model download needs Hugging Face hosts allowed |
| yt-dlp | downloads videos from links | `pip install yt-dlp` | installed; Instagram is blocked from the cloud, so upload clips instead |

## Notes for Claude
- Render in the cloud with the preinstalled headless Chromium:
  - Remotion: `--browser-executable=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell)`
  - HyperFrames: set `PRODUCER_HEADLESS_SHELL_PATH` to that same path.
- Captions: `HF_HUB_DISABLE_XET=1 python3 -I video-toolkit/caption.py input.mp4 output.srt`
- Hosts Whisper needs: huggingface.co, us.aws.cdn.hf.co, cas-server.xethub.hf.co (plus the cdn-lfs hosts).
- Output format: vertical 1080x1920 for Reels.
- I work from my phone/iPad: I upload clips, you send back finished videos.
