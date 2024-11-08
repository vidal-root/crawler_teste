import aio_pika
import asyncio
import json
import sys
from config.rabbit_config import rabbit
from controllers.sintegra_goias_controller import SintegraGoiasController

class RabbitMQConsumer:
    def __init__(self):
        self.queue_name = "CRAWLER_CNPJ_SINTEGRA_GOIAS"
        self.connection = None
        self.channel = None

    async def connect(self):
        # Conectar ao RabbitMQ
        self.connection = await aio_pika.connect_robust(
            f"amqp://{rabbit['User']}:{rabbit['Pass']}@{rabbit['Ip']}:{rabbit['Port']}/"
        )
        self.channel = await self.connection.channel()
        
        # Configurar o prefetch para uma mensagem de cada vez
        await self.channel.set_qos(prefetch_count=1)

    async def process_message(self, message):
        # Processa cada mensagem recebida
        async with message.process():
            
            msg = json.loads(message.body)
            
            sintegra_goias_controller = SintegraGoiasController()
            
            sintegra_goias_controller.scraping(msg)
            
            sys.stdout.flush()


    async def consume(self):
        # Declarar a fila para consumir as mensagens
        queue = await self.channel.declare_queue(self.queue_name, durable=True)
        
        # Inicia o consumo da fila
        async for message in queue:
            await self.process_message(message)

    async def run(self):
        # Conectar e iniciar o consumo
        await self.connect()
        await self.consume()

if __name__ == "__main__":
    consumer = RabbitMQConsumer()
    asyncio.run(consumer.run())
