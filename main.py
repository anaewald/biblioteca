import csv
import os
ARQUIVO = "livros.csv"

#isso é para cadastrar os livros 
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

#carregar os livros salvos
def carregar_livros():
    livros = []
    cabecacho = ["titulo", "autor", "ano", "codigo", "status"]
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='UTF-8', newline='') as biblioteca:
            leitor = csv.DictReader(biblioteca, fieldnames=cabecacho)
            for linha in leitor:
                livros.append(linha)
    return livros

#isso e para mostrar os livros cadastrados
def salvar_todos(livros):
    cabecacho = ["titulo", "autor", "ano", "codigo", "status"]
    with open(ARQUIVO, 'w', encoding='UTF-8', newline='') as biblioteca:
        escritor = csv.DictWriter(biblioteca, fieldnames=cabecacho)
        escritor.writerows(livros)

#isso e para empresstar os livros cadastrados
def emprestar_livro(livros, codigo):
    for livro in livros:
        if livro["codigo"] == codigo and livro["status"] == "disponivel":
            livro["status"] = "emprestado"
            salvar_todos(livros)
            return True
    return False

#isso e para devolver os livros cadastrados
def devolver_livro(livros, codigo):
    for livro in livros:
        if livro["codigo"] == codigo and livro["status"] == "emprestado":
            livro["status"] = "disponivel"
            salvar_todos(livros)
            return True
    return False

#isso e para mostrar os livros cadastrados 
def listar_livros(livros):
    if not livros:
        print("Nenhum livro encontrado.")
        return
    for livro in livros:
        print(f"[{livro['codigo']}] {livro['titulo']} - {livro['autor']} "
              f"({livro['ano']}) - Status: {livro['status']}")

#isso é para buscar os livros
def buscar_livro(livros, termo):
    termo = termo.lower()
    resultado = []
    for livro in livros:
        if termo in livro["titulo"].lower() or termo in livro["autor"].lower():
            resultado.append(livro)
    return resultado

#isso é para mostrar os livros em ordem
def pegar_valor_ordenacao(livro):
    if criterio_atual == "ano":
        return int(livro["ano"])
    return livro[criterio_atual].lower()

def ordenar_livros(livros, criterio):
    global criterio_atual
    criterio_atual = criterio
    return sorted(livros, key=pegar_valor_ordenacao)

#esse é o menu principal

livros = carregar_livros()  #isso e pra carrega o catalogo salvo assim que o programa abre

ativo = True
while ativo:
    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar listagem")
    print("7 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o titulo: ")
        autor = input("Digite o autor: ")
        ano = input("Digite o ano: ")
        codigo = input("Digite o codigo: ")
        cadastrar_livros(titulo, autor, ano, codigo)
        livros = carregar_livros()  
        print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        codigo = input("Digite o codigo do livro a emprestar: ")
        if emprestar_livro(livros, codigo):
            print("Empréstimo registrado!")
        else:
            print("Não foi possível emprestar (livro não existe ou já está emprestado).")

    elif opcao == "3":
        codigo = input("Digite o codigo do livro a devolver: ")
        if devolver_livro(livros, codigo):
            print("Devolução registrada!")
        else:
            print("Não foi possível devolver (livro não existe ou já está disponível).")

    elif opcao == "4":
        listar_livros(livros)

    elif opcao == "5":
        termo = input("Digite o titulo ou autor para buscar: ")
        listar_livros(buscar_livro(livros, termo))

    elif opcao == "6":
        criterio = input("Ordenar por (titulo/autor/ano): ").lower()
        if criterio in ("titulo", "autor", "ano"):
            listar_livros(ordenar_livros(livros, criterio))
        else:
            print("Critério inválido.")

    elif opcao == "7":
        print("Saindo... até mais!")
        ativo = False

    else:
        print("Opção inválida, tente novamente.")