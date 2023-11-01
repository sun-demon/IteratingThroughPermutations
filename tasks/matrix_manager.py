from functools import reduce


def read_matrix(variant):
    file_name = 'in/data.txt'
    with open(file_name) as file:
        template = f'Вариант {variant}\n'
        while ((line := file.readline()) != template) and line:
            continue
        else:
            if not line:
                raise RuntimeError(f'Строка "{template}" не найдена в файле "{file_name}"')
        matrix_rank = int(rank := file.readline())
        matrix = [list(map(int, file.readline().split())) for _ in range(matrix_rank)]
        return matrix


def print_matrix(matrix):
    len_columns = []
    for i in range(len(matrix)):
        len_columns.append(reduce(lambda x, y: max(x, y), [len(str(matrix[i][j])) for j in range(len(matrix[i]))]))
    for row in matrix:
        for j in range(len(row)):
            print(repr(row[j]).rjust(len_columns[j]), end=' ')
        print()
