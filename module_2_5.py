def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0 or value <= 0:
        return matrix
    else:
        for i in range(n):
            stolbec = []
            matrix.append(stolbec)
            for j in range(m):
                stolbec.append(value)
    return matrix


Result_1 = get_matrix(2, 2, 88)
print(Result_1)


Result_2 = get_matrix(3, 5, 0.5)
print(Result_2)

Result_3 = get_matrix(2, 5, 0)
print(Result_3)
