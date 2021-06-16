# coding: UTF-8
# Created by Mark Hsu on 2021/4/11
#
"""
This program converts Big5 file to UTF-8 with BOM file.
"""

import os


def run(path, output_path, sub_path):
    p = os.path.join(path, sub_path)
    op = os.path.join(output_path, sub_path)
    if not os.path.isfile(p):
        raise Exception("Not a file")

    if not os.path.exists((os.path.abspath(os.path.join(op, os.pardir)))):
        os.makedirs((os.path.abspath(os.path.join(op, os.pardir))))
    print(p)
    with open(p, encoding="big5") as reader:
        with open(op, 'w', encoding="utf-8-sig") as writer:
            for row in reader:
                writer.write(row)


def list_dirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            list_dirs(d)
        if os.path.isfile(d) and file != '.DS_Store':
            output_path = os.path.realpath(
                str(rootdir).replace('2017-2019', "trans"))
            run(rootdir, output_path, file)


if __name__ == '__main__':
    base_path = os.path.realpath(os.path.join(os.path.expanduser('~'), "Downloads"))
    target_dir = '2017-2019'
    p = os.path.realpath(os.path.join(base_path, target_dir))
    os.chdir(p)
    list_dirs(p)
