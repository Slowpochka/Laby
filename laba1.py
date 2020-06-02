import matplotlib.pyplot as plt
import random

N = 10  # число абонентов
M = 200  # размер буфера
p = 0
probability_l = []
t_avg = []

while p <= 1 / N:
    # очередь сначала равна 0
    queue = [0]
    probability_l.append(p)
    k = 0
    while k <= M:
        msg_sum = 0
        n = 0
        while n <= N:
            msg_sum += random.choices([1, 0], [p, 1 - p])[0]
            n += 1
        last = queue[-1] + msg_sum
        if queue[-1] > 0:
            last = last - 1
        queue.append(last)
        k += 1
    queue_sum = sum(queue)
    if p == 0:
        t_avg.append(0)
    else:
        t_avg.append(queue_sum / p)
    p += 0.01

plt.ylabel("Среднее время")
plt.xlabel("Вероятность P")
plt.plot(probability_l, t_avg)
plt.show()
