# Alternative - implicit - figure out graph as you go.

def make_board_dict(board_size=16, *robots):
    """ Return a dictionary of game board tiles and associated information for 
    each tile, including paths between tiles.
    
    Make adjacency list showing edges (lines of travel for game pieces) 
    between game board tiles
    """
    board = {}

    # Board configuration specific barrier locations are defined here.
    # Indices refer to lines between tiles.
    #
    # Barrier locations are taken from page 3 of DriftingDroids user documentation.
    horizontal_barriers = [
        (1, 4),
        (3, 1), (3, 11),
        (4, 0), (4, 6), (4, 15),
        (6, 2), 
        (7, 7), (7, 8), (7, 10), (7, 13),
        (8, 5), 
        (9, 7), (9, 8), (9, 12),
        (10, 1), (10, 15),
        (11, 4), (11, 10),
        (12, 0),
        (13, 5),
        (14, 3), (14, 9), (14, 14),
        ]

    vertical_barriers = [
        (0, 4), (0, 10), 
        (1, 6), (1, 14),
        (2, 1), (2, 11),
        (4, 6),
        (6, 3), (6, 14),
        (7, 7), (7, 9), (7, 11),
        (8, 6), (8, 7), (8, 9),
        (9, 2), (9, 13),
        (10, 4), (10, 9),
        (13, 6), (13, 5),
        (14, 3), (14, 9),
        (15, 7), (15, 11)
        ]

    # make barriers wherever there are robots
    # except for edges
    # update paths along robot-position centered axes only?
    for robot in robots:
        if robot[0] is not 0:
            horizontal_barriers.push((robot[0], robot[1]))
        if robot[0] is not board_size - 1:
            horizontal_barriers.push((robot[0] + 1, robot[1]))

        if robot[1] is not 0:
            vertical_barriers.push((robot[0], robot[1]))
        if robot[1] is not board_size - 1:
            vertical_barriers.push((robot[0], robot[1] + 1))
            

    def make_paths(start, destination):
        """Add path to each tile in list of start tile's to destination where robot can travel."""
        for tile in start:
            board[tile]['destinations'].append(destination) 

    def make_graph(outer_range, inner_range, barrier_side, direction):
        """Represent game board as directed graph by adding adjacency list to each tile."""
        for outer in outer_range: 
            path = []
            for inner in inner_range: 

                # Set axis of traversal
                if direction is 'row':
                    (row, col) = (outer, inner)
                elif direction is 'col':
                    (row, col) = (inner, outer)
                
                if board[(row, col)]['barriers'][barrier_side] != 1:
                    path.append((row, col))
                elif board[(row, col)]['barriers'][barrier_side] == 1:
                    make_paths(path, (row, col))
                    path = []

    # Incorporate lists of barrier locations and edge barriers into each tile definition.   
    for row in range(board_size): 
        for col in range(board_size): 
            board[(row, col)] = {
            'occupied': 0,
            'barriers': {'top': 0, 'right': 0, 'bottom': 0, 'left': 0, 'diagonal': 0 },
            'destinations': [] 
            }

            # Add barriers at all edges of game board.
            if (col == 0):
                board[(row, col)]['barriers']['left'] = 1
            if (col == board_size - 1):
                board[(row, col)]['barriers']['right'] = 1
            if (row == 0):
                board[(row, col)]['barriers']['top'] = 1
            if (row == board_size - 1):
                board[(row, col)]['barriers']['bottom'] = 1

            # Add barriers at board setup specific locations.
            if (row, col) in vertical_barriers:
                board[(row, col)]['barriers']['left'] = 1
                board[(row, col - 1)]['barriers']['right'] = 1

            if (row, col) in horizontal_barriers:
                board[(row, col)]['barriers']['top'] = 1 
                board[(row - 1, col)]['barriers']['bottom'] = 1

            # Add barriers for any game piece.    
            #if board[(row, col)]['occupied'] == 1:

    #Direction of loop to find paths between tiles
    forward = range(board_size)
    backward = range(board_size - 1, -1, -1)

    # Traverse rows of board left to right.
    make_graph(forward, forward, 'right', 'row')
    # Traverse rows of board right to left.
    make_graph(forward, backward, 'left', 'row')
    # Traverse columns of board top to bottom.
    make_graph(forward, forward, 'bottom', 'col')
    # Traverse columns of board bottom to top.
    make_graph(forward, backward, 'top', 'col')
    
    return board 



# def find_paths(board, path=[], start=(0, 0), end=(15, 10)):

#     path.append(start)

#     if start == end:
#         return path 

#     for tile in board[start]['destinations']: 
#         if tile in path:
#             return 
#         import pdb; pdb.set_trace()  # breakpoint ccbfffb4 //
#         find_paths(board, path, tile, end)

#     print("no more loop")


def breadth_first_search(board, start, end):
    moves = { start: 0 }
    parent = { start: None }
    i = 1
    #frontier = [start]
    #frontier = board[start]['destinations']
    #for u in frontier:
#     for v in Adj[u]:
#       if v not in level:
#           level[v] = i
#           parent[v] = u
#           next.append(v)
#       frontier = next
#       i += 1
    frontier = [start]
    while frontier:
        # Reinitialize frontier at each number of movess from start tile.
        next = []
        for tile in frontier:
            if tile == end:
                print("found a path in {} moves".format(moves[tile]))
                path = [tile]
                # Reconsruct path taken from start to end.
                while parent[tile]:
                    path.append(parent[tile])
                    tile = parent[tile]
                return path

            for destination in board[tile]['destinations']: 
                if destination not in moves:
                    # How many moves to get to destination.
                    moves[destination] = i
                    # Track which parent tile the current tile was reached from.
                    parent[destination] = tile
                    next.append(destination)
            frontier = next
            i += 1
    board['moves'] = moves
    board['parent'] = parent
    print(level)
    return board


def depth_first_search(board, start, end):
    if start == end:
        return path

def depth_first_start_search(board):
    pass

def main():
    board = make_board_dict()
    breadth_first_search(board, (0,0), (0,9))


if __name__ == '__main__':
    main()