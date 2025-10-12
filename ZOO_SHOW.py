class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def eat(self, food):
        return f' {self.name} кушает {food}'

    def sleep(self, hours):
        return f'{self.name} спит {hours} часов'
    
    def __str__(self):
        return f"Имя: {self.name}\n Возвраст: {self.age} лет"
    
class Mammal(Animal):
    def __init__(self, age, name, color):
        super(). __init__(age, name)
        self.color = color

    def weight(self,kg):
        return f"{self.name}животное весит{kg}кг"
    
    def __str__(self):
        return super().__str__() + f"\nЦвет шерсти:{self.color}"
    
class insect(Animal):
    def __init__(self, age, name,color):
        super().__init__(age, name)
        self.color = color

    def height(self,m):
        return f"{self.name}рост насекомого{m} M"
    
    def __str__(self):
        return super().__str__() + f"\nЦвет насекомого {self.color}"
    
class dog(Mammal):
    def __init__(self, age, name, color):
        super().__init__(age, name, color)
        self.color = color 

    def raw(self):
        return f'{self.name} гавкает:гав'
    
    def __str__(self):
        return super().__str__() + f"\nЦвет {self.color}"
    
class mouse(Mammal):
    def __init__(self, age, name,color, favorite_food):
        super().__init__(age, name,color )
        self.favorite_food = favorite_food

    def pipi(self):
        return f"{self.name} пищит:пипип"
    
    def __str__(self):
        return super().__str__() + f"\n Любимая еда: {self.favorite_food}"
    
class spider(insect):
    def __init__(self, age, name, color):
        super().__init__(age, name, color)
        self.color = color

    def cqqq(self):
        return f"{self.name} рррр:hhhh"
    
    def __str__(self):
        return super().__str__() + f"\n Цвет паука:{self.color}"
    
class Zoo_show:
    def __init__(self,animals):
        self.animals = animals
        self.show = {
            "Млекопитающие":{"cash":1000, "infa": "Мега гав"},
            "Насекомые":{"cash":2200, "infa":"жестко прыгает "}
        }
        
    def show_info(self):
        print("Информация о шоуу:")
        for show, info in self.show.items():
            print(f"\n {show}:")
            print(f"Цена билет: {info['cash']} сом")
            print(f"Описание:{info['infa']}")

    def ticket(self,shows_name):
        if shows_name in self.show:
            info = self.show [shows_name]
            print(f"\n Шоу выбрано '{shows_name}'. Цена билетика: {info['cash']} сом")
            print(f"Описание: {info['infa']}")
            print("\nЖивотные,учавствующие в шоу:")
            for animal in self.animals:
                if (shows_name == "Млекопитающие"and isinstance(animal,Mammal)):
                 print(f"- {animal.name}")
                elif shows_name == "Насекомые"and isinstance(animal,insect):
                  print(f"- {animal.name}")
        else:
            print("Нету такого,другое выбирай")
    
dog = dog(2, "дог", "белый")
mouse = mouse(3,"маус","Бежевый", "Люди")
spider = spider(1,"Спайди","Чернее-черного")

animal_list = [dog,mouse,spider]

zoo_show = Zoo_show(animal_list)
zoo_show.show_info()

while True:
    choice = input("\nВведите название шоу (Млекопитающие / Насекомые) или 'выход' чтобы выйти: ").strip().capitalize()
    
    if choice.lower() == "выход":
        print("Пока")
        break
    if choice not in zoo_show.show:
        print("Нету такого,выбери другое")
        continue
    zoo_show.ticket(choice)