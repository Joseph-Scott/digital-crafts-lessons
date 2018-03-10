listOne = [[2, -2], 
          [5, 3]]
listTwo = [[2, 3], 
          [3, 4]]

result = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]


for i in range(len(listOne)):
    for j in range(len(listOne[0])):
        result[i][j] = listOne[i][j] + listTwo[i][j]

for r in result:
    print(r)