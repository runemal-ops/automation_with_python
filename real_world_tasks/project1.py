#!/usr/bin/env python3
from PIL import Image
import glob,os

size = 128, 128
for infile in glob.glob("ic_*"):
    im = Image.open(infile).convert("RGB")
    im.rotate(-90).resize((size)).save("/opt/icons/" + infile, "JPEG")

