# Hechos iniciales
hechos = {'A': True, 'L': True} # A y L son los hechos iniciales

# Reglas
def R5(hechos):
    if hechos.get('Z', False) and hechos.get('L', False):
        return {'S': True}

def R1(hechos):
    if hechos.get('A', False) and hechos.get('N', False):
        return {'E': True}

def R3(hechos):
    if hechos.get('D', False) or hechos.get('M', False):
        return {'Z': True}

def R2(hechos):
    if hechos.get('A', False):
        return {'M': True}

def R4(hechos):
    if hechos.get('Q', False) and not hechos.get('W', False) and not hechos.get('Z', False):
        return {'N': True}

def R6(hechos):
    if hechos.get('L', False) and hechos.get('M', False):
        return {'E': True}

def R7(hechos):
    if hechos.get('B', False) and hechos.get('C', False):
        return {'Q': True}

reglas = [R5, R1, R3, R2, R4, R6, R7]

def forward_chaining(hechos, reglas):
    cambios = True
    while cambios:
        cambios = False
        conflict_set = []

        # Generación del Conflict Set
        for regla in reglas:
            nuevo_hecho = regla(hechos)
            if nuevo_hecho:
                conflict_set.append(nuevo_hecho)

        # Disparo de Reglas desde el Conflict Set
        for hecho in conflict_set:
            for clave, valor in hecho.items():
                if clave not in hechos or hechos[clave] != valor:
                    hechos[clave] = valor
                    print(f"Nuevo hecho inferido: {clave}: {valor}")
                    cambios = True

    return hechos

# Ejecución del motor de inferencia
hechos_inferidos = forward_chaining(hechos, reglas)
print("Hechos finales:", hechos_inferidos)
