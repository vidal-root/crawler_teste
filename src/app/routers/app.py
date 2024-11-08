from typing import Union
from fastapi import FastAPI, Request

from controllers.sintegra_scraper_controller import SintegraScraperController

app = FastAPI()

@app.get("/")
def home():
    return {"Teste": "Desafio Técnico"}

@app.post("/scrape")
async def scrape(request: Request):

    body = await request.json()
    
    response = await SintegraScraperController().inserir_fila(body)
    
    return response

@app.get("/results/{task_id}")
def results_task(task_id: str):
    
    response = SintegraScraperController().get_task(task_id)
    
    return response