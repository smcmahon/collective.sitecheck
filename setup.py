from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.sitecheck',
      version=version,
      description="Site http check using sitemap",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Steve McMahon',
      author_email='steve@dcn.org',
      url='http://github.com/collective/collective.sitecheck',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'sitecheck = collective.sitecheck:sitecheck'
          ]
      },
      )
