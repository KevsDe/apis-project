
import requests  #Si no llamaba aquí a requests no funcionaba la función, decía que no estaba definida

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