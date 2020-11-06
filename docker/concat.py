import argparse
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o', '--output',
        required=True,
        dest = 'output_file',
        help='The output filename'
    )
    parser.add_argument('input_files', nargs='+')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    mtx_list = []
    for f in args.input_files:
        mtx_list.append(np.loadtxt(f))
    final_mtx = np.vstack(mtx_list)
    np.savetxt(args.output_file, final_mtx, delimiter='\t')