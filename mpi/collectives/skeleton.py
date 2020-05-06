from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4, 'Number of MPI tasks has to be 4.'

if rank == 0:
    print('First collective:')

# DONE: create data vector at task 0 and send it to everyone else
#       using collective communication
if rank == 0:
    data = np.arange(8)
else:
    data = np.empty(8, np.int)
comm.Bcast(data, root=0)
print('  Task {0}: {1}'.format(rank, data))


# Prepare data vectors ..
data += rank*8  # DONE: create the data vectors
# .. and receive buffers
buff = np.full(8, -1, int)

# ... wait for every rank to finish ...
comm.barrier()
if rank == 0:
    print('')
    print('-' * 32)
    print('')
    print('Data vectors:')
print('  Task {0}: {1}'.format(rank, data))
comm.barrier()
if rank == 0:
    print('')
    print('c)')

# DONE: how to get the desired receive buffer using a single collective
#       communication routine?
# evenly distribute data from task 0 to each of the 4 processes: Scatter
comm.Scatter(data, buff[:2], root=0)
print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
comm.barrier()
if rank == 0:
    print('')
    print('d)')

# DONE: how to get the desired receive buffer using a single collective
#       communication routine?
# evenly accumulate data in task 1 from each of the 4 processes: Gather
comm.Gather(data[:2], buff, root=1)
print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
comm.barrier()
if rank == 0:
    print('')
    print('e)')

# DONE: how to get the desired receive buffer using a single collective
#       communication routine?
# task pairwise sum is accumulated in even tasks (0 + 1 --> 0; 2 + 3 --> 3)
color = rank // 2
sub_comm = comm.Split(color)
sub_comm.Reduce(data, buff, op=MPI.SUM, root=0)
print('  Task {0}: {1}'.format(rank, buff))

