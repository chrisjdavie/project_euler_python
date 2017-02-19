from collections import defaultdict

def memoi_twod(orig_func):
    def replace(array, i, j):
        
        if not hasattr(replace, "memoi_array") or replace.base_array is not array:
            replace.memoi_array = defaultdict(lambda: defaultdict(lambda: None))
            replace.base_array = array
        
        if replace.memoi_array[i][j] is None:
            replace.memoi_array[i][j] = orig_func(triangle, i, j)

        return replace.memoi_array[i][j]

    return replace


@memoi_twod
def max_sum_paths(triangle, i, j):
    max_sum = triangle[i][j]
    if i < len(triangle) - 1:
        max_sum += max([max_sum_paths(triangle, i+1, j),
                 	max_sum_paths(triangle, i+1, j+1)])
    return max_sum


T = int(input())

for _ in range(T):
    N = int(input())
    triangle = []
    for _ in range(N):
        nums_str = input()
        triangle.append(list(map(int, nums_str.split())))
    print(max_sum_paths(triangle, 0, 0))


