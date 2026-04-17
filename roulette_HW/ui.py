import flet as ft
from game import Game


class UI:
    def __init__(self, max_lives: int, bullets_count: int, chambers: int = 6):
        self.max_lives = max_lives
        self.bullets_count = bullets_count
        self.chambers = chambers

        # ── Заголовок ───────────────────────────────────────────────────────
        self.title = ft.Text(
            "Русская рулетка",
            size=30,
            weight="bold",
            color="white",
            text_align=ft.TextAlign.CENTER,
        )

        self.subtitle = ft.Text(
            f"Пережи {Game.SURVIVE_ROUNDS} выстрелов, чтобы победить",
            size=13,
            color="#BBBBBB",
            text_align=ft.TextAlign.CENTER,
        )

        # ── Главное изображение ──────────────────────────────────────────────
        self.main_image = ft.Image(
            src="images/revolver.png",
            width=220,
            height=220,
        )

        self.hero_container = ft.Container(
            content=self.main_image,
            width=260,
            height=260,
            alignment=ft.Alignment.CENTER,
            bgcolor="#1B1B26",
            border_radius=22,
            rotate=ft.Rotate(angle=0, alignment=ft.Alignment.CENTER),
            scale=1,
            animate_rotation=ft.Animation(160, "easeInOut"),
            animate_scale=ft.Animation(140, "easeInOut"),
        )

        # ── Статус ───────────────────────────────────────────────────────────
        self.status = ft.Text(
            "Нажми «Выстрел», чтобы начать",
            size=20,
            weight="w600",
            color="white",
            text_align=ft.TextAlign.CENTER,
        )

        self.round_text = ft.Text(
            "Следующая камера: 1 / 6",
            size=16,
            color="#AAAAAA",
        )

        # ── Прогресс выживания ───────────────────────────────────────────────
        self.survive_text = ft.Text(
            f"Выжито: 0 / {Game.SURVIVE_ROUNDS}",
            size=14,
            color="#6699FF",
            text_align=ft.TextAlign.CENTER,
        )

        self.survive_bar = ft.ProgressBar(
            value=0,
            width=220,
            color="#4477DD",
            bgcolor="#2A2A3A",
        )

        # ── Барабан ──────────────────────────────────────────────────────────
        self._drum_cells: list[ft.Container] = []
        self.drum_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=8)
        self._build_drum_row()

        # ── Жизни / патроны ──────────────────────────────────────────────────
        self.hearts_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=8)

        self.bullets_label = ft.Text(
            "Заряжено патронов", size=16, color="#AAAAAA"
        )
        self.bullets_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=10)

        # ── История выстрелов ────────────────────────────────────────────────
        self.history_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=6,
            wrap=True,
        )

        # ── Кнопки ───────────────────────────────────────────────────────────
        self.shoot_btn = ft.ElevatedButton(
            "Выстрел",
            width=180,
            height=48,
            style=ft.ButtonStyle(
                bgcolor={"": "#C62828"},
                color={"": "white"},
                shape=ft.RoundedRectangleBorder(radius=12),
            ),
        )

        self.reset_btn = ft.OutlinedButton(
            "Перезарядка",
            width=180,
            height=48,
            style=ft.ButtonStyle(
                color={"": "white"},
                side={"": ft.BorderSide(1, "#555555")},
                shape=ft.RoundedRectangleBorder(radius=12),
            ),
        )

        self.note = ft.Text(
            "Звук включён, если установлен flet-audio",
            size=12,
            color="#888888",
            text_align=ft.TextAlign.CENTER,
        )

        self.update_lives(self.max_lives)
        self.update_bullets()

    # ── Вспомогательные ─────────────────────────────────────────────────────

    def _image(self, src: str, width: int = 36, height: int = 36):
        return ft.Image(src=src, width=width, height=height)

    def _build_drum_row(self):
        self._drum_cells = []
        for i in range(self.chambers):
            cell = ft.Container(
                width=30,
                height=30,
                border_radius=15,
                bgcolor="#2C2C3C",
                border=ft.border.all(2, "#555566"),
                tooltip=f"Камера {i + 1}",
            )
            self._drum_cells.append(cell)
        self.drum_row.controls = self._drum_cells

    # ── Публичные методы обновления ──────────────────────────────────────────

    def update_lives(self, lives: int):
        self.hearts_row.controls = [
            self._image(
                "images/heart_full.png" if i < lives else "images/heart_empty.png",
                width=38,
                height=38,
            )
            for i in range(self.max_lives)
        ]

    def update_bullets(self):
        self.bullets_row.controls = [
            self._image("images/bullet.png", width=34, height=34)
            for _ in range(self.bullets_count)
        ]

    def set_main_image(self, src: str):
        self.main_image.src = src

    def update_survive_progress(self, streak: int):
        total = Game.SURVIVE_ROUNDS
        self.survive_text.value = f"Выжито: {streak} / {total}"
        self.survive_bar.value = min(streak / total, 1.0)

    def update_drum(self, current_pos: int, highlight_pos=None):
        for i, cell in enumerate(self._drum_cells):
            pos = i + 1
            if pos == highlight_pos:
                cell.bgcolor = "#FF4444"
                cell.border = ft.border.all(2, "#FF8888")
            elif pos == current_pos:
                cell.bgcolor = "#3A5FCC"
                cell.border = ft.border.all(2, "#6688FF")
            else:
                cell.bgcolor = "#2C2C3C"
                cell.border = ft.border.all(2, "#555566")

    def reveal_drum(self, chamber_states: list):
        for i, has_bullet in enumerate(chamber_states):
            cell = self._drum_cells[i]
            cell.bgcolor = "#AA1111" if has_bullet else "#114411"
            cell.border = ft.border.all(2, "#FF4444" if has_bullet else "#44FF44")
            cell.tooltip = f"Камера {i + 1}: {'ПУЛЯ' if has_bullet else 'пусто'}"

    def add_history_item(self, kind: str):
        self.history_row.controls.append(
            self._image(
                "images/fire.png" if kind == "hit" else "images/smoke.png",
                width=26,
                height=26,
            )
        )

    def clear_history(self):
        self.history_row.controls.clear()

    # ── Сборка ───────────────────────────────────────────────────────────────

    def build(self):
        return ft.Container(
            expand=True,
            padding=20,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_CENTER,
                end=ft.Alignment.BOTTOM_CENTER,
                colors=["#10131A", "#181C24", "#0D0F14"],
            ),
            content=ft.SafeArea(
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        self.title,
                        self.subtitle,
                        self.hero_container,
                        self.status,
                        self.round_text,
                        self.survive_text,
                        self.survive_bar,
                        ft.Text("Барабан", size=14, color="#888888"),
                        self.drum_row,
                        ft.Text("История выстрелов", size=14, color="#888888"),
                        self.history_row,
                        ft.Text("Жизни", size=16, color="#AAAAAA"),
                        self.hearts_row,
                        self.bullets_label,
                        self.bullets_row,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=12,
                            controls=[self.shoot_btn, self.reset_btn],
                        ),
                        self.note,
                    ],
                )
            ),
        )
