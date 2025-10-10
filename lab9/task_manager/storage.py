class InMemoryStorage:
    def __init__(self):
        self._data = {}
    def add(self, id, item):
        self._data[id] = item
    def get(self, id):
        return self._data.get(id)
    def get_all(self):
        return
    def delete(self, id):
        return
    def clear(self):
        return
    
"""
add(id, item): Adiciona item com chave id
• get(id): Retorna item ou None
• get_all(): Retorna lista com todos os valores
• delete(id): Remove item, retorna True/False
• clear(): Limpa tudo
"""
