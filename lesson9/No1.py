# 1. Payment — абстрактный класс          сделано......................
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Кредитная карта: оплата {amount}")

    def refund(self, amount):
        print(f"Кредитная карта: возврат {amount}")

class CryptoPayment(Payment):
    def pay(self, amount):
        commission = amount * 0.02  # 2% комисий нормуль
        total = amount + commission
        print(f"Криптовалюта: оплата {total} ")

    def refund(self, amount):
        print(f"Криптовалюта: возврат {amount} (комиссия не возвращается)")

         #проверка
        print(" ОПЛАТЫ ")
payments = [CreditCardPayment(), CryptoPayment(), CreditCardPayment()]
for p in payments:
    p.pay(1)
print()



# 2. Course — абстрактный класс
class Course(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def get_materials(self):
        pass

    @abstractmethod
    def end(self):
        pass

class PythonCourse(Course):
    def start(self):
        print("Курс Python начался")

    def get_materials(self):
        return ["Теория по Python", "Видеоуроки", "Задания по коду "]

    def end(self):
        print("Курс Python завершён")

class MathCourse(Course):
    def start(self):
        print("Курс математики начался")

    def end(self):
        print("Курс математики завершён")

#проверка
print(" КУРСЫ ")
course = PythonCourse()
course.start()
print("Материалы:", course.get_materials())
course.end()
print()


# 3. Delivery — абстрактный класс
class Delivery(ABC):
    @abstractmethod
    def calculate_cost(self, distance):
        pass

    @abstractmethod
    def deliver(self):
        pass

class AirDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 10

    def deliver(self):
        print("Доставка самолётом")

class GroundDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 5

    def deliver(self):
        print("Доставка грузовиком")

class SeaDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 3

    def deliver(self):
        print("Доставка кораблём")

#проверка
print(" ДОСТАВКА ")
for delivery in [AirDelivery(), GroundDelivery(), SeaDelivery()]:
    cost = delivery.calculate_cost(100)
    print(f"Стоимость: {cost}")
    delivery.deliver()
print()





# 4. BankAccount — с приватными полями
class BankAccount:
    def __init__(self, owner, balance=0, pin=1234):
        self.__owner = owner
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount, pin):
        if pin != self.__pin:
            print("Неверный PIN")
            return
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return
        self.__balance += amount
        print(f"Внесено {amount}. Баланс: {self.__balance}")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Неверный PIN")
            return
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return
        if amount > self.__balance:
            print("Недостаточно средств")
            return
        self.__balance -= amount
        print(f"Снято {amount}. Баланс: {self.__balance}")

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            print("Неверный старый PIN")
            return
        self.__pin = new_pin
        print("PIN успешно изменён")

#проверкоооооо мдэээээээээээээээээээээээээээээээээ
print(" БАНКОВСКИЙ СЧЁТ ")
account = BankAccount("Алексей", 1000, 1234)
account.deposit(500, 745)
account.withdraw(200, 1234)
account.change_pin(3245, 4532)
account.withdraw(100, 7867)  
print()


# 5. UserProfile — с приватными и защищёнными полями
class UserProfile:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        self._status = "basic"  
        self.__is_logged_in = False

    def login(self, email, password):
        if email == self.__email and password == self.__password:
            self.__is_logged_in = True
            print("Вход выполнен")
        else:
            self.__is_logged_in = False
            print("Ошибка входа!")

    def upgrade_to_premium(self):
        if not self.__is_logged_in:
            print("Сначала войдите")
            return
        self._status = "premium"
        print("Статус обновлён до premium")

    def get_info(self):
        if not self.__is_logged_in:
            print("Сначала войдите")
            return
        return f"Email: {self.__email}, Статус: {self._status}"

#ПРОВЕРКА
print(" ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ ")
user = UserProfile("tester@gmail.com", "9029")
user.login("tester@gmail.com ", "wrong")
user.login("tester@gmail.com", "9029")
user.upgrade_to_premium()
print(user.get_info())
print()


# 6. Product — с приватной скидкой
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__discount = 0

    def get_price(self):
        return self.price * (1 - self.__discount / 100)

    def set_discount(self, percent, is_admin=False):
        if not is_admin:
            print("Только админ может менять скидку")
            return
        if percent < 0 or percent > 100:
            print("Скидка от 0 до 100")
            return
        self.__discount = percent
        print(f"Скидка {percent}% установлена")

# проверяем
print(" ТОВАР ")
product = Product("Телефон", 30000)
print("Цена:", product.get_price())
product.set_discount(20, is_admin=True)
print("Цена со скидкой:", product.get_price())
print()


# 7. Файлы — полиморфизм
class TextFile:
    def open(self):
        print("Открыт текстовый файл")

class ImageFile:
    def open(self):
        print("Открыто изображение")

class AudioFile:
    def open(self):
        print("Воспроизводится аудио")

def open_all(files):
    for file in files:
        file.open()

#тестируееем
print(" ОТКРЫТИЕ ФАЙЛОВ ")
files = [TextFile(), ImageFile(), AudioFile()]
open_all(files)
print()





# 8. Транспорт — с расчётом времени
class Car:
    def move(self, distance):
        speed = 100  # км/ч speed
        fuel_per_km = 0.1
        time = distance / speed
        fuel = distance * fuel_per_km
        print(f"Машина: {time} ч, топлива: {fuel} л")

class Truck:
    def move(self, distance):
        speed = 80
        fuel_per_km = 0.3
        time = distance / speed
        fuel = distance * fuel_per_km
        print(f"Грузовик: {time:.1f} ч, топлива: {fuel} л")

class Bicycle:
    def move(self, distance):
        speed = 20
        time = distance / speed
        print(f"Велосипед: {time} ч, топлива: 0")

def simulate_transport(transport_list, distance=100):
    for t in transport_list:
        t.move(distance)

#чекаем
print(" ТРАНСПОРТ ")
transports = [Car(), Truck(), Bicycle()]
simulate_transport(transports, 100)
print()




# 9. Портал — разные уровни доступа
class Student:
    def access_portal(self):
        print("Студент: вижу расписание и задания")

class Teacher:
    def access_portal(self):
        print("Преподаватель: могу ставить оценки")

class Administrator:
    def access_portal(self):
        print("Админ: управляю пользователями и системой")

# ура последняя
print(" ПОРТАЛ ")
users = [Student(), Teacher(), Administrator()]
for user in users:
    user.access_portal()