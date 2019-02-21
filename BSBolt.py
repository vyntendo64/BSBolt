import argparse
import sys
from BSB.BSB_Utils.UtilityFunctions import check_python_version, get_external_paths
from BSB.BSB_Utils.Launcher import bsb_launch

bt2_path, art_path = get_external_paths()
check_python_version()


parser = argparse.ArgumentParser(description='BiSulfite Bolt, A Bisulfite sequencing processing tool.',
                                 usage='python3 BSBolt.py Module {Module Arguments}')

subparsers = parser.add_subparsers(description='BSBolt Modules, Please Invoke BSBolt Modules for Help',
                                   metavar='Index, Align, CallMethylation, AggregateMatrix, Simulate',
                                   dest='subparser_name')

align_parser = subparsers.add_parser('Align', help='Alignment Module')
index_parser = subparsers.add_parser('Index', help='Index Generation Module')
call_meth_parser = subparsers.add_parser('CallMethylation', help='Methylation Calling Module')
matrix_parser = subparsers.add_parser('AggregateMatrix', help='CGmap Matrix Aggregation Module')
sim_parser = subparsers.add_parser('Simulate', help='BSBolt Illumina Read Simulation Module')

# Add Alignment Parser Commands

align_parser.add_argument('-F1', type=str, default=None, help='Path to fastq 1', required=True)
align_parser.add_argument('-F2', type=str, default=None, help='Path to fastq 2')
align_parser.add_argument('-U', action="store_false", default=True, help='Library undirectioinal, default=True')
align_parser.add_argument('-BT2', type=str, default=bt2_path, help='Path to bowtie2 aligner, default = bundled '
                                                                   'bowtie2')
align_parser.add_argument('-O', type=str, default=None, help='Path to Output Prefix', required=True)
align_parser.add_argument('-DB', type=str, default=None, help='Path to BSSeeker Database', required=True)
align_parser.add_argument('-CP', type=float, default=0.5, help='Proportion threshold to label read not fully converted')
align_parser.add_argument('-CT', type=int, default=5, help='Number of mCH that must be observed '
                                                           'to label a read unconverted')
align_parser.add_argument('-M', type=int, default=4, help='Read mismatch threshold, reads with mismatches greater than '
                                                          'threshold will be discarded')
align_parser.add_argument('-S', action="store_true", default=False, help='Position Sort Output Bam, default=False')
align_parser.add_argument('-BT2-local', action="store_true", default=False,
                          help='Bowtie2 local alignment or end-to-end, default end-to-end')
align_parser.add_argument('-BT2-D', type=int, default=40, help='Bowtie2 number of consecutive seed extension attempts '
                                                               'that can fail before Bowtie2 move on')
align_parser.add_argument('-BT2-k', type=int, default=2, help='Bowtie2 alignment search limit')
align_parser.add_argument('-BT2-p', type=int, default=2, help='Number of threads for Bowtie2 to use')
align_parser.add_argument('-BT2-L', type=int, default=20, help='Length of subseeds during alignment')
align_parser.add_argument('-BT2-score-min', type=str, default='L,-0.6,-0.6', help='Bowtie2 scoring function')
align_parser.add_argument('-BT2-I', type=int, default=0, help='Bowtie2, minimum fragment length '
                                                              'for a valid paired-end alignment')
align_parser.add_argument('-BT2-X', type=int, default=500, help='Bowtie2, maximum fragment length '
                                                                'for a valid paired-end alignment')

# Add Index Parser Commands

index_parser.add_argument('-G', type=str, required=True,
                          help='Path for reference genome fasta file, fasta file should contain all contigs')
index_parser.add_argument('-DB', type=str, required=True,
                          help='Path to index directory, will create directory if folder does not exist')
index_parser.add_argument('-BT2', type=str, default=bt2_path, help='Path to bowtie2 executable, default = bundled '
                                                                   'bowtie2')
index_parser.add_argument('-BT2-p', type=int, default=2, help='Number of threads for Bowtie2 to use')
index_parser.add_argument('-rrbs', action="store_true", default=False, help='Generate Reduced Representative'
                                                                            ' Bisulfite Sequencing Index')
index_parser.add_argument('-rrbs-cut-format', default='C-CGG',
                          help='Cut format to use for generation of RRBS database, '
                               'default= C-CGG (MSPI), input multiple enzymes as a '
                               'comma seperate string, C-CGG,C-CGG,...')
