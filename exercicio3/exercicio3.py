"""

is_valid(no):
    valida_bst(no, -infinito, +infinito)

# infinito = float("inf")

def valida_bst(no, minimo, maximo):
    if no is None: return True
    if min <= no.chave <= max: 
        return   valida_bsd(no.esquerda, min, no.chave) and
                 valida_bsd(no.direita, no.chave, max)
    return False
"""