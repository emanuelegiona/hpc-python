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

    # ex. 1
    print("---\tExercise 1\t---")

    # step 0
    arr_2d = np.random.random((4, 4))
    np_print(arr_2d)

    # step 1
    row_2nd = arr_2d[1, :]
    np_print(row_2nd, "2nd row")

    # step 2
    col_3rd = arr_2d[:, 2]
    np_print(col_3rd, "3rd column")

    # step 3
    arr_2d[:2, :2] = 0.21
    np_print(arr_2d, "Modified NumPy array")
    print("---\t---\t---\n")

    # ex. 2
    print("---\tExercise 2\t---")
    checkerboard = np.ones((8, 8), dtype=np.int32)
    np_print(checkerboard)

    checkerboard[::2, 1::2] = 0
    checkerboard[1::2, 0::2] = 0
    np_print(checkerboard, "Modified NumPy array")
    print("---\t---\t---\n")


if __name__ == '__main__':
    main()
