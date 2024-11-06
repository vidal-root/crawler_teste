import json

class SintegraGoiasRetorno:

    def __init__(self, html_site):
        self.html_site = html_site

    def tratar_dados(self):
        label_texts = self.html_site.find_all('span', class_='label_text')
    
        retorno_formatado = {
            "cnpj": label_texts[0].text.strip(),
            "inscricao_estadual": label_texts[1].text.strip(),
            "ultima_atualizacao": label_texts[2].text.strip(),
            "nome_empresarial": label_texts[3].text.strip(),
            "contribuinte": label_texts[4].text.strip(),
            "nome_fantasia": label_texts[5].text.strip(),
            "endereco": label_texts[6].text.strip(),
            "atividade_principal": label_texts[8].text.strip(),
            "informacoes_complementares": {
                "unidade_auxiliar": label_texts[9].text.strip(),
                "condicao_uso": label_texts[10].text.strip(),
                "data_final_contrato": label_texts[11].text.strip(),
                "regime_apuracao": label_texts[12].text.strip(),
                "situacao_cadastral_vigente": label_texts[13].text.strip(),
                "data_situacao_cadastral": label_texts[14].text.strip(),
                "data_cadastramento": label_texts[15].text.strip(),
                "operacao_nfe": label_texts[16].text.strip(),
            }
        }

        return retorno_formatado

    def to_json(self):
        return json.dumps(self.tratar_dados(), indent=4)

