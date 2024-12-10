#Pascal'sTriangle
#input is the number of lines

#importing library
import argparse

#creating the nested list function
def get_triangle(rows: int):

    triangle = [[1]]

    for num in range (1, rows):
            prev_row = triangle[-1]
            next_row = [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1]
            triangle.append(next_row)
    return triangle

#passing the value
#pascal_triangle = get_triangle(5)
#for row in pascal_triangle:
#    print(row)

####
#### this part was not clear here as we have not reviewed such things at all through the course
####


def parsing_triangle(rows):
    parser = argparse.ArgumentParser(description="Generate Pascal's Triangle")
    parser.add_argument( rows, type=int, help="The number of rows of Pascal's Triangle")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get the number of rows from the command line arguments
    rows = args.rows
    

    pascal_triangle = get_triangle(rows)

    # Get the width for formatting (based on the last row's number of digits)
    max_width = len(" ".join(map(str, pascal_triangle[-1])))  # Get width based on last row
        
    # Print the resulting Pascal's Triangle
    for row in pascal_triangle:
        row_str = " ".join(map(str, row))  # Convert each number to a string
        print(row_str.center(max_width))  # Center-align each row within the max width



parsing_triangle()