index_parser.add_argument('-rrbs-lower', type=int, default=40, help='Lower bound fragment size to consider RRBS index'
                                                                    'generation, default = 40')
index_parser.add_argument('-rrbs-upper', type=int, default=500, help='Upper bound fragment size to consider RRBS index'
                                                                     'generation, default = 500')

# Add Methylation Calling Parser Arguments

call_meth_parser.add_argument('-I', type=str, required=True,
                              help='Input BAM, input file must be in BAM format')
call_meth_parser.add_argument('-DB', type=str, required=True, help='Path to index directory')
call_meth_parser.add_argument('-O', type=str, required=True, help='Output prefix')
call_meth_parser.add_argument('-remove-ccgg', action="store_true", default=False,
                              help='Remove methylation calls in ccgg sites,'
                                   'default=False')
call_meth_parser.add_argument('-verbose', action="store_true", default=False, help='Verbose Output, default=False')
call_meth_parser.add_argument('-text', action="store_true", default=False,
                              help='Output plain text files, default=False')
call_meth_parser.add_argument('-remove-sx', action="store_false", default=True,
                              help='Remove methylation calls from reads marked '
                                   'as incompletely by BSSeeker-Align, default='
                                   'True')
call_meth_parser.add_argument('-ignore-overlap', action="store_true", default=False,
                              help='Only consider higher quality base '
                                   'when paired end reads overlap, '
                                   'default=False')
call_meth_parser.add_argument('-max', type=int, default=8000, help='Max read depth to call methylation')
call_meth_parser.add_argument('-min', type=int, default=10,
                              help='Minimum read depth required to report methylation site')
call_meth_parser.add_argument('-t', type=int, default=1,
                              help='Number of threads to use when calling methylation values')
call_meth_parser.add_argument('-min-qual', type=int, default=0, help='Minimum base quality for a base to considered for'
                                                                     'methylation calling')

# Add Matrix Aggregation Parser Args

matrix_parser.add_argument('-F', type=lambda file: [file_path for file_path in file.split(',')], required=True,
                           help='Comma separated list of CGmap file paths, or '
                                'path to text file with list of line separated '
                                'CGmap file paths')
matrix_parser.add_argument('-S', type=lambda sample_labels: [sample for sample in sample_labels.split(',')],
                           default=None,
                           help='Comma separated list of samples labels. '
                                'If sample labels are not provided sample labels '
                                'are extracted from CGmap file paths. '
                                'Can also pass path to txt for line separated sample '
                                'labels.')
matrix_parser.add_argument('-min-coverage', type=int, default=10, help='Minimum site read depth coverage for a '
                                                                       'site to be included in the aggregate matrix')
matrix_parser.add_argument('-min-sample', type=float, default=0.80,
                           help='Proportion of samples that must have a valid site '
                                '(above minimum coverage threshold), for a site to be'
                                'included in the aggregate matrix.')
matrix_parser.add_argument('-O', type=str, default=None, required=True, help='Aggregate matrix output path')
matrix_parser.add_argument('-CG', action="store_true", default=False, help='Only output CG sites')
matrix_parser.add_argument('-verbose', action="store_true", default=False, help='Verbose aggregation')

# Add Simulation Parser Args

sim_parser.add_argument('-G', type=str, required=True,
                        help='Path for reference genome fasta file, fasta file should contain all contigs')
sim_parser.add_argument('-A', type=str, default=art_path, help='Path to ART executable, default = bundled ART')
sim_parser.add_argument('-O', type=str, required=True, help='Output prefix')
sim_parser.add_argument('-PE', default=False, action='store_true', help='Simulate Paired End Reads, default Single End')
sim_parser.add_argument('-RL', type=int, default=125, help='Simulated Read Lenghth')
sim_parser.add_argument('-RD', type=int, default=20, help='Simulated Read Depth')
sim_parser.add_argument('-U', default=False, action='store_true',
                        help='Simulate Undirectional Reads, default=Directional')

arguments = parser.parse_args()
if len(sys.argv[1:]) == 0:
    parser.print_help()
    # parser.print_usage() # for just the usage line
    parser.exit()

if __name__ == "__main__":
    launcher = bsb_launch[arguments.subparser_name]
    launcher(arguments)