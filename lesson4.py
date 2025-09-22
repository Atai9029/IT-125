flags = {    
    'ru': {'red blue', 'white'},
    'kg': {"red yellow", 'red'},
    'ua': {"red blue", 'red', 'blue'},
    'uk': {"yellow", "blue"},
    'kz': {'blue yellow', 'blue'},
    'ge': {'red', 'black', 'yellow'},
    'fr': {'blue', 'white', 'red'},
    'jp': {'white',"red"}
}


while True:
    color_ = input("Введите exit для выхода, или же введите цвет. Цвет:  ")
    if color_ == "exit":
        print("пока пока...")
        break
   
    found = []
    for domain, colors in flags.items():
        if color_ in colors:
            found.append(domain)

    if found:
        print(f"совпадениия:  {color_}:", ", ".join(found))
    else:
        print(f"нет стран с таким именем :( {color_}")