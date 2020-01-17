# Задача FizzBuzz :
#
#
# 1. Если заданное число кратно 3 то должно выводиться Fizz
# 2. Если заданное число кратно 5 то должно выводиться Buzz
# 3. Если заданное число кратно и 3 и 5 то должно выводиться FizzBuzz
# 4. Если чило не кратоно не 3 и не кратно 5 то должно вывести на экран число

def fizz_buzz(i): # Создали функцию под названием fizz_buzz , которая хранит в себе какое-то число (i)
    if not (i % 3) and not (i % 5): # Тут сказано : если число не кротно 3 и 5 то выводит на экран FizzBuzz
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:              # 4. Если чило не кратоно не 3 и не кратно 5 то должно вывести на экран число
        print(i)

# Вводим чсисла
fizz_buzz(1)
fizz_buzz(2)
fizz_buzz(3)
fizz_buzz(4)
fizz_buzz(5)
fizz_buzz(6)
fizz_buzz(7)
fizz_buzz(8)
fizz_buzz(9)
fizz_buzz(10)
fizz_buzz(13)
fizz_buzz(15)
fizz_buzz(17)
#-----------------------------------------------------------Неправильный вариант------------------------------------------------------------------------------

def fizz_buzz(i):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif if not (i % 3) and not (i % 5): # Эта строка не будет выполнена !!!
        print('FizzBuzz')
    else:
        print(i)

fizz_buzz(1)
fizz_buzz(2)
fizz_buzz(3)
fizz_buzz(4)
fizz_buzz(5)
fizz_buzz(6)
fizz_buzz(7)
fizz_buzz(8)
fizz_buzz(9)
fizz_buzz(10)
fizz_buzz(13)
fizz_buzz(15)
fizz_buzz(17)
