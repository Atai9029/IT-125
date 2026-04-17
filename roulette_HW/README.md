# Русская рулетка на Flet

Что добавлено:
- звук выстрела;
- жизни;
- несколько пуль;
- плавная async-анимация;
- картинки вместо эмодзи.

## Запуск

```bash
pip install -r requirements.txt
flet run main.py
```

Если нужен веб-запуск:

```bash
flet run --web main.py
```

## Структура

- `main.py` — точка входа;
- `app.py` — логика приложения и анимации;
- `game.py` — механика игры;
- `ui.py` — интерфейс;
- `assets/images/*` — картинки;
- `assets/sounds/shot.wav` — звук выстрела.
