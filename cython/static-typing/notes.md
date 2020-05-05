# Static typing notes

Adding static typing to the `subtract()` function in [cyt_module](./cyt_module.pyx)
in the following combinations:

<table>
<tr>
    <td><b>Case</b></td>
    <td><b>Description</b></td>
    <td><b>Typing</b></td>
    <td><b>Result</b></td>
</tr>
<tr>
    <td>1</td>
    <td>Result variable declared as integer</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/static-typing/cyt_module_case1.pyx">File</a></td>
    <td>
        Correct result with two integers
        <hr>
        Result is always rounded to the lower integer value
    </td>
</tr>

<tr>
    <td>2</td>
    <td>Result variable and function arguments declared as integers</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/static-typing/cyt_module_case2.pyx">File</a></td>
    <td>
        Correct result with two integers
        <hr>
        Function arguments are rounded to the lower integer value before subtraction,
        then integer subtraction is performed
    </td>
</tr>

<tr>
    <td>3</td>
    <td>Result variable and function arguments declared as integer and float, respectively</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/static-typing/cyt_module_case3.pyx">File</a></td>
    <td>Compilation error during make build: <i>Cannot assign 'float' to 'int'</i></td>
</tr>

<tr>
    <td>4</td>
    <td>Result variable and function arguments declared as floats</td>
    <td><a href="https://github.com/emanuelegiona/hpc-python/tree/master/cython/static-typing/cyt_module_final.pyx">File</a></td>
    <td>Correct result (minor rounding errors, as expected)</td>
</tr>
</table>
