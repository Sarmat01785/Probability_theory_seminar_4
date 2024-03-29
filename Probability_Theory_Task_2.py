"""
Задача 2.
О случайной непрерывной равномерно распределенной величине B известно,
что ее дисперсия равна 0.2. Можно ли найти правую границу величины B и ее среднее значение зная,
что левая граница равна 0.5? Если да, найдите ее.
"""
import math

# Известные значения
variance = 0.2
a = 0.5

# Вычисляем правую границу
b = a + math.sqrt(variance * 12)

# Вычисляем среднее значение
mean_value = (a + b) / 2

print(f"Правая граница величины B: {b}")
print(f"Среднее значение величины B: {mean_value}")
