#!/usr/bin/env python3
import sys
import argparse
import pandas as pd
import src.api_related_functions as apif
import src.extract_info as ext

def main():
    parser = argparse.ArgumentParser(description='Harry Potter Data base, get information from this amazing world')
    parser.add_argument('-c','--character', type = str, metavar='', help = 'Select a character from Harry Potter' )
    parser.add_argument('-o','--house', type = str, metavar='', help = 'Select a house from Harry Potter' )
    parser.add_argument('-f','--faction', type = str, metavar='', help = 'Select a faction from Harry Potter')
    parser.add_argument('-g','--gender', type = str, metavar='', help = 'Select the gender')

    args = parser.parse_args()


    ext.correct_name(args.character)
    character = args.character
    ext.correct_name(args.house)
    house = args.house
    ext.correct_name(args.faction)
    faction = args.faction
    ext.gender_check(args.gender)
    gender = args.gender
    print(args)

    #import data frame
    potter = ext.importdataset()
    #extract info from the selected character.
    ext.character_selection(character)
    #extract info from the selected house.
    apif.get_house_info(house)
    #extract rate 
    ext.ratio(house)

    #group_by
    ext.group(potter,'House',faction).sum()
    print(ext.group(potter,'Blood_Status',faction).sum())
    


    

 


if __name__ == '__main__' :
    main()
   