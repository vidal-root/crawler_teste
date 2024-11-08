import json
import requests
import logging
import sys
from bs4 import BeautifulSoup
from sintegra_goias.models.sintegra_goias_retorno import SintegraGoiasRetorno
from sintegra_goias.services.redis_service import RedisService

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
    
    def scraping(self, msg):
        
        payload = {
            "rTipoDoc": "2",
            "tDoc": msg['cnpj'],
            "tCCE": "",
            "tCNPJ": msg['cnpj'],
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

            # chama class de retrono para tratar o html
            sintegra_retorno = SintegraGoiasRetorno(html_site)
            
            cache = RedisService()
            
            cache.set(msg['task_id'], sintegra_retorno.to_json());
            
            cache.close()