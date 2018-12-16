#!/user/bin/env python3

"""tile.py:Module for finding all the ways to pave a wall(m*n)
with tiles(a*b) and visualizing it

__author__ = "Weixin"
__pkuid__  = "1800011764"
__email__  = "1800011764@pku.edu.cn"
"""

import turtle

def can_pave(m, n, a, b, x, y, wall):
    """check the wall whether can be paved
    return True if it can or return False
    """
    if x+a <= m and y+b <= n:
        for i in range(y, y+b):
            for j in range(x, x+a):
                if wall[i*m+j] == 1:
                    return False
        return True
    else:
        return False


def pave(m, a, b, x, y, wall, ans):
    """pave a tlie on the wall if it can be paved from (x, y)
    0 represents unpaved
    1 represents paved
    """
    newpave = []
    for i in range(y, y+b):
        for j in range(x, x+a):
            wall[i*m+j] = 1
            newpave.append(i*m+j)
    ans.append(tuple(newpave))


def tile(m, n, a, b, wall, allans=[], ans=[], x=0, y=0):
    """return all the ways to pave a wall(m*n) with tiles(a*b)
    """
    if a == b:
        if can_pave(m, n, a, b, x, y, wall):
            pave(m, a, b, x, y, wall, ans)
            if 0 in wall:
                p = wall.index(0)
                tile(m, n, a, b, wall, allans, ans, p % m, p//m)
            else:
                allans.append(ans)
    else:
        if can_pave(m, n, a, b, x, y, wall) and can_pave(m, n, b, a, x, y, wall):
            ans2 = ans[:]
            wall2 = wall[:]

            pave(m, a, b, x, y, wall, ans)
            if 0 in wall:
                s = wall.index(0)
                tile(m, n, a, b, wall, allans, ans, s % m, s//m)
            else:
                allans.append(ans)

            pave(m, b, a, x, y, wall2, ans2)
            if 0 in wall2:
                s = wall2.index(0)
                tile(m, n, a, b, wall2, allans, ans2, s % m, s//m)
            else:
                allans.append(ans2)

        elif can_pave(m, n, a, b, x, y, wall):
            pave(m, a, b, x, y, wall, ans)
            if 0 in wall:
                s = wall.index(0)
                tile(m, n, a, b, wall, allans, ans, s % m, s//m)
            else:
                allans.append(ans)

        elif can_pave(m, n, b, a, x, y, wall):
            pave(m, b, a, x, y, wall, ans)
            if 0 in wall:
                s = wall.index(0)
                tile(m, n, a, b, wall, allans, ans, s % m, s//m)
            else:
                allans.append(ans)
    return allans


def visulize(m, n, ans):
    """visulize one of the answers using the turtle moudle
    """
    wu = turtle.Screen()
    tile = turtle.Turtle()
    tile.hideturtle()
    tile.pensize(5)
    tile.speed(0)
    grid = turtle.Turtle()
    grid.hideturtle()
    grid.color('blue')
    grid.speed(0)
    lth = (100000/m/n)**0.5
    for i in ans:
        p = i[0]
        q = i[-1]
        x1 = (p % m - m/2)*lth
        y1 = (p//m - n/2)*lth
        x2 = (q % m + 1 - m/2)*lth
        y2 = (q//m + 1 - n/2)*lth
        tile.penup()
        tile.goto(x1, y1)
        tile.pendown()
        tile.goto(x2, y1)
        tile.goto(x2, y2)
        tile.goto(x1, y2)
        tile.goto(x1, y1)
    for i in range(1, m):
        grid.penup()
        grid.goto((i-m/2)*lth, -n/2*lth)
        grid.pendown()
        grid.goto((i-m/2)*lth, n/2*lth)
    for j in range(1, n):
        grid.penup()
        grid.goto(-m/2*lth, (j-n/2)*lth)
        grid.pendown()
        grid.goto(m/2*lth, (j-n/2)*lth)
    for i in range(n):
        for j in range(m):
            grid.penup()
            grid.goto((j+0.55-m/2)*lth, (i+0.35-n/2)*lth)
            grid.pendown()
            grid.write(i*m+j, align='center', font=('Arial', int(lth//5), 'normal'))
    turtle.done()


def main():
    """work the moudle
    """
    m = int(input('请输入墙面长度:'))
    n = int(input('请输入墙面宽度:'))
    a = int(input('请输入瓷砖长度:'))
    b = int(input('请输入瓷砖宽度:'))
    wall = [0]*(m*n)
    allans = tile(m, n, a, b, wall)
    total = len(allans)
    if total == 0:
        print('无法铺满')
    else:
        print('总方案数:', total)
        for i in allans:
            print(i)
        num = turtle.numinput('Select plan', 'input number of 0 — '+str(total-1), 0)
        ans = allans[int(num)]
        visulize(m, n, ans)


if __name__ == '__main__':
    main()
