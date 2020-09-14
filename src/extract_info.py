import requests  #Si no llamaba aquí a requests no funcionaba la función, decía que no estaba definida
import pandas as pd 
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("Potter_api_key")

def importdataset(name):
    """Import a given dataset"""
    potter = pd.read_csv(f'Output/{name}.csv',encoding='latin1')
    return potter


def character_selection(character_name='Tom Riddle'):
    """This function allows you to select available Harry Potter´s character in the potter.csv data set and display the information"""
    potter = pd.read_csv('Output/potter.csv',encoding='latin1')
    potter = potter.set_index('Name', drop=False)
    potter_t = potter.T
    return potter_t[character_name]


def ratio(house_name='Slytherin'):
    """This function is used to calculate a ratio based in three parameters data frame, column and the attribute of the column, the columna and categoria parameters should be a string"""
    potter = pd.read_csv('Output/potter.csv',encoding='latin1')
    potter=potter.query("House != 'Unknown'")
    a=potter[potter['House']==house_name]
    b=potter['House']

    p1=len(a)
    p2=len(b)
    ratio=(p1/p2)*100
    return f'The ratio of {house_name} students in Hogwarts School of Witchcraft and Wizardry is {ratio:.2f}'


def group(data, columna1, columna2):
    """Simple group by function, that received three parameters dataframe and two columns"""
    gp=data.groupby(columna1)[columna2]
    return gp


def emptyspaces(name):
    """Substitute a '-' for ' ' """
    if '_' in name:
        word= name.replace('_',' ')
        return word
    else: 
        return name
    