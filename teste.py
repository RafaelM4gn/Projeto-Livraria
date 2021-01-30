from livro import Livro
import main
"""
     * create_table(self, table_name = self.table_name) 
     ! read_table(self)
     * update_book(self, specified_column, new_value, id_livro)
     * delete_book(self, id_livro)
     * insert_book(self, livro)
"""


def register_book():
    print('Cadastre um livro: ')
    id = int(input('id: '))
    nome = input('nome: ')
    autor = input('autor: ')
    editora = input('editora: ')
    proprietario = input('proprietario: ')

    return Livro(id, nome, autor, editora, proprietario)


banco = main.DbLivros()
#banco.create_table("livros")
livro = register_book()
banco.insert_book(livro)
# banco.delete_book(2)
#banco.update_book("editora", "Secker & Warburg", 2)
banco.read_table()