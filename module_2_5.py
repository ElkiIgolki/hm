def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        mat = []
        for j in range(m):
            mat.append(value)
        matrix.append(mat)
    return matrix


a = get_matrix(3, 2, 4)
a1 = get_matrix(4, 2, 12)
print(a)
print(a1)
