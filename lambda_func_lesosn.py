def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    return matrix

result1 = get_matrix(3, 5, 10)
print(result1)