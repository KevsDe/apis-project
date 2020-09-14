

def nameshrink(word):
    """This function grab a string and if it´s length is >1, return the first and last object of the string"""
    if len(word.split())==1:
        return word
    else:
        return ' '.join([word.split()[i] for i in (0, -1) ])