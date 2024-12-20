import secrets
import json
import re

from datetime import datetime
from models.response_api_model import ResponseApiModel
from services.producer_sintegra_goias import RabbitMQProducer
from services.redis_service import RedisService

class SintegraScraperController:
    
    async def criar_task(self, body):
        cnpj = body.get("cnpj", None)
        
        #validacoes basicas
        if not cnpj:
            return ResponseApiModel("", {"msg": "CNPJ é obrigatório"}, 'NAO').send()
    
        cnpj = re.sub(r'\D', '', cnpj)
    
        if len(cnpj) != 14:
            return ResponseApiModel("", {"msg": "CNPJ deve ter 14 dígitos"}, 'NAO').send()
        
        task_id = self.gera_task_id()
        
        try:
            
            # enviando mensagem para fila
            producer = RabbitMQProducer()
            
            await producer.send_message(
                "CRAWLER_CNPJ_SINTEGRA_GOIAS",
                {"task_id": task_id, "cnpj": cnpj}
            )
            
            await producer.close()
            
            # salva no redis
            cache = RedisService()
            
            cache.set(task_id, json.dumps({"status_task": "em_andamento", "dados_processados": {}}));
            
            cache.close()
            
            return ResponseApiModel(task_id, {"status_task": "em_andamento", "dados_processados": {}}).send()
        
        except Exception as e:
            return ResponseApiModel("", {"msg": "Ocorreu um erro inesperado"}, 'NAO').send()
    
    def get_task(self, task_id):
        
        if task_id:
    
            #pega informacao do redis
            cache = RedisService()
                
            task = cache.get(task_id);
                
            cache.close()
            
            if task:
                return ResponseApiModel(task_id, json.loads(task)).send()
        
        return ResponseApiModel("", {"msg": "Task não encontrada ou inválida"}, 'NAO').send()
    
    def gera_task_id(self):
        random_code = secrets.token_hex(8) 
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        task_id = f"{random_code}_{timestamp}"
        return task_id