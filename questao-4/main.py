import random
import time

def gerar_lista_isbns(tamanho=100000):
    return sorted(random.randint(1000000000000, 9999999999999) for _ in range(tamanho))


def busca_binaria(lista, isbn_procurado):
    inicio, fim = 0, len(lista) - 1
    iteracoes = 0
    
    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        
        if lista[meio] == isbn_procurado:
            return meio, iteracoes  
        
        if lista[meio] < isbn_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return -1, iteracoes  

def busca_linear(lista, isbn_procurado):
    iteracoes = 0
    
    for i, isbn in enumerate(lista):
        iteracoes += 1
        if isbn == isbn_procurado:
            return i, iteracoes  
    
    return -1, iteracoes 

if __name__ == "__main__":
    lista_isbns = gerar_lista_isbns()
    
    isbn_procurado = lista_isbns[random.randint(0, len(lista_isbns) - 1)]
    
    print(f"ISBN procurado: {isbn_procurado}")
    
    inicio_binaria = time.time()
    indice_binaria, iteracoes_binaria = busca_binaria(lista_isbns, isbn_procurado)
    fim_binaria = time.time()
    

    inicio_linear = time.time()
    indice_linear, iteracoes_linear = busca_linear(lista_isbns, isbn_procurado)
    fim_linear = time.time()
    
    print("\n--- Resultados ---")
    print(f"Busca Binária: Índice = {indice_binaria}, Iterações = {iteracoes_binaria}, Tempo = {fim_binaria - inicio_binaria:.6f} segundos")
    print(f"Busca Linear: Índice = {indice_linear}, Iterações = {iteracoes_linear}, Tempo = {fim_linear - inicio_linear:.6f} segundos")
