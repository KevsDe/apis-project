#!/usr/bin/env python3
import sys
import argparse
import pandas as pd


parser = argparse.ArgumentParser(description='Harry Potter Data base, get information from this amazing world')
parser.add_argument('-c','--character', type = str, metavar='', help = 'Select a character from Harry Potter' )
parser.add_argument('-o','--house', type = str, metavar='', help = 'Select a house from Harry Potter' )
parser.add_argument('-f','--faction', type = str, metavar='', help = 'Select a faction from Harry Potter')
parser.add_argument('-s','--statics', type = str, metavar='', help = 'General statistics from Harry Potter world' )
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action = 'store_true', help = 'hola man')
group.add_argument('-v', '--verbose', action = 'store_true', help ='print verbose')
args = parser.parse_args()







if __name__ == '__main__' :
    print(args.character)
    print(args.house)
    if args.quiet:
        print ('hello')
    elif args.verbose:
        print('message here')
    else:
        print ('nada especificado')