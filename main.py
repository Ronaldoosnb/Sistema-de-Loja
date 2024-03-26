from lib.funcoes import exibir_produtos, novo_produto, del_produto, atualizar_categoria, atualizar_produto, trocar_categoria, nova_categoria, produto_categoria, exibir_categorias
from database import produtos, categorias

while True:
    print('''
        1 - cadastrar produto ---
        2 - consultar produtos ---
        3 - apagar produto ---
        4 - atualizar produto ---
        5 - trocar produto de categoria ---
        6 - cadastrar categoria ---
        7 - atualizar categoria---
        8 - consultar categorias ---
        9 - produtos por categorias   
        ''')
    option = int(input('Qual seção deseja acessar: '))
    if option == 1:
        novo_produto(produtos)
    elif option == 2:
        exibir_produtos(produtos)
    elif option == 3:
        del_produto(produtos)
    elif option == 4:
        atualizar_produto(produtos)
    elif option == 5:
        trocar_categoria(produtos)
    elif option == 6:
        nova_categoria(categorias)
    elif option == 7:
        atualizar_categoria(categorias)
    elif option == 8:
        exibir_categorias(categorias)
    elif option == 9:
        produto_categoria(produtos)
    else:
        print('Erro!Digite uma opção válida')
