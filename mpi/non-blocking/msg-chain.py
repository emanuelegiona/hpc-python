from mpi4py import MPI
import numpy as np


def main():
    """
    See README.md for this exercise.
    :return: None
    """

    communicator = MPI.COMM_WORLD
    rank = communicator.Get_rank()
    size = communicator.Get_size()
    arr_size = 500

    content = np.full(arr_size, rank, np.int)
    buffer = np.empty(arr_size, np.int)

    if rank > 0:
        req = communicator.Irecv(buffer, source=rank - 1)
        req.wait()
        print(f"[{rank}] Received message from {rank - 1}, first element: {buffer[0]}")

    if rank < size - 1:
        req = communicator.Isend(content, dest=rank + 1)
        req.wait()
        print(f"[{rank}] Sent {arr_size} elements to {rank + 1}")


if __name__ == '__main__':
    main()
