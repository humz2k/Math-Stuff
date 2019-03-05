import matplotlib.pyplot as plt

def generate_real_spiral(size):
    points = []
    x = size[0]/2
    y = size[1]/2
    points.append([x,y])
    n = 1
    while len(points) < size[0]*size[1]:
        for i in range(n):
            y += 1
            points.append([x,y])
        for i in range(n):
            x += 1
            points.append([x,y])
        n += 1
        for i in range(n):
            y -= 1
            points.append([x,y])
        for i in range(n):
            x -= 1
            points.append([x,y])
        n += 1
    for i in range(n-1):
        y += 1
        points.append([x,y])
    return points

points = (generate_real_spiral([10,10]))
print(len(points))

x = []
y = []

for point in points:
    x.append(point[0])
    y.append(point[1])

plt.scatter(x,y,s=5)
plt.show()
