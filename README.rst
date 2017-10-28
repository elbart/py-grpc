========================
Python3 GRPC Pet Project
========================

Synopsis
========
I want to test a working example of GRPC in python3.
There are several issues with the generated python3 code and the 
import method. The code is not relatively imported
(see: https://github.com/google/protobuf/issues/1491).

Solution
========
To maintain isolation of the generated protobuf stubs from
the rest of the "business logic" code, I created a separate
egg which contains all the definitions. 

See the ``src/requirements.txt`` how the eggs are used in development mode.

Requirements
============
- python3.6
- pip
- virtualenv
- make

Setup
=====
All should be covered with ``Makefile`` targets.

Build virtualenv and install requirements::

  make
  
Run the server::

  make server.run
  
Run the cliend::

  make client.run
