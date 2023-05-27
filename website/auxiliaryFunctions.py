# Libraries and packages

#
def dogAge(currentYear: int, birthdayYear: int) -> str:
    age = currentYear - birthdayYear

    if age <= 2:
        return 'Cachorro'

    elif 2 < age <= 10:
        return 'Adulto'

    else:
        return 'Mayor'

# Website auxiliary functions
def dogKey(name, userId):
    import random
    Letters = name[0:2].upper()

    for letter in Letters:
        if letter not in "ABCDEFGHIJKLMNOPQRSTWUVXYZ":
            return "ERROR"

    key = str(userId) + Letters + str(random.randint(100, 999))

    return key

# Website calculator functions
def little_puppy_kcal(p):
    return round((0.66 * (p ** 0.75)) * 238.85, 2)

def big_puppy_kcal(p):
    return round((0.75 * (p ** 0.75)) * 238.85, 2) 

def adult_kcal(p):
    return round((0.52 * (p ** 0.75)) * 238.85, 2)

def old_kcal(p):
    return round((0.45 * (p ** 0.75)) * 238.85, 2)

def athletes_kcal(p):    
    return round((0.56 * (p ** 0.75)) * 238.85, 2)

def pregnant_kcal(p):
    return round(1.5 * adult_kcal(p), 2)

def laction_kcal(c, p):    
    if c >= 1 and c < 4:
        return round(1.5 * adult_kcal(p), 2)
    
    elif c >= 4 and c < 8:
        return round(2 * adult_kcal(p), 2)
    
    else:
        return round(3 * adult_kcal(p), 2)
 
def adult_protein(p):
    return round(5 * (p ** 0.72), 2)

def pregnant_protein(p):
    return round(1.5 * adult_protein(p), 2)
