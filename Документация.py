#-----------------------------------------------------------Строки------------------------------------------------------------------------------------
#mutable являются изменяемыми, списки (list), словари (dict) и множества (set).

#immutable Неизменяемыми являются целые и действительные числа (int, float), строки (str), последовательности байтов (бинарные данные, bytes), а также кортежи, все элементы которых неизменяемы (tuple).

#-----------------------------------------------------------Функции------------------------------------------------------------------------------------

def greet(massage, name):# Создали функцию с названием greet она же в свою очередь хронит в себе параметры функции (massage , name).
    result = f'{massage}, {name}'# Создали переменную result которая присваевает себе f - формат меняеет все типы данных в srg, {} - в фигурные скобочки приеносятся параметры нашей созданной функции.
    print(result)# Выводит на экран переменную result на экран.
greet('Hello', 'World')# Закрываем функции greet и передаём в нее аргументы которые будут передаваться в параметры функции непосредственно это massage и name порядок аргументов имеет значение !

print(dir(int)) # Выводит на экран именна переменных доступных в локальной облости, в нашем случаи для функции int.
print(type(1)) # Выводит на экран типы данных в нашем случаи 1 это int.
print (set('hello'))# Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
