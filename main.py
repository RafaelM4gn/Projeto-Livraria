import sqlite3
import pandas as pd
from livro import Livro



class DbLivros:
    """data base methods"""
    data_base = sqlite3.connect("livros.db")

    cursor = data_base.cursor()

    table_name = "livros"

    def __init__(self):
        return

    def create_table(self,):
        """Create a table in database.""" 
        self.cursor.execute(f"CREATE TABLE {self.table_name} (id INTEGER NOT NULL, nome TEXT NOT NULL, autor TEXT NOT NULL,\
                            editora TEXT NOT NULL, proprietario TEXT NOT NULL)")

    def read_table(self):
        """show the first five elements of the table."""
        
        temp = pd.read_sql_table(self.table_name)
        print(temp.head())

    def update_book(self, specified_column, new_value, id_livro ) :
        """update a value in row by ID

        Args:
            specified_column (string): element that will be updated
            new_value (string || int): new value of elements's columns
            id_livro (int): book's ID
        """
        self.cursor.execute(
            f"UPDATE {self.table_name} SET {specified_column} = {new_value} WHERE id = {id_livro} ")

    def delete_book(self, id_livro):
        """delete a row in a table by ID

        Args:
            id_livro (int): table's ID
        """
        self.cursor.execute(f"")

    def insert_book(self, livro):
        """add a new book in table

        Args:
            livro (livro): book object
        """
        self.cursor.execute(f"INSERT INTO {self.table_name} VALUES ('{livro.id}', '{livro.nome}', '{livro.autor}',\
                            '{livro.editora}', '{livro.proprietario}')")

