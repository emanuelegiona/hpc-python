# Fibonacci numbers

Performance comparison for computing Fibonacci numbers using `timeit` module (10 loops, best of 3).

<table>
<tr>
    <td><b>Case</b></td>
    <td><b>Description</b></td>
    <td><b>Module</b></td>
    <td><b>Time per loop</b></td>
</tr>
<tr>
    <td>1</td>
    <td>Pure Python</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/c-functions/fib.py">File</a></td>
    <td>188 ms</td>
</tr>

<tr>
    <td>2</td>
    <td>Cython module with static typing</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/cython/c-functions/fib_typing.pyx">File</a></td>
    <td>46 ms</td>
</tr>

<tr>
    <td>3</td>
    <td>Cython module using C-functions</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/cython/c-functions/fib_cfunc.pyx">File</a></td>
    <td>2.66 ms</td>
</tr>

<tr>
    <td>4</td>
    <td>Cython module splitting `cpdef` and `cdef` functions</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/cython/c-functions/fib_cfunc2.pyx">File</a></td>
    <td>2.76 ms</td>
</tr>

<tr>
    <td>5</td>
    <td>Cython module using `cpdef` and dynamic programming (DP) algorithm</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/cython/c-functions/fib_dp.pyx">File</a></td>
    <td>84.3 ms</td>
</tr>

<tr>
    <td>6</td>
    <td>Cython module using `cpdef` and dynamic programming (DP) and space-efficient algorithm</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/cython/c-functions/fib_dp_eff.pyx">File</a></td>
    <td>0.0398 &mu;s </td>
</tr>
</table>
