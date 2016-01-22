"""
component_params.py

Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

## TODO: here goes the list of the input files. Use flags: 
## '__REQUIRED__' to make it required
## '__FLAG__' to make it a flag or switch.
input_files  = {
                'annotation_gtf_file': None, # --sjdbGTFfile
                'fastq_reads' : '__REQUIRED__', # --readFilesIn
                'genome_dir' : '__REQUIRED__', # --genomeDir
                }

## TODO: here goes the list of the output files.
output_files = {
                'output_prefix' : None, # --outFileNamePrefix 
                'tmp_out_dir' : None, # --outTmpDir
                }

## TODO: here goes the list of the input parameters excluding input/output files.
input_params = {
                'chim_out_type' : None, # --chimOutType
                'chr_prefix' : None, # --sjdbGTFchrPrefix
                'decompress_cmd' : None, #--readFilesCommand
                'derive_strand' : None, # --outSAMstrandField
                'filter_junctions' : None, # --outFilterIntronMotifs
                'genome_load': None, # --genomeLoad
                'max_mem' : None, # --limitGenomeGenerateRAM
                'max_mem_sort' : None, # --limitBAMsortRAM
                'min_chim_seg_size': None, # --chimSegmentMin 
                'num_threads' : None, # --runThreadN
                'output_type' : 'BAM SortedByCoordinate', #--outSAMtype 
                'read_length' : None, # --sjdbOverhang 
                'two_pass_mode' : None, # --twopassMode
                'unmapped_reads' : None, #outReadsUnmapped
                'unmapped_reads_within_outSAM': None, # --outSAMunmapped
                }

## TODO: here goes the return value of the component_seed. 
## DO NOT USE, Not implemented yet!
return_value = []

                    
                    
