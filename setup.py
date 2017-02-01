from setuptools import setup, find_packages

setup(name='hdmedians',
      packages=find_packages(),
      install_requires=['six', 'numpy'],
      version='0.1',
      description='High-dimensional medians',
      url='http://github.com/daleroberts/hdmedians',
      author='Dale Roberts',
      author_email='dale.o.roberts@gmail.com',
      license='GPL3',
      zip_safe=False)
