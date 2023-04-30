def transpose(matrix):
    if matrix == None or len(matrix) == 0:
        return []
        
    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
            
    return result
    
def print_matrix(matrix):
    for row in matrix:
        print(*row)

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
result = transpose(array)
print_matrix(result)