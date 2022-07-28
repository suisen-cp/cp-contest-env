#!/usr/bin/env python3

import argparse
import os
from sys import argv
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Expander')
    parser.add_argument('template', help='Template File')
    parser.add_argument('--dir', help='Output Directory')
    parser.add_argument('-r', '--range', action='store_true', help='Range Based Generation')
    parser.add_argument('--out', nargs='*')
    opts = parser.parse_args()

    input_file_name = opts.template
    if opts.range:
        l, r = opts.out
        files = [f'{chr(i)}.cpp' for i in range(ord(l), ord(r) + 1)]
    else:
        files = [f'{name}.cpp' for name in opts.out]
    out_dir = Path('./')
    if opts.dir:
        out_dir = Path(opts.dir)
    with open(input_file_name, mode='r') as template_file:
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        template = ''.join(template_file)
        for output_file_name in files:
            with open(out_dir / output_file_name, mode='w') as output_file:
                output_file.write(template)