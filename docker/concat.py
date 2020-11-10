import argparse
import numpy as np
import pandas as pd

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
    index = ['g%d' % x for x in range(final_mtx.shape[0])]
    cols = ['C%d' % x for x in range(final_mtx.shape[1])]
    final_df = pd.DataFrame(final_mtx, index=index, columns=cols)
    final_df.to_csv(args.output_file, sep='\t')