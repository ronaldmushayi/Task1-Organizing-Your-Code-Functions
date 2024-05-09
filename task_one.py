import matplotlib.pyplot as plt

def plot_data(file_object):
    file = None
    if choice == 1:
        file = open(x_y_coordinates.txt)
    else:
        print("File choice invalid")
        return file


    x_coords = []
    y_coords = []

    for line in file_object:
        x, y = map(float, line.split())
        x_coords.append(x)
        y_coords.append(y)

    plt.scatter(x_coords, y_coords)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Scatter Plot of Coordinates')
    plt.show()


