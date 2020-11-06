import argparse
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o', '--output',
        required=True,
        dest = 'output_file',
        help='The output filename'
    )
    parser.add_argument('-r', '--rows',
        required=True,
        dest = 'num_rows',
        type = int,
        help='The number of rows in the random matrix'
    )
    parser.add_argument('-c', '--cols',
        required=True,
        dest = 'num_cols',
        type = int,
        help='The number of columns in the random matrix'
    )
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    m = np.random.random(size=(args.num_rows, args.num_cols))
    np.savetxt(args.output_file, m)