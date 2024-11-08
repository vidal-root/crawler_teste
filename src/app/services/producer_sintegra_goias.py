import aio_pika
import json
from config.rabbit_config import rabbit

class RabbitMQProducer:
    def __init__(self):
        self.connection = None
        self.channel = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(
            f"amqp://{rabbit['User']}:{rabbit['Pass']}@{rabbit['Ip']}:{rabbit['Port']}/"
        )
        self.channel = await self.connection.channel()

    async def send_message(self, queue_name: str, message: dict):
        if not self.channel:
            await self.connect()

        # formato JSON
        message_body = json.dumps(message)

        # Declara a fila (se ela não existir)
        queue = await self.channel.declare_queue(queue_name, durable=True)

        # Publica a mensagem na fila
        await self.channel.default_exchange.publish(
            aio_pika.Message(body=message_body.encode()),
            routing_key=queue.name,
        )
        print(f"Mensagem enviada para a fila {queue_name}: {message_body}")

    async def close(self):
        if self.connection:
            await self.connection.close()


