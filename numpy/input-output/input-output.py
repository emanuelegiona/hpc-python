import numpy as np


def main() -> None:
    """
    See README.md for exercises.
    :return: None
    """

    def np_print(x: np.ndarray, msg: str = "NumPy array") -> None:
        """
        Prints contents of a NumPy array along with its type and shape.
        :param x: NumPy array
        :param msg: optional message
        :return: None
        """

        print(f"{msg}:\n{x}\n(type: {x.dtype}, shape: {x.shape})\n")

    filename = "xy-coordinates.dat"
    arr = np.loadtxt(filename)
    np_print(arr)

    arr[:, 1] += 2.5
    np_print(arr, "Modified NumPy array")

    np.savetxt("out_" + filename, arr, fmt="%.4f", header="X Y", delimiter=",")


if __name__ == '__main__':
    main()
