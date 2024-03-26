def exibir_produtos(produtos):
    for produto in produtos:
        print(f'''
    {produto["id"]} - nome:{produto["descrição"]}
    valor:{produto["valor"]} - estoque:{produto["estoque"]} - categoria:{produto["id_categoria"]}''')

def exibição(listas):
    for lista in listas:
        print(lista)

def novo_produto(produtos):
    id = len(produtos) +1
    descricao = input('Descrição do produto: ')
    valor = float(input('Valor do produto: '))
    estoque = int(input('Quantidade em estoque: '))
    id_categoria = int(input('id da categoria do produto: '))
    produto = {"id": id, "descrição": descricao, "valor": valor, "estoque": estoque, "id_categoria": id_categoria}
    produtos.append(produto)
    exibição(produtos)
    print('cliente adicionado com sucesso.')

def nova_categoria(categorias):
    id = len(categorias) +1
    nome = input('Digite o nome da nova categoria: ')
    categoria = {"id": id, "nome": nome}
    categorias.append(categoria)
    exibição(categorias)
    print('cliente adicionado com sucesso.')

def del_produto(produtos):
    id = int(input('Id do produto a ser apagado: ')) -1
    for produto in produtos:
        if produto["id"] == id:
            del produtos[id]
    exibição(produtos)

def atualizar_produto(produtos):
    id = int(input('Digite id do produto: '))
    descricao = input('Nova descrição: ')
    valor = float(input('novo valor: '))
    estoque = int(input('Quantidade em estoque: '))
    id_categoria = int(input('Id da categoria: '))
    for produto in produtos:
        if produto["id"] == id:
                produto["descrição"] = descricao
                produto["valor"] = valor
                produto["estoque"] = estoque
                produto["id_categoria"] = id_categoria
    exibição(produtos)

def atualizar_categoria(categorias):
    id = int(input('Digite id da categoria: '))
    nome = input('nome da categoria: ')
    for categoria in categorias:
        if categoria["id"] == id:
                categoria["nome"] = nome
    exibição(categorias)

def trocar_categoria(produtos):
    id = int(input('Digite id do produto: '))
    categori = int(input('Id da nova categoria: '))
    for produto in produtos:
        if produto["id"] == id:
                produto["nome"] = categori
    exibição(produtos)

def produto_categoria(produtos):
    id = int(input('Id da categoria: '))
    for produto in produtos:
        if produto["id_categoria"] == id:
            print(produto)            

def exibir_categorias(categorias):
    for categoria in categorias:
        print(f'ID:{categoria["id"]} - {categoria["nome"]}')