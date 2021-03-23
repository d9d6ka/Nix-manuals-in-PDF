import os.path
import re
import argparse


parser = argparse.ArgumentParser(
    description="Prepare Nix{,OS} manuals for Pandoc"
)
parser.add_argument(
    '-f', '--file',
    dest='rep_file',
    nargs='?',
    required=True,
    type=str,
    help='The list of replacements'
)
parser.add_argument(
    '-o', '--output',
    dest='out_file',
    nargs='?',
    type=str,
    help='Output file'
)
parser.add_argument(
    '-i', '--input',
    dest='in_file',
    nargs='?',
    required=True,
    type=str,
    help='Input file'
)

args = parser.parse_args()

if __name__ == '__main__':
    in_file = args.in_file
    rep_file = args.rep_file

    if args.out_file:
        out_file = args.out_file
    else:
        path, ext = os.path.splitext(in_file)
        out_file = path + '_out' + ext
    
    with open(in_file, 'r', encoding='utf8') as f:
        content = f.read()

    with open(rep_file, 'r', encoding='utf8') as rfile:
        for pattern, repl in zip(rfile, rfile):
            print('{} :: {}'.format(pattern.strip('\n'), repl.strip('\n')))
            content = re.sub(
                pattern.strip('\n'),
                repl.strip('\n'),
                content,
                flags=re.M
            )

    with open(out_file, 'w', encoding='utf8') as outf:
        outf.write(content)

