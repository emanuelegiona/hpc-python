"""
Setup config for heat2.pyx
"""

from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name="heat-eq-cython",
    version="0.2",
    author="Emanuele Giona",
    description="Cython module optimizing heat equation solver",
    ext_modules=cythonize("heat2.pyx", language_level="3"),  # language_level required or import fails
    include_dirs=[np.get_include()]
)
