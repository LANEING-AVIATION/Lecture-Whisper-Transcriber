# Lecture-Whisper-Transcriber 🎓✨

A lightweight, localized, and efficient tool to transcribe long-duration lectures, classroom recordings, and seminars using the state-of-the-art **OpenAI Whisper (large-v3)** model via `faster-whisper`. 

Stop draining your energy and focus by manually transcribing lengthy academic content. Just record the audio on your phone, run the script locally, and paste the generated clean text directly into **Gemini**, ChatGPT, or Claude to automatically compile well-organized study notes!

![Introduction](https://github.com/LANEING-AVIATION/Lecture-Whisper-Transcriber/blob/main/Gemini_Generated_Image_.png)

---

## 🚀 Key Highlights & Advantages

* **Superior Quality via Offline Recording:** Continuous, uninterrupted local recording on your mobile device yields vastly superior audio quality than real-time cloud translation services.
* **Battery & Power Efficient:** Saves massive phone battery consumption since it doesn't require live screen-on processing or continuous web uploading during the lecture.
* **100% Offline & Network Independent:** No reliance on active internet connections or cellular data during either the recording or transcription phases.
* **Zero-Attention Automation:** Once the script starts, it processes all files in batch. You can walk away without any mid-session supervision.
* **AI-Ready Text Outputs:** Generates structural timestamps that map seamlessly into Large Language Models (like the Gemini Web Interface) for lightning-fast note summarization.

---

## 📋 Prerequisites & Tested Environments

### Validated Environments
* **OS:** Linux (Tested natively on **Ubuntu 22.04 LTS**). *Should theoretically run perfectly on Windows native and Windows Subsystem for Linux (WSL), though not extensively tested.*
* **Hardware:** Dedicated NVIDIA GPU with **at least 8GB VRAM** (Tested and verified on an **NVIDIA RTX 4060 Laptop GPU**).

### Software Requirements
* **CUDA Toolkit:** v12.0 or higher
* **Python Runtime:** version 3.10+ managed via Conda
* **Model Weight Source:** Automatically fetched from Hugging Face during the first execution.

---

## ⚙️ Environment Configuration

Follow these steps to set up your isolated Conda environment and install all dependencies:

```bash
# 1. Create a new conda environment with Python 3.10
conda create -n whisper-env python=3.10 -y

# 2. Activate the newly created environment
conda activate whisper-env

# 3. Install PyTorch with CUDA 12 support (adjust cudatoolkit version if necessary)
# Visit https://pytorch.org/get-started/locally/ for the exact command matching your environment
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia -y

# 4. Install faster-whisper via pip (optimized Whisper implementation using CTranslate2)
pip install faster-whisper
```

---

## 🛠️ Usage Workflow

1. **Record:** Use your smartphone's built-in recorder to capture the lecture (Smartphones typically feature much better directional microphone hardware and noise isolation than laptops).
2. **Transfer:** Export your recording as an audio file (`.mp3`, `.wav`, `.m4a`, or `.flac`) and copy it into the default **`Downloads`** directory of your target computer (`~/Downloads`).
3. **Execute:** Run one of the provided Python scripts depending on your preference for output display.

---

## 📂 Project Structure & Script Options

The repository contains two operational scripts designed to target different linguistic use cases:

### 1. `Test_Script.py` (Multilingual / Mixed Code-Switching)
Best suited for lectures delivered in mixed languages (e.g., Chinese-English code-switching). It prints out full text segments directly to your terminal screen in real-time.
* **Language Detection:** Automatic.
* **Console Behavior:** Prints the transcribed text live line-by-line.

```bash
python Test_Script.py
```

### 2. `Transcription.py` (Pure English / High Efficiency)
Optimized specifically for purely English lectures. It skips full-text terminal printing, showing a clean, real-time dynamic percentage progress bar instead.
* **Language Setting:** Hardcoded to `"en"` to maximize recognition speed and layout accuracy.
* **Console Behavior:** Shows a single-line progress indicator (`Progress: XX.X%`).

```bash
python Transcription.py
```

### Output File
Both scripts automatically look for supported formats in `~/Downloads` and save the corresponding text output as `<original_filename>_result.txt` right alongside the source audio.

---

## ⚖️ Copyright Disclaimer

**IMPORTANT NOTICE FOR USERS & DEVELOPERS:**

This software utility is intended solely for personal study, academic research, and private note-taking purposes. 

1. **Intellectual Property:** Classroom lectures, professor presentations, seminar discussions, and course materials are generally protected by copyright law and belong to the respective lecturers, speakers, or academic institutions.
2. **Consent Requirement:** Before recording any lecture or utilizing this software to transcribe audio, you are highly encouraged to obtain explicit consent from the instructor or event host. 
3. **Distribution Warning:** Distributing, publishing, or sharing transcribed texts or generated notes derived from copyrighted lectures without authorization may constitute copyright infringement.
4. **Developer Liability:** The developer of this tool provides the source code "as-is" without any express or implied warranties. The developer assumes **no responsibility or liability** for any legal complications, academic policy violations, or intellectual property disputes arising from the misuse, unauthorized recording, or distribution of data processed by this program.
