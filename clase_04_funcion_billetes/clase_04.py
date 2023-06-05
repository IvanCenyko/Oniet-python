def vuelto(cantidad, billetes):
    
    vuelto = []
    billetes.sort(reverse=True)

    for b in billetes:
        cant_billetes = cantidad // b
        cantidad -= cant_billetes * b
        vuelto.append(cant_billetes)
        
        if cantidad == 0:
            break
    
    return vuelto

print(vuelto(467, [100, 50, 20, 10, 1]))
