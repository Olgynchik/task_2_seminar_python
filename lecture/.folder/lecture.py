#ввести два числа и определить какое больше
#= int(input("Введите второе число: "))
# type - показывает тип данных  
#c = a / b 
# print (type(a), type(b), type(c))
# print (-5//3)
# print (int("5"))
# print (round(5.50,2)) #округление 
# a = int(input('введите первое число целое = '))
# b = int(input('введите второе число целое = '))
# r = 5.999
# print(-5//3) 
# print(int(5.999))
# print(round(5.50,3))
# if a > b: a == b a <= 
# h= 17
# print(['да', 'NO'][h%3!=0])
# Задача No1. Решение в группах
# За день машина проезжает n километров. 
#Сколько дней нужно, чтобы проехать маршрут 
#длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 Output: 2

# m = 700
# n = 750
# print (-(-m//n))
# print ((m+n-1)//n)
# print (m//n+(m%n !=0))
# P = int(n // 6)
# S = P
# K = 2 * (P + S)
# print(P, K, S)


# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N)
# 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

# number = int(input ("введите число "))
# i = 1
# factorial = 1
# while i <= number: 
#     factorial = factorial *i
#     i = i +1
#     print(factorial)



# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6
a = int(input('Введите число: '))
f0 = 0
f1 = 1
f = 0
i = 1
while f < a:
    f = f0 + f1
    f0 = f1
    f1 = f
    i +=1
    print(f)
if f == a:
    print('номер числа ', i)
else:
    print('-1')
#  перепресваивание
a = 5
b = 10
#  первый способ
a, b = b, a
# второй способ надо добавить переменные в которы времено будут храниться значения 
c = a
a = b
b = c






