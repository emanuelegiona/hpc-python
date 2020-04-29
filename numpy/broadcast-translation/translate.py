import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    """
    See README.md for exercises.
    :return: None
    """

    translation = [2.1, 1.1]
    x, y = [], []
    with open("points_circle.dat", 'r') as file:
        for line in file:
            line = line.split()
            line = [*map(float, line)]
            x.append(line[0])
            y.append(line[1])

    x = np.array(x)
    y = np.array(y)
    plt.plot(x, y, 'o')

    # translation
    new_x = x + translation[0]
    new_y = y + translation[1]
    plt.plot(new_x, new_y, 'o')

    plt.show()


if __name__ == '__main__':
    main()
