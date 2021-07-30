import csv
#------------------------------------------------------------------#
# provided function - do NOT remove or change
def load_puzzle(filename):
    ''' Reads a sudoku puzzle from the text file filename. 
        Returns a list of lists of integers.  
    '''
    puzzle = [] 
    f = open(filename, "r")
    for line in f:
        puzzle.append( [int(val) for val in line.split(",")] )
    f.close()
    return puzzle




#------------------------------------------------------------------#
#------------------------------------------------------------------#


# your functions go here!

def check_rows(puzzle):
    invalid_rows = []
    for row_index in range(9):
        row = []
        for j in range(9):
            cell_value = puzzle[row_index][j]
            if cell_value == 0:
                continue
            row.append(cell_value)
        for i in range(9):
            if row.count(i) > 1:
                invalid_rows.append(row_index)
                break
    return invalid_rows

def check_columns(puzzle):
    invalid_columns = []
    for column_index in range(9):
        column = []
        for j in range(9):
            cell_value = puzzle[j][column_index]
            if cell_value == 0:
                continue
            column.append(cell_value)
        for i in range(9):
            if column.count(i) > 1:
                invalid_columns.append(column_index)
                break
    return invalid_columns

def check_subgrids(puzzle):
    invalid_subgrids = []
    anchor_points = [[0,0],[3,0],[6,0],[0,3],[3,3],[6,3],[0,6],[3,6],[6,6]]
    for subgrid_index in range(9):
        subgrid = []
        for i in range(3):
            for j in range(3):
                cell_value = puzzle[anchor_points[subgrid_index][1]+i][anchor_points[subgrid_index][0]+j]
                if cell_value == 0:
                    continue
                subgrid.append(cell_value)
        for i in range(9):
            if subgrid.count(i) > 1:
                invalid_subgrids.append(subgrid_index)
                break
    return invalid_subgrids

def puzzle_to_string(puzzle):
    puzzle_string = ""
    for row in range(9):
        if row in [3,6]:
            puzzle_string += "------+-------+------\n"
        for col in range(9):
            if col in [3,6]:
                puzzle_string += "| "
            cell_number = puzzle[row][col]
            if cell_number == 0:
                puzzle_string += "  "
            else:
                puzzle_string += str(cell_number) + " "
        puzzle_string += "\n"
    return puzzle_string



#------------------------------------------------------------------#
#------------------------------------------------------------------#



#------------------------------------------------------------------#
# Your "program" is driven by the main method
# Modify as needed
def main():

    puzzle_filename = input("Please enter your sudoku puzzle file: ")
    puzzle = load_puzzle(puzzle_filename)
    print(puzzle_to_string(puzzle))

    complete_puzzle_valid = True
    print("Checking puzzle")
    # check for rows valid
    invalid_rows = check_rows(puzzle)
    if invalid_rows == []:
        print("...Rows OK")
    else:
        print ("...Rows {} failed".format(invalid_rows))
        complete_puzzle_valid = False
    # check for columns valid
    invalid_cols = check_columns(puzzle)
    if invalid_cols == []:
        print("...Columns OK")
    else:
        print ("...Columns {} failed".format(invalid_cols))
        complete_puzzle_valid = False
    # check for subgrids valid
    invalid_subgrids = check_subgrids(puzzle)
    if invalid_subgrids == []:
        print("...Subgrids OK")
    else:
        print ("...Subgrids {} failed".format(invalid_subgrids))
        complete_puzzle_valid = False
    # print final result
    if complete_puzzle_valid:
        print ("Complete Puzzle solution is correct!")
    else:
        print ("Complete Puzzle solution is NOT correct.")







#------------------------------------------------------------------#
# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()