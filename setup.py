"""
hdmedians: High-dimensional medians.
"""

import numpy as np
from setuptools import setup, find_packages, Extension
from setuptools import setup, Extension

#from Cython.Distutils import build_ext

extensions = [Extension('hdmedians.geomedian', 
                        ['hdmedians/geomedian.pyx'],
                        include_dirs = [np.get_include()])]

setup(packages=find_packages(), ext_modules = extensions)
