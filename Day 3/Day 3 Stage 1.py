def main():
    with open("input.txt", "r") as f:
        lines = [i.strip().__add__(".") for i in f]  # get all lines and add a "." at the end, so I don't have to deal with nothing at the end of the lines


    total_sum = 0  # total sum for the answer
    maxRow = len(lines)  # max rows to know the bounds of the matrix
    maxColumn = len(lines[0])  # max columns to know the bounds of the matrix
    numbers_coords = []  # initialise an array of coordinates for each whole number
    for row in range(maxRow):
        debounce = False  # debounce so I know when the start of a number is found
        sub_number = []  # initialise an array for each sub_number coordinate
        for column in range(maxColumn):
            if lines[row][column].isnumeric():  # check if the current character in the column is a number
                sub_number.append([row, column])  # append the numbers coordinates onto the sub_number array
                debounce = True  # set debounce to true because a number has been found
            if not lines[row][column].isnumeric() and debounce is True:  # check if the current character is not a number and if a number has already been found
                numbers_coords.append(sub_number)  # append the sub_number coordinates onto the number_coords list
                sub_number = []  # empty the sub_number array for next loop
                debounce = False  # reset the debounce because the current found number has been dealt with

    for num in numbers_coords:  # loop through each whole number in number_coords
        for char in num:  # loop through each sub number coordinates in array
            if isAdjacent(char[0], char[1], lines, maxRow, maxColumn):  # check if one of the sub numbers has a valid symbol adjacent
                total_sum += coords_to_number(num, lines)  # convert whole number coordinates to its correct character and add to total sum
                break  # break loop to carry on with next whole number

    return total_sum  # return total sum of all numbers with valid symbol adjacent

def isSymbol(char: str):
    symbols = "*&#%$-=+/@"  # string of valid symbols
    if symbols.__contains__(char):  # check if character is in valid symbols list
        return True
    else:
        return False

def isAdjacent(row, column, lines, maxRow, maxColumn):
    # initialise a matrix with offsets for each direction needed to check
    matrix = [[-1, -1],  # Top Left
              [-1, 0],  # Top
              [-1, 1],  # Top Right
              [0, -1],  # Middle Left
              [0, 1],  # Middle Right
              [1, -1],  # Bottom Left
              [1, 0],  # Bottom
              [1, 1]]  # Bottom Right

    for m in matrix:  # loop through each offset
        newRow = row + m[0]  # get correct row including offset
        newColumn = column + m[1]  # get correct column including offset

        if 0 <= newRow < maxRow and 0 <= newColumn < maxColumn and isSymbol(lines[newRow][newColumn]):  # checks if the row/column is above 0 and below the max row/column and if the char in that current offset position is a valid symbol
            return True
    return False

def coords_to_number(coords: [], lines):
    number = ""  # initialise an empty string
    for i in coords:  # loops through list of coordinates
        number += lines[i[0]][i[1]]  # creates a new string by adding old string to characters with the coordinates
    return int(number)  # casts string to integer

if __name__ == "__main__":
    print(main())