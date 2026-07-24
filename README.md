# 🎙️ Qwen3-TTS on Intel ARC (XPU)

> Minimalist demo to run **Qwen3-TTS** locally using hardware acceleration on **Intel Arc GPUs** via *Intel Extension for PyTorch (IPEX)*.

[blog](https://albe.com.ar/articulo/clonar-cualquier-voz-con-qwen-sin-gastar-usd-2000-en-nvidia)
---

## 🚀 Features

- ⚡ **Hardware Acceleration:** Full support for Intel XPU (Intel Arc GPUs).
- 🗣️ **Voice Cloning:** Realistic audio generation using a short reference audio snippet (`reference.wav`).
- 🐧 **Enterprise Ready:** Tested and documented for Linux environments (Rocky Linux / RHEL).

---

## 🎯 Objective

While models like **Qwen3-TTS** natively support standard hardware ecosystems (such as NVIDIA GPUs and CPUs), running them purely on standard CPUs results in extremely slow inference times, making real-time or batch generation impractical. 

The main goal of this project is to bridge this gap for **Intel hardware users**. By leveraging **Intel Extension for PyTorch (IPEX)** and the `xpu` backend, this demo enables developers to run Qwen3-TTS locally on **Intel Arc GPUs**, unlocking proper hardware acceleration, maximizing performance efficiency, and making high-quality voice cloning accessible outside of traditional ecosystems.

## 🛠️ Hardware & Software Requirements

- **GPU:** Intel Arc (XPU-compatible).
- **Drivers:** Intel GPU drivers installed on the host system.
- **OS:** Rocky Linux (or another compatible Linux distribution).

---

## 📦 Installation (Rocky Linux)

Run the following commands in your terminal to set up the virtual environment and install the required dependencies:

```bash
# 1. Create the working directory in /opt (or your preferred path)
sudo mkdir -p /opt/xpu_cloner
sudo chown -R $USER:$USER /opt/xpu_cloner
cd /opt/xpu_cloner

# 2. Create and activate the virtual environment
python3 -m venv clean
source clean/bin/activate

# 3. Upgrade core Python packaging tools
python -m pip install --upgrade pip setuptools wheel

# 4. Install PyTorch with Intel XPU support
pip install torch==2.8.0+xpu torchvision==0.23.0+xpu torchaudio==2.8.0+xpu --index-url https://download.pytorch.org/whl/xpu

# 5. Install Intel Extension for PyTorch (IPEX)
pip install intel-extension-for-pytorch==2.8.10+xpu --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/

# 6. Install the Qwen TTS library
pip install qwen_tts
```

---

## ⚙️ Configuration & Usage

1. **Prepare your reference audio:**
   Place a reference WAV audio file named exactly `reference.wav` in the same directory as the script.

2. **Adjust the texts (Optional):**
   Edit `xpu_voice_cloner.py` to configure:
   - `REFERENCE_TEXT`: The exact transcription of your `reference.wav` file.
   - `TEXT_TO_GENERATE`: The new text you want the AI to speak using the cloned voice.

3. **Run the demo:**
   ```bash
   python xpu_voice_cloner.py
   ```

4. **Output:**
   Once completed, you will find the generated file `cloned_output.wav` with your cloned voice.

---

## 📝 Credits & Links
Based on the official [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) repository.
