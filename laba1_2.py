import matplotlib.pyplot as plt
import random

M = 200  # размер буфера
N = 20  # число абонентов
p = 0.01
probability_l = []
p_loss = []

while p <= 1 / N:
    probability_l.append(p)
    coliz = 0
    s = 0
    k = 0
    while k <= M:
        msg_sum = 0
        n = 0
        while n <= N:
            msg_sum += random.choices([1, 0], [p, 1 - p])[0]
            n += 1
        if msg_sum > 1:
            coliz += msg_sum
        s += msg_sum
        k += 1
    p_loss.append(coliz / s)
    p += 0.01

plt.ylabel('Вероятность потери пакета')
plt.xlabel('Вероятность P')
plt.plot(probability_l, p_loss)
plt.show()
