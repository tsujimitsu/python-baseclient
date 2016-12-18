============================
Command Line (CLI) Template
============================


Setup
-----

.. code::

    # mkvirtualenv clibase
    # pip install pbr cliff
    # git clone https://github.com/tsujimitsu/python-baseclient.git
    # cd python-baseclient && python setup.py build && python setup.py install


Run
---

.. code::

    # base help
    usage: base [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
    
    optional arguments:
      --version            show program's version number and exit
      -v, --verbose        Increase verbosity of output. Can be repeated.
      -q, --quiet          Suppress output except warnings and errors.
      --log-file LOG_FILE  Specify a file to log output. Disabled by default.
      -h, --help           Show help message and exit.
      --debug              Show tracebacks on errors.
    
    Commands:
      complete       print bash completion command
      help           print detailed help for another command
      test cmd       A simple command that prints a message.
      test list      Show a list of test
      test show      Show detail information of test
      test2 cmd      A simple command that prints a message.


Uninstall
---------

.. code::

    # pip uninstall python-baseclient


Reference
----------

* `cliff - Command Line Interface Formulation Framework <http://docs.openstack.org/developer/cliff/>`_
* `OpenStack Osloを使おう - cliff編 <http://www.slideshare.net/h-saito/openstack-oslo-cliff>`_
