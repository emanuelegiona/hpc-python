"""
Setup config for fib_dp_eff.pyx
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="fib-cython",
    version="0.5",
    author="Emanuele Giona",
    description="Cython module for Fibonacci numbers",
    ext_modules=cythonize("fib_dp_eff.pyx", language_level="3")  # language_level required or import fails
)
