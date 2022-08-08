def pole():
    pole = [[j*2 for i in range(8)] for j in range(8)]
    for i in range(8):
        print(pole[i])

def pole1():
    pawn_pole1 = [[2 for i in range(8)] for j in range(8)]

    for i in range(4):
        for j in range(4):
            pawn_pole1[i][j] += (i + j)**2
            pawn_pole1[-i - 1][j] += (i + j)**2
            pawn_pole1[-i - 1][-j - 1] += (i + j)**2
            pawn_pole1[i][-j - 1] += (i + j)**2
    for i in range(8):
        print(pawn_pole1[i])

def pole2():
    pawn_pole2 = [[l*4 for l in range(8)] for k in range(8)]
    for i in range(8):
        for j in range(4):
            pawn_pole2[i][j + 4] -= j*8 + 4
        print(pawn_pole2[i])


def pole3():
    pole = [[j*2 for i in range(8)] for j in range(8)]
    for i in range(8):
        print(pole[i])

"""
[0, 0, 0, 0, 0, 0, 0, 0]
[2, 2, 2, 2, 2, 2, 2, 2]        
[4, 4, 4, 4, 4, 4, 4, 4]        
[6, 6, 6, 6, 6, 6, 6, 6]        
[8, 8, 8, 8, 8, 8, 8, 8]        
[10, 10, 10, 10, 10, 10, 10, 10]
[12, 12, 12, 12, 12, 12, 12, 12]
[14, 14, 14, 14, 14, 14, 14, 14]
------
[0, 4, 8, 12, 12, 8, 4, 0]      
[0, 4, 8, 12, 12, 8, 4, 0]
[0, 4, 8, 12, 12, 8, 4, 0]
[0, 4, 8, 12, 12, 8, 4, 0]
[0, 4, 8, 12, 12, 8, 4, 0]
[0, 4, 8, 12, 12, 8, 4, 0]
[0, 4, 8, 12, 12, 8, 4, 0]
[0, 4, 8, 12, 12, 8, 4, 0]
------
[2, 3, 6, 11, 11, 6, 3, 2]
[3, 6, 11, 18, 18, 11, 6, 3]
[6, 11, 18, 27, 27, 18, 11, 6]
[11, 18, 27, 38, 38, 27, 18, 11]
[11, 18, 27, 38, 38, 27, 18, 11]
[6, 11, 18, 27, 27, 18, 11, 6]
[3, 6, 11, 18, 18, 11, 6, 3]
[2, 3, 6, 11, 11, 6, 3, 2]
"""