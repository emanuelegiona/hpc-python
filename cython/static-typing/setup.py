"""
Setup config for cyt_module.pyx
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="simple-cython-module",
    version="0.2",
    author="Emanuele Giona",
    description="Simple Cython module with static typing",
    ext_modules=cythonize("cyt_module.pyx", language_level="3")  # language_level required or import fails
)
