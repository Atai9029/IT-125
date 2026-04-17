import random


class Game:
    """
    Логика игры «Русская рулетка».

    Победа: пережить SURVIVE_ROUNDS выстрелов.
    Поражение: жизни опускаются до 0.
    """

    SURVIVE_ROUNDS = 6  # сколько выстрелов нужно пережить, чтобы победить

    def __init__(self, chambers: int = 6, bullets_count: int = 2, max_lives: int = 3):
        self.chambers = chambers
        self.bullets_count = bullets_count
        self.max_lives = max_lives
        self.reset()

    def reset(self):
        self.current_position = 1
        self.lives = self.max_lives
        self.alive = True
        self.won = False
        self.total_shots = 0
        self.survived_streak = 0
        self.history: list[str] = []
        self.spin_drum()

    def spin_drum(self):
        self.bullet_positions = set(
            random.sample(range(1, self.chambers + 1), self.bullets_count)
        )

    def chamber_states(self) -> list[bool]:
        """True = пуля, False = пусто (позиции 1..chambers)."""
        return [(i + 1) in self.bullet_positions for i in range(self.chambers)]

    def shot(self) -> dict:
        if not self.alive or self.won:
            return {
                "state": "game_over",
                "hit": False,
                "lives": self.lives,
                "position": self.current_position,
                "respun": False,
            }

        chamber = self.current_position
        hit = chamber in self.bullet_positions
        self.total_shots += 1

        if hit:
            self.lives -= 1
            self.history.append("hit")
            if self.lives <= 0:
                self.alive = False
                return {
                    "state": "dead",
                    "hit": True,
                    "lives": self.lives,
                    "position": chamber,
                    "respun": False,
                }
            state = "hit"
        else:
            state = "empty"
            self.history.append("empty")

        self.survived_streak += 1
        if self.survived_streak >= self.SURVIVE_ROUNDS:
            self.won = True
            return {
                "state": "won",
                "hit": False,
                "lives": self.lives,
                "position": chamber,
                "respun": False,
            }

        self.current_position += 1
        respun = False
        if self.current_position > self.chambers:
            self.current_position = 1
            self.spin_drum()
            respun = True

        return {
            "state": state,
            "hit": hit,
            "lives": self.lives,
            "position": chamber,
            "respun": respun,
        }
