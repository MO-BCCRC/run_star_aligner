""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

from kronos.utils import ComponentAbstract
import os


class Component(ComponentAbstract):
    
    """
    TODO: add component doc here. 
    """

    def __init__(self, component_name="run_star_aligner", 
                 component_parent_dir=None, seed_dir=None):
        
        ## TODO: pass the version of the component here.
        self.version = "v0.99.0"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, 
                                        component_parent_dir, seed_dir)

    ## TODO: write the focus method if the component is parallelizable.
    ## Note that it should return cmd, cmd_args.
    def focus(self, cmd, cmd_args, chunk):
        pass 
#         return cmd, cmd_args

    ## TODO: this method should make the command and command arguments 
    ## used to run the component_seed via the command line. Note that 
    ## it should return cmd, cmd_args. 
    def make_cmd(self, chunk=None):
        cmd = self.requirements['star_binary']
        cmd_args = []
        args = vars(self.args)
        
        ## component params to seed params mapping
        comp_seed_map = {
                         'annotation_gtf_file': 'sjdbGTFfile',
                         'fastq_reads' : 'readFilesIn',
                         'genome_dir' : 'genomeDir',
                         'output_prefix' : 'outFileNamePrefix', 
                         'tmp_out_dir' : 'outTmpDir',
                         'chim_out_type' : 'chimOutType',
                         'chr_prefix' : 'sjdbGTFchrPrefix',
                         'decompress_cmd' : 'readFilesCommand',
                         'derive_strand' : 'outSAMstrandField',
                         'filter_junctions' : 'outFilterIntronMotifs',
                         'genome_load' : 'genomeLoad',
                         'max_mem' : 'limitGenomeGenerateRAM',
                         'max_mem_sort' : 'limitBAMsortRAM',
                         'min_chim_seg_size': 'chimSegmentMin', 
                         'num_threads' : 'runThreadN',
                         'output_type' : 'outSAMtype',
                         'read_length' : 'sjdbOverhang', 
                         'two_pass_mode' : 'twopassMode',
                         'unmapped_reads' : 'outReadsUnmapped',
                         'unmapped_reads_within_outSAM': 'outSAMunmapped',
                        }

        for k, v in args.items():
            if v is None or v is False:
                continue

            k = comp_seed_map[k]            
            cmd_args.append('--' + k)
            
            if isinstance(v, bool):
                continue
            if isinstance(v, str) and k != 'outSAMtype':
                v = repr(v)
            if isinstance(v, (list, tuple)):
                cmd_args.extend(v)
            else:
                cmd_args.extend([v])
        
        return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

