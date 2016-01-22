"""
component_ui.py

Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

import argparse

#==============================================================================
# make a UI 
#==============================================================================
## TODO: pass the name of the component to the 'prog' parameter and a
## brief description of your component to the 'description' parameter.
parser = argparse.ArgumentParser(prog='run_star_aligner', 
                                 description = """
                                 STAR aligner, i.e. maps reads to a
                                 reference genome.""")

## TODO: create the list of input options here. Add as many as desired.
parser.add_argument(
                    "-a", "--annotation_gtf_file", 
                    default = None,
                    help = """
                    specifies the path to the file with annotated transcripts
                    in the standard GTF format.
                    """)

parser.add_argument(
                    "-d", "--decompress_cmd", 
                    default = None, 
                    help = """
                    use this option if the read files are compressed.
                    For example, for gzipped files (*.gz)
                    use -d 'zcat' or -d 'gzip -c'. For bzip2-compressed files,
                    use -d 'bzip2 -c'.
                    The decompression command takes the input file as input
                    parameter, and sends the decompressed output to stdout.
                    """)

parser.add_argument(
                    "-f", "--fastq_reads", 
                    required = True,
                    nargs = '+',
                    help = """
                    /path/to/fastq1 [/path/to/fastq2]
                    """)
                    
parser.add_argument(
                    "-g", "--genome_dir", 
                    required = True,
                    default = None, 
                    help = """
                    path to the directory where the genome indices, generated 
                    by STAR index builder, are stored.
                    """)

parser.add_argument(
                    "-l", "--read_length", 
                    default = None, 
                    help = """
                    specifies the length of the genomic sequence around the
                    annotated junction to be used in constructing the splice
                    junctions database.
                    """)

parser.add_argument(
                    "-n", "--num_threads", 
                    default = None, 
                    help = """
                    the number of threads/cores to be used. 
                    """)

parser.add_argument(
                    "-p", "--output_prefix", 
                    default = None, 
                    help = """
                    All output files have standard names. However, you can specify
                    a prefix for the file names using this option, e.g.: 
                    -p /path/to/output/dir/prefix.
                    """)

parser.add_argument(
                    "-m", "--max_mem", 
                    default = None, 
                    help = """
                    maximum available RAM (in bytes) for genome generation.
                    """)

parser.add_argument(
                    "-t", "--output_type", 
                    default = 'BAM SortedByCoordinate', 
                    choices = ['SAM', 'BAM Unsorted', 'BAM SortedByCoordinate',
                               'BAM Unsorted SortedByCoordinate'],
                    help = """
                    specifies the type of the output. The options are:
                    - 'SAM': outputs SAM file "Aligned.out.sam",
                    - 'BAM Unsorted': outputs unsorted "Aligned.out.bam file",
                    - 'BAM SortedByCoordinate': outputs sorted by coordinate
                    "Aligned.sortedByCoord.out.bam" file, similar to samtools
                    sort command,
                    - 'BAM Unsorted SortedByCoordinate': outputs both unsorted and
                    sorted files.
                    """)

parser.add_argument(
                    "-u", "--unmapped_reads", 
                    default = None, 
                    choices = ['fasta', 'fastq'],
                    help = """
                    outputs unmapped reads in fasta/fastq format (besides SAM
                    format) with names "Unmapped.out.mate1/2". None means no output.
                    """)

parser.add_argument(
                    "-z", "--min_chim_seg_size", 
                    default = None, 
                    help = """
                    specifies minimum length of chimeric segment length.
                    To switch on detection of chimeric (fusion) alignments 
                    (in addition to normal mapping), this option should be set
                    to a positive value. 0 means no chimeric output. If this 
                    option is used, the following files are generated:
                    - "Chimeric.out.sam": contains alignments for
                    fusion-spanning reads, 
                    - "Chimeric.out.junction": contains junction reads. 
                    """)

parser.add_argument(
                    "--chim_out_type", 
                    default = None, 
                    choices = ['SeparateSAMold', 'WithinBAM'],
                    help = """
                    using this option as: -c WithinBAM, Chimeric alignments
                    can be included together with normal alignments in the main 
                    (sorted or un-sorted) output BAM files(s) that are named
                    "Aligned.*.bam". By default, it is written into a separate
                    file called "Chimeric.out.sam".
                    """)

parser.add_argument(
                    "--chr_prefix", 
                    default = None, 
                    help = """
                    prefix for chromosome names in a GTF file, e.g. 'chr' for
                    using ENSMEBL annotations with UCSC geneomes.
                    """)

parser.add_argument(
                    "--derive_strand", 
                    default = None,
                    choices = ['intronMotif'], 
                    help = """
                    Cufflinks-like strand field flag. The options are: 
                    - 'intronMotif': strand derived from the intron motif.
                    Reads with inconsistent and/or non-canonical introns
                    are filtered out.
                    """)

parser.add_argument(
                    "--filter_junctions", 
                    default = None, 
                    choices = ['RemoveNoncanonical',
                               'RemoveNoncanonicalUnannotated'],
                    help = """
                    filter alignment using their motifs. The options are:
                    - 'RemoveNoncanonical': filter out alignments that contain
                    non-canonical junctions,
                    - 'RemoveNoncanonicalUnannotated': filter out alignments
                    that contain non-canonical unannotated junctions when using
                    annotated splice junctions database. The annotated
                    non-canonical junctions will be kept.
                    """)

parser.add_argument(
                    "--genome_load",
                    default = None,
                    choices = ["LoadAndKeep",  "LoadAndRemove",
                               "LoadAndExit", "Remove", "NoSharedMemory"],
                    help = """
                    Specify the mode of shared memory usage for the genome
                    files. The default is "NoSharedMemory". The choices are:
                    - LoadAndKeep: load genome into shared and keep it in
                    memory after run. 
                    - LoadAndRemove: load genome into shared but remove it after
                    run. 
                    - LoadAndExit: load genome into shared memory and exit,
                    keeping the genome in memory for future runs. 
                    - Remove: do not map anything, just remove loaded genome
                    from memory.
                    - NoSharedMemory: do not use shared memory, each job will
                    have its own private copy of the genome. 
                    """)

parser.add_argument(
                   "--max_mem_sort", 
                   default = None,
                   help = """
                   Specify the maximum available RAM for sorting BAM in byte. 
                   If =0, it will be set to the genome index size. Note: 
                   0 value can only be used with "--genome_load NoSharedMemory"
                   option. 
                   """
                   )

parser.add_argument(
                    "--tmp_out_dir", 
                    default = None, 
                    help = """
                    path to a directory that will be used as temporary by STAR.
                    All contents of this directory will be removed! Default name 
                    is "outFileNamePrefix_STARtmp"
                    """)

parser.add_argument(
                    "--two_pass_mode", 
                    default = None,
                    choices = ['Basic'], 
                    help = """
                    To run STAR 2-pass mapping for each sample separately,
                    use: -t Basic. STAR will perform the 1st pass mapping,
                    then it will automatically extract junctions, insert them
                    into the genome index, and, finally, re-map all reads in
                    the 2nd mapping pass.
                    """)

parser.add_argument(
                    "--unmapped_reads_within_outSAM", 
                    default = None, 
                    choices = ['Whithin'],
                    help = """
                    outputs unmapped reads within the main SAM file,
                    i.e. Aligned.out.sam. None means no output.
                    """)

## parse the argument parser.
args, unknown = parser.parse_known_args()
