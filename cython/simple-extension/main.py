from cyt_module import subtract
import sys


def main(a, b) -> None:
    """
    See README.md for exercises.
    :return: None
    """

    print(f"Subtracting {b} from {a}")
    c = subtract(a, b)
    print(f"Result: {c}")


if __name__ == '__main__':
    assert len(sys.argv) == 3, "Subtracts B from A (float values)\nUsage: python main.py A B"
    try:
        arg1 = float(sys.argv[1])
        arg2 = float(sys.argv[2])

        main(arg1, arg2)
    except ValueError as e:
        print(f"Error: {str(e)}")
        print("Usage: python main.py A B")
        exit(1)
