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
    ext.gender_test(args.gender)
    gender = args.gender
    print(args)

    #import data frame
    potter = ext.importdataset()
    #extract info from the selected character.
    print(f'File on {character}')
    print(ext.character_selection(character))
    #extract info from the selected house.
    print(f'Information of {house} house')
    print(apif.get_house_info(house))
    #extract rate 
    print(ext.ratio(house))
    print(ext.ratio_g(gender))
    #probability
    print(ext.probability_faction(house,faction))
    #group_by
    print(f'Number of current or former Hogwarts School of Witchcraft and Wizardry students in the sample that are {faction}')
    print(ext.group(potter,'House',faction).sum())
    print(f'Number of {faction} in the sample based on blood status')
    print(ext.group(potter,'Blood_Status',faction).sum())
    #plots
    ext.ccountplot(potter,faction)
    ext.barplot(potter,faction)

if __name__ == '__main__' :
    main()
   