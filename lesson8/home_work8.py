from abc import ABC, abstractmethod
import math

class Account:
    def __init__(self, account_number, balance, pin):
        self.__account_number = account_number
        self.__balance = float(balance)
        self.__pin = str(pin)
    def deposit(self, amount, pin):
        if str(pin) != self.__pin:
            return "PIN неверный"
        if amount <= 0:
            return "Сумма должна быть положительной"
        self.__balance += amount
        return f"Пополнение успешно. Баланс: {self.__balance}"
    def withdraw(self, amount, pin):
        if str(pin) != self.__pin:
            return "PIN неверный"
        if amount <= 0:
            return "Сумма должна быть положительной"
        if amount > self.__balance:
            return "Недостаточно средств"
        self.__balance -= amount
        return f"Снятие успешно. Баланс: {self.__balance}"
    def get_balance(self, pin):
        if str(pin) != self.__pin:
            return "PIN неверный"
        return self.__balance

class Product:
    def __init__(self, price):
        self.__price = float(price)
        self.__discount_percent = 0.0
    def set_discount(self, percent):
        if percent < 0:
            return "Скидка не может быть отрицательной"
        self.__discount_percent = percent
        if self.final_price() < 0:
            self.__discount_percent = 0
            return "Скидка привела бы к отрицательной цене и была отменена"
        return f"Скидка установлена: {self.__discount_percent}%"
    def final_price(self):
        return max(0.0, self.__price * (1 - self.__discount_percent / 100))

class Course:
    def __init__(self, name, max_seats):
        self.__name = name
        self.__students = []
        self.__max_seats = int(max_seats)
    def add_student(self, name):
        if len(self.__students) >= self.__max_seats:
            return "Мест нет"
        if name in self.__students:
            return "Студент уже записан"
        self.__students.append(name)
        return "Студент добавлен"
    def remove_student(self, name):
        if name in self.__students:
            self.__students.remove(name)
            return "Студент удалён"
        return "Студент не найден"
    def get_students(self):
        return tuple(self.__students)

class SmartWatch:
    def __init__(self, battery=100):
        self.__battery = float(battery)
    def use(self, minutes):
        reduction = minutes / 10.0
        self.__battery = max(0.0, self.__battery - reduction)
        return self.__battery
    def charge(self, percent):
        if percent < 0:
            return self.__battery
        self.__battery = min(100.0, self.__battery + percent)
        return self.__battery
    def get_battery(self):
        return self.__battery

class Transport:
    def __init__(self, speed, capacity):
        self.speed = float(speed)
        self.capacity = int(capacity)
    def travel_time(self, distance):
        if self.speed <= 0:
            return float('inf')
        return distance / self.speed

class Bus(Transport):
    pass

class Train(Transport):
    pass

class Airplane(Transport):
    def travel_time(self, distance):
        base = super().travel_time(distance)
        return base * 0.8

class Order:
    def __init__(self, items):
        self.items = list(items)
    def subtotal(self):
        return sum(self.items)

class DineInOrder(Order):
    def calculate_total(self):
        sub = self.subtotal()
        tip = sub * 0.10
        return sub + tip

class TakeAwayOrder(Order):
    def calculate_total(self):
        return self.subtotal()

class DeliveryOrder(Order):
    def calculate_total(self):
        sub = self.subtotal()
        delivery_fee = sub * 0.10
        return sub + delivery_fee

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack_power = attack

class Warrior(Character):
    def attack(self):
        return f"{self.name} наносит {self.attack_power} урона мечом"

class Mage(Character):
    def attack(self):
        return f"{self.name} наносит {self.attack_power} урона магией"

class Archer(Character):
    def attack(self):
        return f"{self.name} наносит {self.attack_power} урона стрелой"

class MediaFile:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
    def play(self):
        return f"Воспроизведение: {self.name}"

class AudioFile(MediaFile):
    def play(self):
        return f"{self.name} воспроизводится как аудио, длительность {self.duration}"

class VideoFile(MediaFile):
    def play(self):
        return f"{self.name} воспроизводится с изображением, длительность {self.duration}"

class Podcast(MediaFile):
    def play(self):
        return f"{self.name} воспроизводится эпизод, длительность {self.duration}"

class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        fee = amount * 0.02
        return f"Оплата картой: {amount} списано, комиссия {fee}"

class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        return f"Оплата криптовалютой: {amount} отмечено в блокчейне"

class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        fee = 0
        if amount < 100:
            fee = 1
        return f"Банковский перевод: {amount} инициирован, комиссия {fee}"

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass

class Lion(Animal):
    def eat(self):
        return "Лев ест мясо"
    def sleep(self):
        return "Лев спит в тени"

class Elephant(Animal):
    def eat(self):
        return "Слон ест растения"
    def sleep(self):
        return "Слон спит стоя"

class Snake(Animal):
    def eat(self):
        return "Змея ест мелкую добычу"
    def sleep(self):
        return "Змея спит, свернувшись"

