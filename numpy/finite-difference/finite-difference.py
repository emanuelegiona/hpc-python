import math
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

    delta_x = 0.1
    xi = np.arange(0, math.pi/2, delta_x)
    np_print(xi, "x")

    sin_x = np.sin(xi)
    np_print(sin_x, "sin(x)")

    derivative_sin_x = (sin_x[2:] - sin_x[:-2]) / (2 * delta_x)
    np_print(derivative_sin_x, "d/dx sin(x)")

    cos_x = np.cos(xi)
    np_print(cos_x, "cos(x)")

    mse = np.sqrt(np.sum((derivative_sin_x - cos_x[1:-1]) ** 2))
    np_print(mse, "MSE d/dx sin(x) - cos(x)")


if __name__ == '__main__':
    main()
