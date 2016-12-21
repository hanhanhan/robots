def main(board_size=16){

    other_robots = [] #array of tuples? #dictionary with color, location?
    #pieces can be bounced off of from 4 neighboring tiles
    #barrier can affect up to 3 tile locations
    #inside corner, 2 outside sides 

    # graph connections determined by:
    # boardside wall -- same as 1 side barrier

    # tile: 
    # occupied or empty
    # occupied tile makes neighboring tiles blocked on 1 side
    # 4 sides open or blocked

    # Create dictionary of tiles, with indices a key
    board = {}
    # What if there was a separate layout of barriers instead of tiles?
    # How best to ensure barrier on one tile is drawn as barrier on neighbor tile?

    for i in range(board_size):
        for j in range(board_size):
            board[(i,j)] = {
            'occupied': 0,
            'barriers': {'top': 0, 'right': 0, 'bottom': 0, 'left': 0, 'diagonal': 0 }
            }

            if (i == 0):
                board[(i,j)]['barriers']['left'] = 1
            if (i == board_size - 1):
                board[(i,j)]['barriers']['right'] = 1
            if (j == 0):
                board[(i,j)]['barriers']['top'] = 1
            if (j == board_size - 1):
                board[(i,j)]['barriers']['bottom'] = 1

}

if __name__ == '__main__':
    main()