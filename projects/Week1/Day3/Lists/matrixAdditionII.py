listOne = [[2, -2, 4, 4], 
          [5, 3, 2, 1]]
listTwo = [[2, 3, 2, 4], 
          [3, 4, 2, 1]]

# add to the size of the result matrix to correspond to your matrices above
result = [[0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0]]


for i in range(len(listOne)):
    for j in range(len(listOne[0])):
        result[i][j] = listOne[i][j] + listTwo[i][j]

for r in result:
    print(r)