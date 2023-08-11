from random import *
s = []
null = lambda x, y, z, w: True if ((not x or y) and (not y or w)) or (z == (x or y)) else False # ((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y)).
act = True
while act:
    active = 0
    f = [randint(0,1) for i in range(4)]
    if f[0] == 1 and f[3] == 1 and len(s) == 0:s.append(f)
    if f[0] == 1 and len(s) == 1 and f not in s:s.append(f)
    if f[1] == 1 and f[3] == 1 and len(s) == 2 and f not in s:s.append(f)
    if len(s) == 3:
        while active != 1000:
            active += 1
            i_x = choice([i for i in range(4)])
            i_y = choice([i for i in range(4) if i != i_x])
            i_z = choice([i for i in range(4) if i != i_x and i != i_y])
            i_w = choice([i for i in range(4) if i != i_x and i != i_y and i != i_z])
            if null(s[0][i_x], s[0][i_y], s[0][i_z], s[0][i_w]) == False:
                if null(s[1][i_x], s[1][i_y], s[1][i_z], s[1][i_w]) == False:
                    if null(s[2][i_x], s[2][i_y], s[2][i_z], s[2][i_w]) == False and act == True:
                            for i in s:print(i)
                            print(f"Ответ: x = {i_x + 1}; y = {i_y + 1}; z = {i_z + 1}; w = {i_w + 1}")
                            act = False
            if active == 1000:s.clear()