def is_valid_walk(walk):
    if len(walk) % 2 == 1 or len(walk)!=10:
        return False
    else:
        x = []
        y = []
        for i in walk:
            if i == 'n':
                x.append(1)
            elif i == 's':
                x.append(-1)
            elif i == 'w':
                y.append(1)
            elif i == 'e':
                y.append(-1)
        if sum(x) == 0 and sum(y) == 0:
            return True
        else:
            return False

def isValidWalk(walk):
    if len(walk) != 10:
        return False

    x = 0
    y = 0

    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
        else:
            return False

    return x == 0 and y == 0


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(isValidWalk(['n','s','n','s','n','s','n','s','n','s']))