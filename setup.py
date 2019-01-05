import os
import numpy as np
from Cython.Build import cythonize
from setuptools import Extension, setup, find_packages


def os_path(import_path, ext):
    return os.path.join(*import_path.split("."))+ext


def define_cython_extensions(*extensions, link_args=None, compile_args=None, language="c++", file_ext=".pyx"):
    modules = []
    for extension in extensions:
        modules.append(Extension(extension,
                       [os_path(extension, file_ext)],
                       language=language,
                       extra_compile_args=compile_args,
                       extra_link_args=link_args,
                       include_dirs=["."]))

    cythonize(modules)

    return modules


setup(name='cython-tutorials',
      version="1.0.0",
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      ext_modules=define_cython_extensions(
          "cython_tutorial.fibonacci.fibonacci",
      ),
      include_dirs=[np.get_include()],
      setup_requires=["Cython>=0.24"]
      )
