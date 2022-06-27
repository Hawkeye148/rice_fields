from copy import deepcopy

matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
rows, columns = (len(matrix), len(matrix[0]))

for i in range(3):
    step_mat = deepcopy(matrix)
    for i in range(rows):
        for j in range(columns):
            neighbors = []
            for r, c in [(i - 1, j - 1),
                         (i - 1, j),
                         (i - 1, j + 1),
                         (i, j + 1),
                         (i + 1, j + 1),
                         (i + 1, j),
                         (i + 1, j - 1),
                         (i, j - 1)]:
                if 0 <= r <= rows - 1 and 0 <= c <= columns - 1:
                    neighbors.append((r, c))
            alive = 0
            for r, c in neighbors:
                if matrix[r][c] == 1:
                    alive += 1
            if alive <= 1 or alive >= 4:
                step_mat[i][j] = 0
            elif alive == 3:
                step_mat[i][j] = 1
    for row in step_mat:
        print(row)
    print('-'*20)
    matrix=deepcopy(step_mat)