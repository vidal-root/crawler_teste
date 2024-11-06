import redis
import logging

class RedisService:
    def __init__(self, host='10.13.13.236', port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.redis_client = None
        self.connect()

    def connect(self):
        try:
            self.redis_client = redis.Redis(host=self.host, port=self.port, db=self.db)
            self.redis_client.ping()
            logging.info(f"Conectado ao Redis em {self.host}:{self.port}")
        except Exception as e:
            logging.error(f"Erro ao conectar no Redis: {str(e)}")

    def get(self, key):
        try:
            return self.redis_client.get(key)
        except Exception as e:
            logging.error(f"Erro ao obter a chave {key}: {str(e)}")
            return None

    #padrao para expirar em 24 horas
    def set(self, key, value, expires_in=86400):
        try:
            self.redis_client.setex(key, expires_in, value)
        except Exception as e:
            logging.error(f"Erro ao definir a chave {key} com valor {value}: {str(e)}")

    def close(self):
        if self.redis_client:
            self.redis_client.close()
            logging.info("Conexão com Redis fechada.")
