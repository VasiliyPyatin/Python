# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т
# .е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

lucky_ticket = int(input('Введите номер билета: '))

first_lucky_ticket = lucky_ticket // 1000
sum_first_lucky_ticket = first_lucky_ticket % 10 
first_lucky_ticket = first_lucky_ticket // 10
sum_first_lucky_ticket = sum_first_lucky_ticket + (first_lucky_ticket % 10)
first_lucky_ticket = first_lucky_ticket // 10
sum_first_lucky_ticket = sum_first_lucky_ticket + (first_lucky_ticket % 10)

second_lucky_ticket = lucky_ticket % 1000
sum_second_lucky_ticket = second_lucky_ticket % 10 
second_lucky_ticket = second_lucky_ticket // 10
sum_second_lucky_ticket = sum_second_lucky_ticket + (second_lucky_ticket % 10)
second_lucky_ticket = second_lucky_ticket // 10
sum_second_lucky_ticket = sum_second_lucky_ticket + (second_lucky_ticket % 10)

if (sum_first_lucky_ticket == sum_second_lucky_ticket) and 99999 < lucky_ticket < 1000000:
    print ('yes')
else:
    print ('no')