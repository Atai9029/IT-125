import random
import asyncio
import time


class RussianRouletteGame:
    def __init__(self, p1, p2, time_limit=5):
        self.players = [p1, p2]
        self.turn = 0
        self.bullet = random.randint(1, 6)
        self.chamber = 0
        self.is_alive = True
        self.time_limit = time_limit
        self.last_turn_time = time.time()

    def current_player(self):
        return self.players[self.turn]

    def switch_turn(self):
        self.turn = 1 - self.turn
        self.last_turn_time = time.time()

    def shoot(self):
        if not self.is_alive:
            return "Игра окончена"

        
        if time.time() - self.last_turn_time > self.time_limit:
            self.is_alive = False
            return f"⏰ Время вышло! {self.current_player()} проиграл!"

        self.chamber += 1

        if self.chamber == self.bullet:
            self.is_alive = False
            return f"💥 БАХ! {self.current_player()} проиграл!"
        else:
            msg = f"😅 Пусто! Ход переходит к другому игроку."
            self.switch_turn()
            return msg
