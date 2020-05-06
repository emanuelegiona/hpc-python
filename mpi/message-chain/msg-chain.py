from mpi4py import MPI
import numpy as np
import sys


def main(exercise: int = 1) -> None:
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

    if exercise == 1:
        # ex. 1: Send/Recv
        if rank > 0:
            communicator.Recv(buffer, source=rank - 1)
            print(f"[{rank}] Received message from {rank - 1}, first element: {buffer[0]}")

        if rank < size - 1:
            communicator.Send(content, dest=rank + 1)
            print(f"[{rank}] Sent {arr_size} elements to {rank + 1}")

    elif exercise == 2:
        # ex. 2: Sendrecv instead of Send/Recv
        if 0 < rank < size - 1:
            communicator.Sendrecv(content, dest=rank + 1, recvbuf=buffer, source=rank - 1)
            print(f"[{rank}] Sent {arr_size} elements to {rank + 1}")
            print(f"[{rank}] Received message from {rank - 1}, first element: {buffer[0]}")

        elif rank == 0:
            communicator.Send(content, dest=rank + 1)
            print(f"[{rank}] Sent {arr_size} elements to {rank + 1}")

        elif rank == size - 1:
            communicator.Recv(buffer, source=rank - 1)
            print(f"[{rank}] Received message from {rank - 1}, first element: {buffer[0]}")

    else:
        # ex. 3: MPI.PROC_NULL
        tgt = rank + 1 if rank < size - 1 else MPI.PROC_NULL
        src = rank - 1 if rank > 0 else MPI.PROC_NULL

        communicator.Sendrecv(content, dest=tgt, recvbuf=buffer, source=src)

        if tgt != MPI.PROC_NULL:
            print(f"[{rank}] Sent {arr_size} elements to {rank + 1}")
        if src != MPI.PROC_NULL:
            print(f"[{rank}] Received message from {rank - 1}, first element: {buffer[0]}")


if __name__ == '__main__':
    main(exercise=int(sys.argv[1]) if len(sys.argv) == 2 else 1)
