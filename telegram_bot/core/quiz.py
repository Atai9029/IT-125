class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "Столица Германии?",
                "options": ["Берлин", "Париж", "Рим", "Мадрид"],
                "correct": "Берлин",
                "image": "images/berlin.jpg"
            },
            {
                "question": "6 + 2 = ?",
                "options": ["3", "8", "5", "22"],
                "correct": "8",
                "image": "images/math.png"
            },
            {
                "question": "Самый большой океан?",
                "options": ["Атлантический", "Индийский", "Тихий", "Северный Ледовитый"],
                "correct": "Тихий",
                "image": "images/ocean.jpg"
            },
            {
                "question": "Как назвате лучшее аниме на фото?",
                "options": ["Ван Пис", "Блич", "Джо Джо", "Хантер х Хантер"],
                "correct": "Блич",
                "image": "images/blich.jpg"
            },
            {
                "question": "Кто такой человек на фото?",
                "options": ["Эйнштейн", "Трамп", "Илон Маск", "Эпштейн"],
                "correct": "Эйнштейн",
                "image": "images/Anshtein.jpg"
            },
            {
                "question": "Кто создал игру minecraft?",
                "options": ["Воледеморд", "Зевс", "Не знаю", "Пушкин"],
                "correct": "Не знаю",
                "image": "images/dontnow.jpg"
            },
            {
                "question": "Как называется эта игра?",
                "options": ["Майнкрафт", "Капетели Онлайн", "Хайтейл", "Террария"],
                "correct": "Майнкрафт",
                "image": "images/maincraft.jpg"
            },
            {
                "question": "Кто этот рэпер?",
                "options": ["Пидиди", "Кани Уэст", "Эминем", "Джамал"],
                "correct": "Эминем",
                "image": "images/aminem.jpg"
            },
            {
                "question": "Как его зовут?",
                "options": ["Кон чен ый", "Ким чен ёж", "Чон гук", "Ким чен ын"],
                "correct": "Ким чен ын",
                "image": "images/kim_chen_in.png"
            },
            {
                "question": "Кто этот персонаж?",
                "options": ["Фрундель", "Спанж боб", "Скебоб", "Птица из энгибёрдс"],
                "correct": "Спанж боб",
                "image": "images/spanjbob.jpg"
            },
            {
                "question": "Кто эта легенда?",
                "options": ["Лысый избразерс", "Лев Худой", "Сквидвард", "Майк Тайсон"],
                "correct": "Майк Тайсон",
                "image": "images/tayson.jpg"
            },
            {
                "question": "Кем был Адольф Гилтер?",
                "options": ["Спасителем мира", "Художником", "Тираном", "Трансгендором"],
                "correct": "Спасителем мира",
                "image": "images/spas.jpg"
            },
            {
                "question": "Как зовут этого любителя по младше?",
                "options": ["Пидиди", "Альпако", "Кай", "Питер"],
                "correct": "Пидиди",
                "image": "images/pdiddy.jpg"
            },
            {
                "question": "Как звать этого бодибилдера?",
                "options": ["Блум", "Какойто амбал", "Мухамед Абдул", "Морген Штерн"],
                "correct": "Какойто амбал",
                "image": "images/ambal.jpg"
            },
            {
                "question": "Что это за аниме?",
                "options": ["Насруто", "Маг целитель", "Демоны старшей школы", "Межвидовые рецензенты"],
                "correct": "Межвидовые рецензенты",
                "image": "images/recendent.jpg"
            }
        ]

    def get_question(self, index):
        if index < len(self.questions):
            return self.questions[index]
        return None

    def total_questions(self):
        return len(self.questions)
