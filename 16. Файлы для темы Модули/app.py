#Импорт из модулей
import my_module
my_module.foo()
print(my_module.div(10,5))

#Импорт из пакетов
import my_package.module_2 as m2
m2.foo_2

from my_package.subpackage import foo_3
foo_3()
