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

    A = np.random.uniform(size=(2, 2))
    A += A.transpose()
    np_print(A, "Matrix A")

    B = np.random.uniform(size=(2, 2))
    B += B.transpose()
    np_print(B, "Matrix B")

    C = np.dot(A, B)
    np_print(C, "Matrix C = A x B")

    ev = np.linalg.eigvals(C)
    np_print(ev, "C eigenvalues")


if __name__ == '__main__':
    main()
