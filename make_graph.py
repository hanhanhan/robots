def main(board_size=16):

    other_robots = [] 
    board = {}

    #Board configuration specific barrier locations
    #indices refer to lines between tiles

    #barrier locations taken from page 3 of DriftingDroids user documentation
    #I'd like to permute barriers/check and check if solvable within certain # of moves
    #to create other board set ups

    horizontal_barriers = [
        (1, 4),
        (3, 1), (3, 11),
        (4, 0), (4, 6), (4, 15),
        (6, 2), 
        (7, 7),  (7, 8), (7, 10), (7, 13),
        (8, 5), 
        (9, 7), (9, 8), (9,12),
        (10, 1), (10, 15),
        (11, 4), (11, 10),
        (12, 0),
        (13, 5),
        (14, 9), (14, 14),
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

    #Horizontal barriers
    # for i in range(board_size + 1): #row
    #     for j in range(board_size): #column
    #         #from board design
    #         if (i, j) in horizontal_barriers:
    #             horizontal_barriers[(i, j)] = 1
            # #from edges of board
            # else if (i == 0 || i == board_size + 1):
            #     horizontal_barriers[(i, j)] = 1
            # #no barrier on other tiles
            # else:
            #     horizontal_barriers[(i, j)] = 0

    #Veritical barriers
    # for i in range(board_size): #row
    #     for j in range(board_size + 1): #column
    #         if (i, j) in vertical_barriers:
    #             vertical_barriers[(i, j)] = 1
            # else if (j == 0 || j == board_size + 1):
            #     vertical_barriers[(i,j)] = 1
            # else:
            #     vertical_barriers[(i,j)] = 0


    for i in range(board_size): # columns
        for j in range(board_size): # rows
            board[(i, j)] = {
            'occupied': 0,
            'barriers': {'top': 0, 'right': 0, 'bottom': 0, 'left': 0, 'diagonal': 0 }
            }

            # add barriers at all edges of game board
            if (i == 0):
                board[(i, j)]['barriers']['top'] = 1
            if (i == board_size - 1):
                board[(i, j)]['barriers']['bottom'] = 1
            if (j == 0):
                board[(i, j)]['barriers']['left'] = 1
            if (j == board_size - 1):
                board[(i, j)]['barriers']['right'] = 1

            # add barriers at board setup specific locations
            if (i, j) in vertical_barriers:
                board[(i, j)]['barriers']['left'] = 1
                board[(i, j - 1)]['barriers']['right'] = 1

            if (i, j) in horizontal_barriers:
                board[(i, j)]['barriers']['bottom'] = 1 
                board[(i - 1, j)]['barriers']['top'] = 1


    
    print(board[(5,0)])

if __name__ == '__main__':
    main()