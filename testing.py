import matplotlib.pyplot as plt

def rotate_right(direction):
    new_direction = []
    if direction[0] == 1:
        new_direction = [0,-1]
    elif direction[1] == 1:
        new_direction = [1,0]
    elif direction[0] == -1:
        new_direction = [0,1]
    elif direction[1] == -1:
        new_direction = [-1,0]
    return new_direction

def rotate_left(direction):
    new_direction = rotate_right(direction)
    new_direction = rotate_right(direction)
    new_direction = rotate_right(direction)
    return new_direction

def move_direction(position,direction,n):
    new_position = [position[0] + direction[0] * n,position[1] + direction[1] * n]
    return new_position

def generate_real_spiral(size):
    current_position = [size[0]/2,size[1]/2]
    points = [current_position]
    n = 1
    direction = [0,1]
    while len(points) < size[0]*size[1]:
        for i in range(n):
            current_position = move_direction(current_position,direction,1)
            points.append(current_position)
        direction = rotate_right(direction)
        for i in range(n):
            current_position = move_direction(current_position,direction,1)
            points.append(current_position)
        direction = rotate_right(direction)
        n += 1
    for i in range(n-1):
        current_position = move_direction(current_position,direction,1)
        points.append(current_position)
    return points
