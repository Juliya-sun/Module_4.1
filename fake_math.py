def divide(first, second):
    if second == 0:
        return ('Ошибка')
    else:
        return first/second

print(divide(69, 3))
print(divide(3, 0))



# В fake_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать строку 'Ошибка'.
#
#