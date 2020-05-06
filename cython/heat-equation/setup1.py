"""
Setup config for heat1.pyx
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="heat-eq-cython",
    version="0.1",
    author="Emanuele Giona",
    description="Cython module optimizing heat equation solver",
    ext_modules=cythonize("heat1.pyx", language_level="3")  # language_level required or import fails
)
