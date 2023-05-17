# Libraries and packages

# Website auxiliary functions
def dogKey(nomMas,clavUser):
    import random
    Mas = nomMas[0:2]
    for x in Mas:
        if x not in "ABCDEFGHIJKLMNOPQRSTWUVXYZ":
            return "ERROR"
    claveMas = str(clavUser) + Mas + str(random.randint(100,999))
    return claveMas

def calculator():
    pass