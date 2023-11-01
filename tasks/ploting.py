import matplotlib
import matplotlib.pyplot as plt

import numpy as np

from tasks import iterating_through_permutations
from main import cyclic_way_distance


matplotlib.use('TkAgg')


def plot_distances_and_count_cyclic_ways(matrix):
    no_cyclic_way = list(range(len(matrix)))
    data = [cyclic_way_distance(matrix, no_cyclic_way)]
    while iterating_through_permutations.next_permutation(no_cyclic_way):
        data.append(cyclic_way_distance(matrix, no_cyclic_way))

    unique_distances = np.array(sorted(set(data)))
    count_ways = np.array([data.count(distance) for distance in unique_distances])
    plt.plot(unique_distances, count_ways, '-', color='blue')
    plt.xlabel('Длина пути')
    plt.ylabel('Количество путей')
    plt.title('Зависимость количества путей и их длин')
    plt.show()
