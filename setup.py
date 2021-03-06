import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
# with open(os.path.join(here, 'CHANGES.txt')) as f:
#    CHANGES = f.read()

setup(name='docopt_subcommands',
      version='4.0.0',
      description='create subcommand-based CLI programs with docopt',
      long_description=README,
      long_description_content_type="text/markdown",
      license='MIT License',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'License :: OSI Approved :: MIT License',
      ],
      author='Austin Bingham',
      author_email='austin@sixty-north.com',
      url='https://github.com/abingham/docopt-subcommands',
      keywords='command-line docopt',
      packages=find_packages(exclude=['test', 'test.*']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['docopt'],
      # tests_require=tests_require,
      # List additional groups of dependencies here (e.g. development dependencies).
      # You can install these using the following syntax, for example:
      # $ pip install -e .[dev,test]
      extras_require={
          'dev': ['twine', 'wheel'],
          # 'doc': ['sphinx', 'cartouche'],
          'test': ['hypothesis>=1.11', 'pytest>=3.0.7'],
      },
)
