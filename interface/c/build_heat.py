from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
    void evolve(double *u, double *u_previous, int nx, int ny, double a, double dt, double dx2, double dy2);
                """)

ffibuilder.set_source(
    "_c_evolve",
    """
        void evolve(double *u, double *u_previous, int nx, int ny, double a, double dt, double dx2, double dy2);
    """,
    sources=["evolve.c"],
    library_dirs=[],
    libraries=[]
)

ffibuilder.compile(verbose=True)
