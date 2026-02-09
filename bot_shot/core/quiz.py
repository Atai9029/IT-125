class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "Столица Франции?",
                "options": ["Берлин", "Париж", "Рим", "Мадрид"],
                "correct": "Париж",
                "image": "images/france.jpg"
            },
            {
                "question": "2 + 2 = ?",
                "options": ["3", "4", "5", "22"],
                "correct": "4",
                "image": "images/math.jpg"
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
                "correct": "Ван Пис",
                "image": "images/one_piece.jpg"
            },
            {
                "question": "Кто такой человек на фото?",
                "options": ["Эйнштейн", "Трамп", "Илон Маск", "Эпштейн"],
                "correct": "Эпштейн",
                "image": "images/Apshtein.jpg"
            },
            {
                "question": "Кто создал игру FNAF?",
                "options": ["Воледеморд", "Зевс", "Скотт Коутон", "Пушкин"],
                "correct": "Скотт Коутон",
                "image": "images/fnaf.jpg"
            },
            {
                "question": "Как называется эта игра?",
                "options": ["Майнкрафт", "Капетели Онлайн", "Хайтейл", "Террария"],
                "correct": "Майнкрафт",
                "image": "images/maincraft.jpg"
            },
            {
                "question": "Кто этот рэпер?",
                "options": ["Пидиди", "Кани Уэст", "Барак Обама", "Джамал"],
                "correct": "Кани Уэст",
                "image": "images/kanye_east.jpg"
            },
            {
                "question": "Как его зовут?",
                "options": ["Кон чен ый", "Ким чен ёж", "Чон гук", "Ким чен ын"],
                "correct": "Ким чен ын",
                "image": "images/kim_chen_in.jpg"
            },
            {
                "question": "Кто этот персонаж?",
                "options": ["Фрундель", "Мистер мисикс", "Скебоб", "Птица из энгибёрдс"],
                "correct": "Скебоб",
                "image": "images/skebob.jpeg"
            },
            {
                "question": "Кто эта легенда?",
                "options": ["Лысый избразерс", "Лев Худой", "Сквидвард", "Билли Херингтон"],
                "correct": "Билли Херингтон",
                "image": "images/billi.jpg"
            },
            {
                "question": "Кем был Адольф Гилтер?",
                "options": ["Спасителем мира", "Художником", "Тираном", "Трансгендором"],
                "correct": "Художником",
                "image": "images/gitler.jpg"
            },
            {
                "question": "Как зовут этого любителя по младше?",
                "options": ["Пидиди", "Альпако", "Кай", "Питер"],
                "correct": "Пидиди",
                "image": "images/pdiddy.jpg"
            },
            {
                "question": "Как звать этого бодибилдера?",
                "options": ["Блум", "Ронни Колеман", "Мухамед Абдул", "Морген Штерн"],
                "correct": "Ронни Колеман",
                "image": "images/rony_kolman.jpg"
            },
            {
                "question": "Что это за аниме?",
                "options": ["Насруто", "Маг целитель", "Демоны старшей школы", "Межвидовые рецензенты"],
                "correct": "Маг целитель",
                "image": "images/mag.jpg"
            }
        ]

    def get_question(self, index):
        if index < len(self.questions):
            return self.questions[index]
        return None

    def total_questions(self):
        return len(self.questions)
