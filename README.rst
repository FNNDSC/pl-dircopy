##########
pl-dircopy
##########


Abstract
********

A ChRIS *FS* (Feed Synthesis) plugin app that copies file/dir data from an input source to an output sink. If called directly, i.e. from the command line, the *input directory* is an actual specification on an actual filesystem. If called from a client that is talking to CUBE, this *input directory* is interpreted to mean a location within swift storage, and is *not* a file system location.


Pre-conditions
**************

When running this plugin from a client perspective to CUBE, note that the *input directory* is actually assumed to exist within swift storage, thus the value of the *input directory* is the prefix within swift storage. See the wiki pages of CUBE for more information.

Run
***

Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code-block:: bash

    docker run -v /home:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-dircopy dircopy.py            \
            --dir /incoming /outgoing

The above will recursively copy the entire host ``/home`` dir to the container's ``/outgoing``
which in turn has been volume mapped to the host ``$(pwd)/out`` directory.

Make sure that the host ``$(pwd)/out`` directory is world writable!







