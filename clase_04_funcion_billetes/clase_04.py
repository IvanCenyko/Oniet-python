# cantidad es el vuelto, billetes es la lista de denominaciones
def vuelto(cantidad, billetes):
    
    vuelto = []
    #ordeno la lista de mayor a menor para hacer un vuelto con los billetes mas grandes posibles
    billetes.sort(reverse=True)

    #for para calcular el vuelto
    for b in billetes:
        #division sin coma para saber cuantos billetes de ese tipo entran en el vuelto
        cant_billetes = cantidad // b
        #multiplico la cantidad de billetes por su denominacion y resto al vuelto
        cantidad -= cant_billetes * b
        #apendo en una lista la cantidad de billetes que use de esa denominacion
        vuelto.append(cant_billetes)
        
        #si ya cubri todo el vuelto, rompo el for y termino la funcion
        if cantidad == 0:
            break
    
    #devuelvo la lista de billetes usados de cada denominacion
    return vuelto

print(vuelto(467, [100, 50, 20, 10, 1]))
