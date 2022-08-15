from math import factorial
from math import exp

def combination (n , k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# 1.Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз.
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз

n = 100    # число испытания
k = 85     # число наступлений события
p = 0.8    # вероятноять наступления события
q = 1 - p  # обратная вероятность

probability = combination(n, k) * p**k * q**(n-k)
print(f'Вероятность того, что стрелок попадет в цель ровно 85 раз: {round(probability * 100, 3)} %')
print()

# 2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?

n = 5000
p = 0.0004
lambda1 = n * p

m = 0
probability0 = ((lambda1**m) / factorial(m)) * exp(-lambda1)
print(f'Вероятность того, что ни одна из лампочек не перегорит в первый день: {round(probability0 * 100, 3)} %')

m = 2
probability2 = ((lambda1**m) / factorial(m)) * exp(-lambda1)
print(f'Вероятность того, что перегорят ровно две лампочки: {round(probability2 * 100, 3)} %')
print()

# 3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
n = 144    # число испытания
k = 70     # число наступлений события
p = 0.5    # вероятноять наступления события
q = 1 - p  # обратная вероятность

probability = combination(n, k) * p**k * q**(n-k)
print(f'Вероятность того, что орел выпадет ровно 70 раз: {round(probability * 100, 3)} %')
print()

# 4. В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?

# вероятность того, что все мячи белые: надо из первого ящика вытащить оба белых мяча и из второго ящика тоже оба белых мяча
# для первого ящика
combination_white2_box1 = combination(7, 2)   # вариантов вытянуть 2 белых мяча из 7 возможных
combination_all_box1 = combination(10, 2)    # всего вариантов вытянуть 2 мяча из 10

probability_white2_box1 = combination_white2_box1 / combination_all_box1
print(f'Вероятность вытащить из первого ящика оба белых мяча: {round(probability_white2_box1 * 100, 3)} %')

# для второрго ящика
combination_white2_box2 = combination(9, 2)   # вариантов вытянуть 2 белых мяча из 9 возможных
combination_all_box2 = combination(11, 2)    # всего вариантов вытянуть 2 мяча из 11

probability_white2_box2 = combination_white2_box2 / combination_all_box2
print(f'Вероятность вытащить из второго ящика оба белых мяча: {round(probability_white2_box2 * 100, 3)} %')

print(f'Общая вероятность вытащить все белые мячи: {round(probability_white2_box1 * probability_white2_box2 * 100, 3)} %')

#вероятность того, что ровно два мяча белые:
# подойдут ситуации когда:

# из первого ящика взяли 2 белых мяча и из второго 0
# вероятность первого ящика нам уже известна по расчётам ранее
print(f'Вероятность вытащить из первого ящика оба белых мяча: {round(probability_white2_box1 * 100, 3)} %')
# 0 белых из второго ящика, т.е оба чёрные
combination_white0_box2 = combination(2, 2)                                  # вариантов вытянуть 2 чёрных мяча из 2 возможных
probability_white0_box2 = combination_white0_box2 / combination_all_box2
print(f'Вероятность вытащить из второго ящика ни одного белого мяча: {round(probability_white0_box2 * 100, 3)} %')
# или
# из первого ящика 1 белый и из второго ящика 1 белый
# для первого ящика
combination_white1_box1 = combination(7, 1)   # вариантов вытянуть 1 белый мяч из 7 возможных
combination_black1_box1 = combination(3, 1)   # вариантов вытянуть 1 чёрный мяч из 3 возможных
# для второрго ящика
combination_white1_box2 = combination(9, 1)   # вариантов вытянуть 1 белый мяч из 9 возможных
combination_black1_box2 = combination(2, 1)   # вариантов вытянуть 1 чёрный мяч из 2 возможных

probability_white1_box1 = (combination_white1_box1  * combination_black1_box1)/ combination_all_box1
print(f'Вероятность вытащить из первого ящика 1 белый мяч: {round(probability_white1_box1 * 100, 3)} %')

probability_white1_box2 = (combination_white1_box2 * combination_black1_box2) / combination_all_box2
print(f'Вероятность вытащить из второго ящика 1 белый мяч: {round(probability_white1_box2 * 100, 3)} %')
# или
# из первого ящика взяли 0 белых мячей (2 чёрных) и из второго 2
combination_white0_box1 = combination(3, 2)                                  # вариантов вытянуть 2 чёрных мяча из 3 возможных
probability_white0_box1 = combination_white0_box1 / combination_all_box1
print(f'Вероятность вытащить из первого ящика ни одного белого мяча: {round(probability_white0_box1 * 100, 3)} %')
# вероятность вытащить из второго ящика 2 белых мяча нам уже известна по расчётам ранее
print(f'Вероятность вытащить из второго ящика оба белых мяча: {round(probability_white2_box2 * 100, 3)} %')

print(f'Вероятность того, что ровно два мяча белые: { round((probability_white2_box1 * probability_white0_box2 + probability_white1_box1 * probability_white1_box2  + probability_white0_box1 * probability_white2_box2) * 100, 3)} %')

# вероятность того, что хотя бы один мяч белый
#                                                                1 в первом           и 0 во втором            или    1 в первом           и     1 во втором       или       1 в первом       и  2 во втором            или       2 в первом      и      0 во втором       или        2 в первом      и 1 во втором            или     2 в первом       и       2 во втором         или     0 в первом       и   1 во втором           или     0 в первом         и        2 во втором
print(f'Вероятность того, что хотя бы один мяч белый: {round((probability_white1_box1 * probability_white0_box2 + probability_white1_box1 * probability_white1_box2 + probability_white1_box1 * probability_white2_box2 + probability_white2_box1 * probability_white0_box2 + probability_white2_box1 * probability_white1_box2 + probability_white2_box1 * probability_white2_box2 + probability_white0_box1 * probability_white1_box2 + probability_white0_box1 * probability_white2_box2) * 100, 3)} %')