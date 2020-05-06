import numpy as np
cimport numpy as cnp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cython

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'

@cython.boundscheck(False)
@cython.wraparound(False)
cdef evolve(cnp.ndarray u, cnp.ndarray u_previous, float a, float dt, float dx2, float dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    u[1:-1, 1:-1] = u_previous[1:-1, 1:-1] + a * dt * ( \
                (u_previous[2:, 1:-1] - 2 * u_previous[1:-1, 1:-1] + \
                 u_previous[:-2, 1:-1]) / dx2 + \
                (u_previous[1:-1, 2:] - 2 * u_previous[1:-1, 1:-1] + \
                 u_previous[1:-1, :-2]) / dy2)
    u_previous[:] = u[:]

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef iterate(cnp.ndarray field, cnp.ndarray field0, float a, float dx, float dy, int timesteps, int image_interval):
    """Run fixed number of time steps of heat equation.
    Most critical part to optimize.
    """

    cdef float dx2
    cdef float dy2
    cdef float dt
    cdef m

    dx2 = dx**2
    dy2 = dy**2

    # For stability, this is the largest interval possible
    # for the size of the time-step:
    dt = dx2*dy2 / ( 2*a*(dx2+dy2) )

    m = 1
    while m < timesteps+1:
        evolve(field, field0, a, dt, dx2, dy2)
        if m % image_interval == 0:
            write_field(field, m)
        m += 1

cpdef init_fields(str filename):
    # Read the initial temperature field from file
    cdef cnp.ndarray field
    cdef cnp.ndarray field0

    field = np.loadtxt(filename)
    field0 = field.copy() # Array for field of previous time step

    return field, field0

cpdef write_field(cnp.ndarray field, int step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))


