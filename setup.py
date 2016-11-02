import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
#with open(os.path.join(here, 'CHANGES.txt')) as f:
#    CHANGES = f.read()

requires = [
    'docopt',
    ]

setup(name='docopt_subcommands',
      version='0.0',
      description='create subcommand-based CLI programs with docopt',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Austin Bingham',
      author_email='austin@sixty-north.com',
      url='github.com/abingham/docopt-subcommands',
      keywords='command-line',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      # tests_require=tests_require,
      )
