#TODO if
#TODO for while
#Пример использования оператора if
#x = int(input("Введи число: "))

#if x > 0:
    #print("Больше нуля!")
#elif x < 0:
    #print("Меньше нуля!")
#else:
    #print("Равно нулю!")        


# Задача 1
# Приведем список покупок в магазине
#   а. Вставьте рыбу между горошком и рисом

shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']
shop_list.insert(shop_list.index("Рис"), "Рыба")
print(shop_list)
 
#   b. Добавьте фрукты из списка fruits в конец списка shop_list
 
fruits = ['Яблоко', 'Апельсин', 'Клубника']
shop_list.extend(fruits)
print(shop_list)
 
#   c. Удалите из списка shop_list картофель

print(shop_list.pop(0))
print(shop_list, len(shop_list))
# второй метод исключения - shop_list.remove("Картофель")

#   d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате
#   Номер "продукта" в списке - N

print(f"Номер хлеба в списке - {shop_list.index('Хлеб')}")

#Оператор while
room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
min_price = min(room_prices)

i = 0
while i < len(room_prices):
    price = room_prices[i]
    if price == min_price:
       print(f"Найдена минимальная цена - {price}")
       break
    i += 1   

    #Задача 3
    # Дано 2 числа
    #описать логику деления числа a на число b, не используя операции деления
    
def div(a, b):
    i = a
    count_div = 0

    while i > 0:
        i -= b
        count_div += 1
    return count_div

print(div(10, 5))




