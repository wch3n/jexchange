try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='jexchange',
    version='0.0.1',
    url='https://github.com/wch3n/jexchange',
    author='Wei Chen',
    author_email='waynechen@gmail.com',
    description='jexchange determines the exchange interactions among '
                'magnetic sites within the Heisenberg model.',
    install_requires=[
        'numpy>=1.18.1',
        'pymatgen>=2018.7.15',
    ],
    scripts=[
        'scripts/run.py',
    ],
    packages=[
        'jexchange',
    ],
)
