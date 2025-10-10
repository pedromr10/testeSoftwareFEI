'''
Funcionalidades obrigatórias:
1 - Criar tarefas ( tem de ter título, descrição, prioridade, prazo);
2 - Listar todas as tarefas;
3 - Buscar tarefas por ID - index da lista;
4 - Atualizar status da arefa;
5 - Deletar tarefas.
'''

from enum import IntEnum
class Priority(IntEnum):
  BAIXA = 1
  MEDIA = 2
  ALTA = 3

class Status(Enum):
  PENDENTE = "pendente"
  EM_PROGRESSO = "em_progresso"
  CONCLUIDA = "concluida"

class Atributes():
  id = 1
  titulo = ""
  descricao = ""
  prioridade = Priority
  prazo = 
  status: Status (padrão: PENDENTE)
