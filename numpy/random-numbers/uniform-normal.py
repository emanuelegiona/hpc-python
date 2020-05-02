import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    """
    See README.md for exercises.
    :return: None
    """

    # ex. 1
    print("--- Exercise 1 ---")
    arr_uniform = np.random.uniform(size=1000)
    plt.hist(arr_uniform)
    plt.title("uniform")
    print(f"Mean: {np.mean(arr_uniform)} | StdDev: {np.std(arr_uniform)}")
    print("--- --- ---\n")

    # ex. 2
    print("--- Exercise 2 ---")
    arr_normal = np.random.normal(size=1000)
    plt.figure()
    plt.hist(arr_normal)
    plt.title("normal")
    print(f"[Normal] Mean: {np.mean(arr_normal)} | StdDev: {np.std(arr_normal)}")

    arr_poisson = np.random.poisson(size=1000)
    plt.figure()
    plt.hist(arr_poisson)
    plt.title("poisson")
    print(f"[Poisson] Mean: {np.mean(arr_poisson)} | StdDev: {np.std(arr_poisson)}")
    print("--- --- ---\n")

    plt.show()


if __name__ == '__main__':
    main()
