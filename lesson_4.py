from math import sqrt

# 1. Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.

a = 200
b = 800

print(f'Cреднее: (a + b) / 2 = {(200 + 800) / 2}')
print(f'Дисперсия: (b - a)** 2 / 12 = {((800 - 200)**2) / 12}')

# 2. О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.

a = 0.5

# (( b-0.5) ** 2) / 12 = 0.2
# (( b-0.5) ** 2) = 0.2 * 12 = 2.4
# b - 0.5 = sqrt(2.4) = 1.549
# b = 1.549 + 0.5 =  2.049

b = sqrt(0.2 * 12) + 0.5
print(f'Правая граница величины = {b} ')
print(f'Среднее значение величины (a + b) /2 = {(a + b) / 2 }')

# 3. Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)

# исходя из формулы описывающей плотность вероятности нормально распределённой случайной величины следует, что:
print(f'Среднее = -2')
print(f'Дисперсия = 16')
print(f'СКО = 4')

#4.  Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:

# а). больше 182 см
#  182 это среднее + 1 сигма. по правилу 3 сигм в пределах +-1 сигмы лежит примерно 68% наблюдений. нужна площать правее 1 сигмы: от общай площади отнимаем половину и площать 1 сигмы
print(f'больше 182 см: {round((1 - 0.5 - 0.68/2) * 100, 2)} %')

# б). больше 190 см
#  190 это среднее + 2 сигмы. по правилу 3 сигм в пределах +-2 сигм лежит примерно 95,4% наблюдений. ужна площать правее 2 сигм: от общай площади отнимаем половину и площать 2 сигм
print(f'больше 190 см: {round((1 - 0.5 - 0.954/2) * 100, 3)} %')

# в). от 166 см до 190 см
# необходимо найти площать от - 1 сигмы до 0  и от 0 до  2 сигм
print(f'от 166 см до 190 см: {round((0.68/2 + 0.954/2) * 100, 3)} %')

# г). от 166 см до 182 см
# необходимо найти площать от - 1 сигмы до 1 сигмы. по правилу 3 сигм в пределах +-1 сигмы лежит примерно 68% наблюдений
print(f'от 166 см до 182 см: 68 %')

# д). от 158 см до 190 см
# необходимо найти площать от - 2 сигмы до 2 сигмы. по правилу 3 сигм в пределах +-2 сигмы лежит примерно 95,4% наблюдений
print(f'от 158 см до 190 см: 95,4 %')

# е). не выше 150 см или не ниже 190 см
# необходимо найти площать менее - 3 сигмы и более 2 сигм. по правилу 3 сигм в пределах +-3 сигмы лежит примерно 99,72% наблюдений
print(f'не выше 150 см или не ниже 190 см: {round(((1 - 0.9972)/2 + (1 - 0.954)/2) * 100, 3)} %')

# ё). не выше 150 см или не ниже 198 см
# 150 это -3 сигмы, а 198 это =3 сигмы. по правилу 3 сигм в пределах +-3 сигмы лежит примерно 99,72% наблюдений. нам нужен остаток
print(f'не выше 150 см или не ниже 198 см: {round((1 - 0.9972) * 100, 3)} %')

# ж). ниже 166 см.
# 166 это - 1 сигма. надо найти площадь менее -1 сигмы. тоже что и пупкт а
print(f'ниже 166 см: {round((1 - 0.5 - 0.68/2) * 100, 2)} %')

#5. На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

# Z = (X(i) - M(X)) / сигма(корень из дисперсии)
print(f'на {round((190 - 178) / sqrt(25), 3)} сигм')