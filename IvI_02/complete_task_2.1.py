# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


n_1 = [4,6,2,1,9,63,-134,566]
n_2 = [-52, 56, 30, 29, -54, 0, -110]
n_3 = [42, 54, 65, 87, 0]
n_4 = [5]

def minimum(n):
  min_num = n[0]
  for num in n:
    if num < min_num:
      min_num = num
  return(min_num)

def maximum(n):
  max_num = n[0]
  for num in n:
    if num > max_num:
      max_num = num
  return(max_num)

print(f"min = {minimum(n_1)}, max = {maximum(n_1)}")
print(f"min = {minimum(n_2)}, max = {maximum(n_2)}")
print(f"min = {minimum(n_3)}, max = {maximum(n_3)}")
print(f"min = {minimum(n_4)}, max = {maximum(n_4)}")


       


        