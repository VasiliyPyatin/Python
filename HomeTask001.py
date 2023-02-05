# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))
lengh_number = str(number)
if len(lengh_number) == 3: # либо if 99 < number < 1000
    x1 = number % 10
    number = number // 10
    x2 = number % 10
    number = number // 10
    x3 = number % 10
    number = number // 10
    print (f'{x3} + {x2} + {x1} = {x1+x2+x3}')
else:
    print ('Введено неверное число')