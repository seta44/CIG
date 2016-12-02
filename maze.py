import sys
import math
import numpy as np
from collections import deque

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]

grid = []
getMove = {}
getMove = {
    0:'LEFT',
    1:'UP',
    2:'DOWN',
    3:'RIGHT'
}

getInvMove = {
    'LEFT':'RIGHT',
    'UP':'DOWN',
    'DOWN':'UP',
    'RIGHT':'LEFT'
}

recPath = []
isReturn = False

def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph
    
def getChildren(point,grid):
    x,y = point.point
    links = [grid[d[0]][d[1]] for d in [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]]
    return [link for link in links if link.value != '#']

def explore(grid, x, y):
    #On explore si l'arrivée n'a pas été trouvé sur la map
    for i, d in enumerate([(x-1, y),(x,y-1),(x,y+1),(x+1,y)]):
        
        #print("d0 : " + str(grid[d[0]][d[1]]), file=sys.stderr)
        value = grid[d[1]][d[0]]
        print("d(x,y) : (" + str(d[0]) + "," + str(d[1])+") = "+str(value), file=sys.stderr)
        #print("Valeur case : " + str(value), file=sys.stderr)
        if "C" in value:
            #On rembrousse chemin
            print(str(getMove.get(i)), file=sys.stderr)
            print(getMove.get(i))
            for elt in recPath:
                print(getInvMove(elt), file=sys.stderr)
        elif "?" in value:
             print("No where !!", file=sys.stderr)
        elif "#" in value:
             print("Wall !!!", file=sys.stderr)
       
        elif "." in value:
            recPath.append(i)
            print("Move to : " +str(i)+ " " + str(getMove.get(i)), file=sys.stderr)
            print(getMove.get(i))
            continue
        elif "T" in value and not isReturn:
            continue
        elif "T" in value and isReturn:
            print("T !!", file=sys.stderr)
            print(getMove.get(i))
        else:
            print("D la réponse D !! ", file=sys.stderr)
            print("RIGHT")
        
            

        
    
    
# game loop
while True:
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]
    x, y = kr, kc

    kirkPoint = (x, y)
    print("Kirk (x, y) : (" + str(kc) + "," + str(kr) + ")", file=sys.stderr)
    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        grid.append(list(row.strip()))
        print("Map " + str(i) + " : " + str(row), file=sys.stderr)
        
    print("Grid " + str(grid[6][5]), file=sys.stderr)
    
    explore(grid, kc, kr)
        
    


    # To debug: print("Debug messages...", file=sys.stderr)

    # Kirk's next move (UP DOWN LEFT or RIGHT).

