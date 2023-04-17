import numpy as np
from AiresInfoFunctions import GetZHSEffectiveRefractionIndex

def add_new_integral(pos, antena):
    return GetZHSEffectiveRefractionIndex(pos[0], pos[1], pos[2], xant=antena[0], yant=antena[1], zant=antena[2])


def Find_on_list(Pos, antena, core,discrete):
    Pos[0] = (Pos[0] - antena[0]) * discrete // (core_pos[0] - antena_pos[0])
    Pos[1] = (Pos[1] - antena[1]) * discrete // (core_pos[1] - antena_pos[1])
    Pos[2] = (Pos[2] - antena[2]) * discrete // (core_pos[2] - antena_pos[2])
    return Pos


if __name__ == "__main__":
    print("empezar")
    core_pos = [1000, 0, 15000]
    antena_pos = [0, 0, 0]
    saved = []
    discrete = 3 # How much the space is divided.


    # Fill the table.
    for i in range(discrete):
        saved.append([])
        for j in range(discrete):
            saved[i].append([])
            for k in range(discrete):
                x = antena_pos[0] + i * (core_pos[0] - antena_pos[0]) / discrete
                y = antena_pos[0] + j * (core_pos[1] - antena_pos[1]) / discrete
                z = antena_pos[0] + k * (core_pos[2] - antena_pos[2]) / discrete
                saved[i][j].append(add_new_integral([x, y, z], antena_pos))

            
print(np.array(saved))