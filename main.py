# importando modulos das classes Menu, Sistema, GerenciadorDeTarefas e RepositorioDeTarefas
from gerenciador import GerenciadorDeTarefas
from menu import Menu
from repositorio import RepositorioDeTarefas
from sistema import Sistema


# criando funcao principal do programa para instaciar os objetos
def mian():

    # Instancia para armazenar nossos dados
    repositorio = RepositorioDeTarefas()
    # O gerenciador recebe repositorio para salvar tarefas listadas
    gerenciador = GerenciadorDeTarefas(repositorio)
    # Instancia responsavel pela interacao com o usuario
    menu = Menu()
    # Instancia maestra que recebera os argumentos do usuario e aplica a regra de negocio
    sistema = Sistema(menu, gerenciador)

    sistema.iniciar()
