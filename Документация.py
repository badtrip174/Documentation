# !=  - Не равно
# <=  - Меньше или равно
# >=  - Больше или равно
# not - Отрицание
# and - И
# or  - или
#-----------------------------------------------------------Строки------------------------------------------------------------------------------------
#mutable являются изменяемыми, списки (list), словари (dict) и множества (set).

#immutable Неизменяемыми являются целые и действительные числа (int, float), строки (str), последовательности байтов (бинарные данные, bytes), а также кортежи, все элементы которых неизменяемы (tuple).
#-----------------------------------------------------------Обращение к индексу-------------------------------------------------------------------------------
# Имеем некуб переменную A, в которой хрониться тип данных список [] , а в нём может хрониться всё что угодно от числа до типа данных класса bool
A = [15, 11.2, 'Hello', True, "World"]
print(A[0]) # Выводит на экран 15
print(A[1]) # Выводит на экран 11.2
print(A[2]) # Выводит на экран Hello
print(A[3]) # Выводит на экран True
print(A[4]) # Выводит на экран World
# Мы обратились к функции print что бы она вывела переменную A , а конкертно index (ИНДЕКС В PYTHON НАЧИНАЕТСЯ С 0, А НЕ С 1.)
# Можно оброщаться и к отрицательному индексу тогда данные будут браться с конца
print(A[-1]) # Выводит на экран World
print(A[-2]) # Выводит на экран True и Т.Д.
# Взятие из списка по index назвается Getter от слова get-брать
#----------------------------------------------------------Проверка длины-------------------------------------------------------------------------------------
# Для определения длины строки в Python есть функия len от слова length - длина
print(len(A[2])) # Выводит на экран длину слова Hello взятую из перемнной A
test = "Этот текс пойдёт на проверку"
print(len(test)) # выводит 28 с учётом всех пробелов !!!

#----------------------------------------------------------Модификация по индексу-----------------------------------------------------------------------------
A[0] = 'hi'
A[1] = 'Этот текст был модифицирован!'
print(A[0]) # Выводит на экран hi потому что мы модифицировали содержимое перемнной A , конкретно в index 0
print(A[1]) # А тут выводит на экран Этот текст был модифицирован! потому что мы модифицировали содержимое перемнной A , конкретно в index 1
# Данный приём в программирование называется Setter от слова set - устанавливать
#-----------------------------------------------------------Функции-------------------------------------------------------------------------------------------
def a(name):# Выдаёт все локальные переменные и аргументы функции в нащем случаи выаст {'name': 'World', 'p': 100}
    p = 100
    print(locals())
a("World")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def greet(massage, name): # Создали функцию с названием greet она же в свою очередь хронит в себе параметры функции (massage , name).
    result = f'{massage}, {name}' # Создали переменную result которая присваевает себе f - формат меняеет все типы данных в srg, {} - в фигурные скобочки приеносятся параметры нашей созданной функции.
    print(result) # Выводит на экран переменную result на экран.
greet('Hello', 'World')# Закрываем функции greet и передаём в нее аргументы которые будут передаваться в параметры функции непосредственно это massage и name порядок аргументов имеет значение !
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
print(dir(int)) # Выводит на экран именна переменных доступных в локальной облости, в нашем случаи для функции int.
print(type(1)) # Выводит на экран типы данных в нашем случаи 1 это int.
print (set('hello')) # Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
# isalpha
name = "Monica"
print(name.isalpha()) # Проверка на буквы в данном случаи вернёт True так как это в переменной name хронятся буквы
# isdigit
name = '123456';
print (name.isdigit()) # Возвращает True так как в переменной name хроняться цыфры