class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def edit(self, content):
        pass
    @abstractmethod
    def save(self):
        pass

class WordDocument(Document):
    def __init__(self):
        self.content = ""
    def open(self):
        return "Word открыт"
    def edit(self, content):
        self.content += content
        return "Word изменён"
    def save(self):
        return "Word сохранён"

class PdfDocument(Document):
    def __init__(self):
        self.content = ""
    def open(self):
        return "PDF открыт"
    def edit(self, content):
        return "PDF нельзя редактировать напрямую"
    def save(self):
        return "PDF сохранён"

class SpreadsheetDocument(Document):
    def __init__(self):
        self.content = []
    def open(self):
        return "Таблица открыта"
    def edit(self, content):
        self.content.append(content)
        return "Таблица изменена"
    def save(self):
        return "Таблица сохранена"

class Lesson(ABC):
    @abstractmethod
    def start(self):
        pass

class VideoLesson(Lesson):
    def __init__(self, title):
        self.title = title
    def start(self):
        return f"Видео урок '{self.title}' начинается"

class QuizLesson(Lesson):
    def __init__(self, title):
        self.title = title
    def start(self):
        return f"Викторина '{self.title}' запущена"

class TextLesson(Lesson):
    def __init__(self, title):
        self.title = title
    def start(self):
        return f"Текстовый урок '{self.title}' открыт"

class EmailNotification:
    def send(self, message):
        return f"Email отправлен: {message}"

class SMSNotification:
    def send(self, message):
        return f"SMS отправлено: {message}"

class PushNotification:
    def send(self, message):
        return f"Push уведомление: {message}"

class Square:
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        return self.side * 4

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c

class Manager:
    def work(self):
        return "Менеджер планирует и координирует"

class Developer:
    def work(self):
        return "Разработчик пишет код"

class Designer:
    def work(self):
        return "Дизайнер создает макеты"

class FireSpell:
    def cast(self, target):
        return f"{target}: наносит урон огнём"

class IceSpell:
    def cast(self, target):
        return f"{target}: замораживает"

class HealingSpell:
    def cast(self, target):
        return f"{target}: восстанавливает здоровье"

if __name__ == "__main__":
    a = Account("0001", 1000, "1234")
    print(a.deposit(200, "1234"))
    print(a.withdraw(50, "1234"))
    print(a.get_balance("1234"))
    p = Product(150)
    print(p.set_discount(10))
    print(p.final_price())
    c = Course("Python", 2)
    print(c.add_student("Анна"))
    print(c.add_student("Борис"))
    print(c.add_student("Виктор"))
    print(c.get_students())
    s = SmartWatch(80)
    print(s.use(30))
    print(s.charge(15))
    print(s.get_battery())
    b = Bus(60, 50)
    t = Train(120, 200)
    ap = Airplane(800, 180)
    print(b.travel_time(120))
    print(t.travel_time(240))
    print(ap.travel_time(1600))
    d1 = DineInOrder([10, 20, 30])
    t1 = TakeAwayOrder([5, 5])
    del1 = DeliveryOrder([15, 10])
    print(d1.calculate_total())
    print(t1.calculate_total())
    print(del1.calculate_total())
    w = Warrior("Иван", 100, 15)
    m = Mage("Мира", 80, 20)
    ar = Archer("Олег", 70, 12)
    print(w.attack())
    print(m.attack())
    print(ar.attack())
    af = AudioFile("Песня", "3:20")
    vf = VideoFile("Видео", "10:00")
    pod = Podcast("Подкаст", "45:00")
    print(af.play())
    print(vf.play())
    print(pod.play())
    cc = CreditCardPayment()
    cr = CryptoPayment()
    bt = BankTransfer()
    print(cc.process_payment(100))
    print(cr.process_payment(50))
    print(bt.process_payment(80))
    animals = [Lion(), Elephant(), Snake()]
    for an in animals:
        print(an.eat())
        print(an.sleep())
    wd = WordDocument()
    print(wd.open())
    print(wd.edit("текст"))
    print(wd.save())
    pd = PdfDocument()
    print(pd.open())
    print(pd.edit("x"))
    print(pd.save())
    sd = SpreadsheetDocument()
    print(sd.open())
    print(sd.edit("A1=1"))
    print(sd.save())
    lessons = [VideoLesson("Введение"), QuizLesson("Повтор"), TextLesson("Материал")]
    for les in lessons:
        print(les.start())
    notifications = [EmailNotification(), SMSNotification(), PushNotification()]
    for n in notifications:
        print(n.send("Привет!"))
    shapes = [Square(4), Circle(3), Triangle(3,4,5)]
    for sh in shapes:
        print(sh.perimeter())
    staff = [Manager(), Developer(), Designer()]
    for p in staff:
        print(p.work())
    spells = [FireSpell(), IceSpell(), HealingSpell()]
    for sp in spells:
        print(sp.cast("Враг"))
