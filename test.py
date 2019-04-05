#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os

parser = argparse.ArgumentParser(description='Test in Websites use selenium ')
parser.add_argument('--testlist',default="output", help='file name without extension')
args = parser.parse_args()

print(args.testlist)

if os.path.exists(args.testlist):
    lines = open(args.list,"r")
    for l in lines:
       print(l) 
            
       one_test_google (l.rstrip('\n'),l.rstrip('\n'))
