import aio_pika
import asyncio
import json
import sys
from rabbit_config import rabbit

async def main():
    # Conectar ao RabbitMQ
    conn = await aio_pika.connect_robust(
        f"amqp://{rabbit['User']}:{rabbit['Pass']}@{rabbit['Ip']}:{rabbit['Port']}/"
    )

    async with conn:
        # canal de comunicação
        channel = await conn.channel()

        # Configurar o prefetch para uma mensagem de cada vez
        await channel.set_qos(prefetch_count=1)

        # fila onde as mensagens serão consumidas
        queue_name = "CRAWLER_CNPJ_SINTEGRA_GOIAS"
        queue = await channel.declare_queue(queue_name, durable=True)

        # processa a mensagem
        async for message in queue:
            async with message.process():
                data = json.loads(message.body)
                print(data)
                sys.stdout.flush()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
