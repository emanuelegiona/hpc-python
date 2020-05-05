"""
Setup config for fib_cfunc.pyx
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="fib-cython",
    version="0.2",
    author="Emanuele Giona",
    description="Cython module for Fibonacci numbers",
    ext_modules=cythonize("fib_cfunc.pyx", language_level="3")  # language_level required or import fails
)
