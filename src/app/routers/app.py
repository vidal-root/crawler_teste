from typing import Union
from fastapi import FastAPI, Request

from controllers.sintegra_scraper_controller import SintegraScraperController

app = FastAPI()

@app.get("/")
def home():
    return {"Teste": "Desafio Técnico"}

@app.post("/scrape")
async def scrape(request: Request):
    # Aguardando para obter o corpo da requisição como JSON (assíncrono)
    body = await request.json()  # Usando 'await' para resolver o corpo da requisição
    
    # Passando o corpo para o controller (por exemplo, você poderia passar um campo específico)
    response = SintegraScraperController().inserir_fila(body)
    
    return response

@app.get("/results/{task_id}")
def results(task_id: str, q: Union[str, None] = None):
    return {"task_id": task_id, "q": q}