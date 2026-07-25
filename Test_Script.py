import os
from pathlib import Path
from faster_whisper import WhisperModel

# 1. Initialize the model
# It's highly recommended to keep 'large-v3', as its recognition for mixed Chinese-English (code-switching) is significantly better than other versions.
model = WhisperModel("large-v3", device="cuda", compute_type="float16")

# 2. Set input and output paths
download_path = Path.home() / "Downloads"
extensions = [".mp3", ".wav", ".m4a", ".flac"]

# 3. Iterate through and process files
audio_files = [f for f in download_path.iterdir() if f.suffix.lower() in extensions]

print(f"Found {len(audio_files)} audio file(s). Preparing to process...")

for audio_file in audio_files:
    print(f"\n--- Processing: {audio_file.name} ---")

    # Transcribe parameters breakdown:
    # - language=None: Let the model auto-detect the language (ideal for mixed Chinese-English).
    # - task="transcribe": Maintain transcription in the original language.
    segments, info = model.transcribe(
        str(audio_file),
        beam_size=5,
        condition_on_previous_text=False,  # Solves the repetitive text bug
        vad_filter=True,  # Filters out silence and background noise
        vad_parameters=dict(min_silence_duration_ms=500)  # Fine-tunes VAD to avoid cutting off fluent Chinese-English speech
    )

    # Prepare the output filename (e.g., audio.mp3 -> audio_result.txt)
    output_file = audio_file.with_name(f"{audio_file.stem}_result.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        for segment in segments:
            line = f"[{segment.start:>7.2f}s -> {segment.end:>7.2f}s] {segment.text}"
            print(line)  # Real-time console display
            f.write(line + "\n")

print("\n✨ All files processed successfully! The results have been saved to the Downloads directory.")