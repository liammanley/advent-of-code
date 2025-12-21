# https://adventofcode.com/2025/day/9
#corner 1 and corner 2 are tuples in the form of (row, col)
def rectangle_area(corner1, corner2):
    height = abs(corner1[0] - corner2[0]) + 1
    base = abs(corner1[1] - corner2[1]) + 1
    return base*height

def find_largest_rectangle_area(coordinates):
    largest_area = 0
    for corner1 in coordinates:
        for corner2 in coordinates:
            area = rectangle_area(corner1, corner2)
            if area > largest_area:
                largest_area = area
    return largest_area

if __name__=="__main__":
    with open("input.txt", "r") as file:
        coordinates = []
        for line in file:
            #get coordinate from line
            coordinate = tuple(map(int, line.strip().split(",")))
            coordinates.append(coordinate)
        largest_rectangle_area = find_largest_rectangle_area(coordinates)
        print(largest_rectangle_area)
