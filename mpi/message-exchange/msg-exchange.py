from mpi4py import MPI
import numpy as np


def main() -> None:
    """
    See README.md for this exercise.
    :return: None
    """

    communicator = MPI.COMM_WORLD
    rank = communicator.Get_rank()

    content = {"rank": rank}

    # ex. 1
    src = 0
    dictionary = {}
    if rank == 0:
        src = 1
        communicator.send(content, dest=1)
        dictionary = communicator.recv(source=src)
    elif rank == 1:
        src = 0
        dictionary = communicator.recv(source=src)
        communicator.send(content, dest=0)

    print(f"[{rank}] Data received from {src}:\n{dictionary}")

    # ex. 2
    arr_size = 100_000
    arr = np.full(arr_size, rank, np.int)
    arr_r = np.empty(arr_size, np.int)

    if rank == 0:
        src = 1
        communicator.Send(arr, dest=1)
        communicator.Recv(arr_r, source=src)
        print(f"[{rank}] Data received from {src} (first element):\n{arr_r[0]}")
    elif rank == 1:
        src = 0
        communicator.Recv(arr_r, source=src)
        communicator.Send(arr, dest=0)
        print(f"[{rank}] Data received from {src} (first element):\n{arr_r[0]}")


if __name__ == '__main__':
    main()
