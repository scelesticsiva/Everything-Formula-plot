"""
@author - Sivaramakrishnan
"""
import numpy as np
from src import utils
import argparse

def save_graph_and_k(inp_string,save_fig = False):
    grid = utils.char_to_bitmap(inp_string)
    k = utils.find_k(grid)
    utils.plot_grid(grid,k,save_fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--string",type = str,\
                        help = "String to which k value has to be found")
    parser.add_argument("--save",type = bool,\
                        help = "Whether to save the figure")
    args = parser.parse_args()
    save_graph_and_k(args.string,args.save)