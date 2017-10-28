import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'VERSION')) as f:
    VERSION = f.read().strip()


setup(name='grpc_proto',
      version=VERSION,
      description='GRPC definitions',
      long_description="",
      classifiers=[
          "Programming Language :: Python",
          "Framework :: GRPC",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='CeleraOne GmbH',
      author_email='tim.eggert@celeraone.com',
      url='https://www.celeraone.com',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['grpcio', 'grpcio-tools'],
      entry_points="""\
      [paste.app_factory]
      main=py_grpc:main
      """)