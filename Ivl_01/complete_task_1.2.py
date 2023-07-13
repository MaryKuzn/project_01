# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
# 1 способ решения пункта А
print(f"Три песни звучат {my_favorite_songs[2][1] + my_favorite_songs[5][1] + my_favorite_songs[8][1]} минут")

## 1 способ решения задачи 1.2 пункт С c использованием модуля random
import random
print(f"Три песни звучат {my_favorite_songs[random.randint(0,len(my_favorite_songs)-1)][1] + my_favorite_songs[random.randint(0,len(my_favorite_songs)-1)][1] + my_favorite_songs[random.randint(0,len(my_favorite_songs)-1)][1]} минут")

## 2 способ решения задачи 1.2 пункт С c использованием модуля random
import random
sum_songs = 0
for i in random.choices(my_favorite_songs, k=3):
    sum_songs += i[1]
print(f"Сумма трех случайных треков {sum_songs} минут")
   
# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# 1 способ решения пункта В
print(f"Три песни звучат {my_favorite_songs_dict['Easy'] + my_favorite_songs_dict['In This World'] + my_favorite_songs_dict['Waste a Moment']} минут")

## 1 способ решения пункта В, C c использованием модуля random
import random
print(f"Три песни звучат {random.choice(list(my_favorite_songs_dict.values())) + random.choice(list(my_favorite_songs_dict.values())) + random.choice(list(my_favorite_songs_dict.values()))} минут")

## 2 способ решения пункта В, C c использованием модуля random
import random
sum_songs1 = 0
for i in random.sample(list(my_favorite_songs_dict), 3):
    sum_songs1 += my_favorite_songs_dict[i]
print(f"Сумма трех случайных треков {sum_songs1} минут")

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

