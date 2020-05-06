from mpi4py import MPI


def main() -> None:
    """
    See README.md for this exercise.
    :return: None
    """

    communicator = MPI.COMM_WORLD
    rank = communicator.Get_rank()
    size = communicator.Get_size()
    print(f"Process #{rank} (total: {size})")


if __name__ == '__main__':
    main()
