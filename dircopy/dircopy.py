#                                                            _
# dircopy fs app
#
# (c) 2016 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os

# import the Chris app superclass
from chrisapp.base import ChrisApp
from distutils.dir_util import copy_tree

class DirCopy(ChrisApp):
    """
    Copy an entire directory given by the --dir argument to the output directory.
    """
    AUTHORS         = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH        = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC        = os.path.basename(__file__)
    EXECSHELL       = 'python3'
    TITLE           = 'A directory copy chris fs app'
    CATEGORY        = ''
    TYPE            = 'fs'
    DESCRIPTION     = 'A plugin fs app to copy an entire directory'
    DOCUMENTATION   = 'http://wiki'
    LICENSE         = 'Opensource (MIT)'
    VERSION         = '0.1'

    def define_parameters(self):
        self.add_argument('--dir', dest='dir', type=str, default='./', optional=True,
                          help='directory to be copied')

    def run(self, options):
        output_folder = os.path.basename(options.dir.rstrip('/'))
        output_path = os.path.join(options.outputdir, output_folder)
        # print('Copying %s to %s' % (options.dir, options.outputdir))
        copy_tree(options.dir, options.outputdir)


# ENTRYPOINT
if __name__ == "__main__":
    app = DirCopy()
    app.launch()
