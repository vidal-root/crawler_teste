
from models.response_api_model import ResponseApiModel

class SintegraScraperController:
    
    def inserir_fila(self, body):
        
        cnpj = body.get("cnpj", None)
        
        if not cnpj:
            return ResponseApiModel('7289789273728', {"message": "CNPJ é obrigatório"}, 'NAO').send()
    
        if len(cnpj) != 14 or not cnpj.isdigit():
            return ResponseApiModel('7289789273728', {"message": "CNPJ deve ter 14 dígitos e ser numérico"}, 'NAO').send()
        
        return ResponseApiModel('7289789273728', {"cnpj": cnpj}).send()
    
    def get_task(self):
        pass