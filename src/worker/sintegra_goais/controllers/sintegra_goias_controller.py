import json
import requests
import logging
from bs4 import BeautifulSoup
from worker.sintegra_goais.models.sintegra_goias_retorno import SintegraGoiasRetorno
from services.redis_service import RedisService

class SintegraGoiasController:

    def __init__(self):
        self.url = 'http://appasp.sefaz.go.gov.br/Sintegra/Consulta/consultar.asp'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://appasp.sefaz.go.gov.br',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://appasp.sefaz.go.gov.br/Sintegra/Consulta/default.html',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
        }
    
    def scraping(self):
        payload = {
            "rTipoDoc": "2",
            "tDoc": "00.006.486/0001-75",
            "tCCE": "",
            "tCNPJ": "00.006.486/0001-75",
            "tCPF": "",
            "btCGC": "Consultar",
            "zion.SystemAction": "consultarSintegra()",
            "zion.OnSubmited": "",
            "zion.FormElementPosted": "zionFormID_1",
            "zionPostMethod": "",
            "zionRichValidator": "true"
        }

        response = requests.request("POST", self.url, headers=self.headers, data=payload)

        if response.status_code == 200:
            
            html_site = BeautifulSoup(response.text, 'html.parser')

            sintegra_retorno = SintegraGoiasRetorno(html_site)
            
            cache = RedisService()
            
            cache.set('cnpj00006486000175', sintegra_retorno.to_json());
            
            cache.close()
            

app = SintegraGoiasController()
app.scraping()