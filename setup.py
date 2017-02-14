"""
hdmedians: High-dimensional medians.
"""

import numpy as np
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

extensions = [Extension('hdmedians.geomedian', 
                        ['hdmedians/geomedian.pyx'],
                        include_dirs = [np.get_include()])]

setup(name='hdmedians',
      packages=find_packages(),
      setup_requires=['nose>=1.0', 'Cython >= 0.23'],
      install_requires=['numpy'],
      version='0.11',
      description='High-dimensional medians',
      url='http://github.com/daleroberts/hdmedians',
      author='Dale Roberts',
      author_email='dale.o.roberts@gmail.com',
      license='GPL3',
      ext_modules = cythonize(extensions))
