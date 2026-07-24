# 🎙️ Qwen3-TTS en Intel ARC (XPU)

> Demo mínima para ejecutar **Qwen3-TTS** localmente utilizando aceleración por hardware en GPUs **Intel ARC** mediante *Intel Extension for PyTorch (IPEX)*.

[🇬🇧 Read in English](README.md)

---

## 🚀 Características

- ⚡ **Aceleración por Hardware:** Soporte completo para Intel XPU (GPUs Intel Arc).
- 🗣️ **Clonación de Voz:** Generación de audio realista a partir de un pequeño fragmento de referencia (`reference.wav`).
- 🐧 **Listo para Enterprise:** Probado y documentado para entornos basados en Linux (Rocky Linux / RHEL).

---

## 🎯 Objetivo

Si bien modelos avanzados como **Qwen3-TTS** están preparados de forma nativa para ejecutarse en CPUs y GPUs NVIDIA, correrlos puramente sobre CPU genera tiempos de inferencia sumamente lentos, volviendo la generación de voz poco práctica para el día a día.

El objetivo principal de este proyecto es derribar esa barrera para los usuarios de **hardware Intel**. Mediante el uso de **Intel Extension for PyTorch (IPEX)** y el backend `xpu`, esta demo permite aprovechar la potencia de las **GPUs Intel Arc**, logrando una aceleración real por hardware, optimizando el rendimiento y haciendo viable la clonación y síntesis de voz local fuera de los ecosistemas tradicionales.


## 🛠️ Requisitos de Hardware y Software

- **GPU:** Intel Arc (compatible con XPU).
- **Drivers:** Drivers de Intel para GPU instalados en el sistema.
- **OS:** Rocky Linux (u otra distro Linux compatible).

---

## 📦 Instalación (Rocky Linux)

Sigue estos pasos en la terminal para preparar el entorno virtual e instalar las dependencias necesarias:

```bash
# 1. Crear directorio de trabajo en /opt (o tu ruta preferida)
sudo mkdir -p /opt/xpu_cloner
sudo chown -R $USER:$USER /opt/xpu_cloner
cd /opt/xpu_cloner

# 2. Crear y activar el entorno virtual
python3 -m venv clean
source clean/bin/activate

# 3. Actualizar herramientas base de Python
python -m pip install --upgrade pip setuptools wheel

# 4. Instalar PyTorch con soporte para Intel XPU
pip install torch==2.8.0+xpu torchvision==0.23.0+xpu torchaudio==2.8.0+xpu --index-url https://download.pytorch.org/whl/xpu

# 5. Instalar Intel Extension for PyTorch (IPEX)
pip install intel-extension-for-pytorch==2.8.10+xpu --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/

# 6. Instalar la librería del modelo de voz
pip install qwen_tts
```

---

## ⚙️ Configuración y Uso

1. **Prepara tu audio de referencia:**
   Coloca un archivo de audio en formato WAV llamado exactamente `reference.wav` en el mismo directorio del script.

2. **Ajusta los textos (Opcional):**
   Edita el script `xpu_voice_cloner.py` para configurar:
   - `REFERENCE_TEXT`: Lo que dice exactamente el archivo `reference.wav`.
   - `TEXT_TO_GENERATE`: El texto que deseas que la IA lea con la voz clonada.

3. **Ejecuta la demo:**
   ```bash
   python xpu_voice_cloner.py
   ```

4. **Resultado:**
   Al finalizar, obtendrás un archivo llamado `cloned_output.wav` con la voz sintetizada.

---

## 📄 Licencia

Este proyecto es de código abierto bajo la [Licencia Apache 2.0](LICENSE).
