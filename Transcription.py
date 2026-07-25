import os
from pathlib import Path
from faster_whisper import WhisperModel
import sys

# 1. Initialize the model
# Keep 'large-v3' for the best recognition accuracy
model = WhisperModel("large-v3", device="cuda", compute_type="float16")

# 2. Set input and output paths
download_path = Path.home() / "Downloads"
extensions = [".mp3", ".wav", ".m4a", ".flac"]

# 3. Iterate through and process files
audio_files = [f for f in download_path.iterdir() if f.suffix.lower() in extensions]
total_files = len(audio_files)

print(f"Found {total_files} audio file(s). Preparing to process...")

for index, audio_file in enumerate(audio_files, start=1):
    # Prepare the output filename
    output_file = audio_file.with_name(f"{audio_file.stem}_result.txt")

    # Transcribe parameters
    segments, info = model.transcribe(
        str(audio_file),
        language="en",  # Explicitly set language to English to boost recognition speed and accuracy
        beam_size=5,
        condition_on_previous_text=False,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500)
    )

    total_duration = info.duration  # Get total audio duration

    print(f"\n[{index}/{total_files}] Processing: {audio_file.name}")

    with open(output_file, "w", encoding="utf-8") as f:
        for segment in segments:
            # Calculate current progress percentage
            # 'segment.end' represents the timestamp where the current segment ends
            progress = (segment.end / total_duration) * 100
            if progress > 100: progress = 100  # Prevent floating-point inaccuracy from exceeding 100%

            # Construct the text to write into the file
            line = f"[{segment.start:>7.2f}s -> {segment.end:>7.2f}s] {segment.text}"
            f.write(line + "\n")

            # Update the progress in real-time on the console instead of printing the full text
            sys.stdout.write(f"\rProgress: {progress:.1f}% | Processed Duration: {segment.end:.1f}/{total_duration:.1f}s")
            sys.stdout.flush()

    # Move to a new line after finishing a file
    print(f"\nDone! Results saved to: {output_file.name}")

print("\n✨ All files processed successfully!")