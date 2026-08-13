import csv
ARQUIVO = "livros.csv"

#isso é para carregar os livros salvos
def cadastrar_livros(titulo, autor, ano, codigo, status = "disponivel"):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "codigo": codigo,
        "status":status
        }
    cabecacho = ["titulo", "autor", "ano", "codigo", "status"]
    with open('livros.csv','a',encoding='UTF-8',newline='') as biblioteca:
        escritor = csv.DictWriter(biblioteca,fieldnames=cabecacho)
        escritor.writerow(livro)
