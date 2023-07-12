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
#1 способ решения
print(f"Три песни звучат {my_favorite_songs[2][1] + my_favorite_songs[5][1] + my_favorite_songs[8][1]} минут")

#2 способ решения
import random
print(f"Три песни звучат {my_favorite_songs[random.randint(0,len(my_favorite_songs)-1)][1] + my_favorite_songs[random.randint(0,len(my_favorite_songs)-1)][1] + my_favorite_songs[random.randint(0,len(my_favorite_songs)-1)][1]} минут")

#3 способ решения random.choices(my_favorite_songs, k=3)
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

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

