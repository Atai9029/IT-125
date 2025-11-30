import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from scipy.fft import rfft, rfftfreq
import tkinter as tk
import threading
from tkinter import filedialog

audio_data = []
is_recording = False
sample_rate = 44100

def record_callback(indata, frames, time, status):
    audio_data.append(indata.copy())

def start_recording():
    global is_recording, audio_data
    is_recording = True
    audio_data = []
    print("Запись началась...")

    def rec():
        with sd.InputStream(samplerate=sample_rate, channels=1, callback=record_callback):
            while is_recording:
                sd.sleep(100)

    threading.Thread(target=rec).start()

def stop_recording():
    global is_recording, audio_data
    is_recording = False
    print("Запись остановлена")

    if audio_data:
        audio_data[:] = [x.flatten() for x in audio_data]
        audio_data[:] = [item for sub in audio_data for item in sub]
def save_file():
    if not audio_data:
        print("Нет данных!")
        return

    f = filedialog.asksaveasfilename(defaultextension=".wav")
    if f:
        arr = np.array(audio_data, dtype=np.float32)
        write(f, sample_rate, (arr * 32767).astype(np.int16))
        print("Файл сохранён!")

def detect_animal():
    if not audio_data:
        result_label.config(text="Сначала запиши звук")
        return

    arr = np.array(audio_data, dtype=np.float32)

    N = len(arr)
    if N < 1000:
        result_label.config(text="Слишком короткая запись")
        return

    yf = np.abs(rfft(arr))
    xf = rfftfreq(N, 1 / sample_rate)

    peak = xf[np.argmax(yf)]
    print("Пиковая частота:", peak)

    if 200 < peak < 600:
        result_label.config(text="Похоже на: СОБАКУ (гав)")
    elif 600 < peak < 2000:
        result_label.config(text="Похоже на: КОТА (мяу)")
    else:
        result_label.config(text="Не получилось определить")

root = tk.Tk()
root.title("Дикто")
root.geometry("300x300")

tk.Button(root, text="Запись", command=start_recording).pack(pady=5)
tk.Button(root, text="Стоп", command=stop_recording).pack(pady=5)
tk.Button(root, text="Сохранить", command=save_file).pack(pady=5)
tk.Button(root, text="Определить", command=detect_animal).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
