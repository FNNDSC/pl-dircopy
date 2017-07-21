#######
pl-copy
#######


Abstract
********

A Chris 'fs' plugin app to copy file/folders from a directory into a Chris' feed.

Run
***

Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code-block:: bash

    docker run -v /home:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-copy copy.py            \
            --dir /incoming /outgoing

The above will copy the contents of the host ``/home`` dir to the container's ``/outgoing``
which in turn has been volume mapped to the host ``$(pwd)/out`` directory.

Make sure that the host ``$(pwd)/out`` directory is world writable!







