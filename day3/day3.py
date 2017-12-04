#!/usr/bin/env python
# -*- coding: utf-8 -*-

target = 347991

def puzzle1():
    i = 0

    x = [1, 1, 1, 1]
    delta = [1, 3, 5, 7]

    while True:
        for a in range(len(x)):
            x[a] += 8 * i + delta[a]

            if x[a] - i <= target and x[a] + i +1 >= target:
                return i + 1 + abs(x[a] - target)

        i += 1


def puzzle2():
    size = 1
    grid = [[1]]
    row = 0
    column = 1
    direction = 'r' #initially we wrap to the right

    def get_idx(idx):
        return idx + (size / 2)

    def sum_neighbors(r, c):
        s = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                xidx = get_idx(r + x)
                yidx = get_idx(c + y)
                if (xidx >= 0 and xidx < size) and (yidx >= 0 and yidx < size):
                    s += grid[xidx][yidx]
        return s

    def grow_grid():
        new_grid = [[0] * (size + 2)]
        for r in grid:
            new_grid.append([0] + r + [0])

        new_grid.append([0] * (size + 2))
        return new_grid
    
    while True:
        if abs(row) > size / 2 or abs(column) > size / 2:
            grid = grow_grid()
            size += 2

        s = sum_neighbors(row, column)
        grid[get_idx(row)][get_idx(column)] = s

        if s > target: return s

        if direction == 'r':
            if grid[get_idx(row - 1)][get_idx(column)] == 0: 
                direction = 'u'
                row -= 1
            else:
                column += 1
        elif direction == 'u':
            if grid[get_idx(row)][get_idx(column - 1)] == 0: 
                direction = 'l'
                column -= 1
            else:
                row -= 1

        elif direction == 'l':
            if grid[get_idx(row + 1)][get_idx(column)] == 0: 
                direction = 'd'
                row += 1
            else:
                column -= 1

        elif direction == 'd':
            if grid[get_idx(row)][get_idx(column + 1)] == 0: 
                direction = 'r'
                column += 1
            else:
                row += 1

        else: # panic
            return 0




if __name__ == "__main__":
    print("1: {}".format(puzzle1()))
    print("2: {}".format(puzzle2()))
