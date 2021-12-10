
def low_point(point, surrounding):
    return all(adjacent > point for adjacent in surrounding)

def low_points(input):
    # print(input)
    low_points = []
    for row in range(len(input)):
        for column in range(len(input[row])):
            surrounding = []
            if row > 0:
                surrounding.append(input[row-1][column])
            if row < len(input)-1:
                surrounding.append(input[row + 1][column])

            if column > 0:
                surrounding.append(input[row][column-1])
            if column < len(input[row])-1:
                surrounding.append(input[row][column+1])

            if low_point(input[row][column],surrounding):
                low_points.append(input[row][column])
    return low_points

def risk(input):
    lowpoints = low_points(input)
    risk = 0
    # print('Low Points:{}'.format(lowpoints))
    for low in lowpoints:
        risk += low + 1
    print('Risk:{}'.format(risk))

def main():
    with open('input_example.txt') as f:
        lines = f.readlines()
    input_example = [[int(i) for i in line.strip()] for line in lines]
    risk(input_example)

    with open('input.txt') as f:
        lines = f.readlines()
    input_example = [[int(i) for i in line.strip()] for line in lines]
    risk(input_example)

if __name__ == '__main__':
    main()
