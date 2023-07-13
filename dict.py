# Поиск самых высокооплачиваемых работников с помощью спискового включения
# нужно найти всех сотрудников, 
# зарабатывающих по крайней мере 100 000 долларов в год

employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}
top_men = []
for i in employees:
    if employees[i] >= 100000:
        top_men.append(i)
print(top_men)

print([i for i in employees if employees[i] >= 100000])