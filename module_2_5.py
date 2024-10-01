def get_matrix(n, m, value):
    matrix = []
    if n < 1 or m < 1 or value < 1:
        return matrix
    else:
        for i in range(n):
            column = []
            matrix.append(column)
            for j in range(m):
                column.append(value)
    return matrix


result1 = get_matrix(2, 2, 7)
print(result1)

result2 = get_matrix(3, 5, 8)
print(result2)

result3 = get_matrix(2, 5, 0)
print(result3)
