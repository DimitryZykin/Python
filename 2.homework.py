# Урок 2. Циклы (for, while)
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть
# Решение:

n = [0,1,1,1,1,0,0,0,0,0,1]
    a = 0
    b = 0
    for i in n:
        if int(i) == 1:
            a += 1
        else:
            b += 1

print(a if a < b else b)



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – 
# школьница. Петя помогает Кате по математике. Он задумывает два 
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих 
# чисел S и их произведение P. Помогите Кате отгадать задуманные 
# Петей числа.

# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.
