pl-dircopy
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-dircopy
    :target: https://hub.docker.com/r/fnndsc/pl-dircopy

.. image:: https://img.shields.io/github/license/fnndsc/pl-dircopy
    :target: https://github.com/FNNDSC/pl-dircopy/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-dircopy/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/pl-dircopy/actions


.. contents:: Table of Contents


Abstract
--------

A ChRIS *FS* (Feed Synthesis) plugin app that copies file/dir data from an input source to an
output sink. When called from a client that is talking to CUBE, this *input directory* is
interpreted to mean a location within swift storage, and is *not* a file system location.


Description
-----------

``dircopy`` is a ChRIS-based application to copy the *contents* of one or more obj storage
directories given by the --dir argument to a new directory specified by <options.outpudir>.
This argument is a string containing one or more directories separated by comma.


Pre-conditions
**************

When running this plugin from a client perspective to CUBE, note that the *input directory* is
actually assumed to exist within swift storage, thus the value of the *input directory* is the
prefix within swift storage. See the wiki pages of CUBE for more information.


Usage
-----

.. code::

        python dircopy.py
            [-h] [--help]
            [--json]
            [--man]
            [--meta]
            [--savejson <DIR>]
            [-v <level>] [--verbosity <level>]
            [--version]
            <outputDir>
            [--dir <DIR>]


Arguments
~~~~~~~~~

.. code::

    [-h] [--help]
    If specified, show help message and exit.
    
    [--json]
    If specified, show json representation of app and exit.
    
    [--man]
    If specified, print (this) man page and exit.

    [--meta]
    If specified, print plugin meta data and exit.
    
    [--savejson <DIR>] 
    If specified, save json representation file to DIR and exit. 
    
    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.
    
    [--version]
    If specified, print version number and exit.

    <outputDir>
    Output directory.

    [--dir <DIR>]
    Required, it's a string representing a comma-separated list of one or more
    directories.


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-dircopy dircopy --man


Run
~~~

You need you need to specify the output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u) -v $(pwd)/out:/outgoing      \
        fnndsc/pl-dircopy dircopy /outgoing --dir <DIR>


Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-dircopy .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-dircopy nosetests

Examples
--------

This example will copy all files in the `cube/uploads` and `SERVICES/PACS/BCH` directories
into the output dir. Note: This is a utility 'fs' plugin that only works in the context of
the ChRIS platform.

.. code:: bash

    docker run --rm -v $(pwd)/out:/outgoing fnndsc/pl-dircopy    \
        dircopy /outgoing --dir 'cube/uploads,SERVICES/PACS/BCH'


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
