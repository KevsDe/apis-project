import requests
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

def probability_faction (house_name,faction):
    potter = pd.read_csv('Output/potter.csv',encoding='latin1')
    potter_sample = potter.value_counts().sum()
    potter_faction = potter.query(f'{faction}' '==' "True").value_counts().sum()
    
    if house_name == 'Gryffindor':
        potter_house = potter.query("House" '==' "'Gryffindor'").value_counts().sum()
    elif house_name == 'Slytherin':
        potter_house = potter.query("House" '==' "'Slytherin'").value_counts().sum()
    elif house_name == 'Ravenclaw':
        potter_house = potter.query("House" '==' "'Ravenclaw'").value_counts().sum()
    elif house_name == 'Hufflepuff':
        potter_house = potter.query("House" '==' "'Hufflepuff'").value_counts().sum()
    
    prob = (potter_house/potter_sample) * (potter_faction/potter_sample)
    
    return f"The probability of being {house_name} and {faction} in the sample is {prob:.2f}%"



def importdataset():
    """Import a given dataset"""
    potter = pd.read_csv(f'Output/potter.csv',encoding='latin1')
    return potter


def character_selection(character_name):
    """This function allows you to select available Harry Potter´s character in the potter.csv data set and display the information"""
    potter = pd.read_csv('Output/potter.csv',encoding='latin1')
    potter = potter.set_index('Name', drop=False)
    potter_t = potter.T
    return potter_t[character_name]


def ratio(house_name):
    """This function is used to calculate a ratio based in three parameters data frame, column and the attribute of the column, the columna and categoria parameters should be a string"""
    potter = pd.read_csv('Output/potter.csv',encoding='latin1')
    potter=potter.query("House != 'Unknown'")
    a=potter[potter['House']==house_name]
    b=potter['House']

    p1=len(a)
    p2=len(b)
    ratio=(p1/p2)*100
    return f'The ratio of {house_name} students in Hogwarts School of Witchcraft and Wizardry in the sample is {ratio:.2f}%'

def ratio_g(gender):
    """This function is used to calculate a ratio based in three parameters data frame, column and the attribute of the column, the columna and categoria parameters should be a string"""
    potter = pd.read_csv('Output/potter.csv',encoding='latin1')
    a=potter[potter['Gender']==gender]
    b=potter['Gender']

    p1=len(a)
    p2=len(b)
    ratio=(p1/p2)*100
    return f'The ratio of {gender} gender in the sample of the Harry Potter universe is {ratio:.2f}%'

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
    

def correct_name(character):
    """Input validation"""
    valid_names = ['Aberforth Dumbledore', 'Alastor Moody', 'Albus Dumbledore', 'Alecto Carrow', 'Alice Longbottom', 'Alicia Spinnet', 'Amos Diggory', 'Amycus Carrow', 'Angelina Johnson', 'Anthony Goldstein', 'Antonin Dolohov', 'Argus Filch', 'Arthur Weasley', 'Aurora Sinistra', 'Bellatrix Lestrange', 'Blaise Zabini', 'Bloody Baron', 'Cedric Diggory', 'Charity Burbage', 'Charles Weasley', 'Cho Chang', 'Colin Creevey', 'Corban Yaxley', 'Cornelius Fudge', 'Cuthbert Binns', 'Dean Thomas', 'Dedalus Diggle', 'Dennis Creevey', 'Dobby', 'Dolores Umbridge', 'Draco Malfoy', 'Dudley Dursley', 'Elphias Doge', 'Emmeline Vance', 'Ernest Macmillan', 'Fat Friar', 'Fenrir Greyback', 'Filius Flitwick', 'Firenze', 'Fleur Delacour', 'Frank Longbottom', 'Fred Weasley', 'Gabrielle Delacour', 'Garrick Ollivander', 'Gellert Grindelwald', 'George Weasley', 'Gilderoy Lockhart', 'Ginevra Weasley', 'Godric Gryffindor', 'Gregory Goyle', 'Hannah Abbott', 'Harry Potter', 'Helena Ravenclaw', 'Helga Hufflepuff', 'Hermione Granger', 'Horace Slughorn', 'Igor Karkaroff', 'Irma Pince', 'James Potter I', 'Justin Finch-Fletchley', 'Katie Bell', 'Kingsley Shacklebolt', 'Kreacher', 'Lavender Brown', 'Lee Jordan', 'Lily J. Potter', 'Lucius Malfoy', 'Luna Lovegood', 'Marcus Flint', 'Marietta Edgecombe', 'Michael Corner', 'Millicent Bulstrode', 'Minerva McGonagall', 'Molly Weasley', 'Mundungus Fletcher', 'Narcissa Malfoy', 'Neville Longbottom', 'Nymphadora Tonks', 'Oliver Wood', 'Padma Patil', 'Pansy Parkinson', 'Parvati Patil', 'Penelope Clearwater', 'Percy Weasley', 'Peter Pettigrew', 'Petunia Dursley', 'Pomona Sprout', 'Poppy Pomfrey', 'Quirinus Quirrell', 'Regulus Black', 'Remus Lupin', 'Rodolphus Lestrange', 'Rolanda Hooch', 'Romilda Vane', 'Ronald Weasley', 'Rowena Ravenclaw', 'Rubeus Hagrid', 'Rufus Scrimgeour', 'Salazar Slytherin', 'Seamus Finnigan', 'Septima Vector', 'Severus Snape', 'Sirius Black', 'Sturgis Podmore', 'Susan Bones', 'Sybill Trelawney', 'Terry Boot', 'Theodore Nott', 'Tom Riddle', 'Vernon Dursley', 'Viktor Krum', 'Vincent Crabbe', 'Walden Macnair', 'Wilhelmina Grubbly-Plank', 'Zacharias Smith']
    try:
        if character in valid_names:
            return  character
    except Exception:
            raise argparse.ArgumentTypeError(f"{args.character} is an invalid name")


def correct_house(house):
    """Input validation"""
    valid_houses = ['Gryffindor','Slytherin','Ravenclaw','Hufflepuff']
    try:
        if house in valid_houses:
            return house
    except Exception:
            raise argparse.ArgumentTypeError(f"{args.house} is an invalid house")

def correct_faction(faction):
    """Input validation"""
    valid_factions = ['Dumbledores_Army','Death_Eater','Ministry_Of_Magic','Order_Of_The_Phoenix']
    try:
        if faction in valid_factions:
            return faction
    except Exception:
            raise argparse.ArgumentTypeError(f"{args.faction} is an invalid faction")



def gender_test (gb):
    """Input validation"""
    g_b = ['Male','Fermale','Unknown']
    try:
        if gb in g_b:
            return gb
    except Exception:
            raise argparse.ArgumentTypeError(f"{args.gb} is an invalid input")       


def ccountplot (data,column, pal="Set2"):
    """Create a seaborn count plot, 2 parameters, colum and palette set (optional, default 2)"""
    ax = sns.countplot(x=column, data=data, palette=pal)
    plt.title(f'Number of {column} in the sample')
    plt.savefig("grafico_faction")


def barplot (data,faction):
    ax = sns.barplot(x=faction, y="House", data=data)
    plt.title(f'Relationship between being {faction} and the house')
    plt.savefig("barplot")


    