import aio_pika
import json
from rabbit_config import rabbit

class RabbitMQProducer:
    def __init__(self):
        self.connection = None
        self.channel = None

    async def connect(self):
        """
        Estabelece uma conexão assíncrona com o RabbitMQ.
        """
        self.connection = await aio_pika.connect_robust(
            f"amqp://{rabbit['User']}:{rabbit['Pass']}@{rabbit['Ip']}:{rabbit['Port']}/"
        )
        self.channel = await self.connection.channel()

    async def send_message(self, queue_name: str, message: dict):
        """
        Envia uma mensagem assíncrona para a fila especificada.
        
        :param queue_name: Nome da fila para onde a mensagem será enviada.
        :param message: Mensagem (como dicionário Python) a ser enviada.
        """
        if not self.channel:
            # Caso a conexão não esteja aberta, conecta ao RabbitMQ.
            await self.connect()

        # Serializa a mensagem para o formato JSON
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
        """
        Fecha a conexão assíncrona com o RabbitMQ.
        """
        if self.connection:
            await self.connection.close()

# Exemplo de uso:
async def main():
    producer = RabbitMQProducer()

    # Dados a serem enviados
    message = {
        "cnpj": "12345678000195",
        "razao_social": "Empresa XYZ LTDA"
    }

    # Envia a mensagem para a fila
    await producer.send_message("CRAWLER_CNPJ_SINTEGRA_GOIAS", message)

    # Fecha a conexão depois de enviar a mensagem
    await producer.close()

# Rodando o exemplo
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
