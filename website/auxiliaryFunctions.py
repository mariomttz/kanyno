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

#!/usr/bin/env python
# coding: utf-8

# ---

# # Demanda de conservación de energía 
# 
# Unidad de medida Kcal

# ## Cachorros

# ${DCEC} = ({v} * {kg} ^ {0.75}) * 238.85$
# 
# - DCEPA = Demanda de conservación de energía en Cachorros(en kcal)
# - kg = Peso del perro
# - v = [0.66, 0.75] depende de la raza del cachorro (pequeña o grande)



def little_puppy_kcal(p):
    
    return ((0.66 * (p**0.75))* 238.85, 2)




def big_puppy_kcal(p):
    
    return ((0.75 * (p**0.75))* 238.85, 2) 


# > - p = peso en kg

# ## Perros adultos

# ${DCEPA} = ({0.52} * {kg} ^ {0,75}) * 238.85$
# 
# - DCEPA = Demanda de conservación de energía en perros adultos(en kcal)
# - kg = Peso del perro




def adult_kcal(p):
    
    return round((0.52 * (p**0.75))* 238.85, 2)


# > - p = peso en kg

# ## Perros mayores

# ${DCEPM} = ({0.45} * {kg} ^ {0.75}) * 238.85$
# 
# - DCEPA = Demanda de conservación de energía en Perros Mayores(en kcal)
# - kg = Peso del perro




def old_kcal(p):
    
    return round((0.45 * (p**0.75))* 238.85, 2)


# > - p = peso en kg

# ## Perros Deportistas

# ${DCEPD} = ({0.52} * {kg} ^ {0,75}) * 238.85$
# 
# - DCEPA = Demanda de conservación de energía en perros deportistas(en kcal)
# - kg = Peso del perro



def athletes_kcal(p):
    
    return round((0.56 * (p**0.75))* 238.85, 2)


# > - p = peso en kg

# ## Perras embarazadas

# ${DCEPE} = {1.5}*{𝐷𝐶𝐸𝑃𝐴}$
# 
# - DCEPE = Demanda de conservación de energía para perras embarazadas(en kcal)
# - DCEPA = Demanda de conservación de energía en perros adultos(en kcal)



def pregnant_kcal(p):
    
    return round(1.5 * adult_kcal(p), 2)


# > - p = peso en kg

# ## Perras lactantes

# | No. de Cahorros | No. de Demandas energéticas |
# | --- | --- |
# | 1 | 1.5 | 
# | 4 | 2 |
# | 8 | 3 |

# ---



def laction_kcal(c, p):
    
    if c >= 1 and c < 4:
        
        return round(1.5 * adult_kcal(p), 2)
    
    elif c >= 4 and c < 8:
        
        return round(2 * adult_kcal(p), 2)
    
    else:
        
        return round(3 * adult_kcal(p), 2)
 


# > - p = peso en kg
# > - c = número de cachorros

# ---

# ---

# # Demanda de proteínas 
# 
# Unidad de medida gr

# ## Perros adultos

# ${DPPA} = {5} ({kg} ^ {0,75})$
# 
# - DPPA = Demanda de proteínas de los perros adultos(en gr)
# - kg = Peso del perro
# 
# Para perros deportistas y perras lactando no aumenta mucho la demanda de proteína



def adult_protein(p):
    
    return round(5*(p**0.72), 2)


# > - p = peso en kg

# ---

# ## Perras embarazadas

# ${DPPE} = {1.5}*{DPPA}$
# 
# - DPPE = Demanda de proteínas para perras embarazadas (en gr)
# - DPPA = Demanda de proteínas de los perros adultos(en gr)




def pregnant_protein(p):
    
    return round(1.5 * adult_protein(p), 2)


# > - p = peso en kg
