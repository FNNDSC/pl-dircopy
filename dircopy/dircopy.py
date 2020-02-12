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
    Copy the *contents* of a directory given by the --dir argument to a new 
    directory specified by <options.outpudir>.
    """
    AUTHORS         = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH        = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC        = os.path.basename(__file__)
    EXECSHELL       = 'python3'
    TITLE           = 'A directory copy chris fs app'
    CATEGORY        = 'copy'
    TYPE            = 'fs'
    DESCRIPTION     = 'A plugin fs app to copy an entire directory'
    DOCUMENTATION   = 'http://wiki'
    LICENSE         = 'Opensource (MIT)'
    VERSION         = '0.1.1'
    MAX_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS = 1  # Override with integer value
    MAX_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Fill out this with key-value output descriptive info (such as an output file path
    # relative to the output dir) that you want to save to the output meta file when
    # called with the --saveoutputmeta flag
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        """
        self.add_argument('--dir', 
                          dest          = 'dir', 
                          type          = ChrisApp.path, 
                          optional      = False,
                          help          = 'directory to be copied')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        #output_folder = os.path.basename(options.dir.rstrip('/'))
        #output_path = os.path.join(options.outputdir, output_folder)
        # print('Copying %s to %s' % (options.dir, options.outputdir))
        copy_tree(options.dir, options.outputdir)


# ENTRYPOINT
if __name__ == "__main__":
    app = DirCopy()
    app.launch()
