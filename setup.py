from setuptools import setup, find_packages
import os

version = '2.0b9.dev0'

setup(name='raptus.article.files',
      version=version,
      description="Provides support for adding attachments to articles.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "MANUAL.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Raptus AG',
      author_email='dev@raptus.com',
      url='https://github.com/Raptus/raptus.article.files',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['raptus', 'raptus.article'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'raptus.article.core',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
