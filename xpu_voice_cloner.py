import warnings
import os

os.environ["PYTHONWARNINGS"] = "ignore"
os.environ["TORCH_CPP_LOG_LEVEL"] = "ERROR"

warnings.filterwarnings("ignore")

# --------------------------------------------
# Qwen3-TTS Intel ARC XPU Demo
# --------------------------------------------
#
# Ejemplo de clonación de voz usando:
# - Intel Extension for PyTorch
# - Intel ARC GPU (XPU)
# - Qwen3-TTS Base Model
#
# Colocar el WAV de referencia como:
#     reference.wav
#
# Ejecutar:
#     python xpu_voice_cloner.py
#
# --------------------------------------------

# Imports pesados solamente cuando ejecutamos
import torch
import intel_extension_for_pytorch as ipex
import soundfile as sf
import transformers

transformers.modeling_utils.caching_allocator_warmup = (
    lambda *args, **kwargs: None
)

from qwen_tts import Qwen3TTSModel

REFERENCE_AUDIO = "reference.wav"
OUTPUT_AUDIO = "cloned_output.wav"

MODEL_ID = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"


# Texto exacto correspondiente al WAV
REFERENCE_TEXT = (
    " No es espectacular, si bien en Barcelona ellos eran chiquitos y íbamos a ver entrenamientos "
    " empezábamos a ver algunos partidos que recien empezaban a jugar, aca lo estoy viviendo mucho mas "
    " con toda la semana y pasamos mucho tiempo en el club porque entrenan tres o cuatro veces por semana "
    " tienen partido, no, cuando estan jugando depende, son muy diferentes tambien, a Thiago no, no le puedo hablar, "
    " no le puedo decir nada porque reacciona de una manera, y a Mateo todo lo contrario, está continuamente para "
)


TEXT_TO_GENERATE = (
    " Hola argentinos. Lamentablemente esta vez no se pudo traer la Copa. "
    "Lo intentamos hasta el final, dejamos todo, pero el fútbol a veces tiene estas cosas. "
    "Gracias por el apoyo, por el cariño y por acompañarnos siempre. "
    "Sentimos ese aliento en cada partido. "
    "Vamos a seguir trabajando y defendiendo esta camiseta como siempre. "
    "Gracias de corazón. Un abrazo grande."
)


def main():

    print("""
============================================================
              Qwen3-TTS Voice Clone Demo
============================================================

Modelo:
  Qwen/Qwen3-TTS-12Hz-1.7B-Base

Backend:
  Intel Extension for PyTorch (IPEX)
  Intel ARC GPU - XPU acceleration

Proceso:
  1. Cargar modelo Qwen3-TTS en Intel ARC XPU
  2. Usar audio de referencia para clonar voz
  3. Generar nuevo audio con la voz clonada

============================================================
""")



    if not os.path.isfile(REFERENCE_AUDIO):
        print(
            f"ERROR: falta el archivo {REFERENCE_AUDIO}"
        )
        print(
            "Coloque un WAV de referencia junto al script."
        )
        return


    # --------------------------------------------
    # Verificar Intel XPU
    # --------------------------------------------

    print("Verificando dispositivo XPU...")

    if not torch.xpu.is_available():
        print()
        print("ERROR: Intel XPU no está disponible.")
        print("Verifique:")
        print("- Driver Intel GPU instalado")
        print("- Intel Extension for PyTorch instalado")
        print("- GPU Intel ARC compatible")
        return


    print("XPU disponible:")
    print("PyTorch:", torch.__version__)
    print("IPEX:", ipex.__version__)
    print("XPU:", torch.xpu.get_device_name())

    print("============================================================")
    print(" ")
    print("Cargando Qwen3-TTS en Intel ARC XPU...")


    model = Qwen3TTSModel.from_pretrained(
        MODEL_ID,
        device_map="xpu",
        dtype=torch.bfloat16,
        attn_implementation="sdpa",
    )


    print("Generando voz clonada...")


    wavs, sr = model.generate_voice_clone(
        text=TEXT_TO_GENERATE,
        language="spanish",
        ref_audio=REFERENCE_AUDIO,
        ref_text=REFERENCE_TEXT,
    )


    audio = wavs[0]

    if hasattr(audio, "cpu"):
        audio = audio.cpu().numpy()


    sf.write(
        OUTPUT_AUDIO,
        audio,
        sr
    )


    print()
    print("OK - Audio generado:")
    print(OUTPUT_AUDIO)


if __name__ == "__main__":
    main()
