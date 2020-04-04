#!/usr/bin/env python3

import sys
import subprocess

filename = sys.argv[1]
old_name = "jane"
new_name = "jdoe"

with open(filename) as f:
    for line in f:
        words = line.strip()
        if old_name in words:
            old_string = words
            new_string = words.replace(old_name,new_name)
            subprocess.run(["mv",old_string,new_string])
