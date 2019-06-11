from __future__ import absolute_import

import os
import re

from setuptools import setup, find_packages


def get_version():
    root = os.path.dirname(__file__)
    version_re = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

    init = read(os.path.join(root, 'fastestimator', '__init__.py'))
    return version_re.search(init).group(1)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name="fastestimator",
      version=get_version(),
      description="Deep learning Application framework",
      packages=find_packages(),
      package_dir={'': '.'},
      long_description=read('README.md'),
      author="FastEstimator Dev",
      url='https://github.build.ge.com/EdisonAITK/FastEstimator',
      license="Apache License 2.0",
      keywords="keras tensorflow",
      classifiers=[
          "Development Status :: 3 - Development/Stable",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.5",
      ],

      # Declare minimal set for installation
      install_requires=[
          'numpy',
          'pyfiglet',
          'pandas',
          'pillow',
          'sklearn',
          'wget',
          'matplotlib',
          'seaborn>= 0.9.0',
          'scipy',
          'pytest',
          'pytest-cov',
          'opencv-python'
      ],
      # Declare extra set for installation
      extras_require={
      },
      scripts=['bin/fastestimator', 'bin/fastestimator_train']
      )
