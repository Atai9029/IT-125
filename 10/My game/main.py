from engine import start_game   # ← правильный импорт

def main():
    print("Добро пожаловать в лабиринт с призраками!")
    name = input("Введите ваше имя: ")
    print(f"Удачи, {name}! Игра начинается...")
    start_game(name)

if __name__ == "__main__":
    main()
