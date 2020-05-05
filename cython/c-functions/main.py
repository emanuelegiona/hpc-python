from cyt_module import subtract


def main() -> None:
    """
    See README.md for exercises.
    :return: None
    """

    print(f"Subtracting 2 from 4")
    c = subtract(4, 2)
    print(f"Result: {c}")

    print(f"Subtracting 2 from 4.4")
    c = subtract(4.4, 2)
    print(f"Result: {c}")

    print(f"Subtracting 2 from 4.6")
    c = subtract(4.6, 2)
    print(f"Result: {c}")

    print(f"Subtracting 2.2 from 4")
    c = subtract(4, 2.2)
    print(f"Result: {c}")

    print(f"Subtracting 1.9 from 4")
    c = subtract(4, 1.9)
    print(f"Result: {c}")


if __name__ == '__main__':
    main()
