import copy


def get_generation(cells, generations):
    lenx = len(cells)
    leny = len(cells[0])
    for i in range(generations):
        cadr=copy.deepcopy(cells)
        # print("epocha =", i + 1)
        for x in range(lenx):
            for y in range(leny):
                cadr[x][y]=onecell(cells, x, y)
                # print(cadr[x][y])
        cells=copy.deepcopy(cadr)
    return cells


def onecell(cells, x, y):
    live = 0
    for ox in range(x - 1, x + 2):
        for oy in range(y - 1, y + 2):
            if ox < 0 or ox > len(cells) - 1:
                continue
            if oy < 0 or oy > len(cells[0]) - 1:
                continue
            if oy == y and ox == x:
                continue
            if cells[ox][oy]:
                live+=1
                # print(True)
            # print(x, 'x = ', ox, '  ', y, 'y = ', oy)
    # print('cells[{0}][{1}] ='.format(x,y),live)
    # print()
    if cells[x][y] and (live<2 or live>3):
        return 0
    elif cells[x][y] and (live==2 or live==3):
        return 1
    elif cells[x][y]==False and live==3:
        return 1
    else:
        return 0


start = [[1, 0, 0],  # [0,0][0,1][0,2]       [q-1,w-1][q-1,w][q,w+1]
         [0, 1, 1],  # [1,0][1,1][1,2]       [q,w-1]  [q,w]  [q,w+1]
         [1, 1, 0]]  # [2,0][2,1][2,2]       [q+1,w-1][q+1,w][q+1,w+1]
end = [[0, 1, 0],
       [0, 0, 1],
       [1, 1, 1]]

print(get_generation(start, 1))
