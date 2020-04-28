import numpy as np


def main() -> None:
    """
    See README.md for exercises.
    :return: None
    """

    def np_print(x: np.ndarray) -> None:
        """
        Prints contents of a NumPy array along with its type and shape.
        :param x: NumPy array
        :return: None
        """

        print(f"NumPy array: {x} (type: {x.dtype}, shape: {x.shape})")

    # ex. 1
    print("---\tExercise 1\t---")
    int_list = [*range(5)]
    float_list = [*map(lambda x: x + 0.5, int_list)]
    mixed_list = int_list + float_list
    print(f"Python list: {mixed_list} (size: {len(mixed_list)})")

    arr = np.array(mixed_list)
    np_print(arr)
    print("---\t---\t---\n")

    # ex. 2
    print("---\tExercise 2\t---")
    step_02 = np.arange(-2., 2.2, 0.2, dtype=np.float32)
    np_print(step_02)
    print("---\t---\t---\n")

    # ex. 3
    print("---\tExercise 3\t---")
    eq_spaced = np.linspace(0.5, 1.5, 11)
    np_print(eq_spaced)
    print("---\t---\t---\n")

    # ex. 4
    print("---\tExercise 4\t---")
    zen = "The Zen of Python, by Tim Peters"
    zen_arr = np.array(zen, dtype='c')
    np_print(zen_arr)
    print("---\t---\t---\n")


if __name__ == "__main__":
    main()
