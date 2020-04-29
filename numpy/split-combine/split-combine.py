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

    arr = np.random.random((8, 8))
    np_print(arr)

    # ex. 1
    print("--- Exercise 1 ---")
    vsplit1, vsplit2 = np.split(arr, 2)
    np_print(vsplit1, "Vertical split 1")
    np_print(vsplit2, "Vertical split 2")

    vconc = np.concatenate((vsplit1, vsplit2))
    print(f"Reconstructed array: {np.equal(arr, vconc).all()}")
    print("--- --- ---\n")

    # ex. 2
    print("--- Exercise 2 ---")
    hsplit1, hsplit2 = np.split(arr, 2, axis=1)
    np_print(hsplit1, "Horizontal split 1")
    np_print(hsplit2, "Horizontal split 2")

    hconc = np.concatenate((hsplit1, hsplit2), axis=1)
    print(f"Reconstructed array: {np.equal(arr, hconc).all()}")
    print("--- --- ---\n")


if __name__ == '__main__':
    main()
