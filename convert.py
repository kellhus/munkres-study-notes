from __future__ import print_function

import os
import sys
import argparse
import subprocess


def write_combined_markdown(dirname, combined_name):
    with open(combined_name, 'w') as combined:
        for root, dirs, filenames in os.walk(dirname):
            path = root.split('/')
            print('# {}\n'.format(os.path.basename(root)), file=combined)
            for filename in filenames:
                with open('{}/{}'.format(root, filename), 'r') as piece:
                    markdown = piece.read()
                    print(markdown, file=combined)


def convert_with_pandoc(filename, extension):
    options = ['pandoc',
               '{}.md'.format(filename),
               '-o',
               '{}.{}'.format(filename, extension)]
    try:
        output = subprocess.check_output(options, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exception:
        print(exception.output)
    else:
        print(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dirname', help='directory to grep for .md files')
    parser.add_argument('-s', '--save-markdown',
                        help='store the combined markdown file',
                        action='store_true')
    parser.add_argument('-e', '--ext',
                        help="format to export the markdown to, default 'pdf'",
                        default='pdf')
    args = parser.parse_args()

    combined_name = '{}.md'.format(args.dirname)
    write_combined_markdown(args.dirname, combined_name)
    convert_with_pandoc(args.dirname, args.ext)
    if not args.save_markdown:
        os.remove(combined_name)
