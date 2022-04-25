# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните
# в переменные, затем выведите на экран.

age = None
weight = None
print(type(age))
age = int(input('Введите ваш возвраст '))
weight = int(input('Введите ваш вес '))
print(type(age))
print(type(weight))
print(isinstance(weight, int))
print(isinstance(age, int))
print(f"Your age is {age} and your weight is {weight}.")