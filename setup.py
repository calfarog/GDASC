try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

requires = []


with open('requirements.txt') as fp:
    requires = fp.read()

setup(
    name='GDASC',
    version='0.0.1',
    packages=['GDASC', 'GDASC.clustering_algorithms', 'benchmarks', 'benchmarks.plotting', 'benchmarks.algorithms',
              'benchmarks.algorithms.Exact', 'benchmarks.algorithms.FLANN', 'benchmarks.algorithms.GDASC',
              'benchmarks.algorithms.Pynndescent'],
    url='',
    license='',
    author='elenagarciamorato',
    author_email='',
    description='',
    #packages=find_packages(),
    platforms='any',
    install_requires=requires
)
