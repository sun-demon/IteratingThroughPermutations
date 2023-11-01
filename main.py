from contextlib import redirect_stdout

from tasks import matrix_manager, iterating_through_permutations, graph_drawing, ploting


def cyclic_way_distance(matrix, no_cyclic_way):
    return sum([matrix[no_cyclic_way[i]][no_cyclic_way[(i + 1) % len(matrix)]] for i in range(len(no_cyclic_way))])


if __name__ == '__main__':
    # 2 вариант
    variant = 2
    print(f'Вариант {variant}')
    print()

    # Задание 1
    matrix_A = matrix_manager.read_matrix(variant)
    n = len(matrix_A)
    print('Матрица:')
    matrix_manager.print_matrix(matrix_A)
    print()

    # Задание 2
    # не библиотечная функция для перебора перестановок
    # iterating_through_permutations.next_permutation

    # Задание 3
    way = list(range(n))
    min_way = way.copy()
    min_distance = sum([matrix_A[i][(i + 1) % n] for i in range(n)])
    while iterating_through_permutations.next_permutation(way):
        if (distance := cyclic_way_distance(matrix_A, way)) < min_distance:
            min_distance = distance
            min_way = way.copy()
    print(f'Минимальный путь: ', min_way, f' с длиной: {min_distance}')
    print()

    # Задание 4
    graph_drawing.draw_with_cyclic_way(min_way)
    print()

    # Задание 5
    ploting.plot_distances_and_count_cyclic_ways(matrix_A)
    print('График построен')

    # Вариативное задание
    permutations_file_name = 'permutations.txt'
    with open(permutations_file_name, 'w') as f:
        print(f'Все перестановки сохраняются в файле: {permutations_file_name}')
        with redirect_stdout(f):
            permutation = list(range(n))
            permutations = [permutation.copy()]
            while iterating_through_permutations.next_permutation(permutation):
                permutations.append(permutation.copy())
            print(permutations)
