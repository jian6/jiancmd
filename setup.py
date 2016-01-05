from setuptools import setup

install_rerquires = [
     'setuptools',
     'docopt',
     'requests'
]
setup(name='jiancmd',
      version='1.0',
      packages=['jiancmd'],
      entry_points={
          'console_scripts': [
              'jiancmd = jiancmd.main:main'
          ]
      },
)
