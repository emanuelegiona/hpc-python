# Heat equation solver optimization notes

Performance comparison among different techniques of optimizing
the [heat equation solver](./heat_main.py) using Cython.

Timing are the ones computed inside the `main` function; S, M, and L refer to
[bottle.dat](./bottle.dat), [bottle_medium.dat](./bottle_medium.dat), and
[bottle_large.dat](./bottle_large.dat) input files respectively, passed via
the `-f` argument.

<table>
<tr>
    <td><b>Case</b></td>
    <td><b>Description</b></td>
    <td><b>Module</b></td>
    <td><b>Time</b></td>
</tr>
<tr>
    <td>0</td>
    <td>Baseline: pure Python code</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/heat-equation/heat.py">File</a></td>
    <td>
        S: 17.722 s
        <hr>
        M: 119.922 s
        <hr>
        L: 506.043 s
    </td>
</tr>

<tr>
    <td>1</td>
    <td>Trivial cythonize()</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/heat-equation/heat1.pyx">File</a></td>
    <td>
        S: 14.768 s
        <hr>
        M: 110.484 s
        <hr>
        L: 434.670 s
    </td>
</tr>

<tr>
    <td>2</td>
    <td>Full Cython tools (static typing, C functions, fast indexing) + NumPy indexing</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/heat-equation/heat2.pyx">File</a></td>
    <td>
        S: 0.064 s
        <hr>
        M: 1.049 s
        <hr>
        L: 3.468 s
    </td>
</tr>

</table>
