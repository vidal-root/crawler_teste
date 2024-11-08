from fastapi.testclient import TestClient
from routers.app import app

#Teste de requisicao para rotas

client = TestClient(app)

def teste_home():
    # testa a rota de home
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Teste": "Desafio Técnico"}

def teste_scrape_cnpj_valido():
    # testa a rota com requisição válido
    body = {"cnpj": "12345678000195"} 
    response = client.post("/scrape", json=body)
    assert response.status_code == 200
    assert "task_id" in response.json()

def teste_scrape_cnpj_invalido():
    # testa a rota com CNPJ incorreto
    body = {"cnpj": "12345"}
    response = client.post("/scrape", json=body)
    assert response.status_code == 200
    assert "CNPJ deve ter 14 dígitos" in response.json()['content']['msg']
    
def teste_resultados_task():
    # testa a rota com um task_id fictício
    task_id = "1b84980b37370d59_20241108034959"
    response = client.get(f"/results/{task_id}")
    assert response.status_code == 200
    assert "sucesso" in response.json()

