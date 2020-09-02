import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    """

    Args:
        color:
        grid:
        beliefs:    current beliefs of robot location
        p_hit:      
        p_miss:
    
    return:
        new_beliefs:
    """
    
    new_beliefs = []
    total_probability =0
    #
    # TODO - implement this in part 2
    #
    
    for i, row in enumerate(grid):
        belief_temp = []
        for j, v in enumerate(row):
            if color == v:
                p = p_hit
            else:
                p = p_miss
            belief_temp.append(p)
            total_probability += p 
        new_beliefs.append(belief_temp)
    
    for i,row in enumerate(new_beliefs):
        for j,v in enumerate(row):
            new_beliefs[i][j] = new_beliefs[i][j] / total_probability

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    print(height)
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)