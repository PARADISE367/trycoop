import tkinter as tk
from PIL import ImageTk, Image
import pygame

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("moan.mp3")  # Укажите путь к вашему аудиофайлу
    pygame.mixer.music.play(-1)  # -1 означает бесконечное повторение

def exit_fullscreen():
    window.attributes("-fullscreen", False)

# Создаем графический интерфейс
window = tk.Tk()
window.title("moan and go")
# Устанавливаем окно в полноэкранный режим
window.attributes("-fullscreen", True)

# Создаем кнопку для выхода из полноэкранного режима
# Функция для обработки нажатия кнопки
def button_clicked():
    exit_button = tk.Button(window, text="Выход из полноэкранного режима", command=exit_fullscreen)
    exit_button.pack()

# Применяем стилизацию кнопки
button.config(
    highlightbackground="darkblue",  # Цвет границы кнопки
    highlightcolor="skyblue",  # Цвет границы кнопки при наведении
    highlightthickness=2,  # Толщина границы кнопки
    bg="lightblue",  # Цвет фона кнопки
    fg="black",  # Цвет текста на кнопке
    font=("Arial", 12),  # Шрифт и размер текста на кнопке
    relief=tk.RAISED  # Стиль границы кнопки
)

# Размещаем кнопку на окне
button.pack(pady=10)

# Создаем кнопку
button = tk.Button(window, text="Нажми меня", command=button_clicked)

# Загружаем фотографию
image = Image.open("gg.jpg")  # Укажите путь к вашей фотографии
photo = ImageTk.PhotoImage(image)
label = tk.Label(window, image=photo)
label.pack()

# Проигрываем звук
play_sound()

# Запускаем главный цикл окна
window.mainloop()
