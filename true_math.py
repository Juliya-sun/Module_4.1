from math import inf
def divide(first, second):
    if second == 0:
        return inf
    else:
        return first/second

print(divide(49, 7))
print(divide(15, 0))



# В true_math создайте функцию divide, которая принимает два параметра
# first и second.
# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать бесконечность.
# Бесконечность можно импортировать из встроенной библиотеки math
# (from math import inf)