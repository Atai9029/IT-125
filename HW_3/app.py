import flet as ft
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ui import UI


class ProfileApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Анкеты"
        self.page.window.width = 550
        self.page.window.height = 900
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.bgcolor = ft.Colors.BLUE_50
        self.page.padding = 20

        self.ui = UI()
        self.ui.page_ref = self.page

        self.ui.button.on_click = self.create_profile
        self.ui.age.on_change = self.update_age

        self.page.add(*self.ui.build())

    def update_age(self, e):
        self.ui.age_text.value = f"Возраст: {int(self.ui.age.value)}"
        self.page.update()

    def validate_form(self):
        is_valid = True

        # проверка имени
        if not self.ui.name.value or self.ui.name.value.strip() == "":
            self.ui.name_error.value = "Пожалуйста, введите имя"
            self.ui.name.border_color = ft.Colors.RED_400
            is_valid = False
        else:
            self.ui.name_error.value = ""
            self.ui.name.border_color = ft.Colors.GREEN_400

        # проверка города
        if not self.ui.city.value:
            self.ui.city_error.value = "Выберите город"
            is_valid = False
        else:
            self.ui.city_error.value = ""

        # проверка навыков
        skills_ok = (
            self.ui.skill1.value or
            self.ui.skill2.value or
            self.ui.skill3.value
        )
        if not skills_ok:
            self.ui.skills_error.value = "Выберите хотя бы один навык"
            is_valid = False
        else:
            self.ui.skills_error.value = ""

        # проверка уровня
        if not self.ui.level.value:
            self.ui.level_error.value = "Выберите уровень"
            is_valid = False
        else:
            self.ui.level_error.value = ""

        # проверка email
        email = self.ui.notify_email.value
        if not email or email.strip() == "":
            self.ui.email_error.value = "Введите email для уведомления"
            self.ui.notify_email.border_color = ft.Colors.RED_400
            is_valid = False
        elif "@" not in email or "." not in email:
            self.ui.email_error.value = "Неверный формат email (пример: name@mail.com)"
            self.ui.notify_email.border_color = ft.Colors.RED_400
            is_valid = False
        else:
            self.ui.email_error.value = ""
            self.ui.notify_email.border_color = ft.Colors.GREEN_400

        self.page.update()
        return is_valid

    def send_email_notification(self, profile_text, to_email):
        # замените на свой gmail и пароль приложения
        sender_email = "your_email@gmail.com"
        sender_password = "your_app_password"

        # пока не настроено - выводим в консоль
        if sender_email == "your_email@gmail.com":
            print("=" * 40)
            print("УВЕДОМЛЕНИЕ (почта не настроена, вывод в консоль):")
            print(f"Кому: {to_email}")
            print("Тема: Новая анкета создана!")
            print(profile_text)
            print("=" * 40)
            return True

        try:
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = to_email
            msg["Subject"] = "Новая анкета создана!"
            body = f"Была создана новая анкета:\n\n{profile_text}"
            msg.attach(MIMEText(body, "plain", "utf-8"))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()
            return True

        except Exception as error:
            print(f"Ошибка отправки: {error}")
            return False

    def create_profile(self, e):
        if not self.validate_form():
            return

        skills = []
        if self.ui.skill1.value:
            skills.append("Python")
        if self.ui.skill2.value:
            skills.append("Django")
        if self.ui.skill3.value:
            skills.append("Flet")

        photo_info = self.ui.photo_path if self.ui.photo_path else "Не загружено"

        profile_text = (
            f"Имя: {self.ui.name.value}\n"
            f"Город: {self.ui.city.value}\n"
            f"Возраст: {int(self.ui.age.value)}\n"
            f"Навыки: {', '.join(skills)}\n"
            f"Уровень: {self.ui.level.value}\n"
            f"Готов к работе: {'Да' if self.ui.active.value else 'Нет'}\n"
            f"Фото: {photo_info}"
        )

        self.ui.result.value = "Анкета создана!\n\n" + profile_text
        self.ui.result.color = ft.Colors.GREEN_800

        email_sent = self.send_email_notification(
            profile_text,
            self.ui.notify_email.value,
        )

        if email_sent:
            snack_text = f"Уведомление отправлено на {self.ui.notify_email.value}"
            snack_color = ft.Colors.GREEN_100
        else:
            snack_text = "Анкета создана, но письмо не отправлено"
            snack_color = ft.Colors.ORANGE_100

        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(value=snack_text),
            bgcolor=snack_color,
        )
        self.page.snack_bar.open = True
        self.page.update()
