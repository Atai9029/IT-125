import flet as ft


class UI:
    def __init__(self):
        self.page_ref = None
        self.photo_path = ""

        self.title = ft.Text(
            value="Создание анкеты",
            size=22,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_700,
        )

        # --- фото ---
        self.photo_image = ft.Image(
            src="",
            width=100,
            height=100,
            fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(50),
            visible=False,
        )
        self.photo_placeholder = ft.Container(
            content=ft.Icon(
                name=ft.Icons.PERSON,
                size=50,
                color=ft.Colors.GREY_400,
            ),
            width=100,
            height=100,
            border_radius=ft.border_radius.all(50),
            bgcolor=ft.Colors.GREY_200,
            alignment=ft.alignment.center,
        )
        self.photo_status = ft.Text(
            value="",
            color=ft.Colors.GREEN_600,
            size=12,
        )
        self.photo_button = ft.ElevatedButton(
            text="Загрузить фото",
            icon=ft.Icons.UPLOAD_FILE,
            on_click=self.pick_photo,
        )
        self.file_picker = ft.FilePicker(on_result=self.on_photo_picked)

        # --- имя ---
        self.name = ft.TextField(
            label="Имя",
            width=300,
            hint_text="Введите ваше имя",
        )
        self.name_error = ft.Text(value="", color=ft.Colors.RED_500, size=12)

        # --- город ---
        self.city = ft.Dropdown(
            label="Город",
            width=300,
            options=[
                ft.dropdown.Option("Бишкек"),
                ft.dropdown.Option("Ош"),
                ft.dropdown.Option("Токмок"),
                ft.dropdown.Option("Джалал-Абад"),
            ],
        )
        self.city_error = ft.Text(value="", color=ft.Colors.RED_500, size=12)

        # --- возраст ---
        self.age_text = ft.Text(value="Возраст: 18", size=14)
        self.age = ft.Slider(
            min=10,
            max=60,
            divisions=50,
            value=18,
            label="{value}",
            active_color=ft.Colors.BLUE_600,
        )

        # --- навыки ---
        self.skill1 = ft.Checkbox(label="Python", fill_color=ft.Colors.BLUE_600)
        self.skill2 = ft.Checkbox(label="Django", fill_color=ft.Colors.BLUE_600)
        self.skill3 = ft.Checkbox(label="Flet", fill_color=ft.Colors.BLUE_600)
        self.skills_error = ft.Text(value="", color=ft.Colors.RED_500, size=12)

        # --- уровень ---
        self.level = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Jun", label="Junior"),
                ft.Radio(value="Mid", label="Middle"),
                ft.Radio(value="Sen", label="Senior"),
            ])
        )
        self.level_error = ft.Text(value="", color=ft.Colors.RED_500, size=12)

        # --- переключатель ---
        self.active = ft.Switch(
            label="Готов к работе",
            active_color=ft.Colors.BLUE_600,
        )

        # --- тема ---
        self.theme_label = ft.Text(
            value="Цвет оформления:",
            size=13,
            color=ft.Colors.GREY_700,
        )
        self.theme_blue = ft.ElevatedButton(
            text="Синяя",
            bgcolor=ft.Colors.BLUE_100,
            on_click=lambda e: self.change_theme("blue"),
        )
        self.theme_green = ft.ElevatedButton(
            text="Зелёная",
            bgcolor=ft.Colors.GREEN_100,
            on_click=lambda e: self.change_theme("green"),
        )
        self.theme_purple = ft.ElevatedButton(
            text="Фиолетовая",
            bgcolor=ft.Colors.PURPLE_100,
            on_click=lambda e: self.change_theme("purple"),
        )

        # --- email ---
        self.notify_email = ft.TextField(
            label="Email для уведомления",
            width=300,
            hint_text="example@mail.com",
            keyboard_type=ft.KeyboardType.EMAIL,
        )
        self.email_error = ft.Text(value="", color=ft.Colors.RED_500, size=12)

        # --- кнопка и результат ---
        self.button = ft.ElevatedButton(
            text="Создать анкету",
            icon=ft.Icons.SEND,
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
        )
        self.result = ft.Text(value="", selectable=True)

    def pick_photo(self, e):
        self.file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["png", "jpg", "jpeg"],
        )

    def on_photo_picked(self, e):
        if e.files:
            file = e.files[0]
            self.photo_path = file.path
            self.photo_image.src = file.path
            self.photo_image.visible = True
            self.photo_placeholder.visible = False
            self.photo_status.value = f"Фото загружено: {file.name}"
            if self.page_ref:
                self.page_ref.update()

    def change_theme(self, theme_name):
        if self.page_ref is None:
            return
        if theme_name == "blue":
            self.page_ref.bgcolor = ft.Colors.BLUE_50
            self.title.color = ft.Colors.BLUE_700
        elif theme_name == "green":
            self.page_ref.bgcolor = ft.Colors.GREEN_50
            self.title.color = ft.Colors.GREEN_700
        elif theme_name == "purple":
            self.page_ref.bgcolor = ft.Colors.PURPLE_50
            self.title.color = ft.Colors.PURPLE_700
        self.page_ref.update()

    def build(self):
        return [
            self.file_picker,
            self.title,
            ft.Divider(),

            ft.Text(value="Фото профиля:", size=14, weight=ft.FontWeight.W_500),
            ft.Row(
                controls=[
                    ft.Stack(controls=[self.photo_placeholder, self.photo_image]),
                    ft.Column(controls=[self.photo_button, self.photo_status]),
                ],
                spacing=15,
            ),
            ft.Divider(),

            self.theme_label,
            ft.Row(
                controls=[self.theme_blue, self.theme_green, self.theme_purple],
                spacing=10,
            ),
            ft.Divider(),

            self.name,
            self.name_error,
            self.city,
            self.city_error,
            self.age_text,
            self.age,

            ft.Text(value="Навыки:", size=14, weight=ft.FontWeight.W_500),
            self.skill1,
            self.skill2,
            self.skill3,
            self.skills_error,

            ft.Text(value="Уровень:", size=14, weight=ft.FontWeight.W_500),
            self.level,
            self.level_error,

            self.active,
            ft.Divider(),

            ft.Text(value="Уведомление на email:", size=14, weight=ft.FontWeight.W_500),
            self.notify_email,
            self.email_error,
            ft.Divider(),

            self.button,
            ft.Divider(),
            self.result,
        ]
