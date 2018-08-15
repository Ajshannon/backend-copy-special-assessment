#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
# import commands
import argparse
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def find_special_paths(dir):
    matches = []
    filesInDir = os.listdir(dir)
    for file in filesInDir:
        match = re.search(r'__(\w+)__', file)
        if match:
            matches.append(os.path.abspath(os.path.join(dir, file)))
    return matches


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='whatever')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    if not args:
        print "no you didnt do it right"
        sys.exit()
    if args.todir:
        # do a thing
        for file in find_special_paths(args.fromdir):
            if not os.path.exists(args.todir):
                os.makedirs(args.todir)
            shutil.copy2(file, args.todir)

    if args.tozip:
        subprocess.call(['zip', '-j', args.tozip]
                        + find_special_paths(args.fromdir))

    if not args.todir and not args.tozip:
        # do a thing
        for file in find_special_paths(args.fromdir):
            print os.path.abspath(file)

        # This is input data validation.  If something is wrong
        # (or missing) with any
        # required args, the general rule is to print a usage message 
        # and exit(1).

        # +++your code here+++
        # Call your functions


if __name__ == "__main__":
    main()

