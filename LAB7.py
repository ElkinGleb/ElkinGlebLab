import csv
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from time import perf_counter


def task1():
    list1 = [randint(-1000, 1000) for _ in range(10 ** 6)]
    list2 = [randint(-1000, 1000) for _ in range(10 ** 6)]
    np_mass1 = np.array(list1)
    np_mass2 = np.array(list2)

    t_start1 = perf_counter()
    for i in range(10 ** 6):
        list1[i] *= list2[i]
    t_all1 = perf_counter() - t_start1

    t_start2 = perf_counter()
    np.multiply(np_mass1, np_mass2)
    t_all2 = perf_counter() - t_start2

    print(f'Время перемножения стандартных списков - {t_all1}')
    print(f'Время перемножения numpy массивов - {t_all2}')
    print(f'Разница во времени - {t_all1 - t_all2}')


def task2():
    with open('data2.csv', 'r') as table:
        table = list(csv.reader(table, delimiter=','))
        column = np.array([])
        table.pop(0)
        for row in table:
            column = np.append(column, float(row[0]))
        fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(14, 6))
        ax0.set_title('Гистограмма')
        ax0.set_xlabel('Интервалы')
        ax0.set_ylabel(
            'Количество значений, которые попали в заданные интервалы')
        ax0.hist(column, 20)
        ax0.grid()

        ax1.set_title('Нормализованная гистограмма')
        ax1.hist(column, 20, density=True)
        ax1.set_xlabel('Интервалы')
        ax1.set_ylabel('Вероятность')
        ax1.grid()

    plt.show()

    print(f'Cреднеквадратичное отклонение - {np.std(column)}')


def task3():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y = np.sin(x) * np.cos(x)
    z = np.sin(x) * np.cos(x)

    ax.plot(x, y, z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
