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

setup(name='hdmedians',
      packages=find_packages(),
      tests_require=['pytest', 'pytest-cov'],
      setup_requires=['Cython>=0.23'],
      install_requires=['numpy', 'Cython>=0.23'],
      version='0.14.1',
      description='High-dimensional medians',
      url='http://github.com/daleroberts/hdmedians',
      author='Dale Roberts',
      author_email='dale.o.roberts@gmail.com',
      license='Apache License, Version 2.0',
#      cmdclass = {'build_ext': build_ext},
      ext_modules = extensions)
