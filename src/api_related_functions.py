
import requests  #Si no llamaba aquí a requests no funcionaba la función, decía que no estaba definida
import pandas as pd 
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("Potter_api_key")


def call_api(endp,key):
    """This function perform a call to the Potterapi, receive 1 value endp, the endpoint from the api for further information visit https://www.potterapi.com/"""
    base='https://www.potterapi.com/v1/'
    endpoint=endp
    url=base+endpoint+"?key="+key
    res=requests.get(url)
    data = res.json()
    return data



def api_extraction(data):

    """Create a dictionary with the selected information received from the potterapi"""
    dictionary=[]
    for x in range(0,len(data)):
        try:
            name={'name':data[x]['name'],
            'role':data[x]['role'],
            'species':data[x]['species'],
            'bloodStatus':data[x]['bloodStatus'],
             'dumbledoresArmy':data[x]['dumbledoresArmy'],
             'deathEater':data[x]['deathEater'],
            'ministryOfMagic':data[x]['ministryOfMagic'],
            'orderOfThePhoenix':data[x]['orderOfThePhoenix']
             }
            dictionary.append(name)
        except:
            name={'name':data[x]['name'],
            'role':'Unknown',
            'species':data[x]['species'],
            'bloodStatus':data[x]['bloodStatus'],
             'dumbledoresArmy':data[x]['dumbledoresArmy'],
             'deathEater':data[x]['deathEater'],
            'ministryOfMagic':data[x]['ministryOfMagic'],
            'orderOfThePhoenix':data[x]['orderOfThePhoenix']
             }
            dictionary.append(name)
    return dictionary 


def house_api_id (house,key):
        """Get the house _id from the potterapi, accepted values Gryffindor, Ravenclaw , Slytherin, Hufflepuff"""
        data = call_api('houses',key)
        list_houses=['Gryffindor','Ravenclaw','Slytherin','Hufflepuff']
        house_idx = list_houses.index(house)
        return (data[house_idx].get('_id'))


def get_house_info(house,key):
    """Create a Pandas DataFrame with the selected information received from the potterapi"""
    house_id = house_api_id(house,key)
    data = call_api(f'houses/{house_id}',key)
 
    dictionary=[]
    for x in range(0,len(data)):
        name={'name':data[x]['name'],
        'Mascot':data[x]['mascot'],
        'Head_Of_House':data[x]['headOfHouse'],
        'House_Ghost':data[x]['houseGhost'],
        'Founder':data[x]['founder'],
        'Values':data[x]['values'],
        'Colors':data[x]['colors']
        }
        dictionary.append(name)
        df = pd.DataFrame(dictionary)
    return df     