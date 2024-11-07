#class responsavel para padronizar o retorno de resposta
class ResponseApiModel:
    def __init__(self, task_id='', content=[], sucesso='SIM'):
        self.sucesso = sucesso
        self.task_id = task_id
        self.content = content
        
    def send(self):
        
        retorno = {
            "sucesso": self.sucesso,
            "task_id": self.task_id,
            "content": self.content
        }
        
        return retorno