"""
- Raiz comum

a <= r <= b

- Distância 

a -> r
b -> r

- níveis



novel(no, a, 0):
    se no.chave == a, retprna valor_quero_achar
    senao
        se a < no.chave retorna
            nivel(no.esquerda, a, ++1)
        se a > no.chave retorna
            nivel(no.direita, a, ++1)
"""
