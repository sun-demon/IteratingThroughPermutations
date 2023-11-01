# input_list must be only sorted list with unique values
def get_all_permutations(input_list):
    permutations = []
    indexes_permutation = [range(len(input_list))]
    isHasNextPermutation = True
    while isHasNextPermutation:
        permutations.append([input_list[i] for i in indexes_permutation])
        isHasNextPermutation = next_permutation(indexes_permutation)
    return permutations


# in_list       must be  list
# bi_predicate  must be  f(in_list: list, id: int) -> bool
# _from         must be  in range(0, len(in_list) + 1)
def rfind_with_index(in_list, bi_predicate, _to = 0, _from = -1):
    if _from < 0:
        _from += len(in_list)
    if _to < 0:
        _to += len(in_list)
    for i in range(_from, _to - 1, -1):
        if bi_predicate(in_list, i):
            return i
    return -1


# permutation  must be  list
# The function change input permutation to the next in a primary order
def next_permutation(permutation):
    i = rfind_with_index(permutation, lambda in_list, k: in_list[k - 1] < in_list[k], 1)
    if i == -1:
        return False
    for j in range(i + 1, len(permutation)):
        if permutation[j] < permutation[i - 1]:
            permutation[i:] = reversed(permutation[i:])
            permutation[i - 1], permutation[i - j] = permutation[i - j ], permutation[i - 1]
            return True
    permutation[i:] = reversed(permutation[i:])
    permutation[i - 1], permutation[i] = permutation[i], permutation[i - 1]
    return True
