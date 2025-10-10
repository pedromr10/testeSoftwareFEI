'''
Funcionalidades obrigatórias:
1 - Criar tarefas ( tem de ter título, descrição, prioridade, prazo);
2 - Listar todas as tarefas;
3 - Buscar tarefas por ID - index da lista;
4 - Atualizar status da arefa;
5 - Deletar tarefas.
'''
from datetime import datetime
from enum import IntEnum, Enum

class Priority(IntEnum):
  def __init__(self):
    self._BAIXA = 1
    self._MEDIA = 2
    self._ALTA = 3

class Status(Enum):
  def __init__(self):
    self._PENDENTE = "pendente"
    self._EM_PROGRESSO = "em_progresso"
    self._CONCLUIDA = "concluida"

class Atributes():
  def __init__(self):
    self._id = 1
    self._titulo = ""
    self._descricao = ""
    self._prioridade = Priority
    self._prazo = datetime.now()
    self._status = Status


def criar_tarefa():
  return 
def listar_tarefas():
  return
def buscar_tarefas():
  return
def atualizar_tarefas():
  return
def deletar_tarefas():
  return
def sair():
  return

def menu():
  print("1 - Criar tarefa\n2 - Listar tarefas\n3 - Buscar tarefas\n4 - Atualizar tarefas\n5 - Deletar tarefas\n\n0 - Sair\n")
  esc = int(input("Insira o número referente a sua escolha: "))
  
  if esc == 1:
    criar_tarefa()
  elif esc == 2:
    listar_tarefas()
  elif esc == 3:
    buscar_tarefas()
  elif esc == 4:
    atualizar_tarefas()
  elif esc == 5:
    deletar_tarefas()
  elif esc == 0:
    sair()
  else:
    menu()
