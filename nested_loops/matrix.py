#Nested loops to iterate over a two-dimensional list
matrix = [[1,2,4],[3,1,2],[2,3,1]]
for row in matrix:
    for element in row:
        print( f'{element}' ,end=" ")
    print()