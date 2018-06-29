"""
@author - Sivaramakrishnan
"""
import matplotlib.pyplot as plt
import numpy as np

def find_k(grid):
    grid_flattened = grid.flatten("F").tolist()
    binary_string = "0b" + "".join(list(map(lambda x:str(x),grid_flattened)))
    k = int(binary_string,2)*17
    return k

def formula_result(x,y):
    result = ((((y // 17)) // (2 ** ((17 * (x // 1)) + (((y // 1)) % 17)))) % 2) // 1
    return result < (1 / 2)

def create_graph_with_k(k):
    dummy_grid = np.zeros((17,106))
    for i in range(dummy_grid.shape[0]):
        for j in range(dummy_grid.shape[1]):
            dummy_grid[i][j] = int(not formula_result(j,k+i))
    return np.flip(np.flip(dummy_grid,axis = 1),axis = 0)

def plot_grid(result_grid):
    plt.imshow(result_grid,cmap="binary")
    plt.show()