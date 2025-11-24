import tkinter as tk
from tkinter import PhotoImage
import pygame

# Инициализация звука
pygame.mixer.init()

# Функция воспроизведения звука
def play(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()

# Окно
root = tk.Tk()
root.title("Meme Soundboard")
root.geometry("650x420")
root.configure(bg="#1e1e1e")

# Загрузка картинок
img_jackson = PhotoImage(file="images/Hee-hee.png")
img_scared_cat = PhotoImage(file="images/Испугался-не-бойся.png")
img_giga = PhotoImage(file="images/Гигачад.png")
img_troll = PhotoImage(file="images/Trollface.png")
img_yes_cat = PhotoImage(file="images/еще_один_кот.png")

# Кнопки
btn1 = tk.Button(
    root, image=img_jackson, 
    command=lambda: play("sounds/Hee-hee.wav")
)
btn2 = tk.Button(
    root, image=img_scared_cat, 
    command=lambda: play("sounds/испугался_не_бойся.wav")
)
btn3 = tk.Button(
    root, image=img_giga, 
    command=lambda: play("sounds/Гигачад.wav")
)
btn4 = tk.Button(
    root, image=img_troll, 
    command=lambda: play("sounds/trollFace.wav")
)
btn5 = tk.Button(
    root, image=img_yes_cat, 
    command=lambda: play("sounds/еще_один_кот.wav")
)

# Расположение
btn1.grid(row=0, column=0, padx=15, pady=15)
btn2.grid(row=0, column=1, padx=15, pady=15)
btn3.grid(row=0, column=2, padx=15, pady=15)
btn4.grid(row=1, column=0, padx=15, pady=15)
btn5.grid(row=1, column=1, padx=15, pady=15)

root.mainloop()
