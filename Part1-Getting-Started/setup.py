import os
from Cython.Build import cythonize
from setuptools import Extension, setup, find_packages


def os_path(import_path: str, ext: str) -> str:
    """
    Build the path to a module from it's import path.
    """

    return os.path.join(*import_path.split("."))+ext


def define_cython_extensions(*extensions: str, 
                             link_args: list=None, 
                             compile_args: list=None, 
                             language: str="c", 
                             file_ext: str=".pyx") -> list:
    """
    Build a list of Cython extension modules.
    """

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


# list your extensions here
ext_modules = define_cython_extensions(
    "fibonacci_example.fast.fibonacci",
)

setup(name="fibonacci-example",
      version="1.0.0",
      license="MIT",
      packages=find_packages(exclude=["contrib", "docs", "tests*"]),
      ext_modules=ext_modules,
      setup_requires=["Cython>=0.24"]
    )