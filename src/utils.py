"""
@author - Sivaramakrishnan
"""
import matplotlib.pyplot as plt
import numpy as np
import json

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

def break_string_of_k(k,break_point = 80):
    string_k = str(k)
    return_string = ""
    len_string,i = len(string_k),0
    print("k:",string_k)
    while(i < len_string//break_point):
        return_string += string_k[i*break_point:(i+1)*break_point]+"\n"
        i += 1
    return_string += string_k[i*break_point:]
    return return_string

def char_to_bitmap(inp_string,JSON_FILE = "char_bitmap_5x5.json"):
    string = inp_string.lower()
    new_grid = np.zeros((17,106),dtype = np.int32)
    index = 1
    with open(JSON_FILE) as json_file:
        char_to_bitmap_dict = json.load(json_file)
    for each_letter in string:
        temp = np.array(char_to_bitmap_dict[each_letter],dtype = np.int32)
        height,width = temp.shape
        reshaped_temp = np.zeros((17,width+1))
        reshaped_temp[(17//2 - height//2):((17//2 - height//2)+height),0:-1] = temp
        new_grid[:,index:index+width+1] = reshaped_temp
        index += (width + 1)
    return new_grid

def plot_grid(result_grid,k,save = False):
    plt.imshow(result_grid,cmap="binary")
    plt.xlabel("k = "+break_string_of_k(k),fontsize = 8)
    plt.yticks([])
    if save:
        plt.savefig("grid.png",bbox_inches = "tight",dpi = 300)