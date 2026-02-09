from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from core.quiz import Quiz
from core.roulette import RussianRouletteGame
import os


class BotHandlers:
    def __init__(self, bot):
        self.router = Router()
        self.bot = bot
        self.quiz = Quiz()
        self.user_data = {}
        
        self.roulette_games = {}
        self.register_handlers()

    def register_handlers(self):
        self.router.message.register(self.start_command, Command("start"))

        
        self.router.message.register(self.start_quiz, Command("quiz"))
        self.router.callback_query.register(self.handle_answer)

        
        self.router.message.register(self.start_roulette, Command("roulette"))
        self.router.message.register(self.shoot_roulette, Command("shoot"))
        self.router.message.register(self.stop_roulette, Command("stop"))

        self.router.message.register(self.handle_names)

    
    async def start_command(self, message: types.Message):
        await message.answer(
            "Привет 👋\n"
            "Напиши /roulette чтобы начать русскую рулетку 🔫\n"
            "После /roulette используй /shoot для выстрела и /stop чтобы остановиться."
        )

    
    async def start_quiz(self, message: types.Message):
        user_id = message.from_user.id
        self.user_data[user_id] = {"score": 0, "q_index": 0}
        await self.send_question(message.chat.id, user_id)

    
    async def send_question(self, chat_id, user_id):
        data = self.user_data.get(user_id)
        if not data:
            await self.bot.send_message(chat_id, "Сначала начни викторину командой /quiz")
            return

        q_index = data["q_index"]
        question = self.quiz.get_question(q_index)

        if not question:
            await self.finish_quiz(chat_id, user_id)
            return

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=opt, callback_data=opt)]
                for opt in question["options"]
            ]
        )

        text = f"❓ {question['question']}"

        
        if "image" in question and os.path.exists(question["image"]):
            photo = FSInputFile(question["image"])
            await self.bot.send_photo(
                chat_id,
                photo=photo,
                caption=text,
                reply_markup=keyboard
            )
        else:
            await self.bot.send_message(chat_id, text, reply_markup=keyboard)

    
    async def handle_answer(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        data = self.user_data.get(user_id)

        if not data:
            await callback.answer("Сначала запусти викторину через /quiz", show_alert=True)
            return

        question_data = self.quiz.get_question(data["q_index"])
        selected_answer = callback.data

        if selected_answer == question_data["correct"]:
            data["score"] += 1

        data["q_index"] += 1

        await callback.answer("Ответ принят!")
        await self.send_question(callback.message.chat.id, user_id)

    
    async def finish_quiz(self, chat_id, user_id):
        score = self.user_data[user_id]["score"]
        total = self.quiz.total_questions()

        await self.bot.send_message(
            chat_id,
            f"🏁 Викторина окончена!\nТвой результат: {score} из {total}"
        )

        del self.user_data[user_id]

    # Рулетка

    async def start_roulette(self, message: types.Message):
        user_id = message.from_user.id
        if self.roulette_games.get(user_id):
            await message.answer("Игра уже запущена! Используй /shoot или /stop.")
            return

        
        self.roulette_games[user_id] = {"state": "wait_names"}
        await message.answer("Введите имена двух игроков через запятую:\nПример: Эпштейн, Иван")

    async def handle_names(self, message: types.Message):
        user_id = message.from_user.id
        game = self.roulette_games.get(user_id)

        if not game or game.get("state") != "wait_names":
            return

        
        try:
            p1, p2 = [x.strip() for x in message.text.split(",")]
        except Exception:
            await message.answer("Неверный формат. Напиши так: Имя1, Имя2")
            return

        
        game_obj = RussianRouletteGame(p1, p2, time_limit=5)
        game["obj"] = game_obj
        game["state"] = "playing"

        await message.answer(
            f"🎯 Игра началась!\n"
            f"Игроки: {p1} vs {p2}\n\n"
            f"Ходит: {game_obj.current_player()}\n"
            f"Нажимай /shoot (5 секунд!)"
        )

    async def shoot_roulette(self, message: types.Message):
        user_id = message.from_user.id
        game = self.roulette_games.get(user_id)

        if not game or game.get("state") != "playing":
            await message.answer("Сначала запусти игру командой /roulette")
            return

        result = game["obj"].shoot()
        await message.answer(result)

        if not game["obj"].is_alive:
            del self.roulette_games[user_id]
        else:
            await message.answer(f"👉 топает: {game['obj'].current_player()} (5 second!) /shoot")

    async def stop_roulette(self, message: types.Message):
        user_id = message.from_user.id
        game = self.roulette_games.get(user_id)

        if not game:
            await message.answer("Игра не врубиться!")
            return

        del self.roulette_games[user_id]
        await message.answer("Игра стопе — очки не получаешь.")
