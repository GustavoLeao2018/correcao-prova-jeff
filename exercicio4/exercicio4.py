class HashTable:
    def __init__(self):
        self.dados = []

    def hash(self, chave):
        return int(chave)
    
    def __put(self, int, chave, valor):
        self.dados.append({chave: valor})


"""
backup = dados
dados = novo_array(t * 2)

for elemento in backup:
    hash = hash(elemento.chave)
    __put(h % (t * 2), elemento.chave, elemento.valor)
"""