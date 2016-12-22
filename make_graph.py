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
    (9, 7), (9, 8), (9,12),
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

def main(board_size=16, horizontal_barriers=horizontal_barriers, vertical_barriers=vertical_barriers):
    """ Return a dictionary of game board tiles and associated information for 
    each tile, including a
    .
    Make adjacency list showing edges (lines of travel for game pieces) 
    between game board tiles
    """
    board = {}

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

if __name__ == '__main__':
    main()