contatos = [
    {"nome": "Joquin", "telefone": "55666224"},
    {"nome": "Helena", "telefone": "522658941"},
    {"nome": "Carol", "telefone": "55698412"},
    {"nome": "Amon", "telefone": "6698433"},
]

def buscar_contato(nome_procurado, lista_contatos):
    for contato in lista_contatos:
        if contato["nome"] == nome_procurado:
            return f"Contato encontrado: {contato['nome']}, Telefone: {contato['telefone']}"
    return "Contato não encontrado."

nome_para_buscar = "Amon"
resultado = buscar_contato(nome_para_buscar, contatos)

print(resultado)
