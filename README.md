## Estrutura do PROJETO

Projeto referente ao Desafio Técnico - Squad "Melhorias Estruturantes". O projeto possui uma API em python, há uma rota que cria uma Tarefa, e realiza o envio de um cnpj para uma fila no RabbitMQ e devolve um ID da Tarefa. O Worker/Consumer fica escutando essa fila, ao receber uma mensagem, processa a mesma realizando um scraping e salvando a informacao no Redis atualizando o status da tarefa. Com outra rota da API é possivel pegar os dados processados.

## O FUNCIONAMENTO

O projeto utiliza 4 contêineres, são eles:

1. `rabbitmq`: Container que possui o RabbitMQ para o uso de mensageria.
2. `worker`: Container responsavel pelo "Consumidor" da estrutura de mensageria.
    - Obs: Utilizado o supervisor para subir os consumidores e numero de processo
3. `api`: Container da API, responsavel pelas rotas.
4. `redis`: Conatiner responsavel pelo sistema de cache usando REDIS.

## Iniciando o Projeto via CONTAINER

Para iniciar o projeto via contêiner, siga os passos:

1. Clone do Projeto
```sh
git clone https://github.com/vidal-root/crawler_teste.git
```
2. Entre na pasta do Projeto
```sh
cd crawler_teste/
```
3. Para iniciar
```sh
docker-compose up
```
- Obs: aguarde todos os containers subir
5. Verificar os containes
```sh
docker-compose ps
```

## Acessos e Rotas
- Acessar interface web RabbitMQ: `http://localhost:15672/` ou `http://{IPVM}:15672/` (caso tenha)
- Acessar Redis-Cli: `docker exec -it redis redis-cli`
- Rota /scrape: `http://localhost:8000/scrape`
```sh
{
    "cnpj": "00012377000160"
}
```
- Curl importar
```sh
curl --location --request POST 'http://10.13.13.236:8000/scrape' \
--header 'Content-Type: application/json' \
--data-raw '{
    "cnpj": "00012377000160"
}'
```
- Rota /results/{task_id}: `http://localhost:8000/results/{task_id}`
- Rodar o teste de API: `docker exec -it api pytest`

## Observações
Adicionei o supervisor para subir o consumidor, assim nao preciso chamar direto o arquivo ou adiconar um cron por exemplo e tenho mais logs, consigo também setar facilmente o numero de consumidor (No projeto em questão esta com 2 consumidores).
Existem alguns arquivos "duplicados", mas fiz isso considerando que são projetos separados.

Comandos docker-compose:
docker-compose build: Realiza o apenas a etapa Build das imagens que serão usadas nos containers
docker-compose start: Inicia os containers
docker-compose stop: Para os containers
docker-compose restart: Reinicia os containers
docker-compose ps: Lista os containers
docker-compose up: Cria e inicia os containers
docker-compose down: Para e remove os containers
docker-compose logs: Mostra o logs do containers
docker-compose scale: Define o números de réplicas de um container