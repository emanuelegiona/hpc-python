## Interfacing with Fortran

The file [evolve.f90](evolve.f90) contain a pure Fortran implementation of the
single time step in heat equation. Use **f2py** for creating Python interface,
and use the Fortran function instead the Python function in
(heat.py)[heat.py].
You may need to insert `f2py` attributes into the Fortran file.

### Timing

Using pre-compiled Fortran code, we're able to achieve **0.019 s** running time for the heat
equation solver on the small instance of the bottle file.

Same performance as using CFFI, but definitely less configuration needed.
