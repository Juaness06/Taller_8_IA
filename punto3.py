# Hechos iniciales
hechos = {'the sun is behind the clouds': True, 'air is very heavy and cool': True}


# Reglas
def R1(hechos):
    if hechos.get('temperature is les than 20*', True) and hechos.get('there is humidity on the air', True):
        return {'there are chances of rain': True}

def R2(hechos):
    if hechos.get('the sun id behind the clouds', False) and hechos.get('air is very heavy and cool', True):
        return {'the temperature is less than 20*': True}

def R3(hechos):
    if hechos.get('air is heavy', False):
        return {'there is humidity on the air': True}


reglas = [R1, R2, R3]


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