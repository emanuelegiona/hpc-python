import math
import numpy as np


def riemann_sum(delta_x: float) -> np.array:
    """
    Computes the Riemann Sum for sin(x), given the interval delta_x.
    :param delta_x: step in [0, pi/2] for evaluating sin(x)
    :return: NumPy array containing the estimated integral of sin(x)
    """

    xi = np.arange(0, math.pi / 2, delta_x)
    integral_sin_x = np.sum(np.sin((xi[1:] + xi[:-1])/2) * delta_x)

    return integral_sin_x


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

    for delta_x in [0.1, 0.05, 0.01, 0.005, 0.001]:
        integral_sin_x = riemann_sum(delta_x)

        mse = np.sqrt(np.sum((integral_sin_x - 1) ** 2))
        np_print(mse, f"MSE integral sin(x) - 1 | delta_x={delta_x}")


if __name__ == '__main__':
    main()
