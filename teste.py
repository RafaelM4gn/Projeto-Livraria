from livro import Livro
import main


banco = main.DbLivros()
#banco.create_table()

banco.read_table()


"""while True:
    print('Cadastre um livro: ')
    id = int(input('id: '))
    nome = input('nome: ')
    autor = input('autor: ')
    editora = input('editora: ')
    proprietario = input('proprietario: ')

    livro = Livro(id, nome, autor, editora, proprietario)

    banco.insert_book(livro)

    break"""

'''print('O que você deseja fazer?\n1) Adicionar um novo livro\n2) Atualizar um livro\n3) Deletar um livro')

    desejo = int(input('Desejo: '))

    if desejo == 1:
        
    elif desejo == 2:
        pass
    elif desejo == 3:
        pass
    else:
        print('Opção inválida!')'''
