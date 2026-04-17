import asyncio
from pathlib import Path

import flet as ft

from game import Game
from ui import UI

try:
    import flet_audio as fta
except ImportError:
    fta = None


class RouletteApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Русская рулетка"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.padding = 0

        if self.page.window is not None:
            self.page.window.width = 520
            self.page.window.height = 820
            self.page.window.resizable = False

        self.game = Game(chambers=6, bullets_count=2, max_lives=3)
        self.ui = UI(
            max_lives=self.game.max_lives,
            bullets_count=self.game.bullets_count,
            chambers=self.game.chambers,
        )
        self._busy = False

        self.shot_audio = None
        self._setup_audio()
        self.bind_events()
        self.refresh_ui()
        self.page.add(self.ui.build())

    # ── Аудио ────────────────────────────────────────────────────────────────

    def _setup_audio(self):
        if fta is None:
            self.ui.note.value = "Для звука установи: pip install flet-audio"
            return

        sound_path = Path(__file__).parent / "assets" / "sounds" / "shot.wav"
        if not sound_path.exists():
            self.ui.note.value = "Файл sounds/shot.wav не найден"
            return

        self.shot_audio = fta.Audio(src="sounds/shot.mp3", autoplay=False, volume=1.0)
        self.page.overlay.append(self.shot_audio)
        self.ui.note.value = "Звук выстрела активен"

    async def play_shot_sound(self):
        if self.shot_audio is None:
            return
        try:
            await self.shot_audio.play_async()
        except Exception:
            try:
                self.shot_audio.play()
            except Exception:
                self.ui.note.value = "Звук недоступен."
                self.page.update()

    # ── Привязка событий ─────────────────────────────────────────────────────

    def bind_events(self):
        self.ui.shoot_btn.on_click = self.shoot
        self.ui.reset_btn.on_click = self.restart

    # ── Обновление состояния UI ──────────────────────────────────────────────

    def refresh_ui(self):
        g = self.game
        self.ui.round_text.value = (
            f"Следующая камера: {g.current_position} / {g.chambers}"
        )
        self.ui.update_lives(g.lives)
        self.ui.update_bullets()
        self.ui.update_survive_progress(g.survived_streak)
        self.ui.update_drum(g.current_position)
        self.ui.shoot_btn.disabled = not g.alive or g.won or self._busy

    # ── Анимации ─────────────────────────────────────────────────────────────

    async def _shake_animation(self):
        """Анимация дрожания при попадании."""
        for dx in [0.08, -0.08, 0.05, -0.05, 0.02, 0.0]:
            self.ui.hero_container.rotate = ft.Rotate(
                angle=dx, alignment=ft.Alignment.CENTER
            )
            self.page.update()
            await asyncio.sleep(0.04)

    async def _spin_animation(self):
        """Плавное вращение перед выстрелом."""
        steps = [0.2, 0.55, 0.95, 1.35]
        scales = [1.05, 1.12, 1.18, 1.06]
        for i, angle in enumerate(steps):
            self.ui.hero_container.rotate = ft.Rotate(
                angle=angle, alignment=ft.Alignment.CENTER
            )
            self.ui.hero_container.scale = scales[i]
            self.page.update()
            if i == 1:
                await self.play_shot_sound()
            await asyncio.sleep(0.08)

    async def animate_shot(self, hit: bool, fired_chamber: int):
        self._busy = True
        self.refresh_ui()
        self.page.update()

        await self._spin_animation()

        self.ui.update_drum(self.game.current_position, highlight_pos=fired_chamber)

        if hit:
            self.ui.set_main_image("images/fire.png")
            self.ui.hero_container.scale = 1.22
            self.page.update()
            await asyncio.sleep(0.12)
            await self._shake_animation()
        else:
            self.ui.set_main_image("images/smoke.png")
            self.ui.hero_container.scale = 1.12
            self.page.update()
            await asyncio.sleep(0.14)

        self.ui.set_main_image("images/revolver.png")
        self.ui.hero_container.rotate = ft.Rotate(angle=0, alignment=ft.Alignment.CENTER)
        self.ui.hero_container.scale = 1
        self._busy = False

    # ── Основные обработчики ─────────────────────────────────────────────────

    async def shoot(self, e):
        if not self.game.alive or self.game.won or self._busy:
            return

        result = self.game.shot()
        fired_pos = result["position"]

        await self.animate_shot(hit=result["hit"], fired_chamber=fired_pos)

        self.ui.add_history_item("hit" if result["hit"] else "empty")

        if result["state"] == "won":
            self.ui.status.value = "Ты выжил! ПОБЕДА!"
            self.ui.status.color = "#FFD700"
            self.ui.reveal_drum(self.game.chamber_states())
            self.refresh_ui()
            self.page.update()
            self.show_dialog(
                "Победа!",
                f"Ты пережил {Game.SURVIVE_ROUNDS} выстрелов!\n"
                f"Жизней осталось: {self.game.lives}.\n"
                "Нажми «Перезарядка», чтобы сыграть снова.",
            )
            return

        if result["state"] == "dead":
            self.ui.status.value = "BOOM! Жизни закончились"
            self.ui.status.color = "#EF5350"
            self.ui.reveal_drum(self.game.chamber_states())
            self.refresh_ui()
            self.page.update()
            self.show_dialog(
                "Игра окончена",
                "Ты проиграл. Все жизни потрачены.\n"
                "Нажми «Перезарядка», чтобы начать заново.",
            )
            return

        if result["state"] == "hit":
            text = f"Попадание! Осталось жизней: {self.game.lives}"
            color = "#FFA726"
        else:
            text = "Щелчок... пусто. Повезло!"
            color = "#66BB6A"

        if result["respun"]:
            text += " Барабан прокручен заново."

        self.ui.status.value = text
        self.ui.status.color = color
        self.refresh_ui()
        self.page.update()

    async def restart(self, e):
        if self._busy:
            return

        self.game.reset()
        self.ui.status.value = "Нажми «Выстрел», чтобы начать"
        self.ui.status.color = "white"
        self.ui.set_main_image("images/revolver.png")
        self.ui.hero_container.rotate = ft.Rotate(angle=0, alignment=ft.Alignment.CENTER)
        self.ui.hero_container.scale = 1
        self.ui.clear_history()
        self.refresh_ui()
        self.page.update()

    # ── Диалог ───────────────────────────────────────────────────────────────

    def show_dialog(self, title: str, message: str):
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, weight="bold"),
            content=ft.Text(message),
            actions=[
                ft.TextButton("OK", on_click=lambda _: self.close_dialog()),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    def close_dialog(self):
        if self.page.dialog:
            self.page.dialog.open = False
            self.page.update()
