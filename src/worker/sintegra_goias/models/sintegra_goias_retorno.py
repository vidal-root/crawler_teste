import json

class SintegraGoiasRetorno:

    def __init__(self, html_site):
        self.html_site = html_site

    def tratar_dados(self):
        
        retorno_formatado = {}

        retorno_formatado['cnpj'] = self.getLabelText('CNPJ')    

        retorno_formatado['inscricao_estadual'] = self.getLabelText('Inscrição Estadual')

        retorno_formatado['cadastro_atualizado_em'] = self.getLabelText('Cadastro Atualizado em')

        retorno_formatado['nome_empresarial'] = self.getLabelText('Nome Empresarial')

        retorno_formatado['contribuinte'] = self.getLabelText('Contribuinte?')

        retorno_formatado['nome_propriedade'] =  self.getLabelText('Nome da Propriedade:')
        
        retorno_formatado['nome_fantasia'] =  self.getLabelText('Nome Fantasia')
               
        retorno_formatado['endereco_estabelecimento'] =  self.getLabelText('Endereço Estabelecimento ', 'div')
           
        retorno_formatado['informacoes_complementares'] = {
            "unidade_auxiliar": self.getLabelText('Unidade Auxiliar:'),
            "condicao_uso": self.getLabelText('Condição de Uso:'),
            "data_final_contrato": self.getLabelText('Data Final de Contrato:'),
            "regime_apuracao": self.getLabelText('Regime de Apuração:'),
            "situacao_cadastral_vigente": self.getLabelText('Situação Cadastral Vigente:'),
            "data_desta_situacao_cadastral": self.getLabelText('Data desta Situação Cadastral:'),
            "data_cadastramento": self.getLabelText('Data de Cadastramento:'),
            "operacao_nfe": self.getLabelText('Operações com NF-E:'),
        }

        return retorno_formatado
    
    # O site segue um padrao simples, logo da para facilitar a busca dos label_text
    def getLabelText(self, nm_busca, html_busca='span'):
        dado = self.html_site.find(html_busca, text=nm_busca)
        if dado:
            dado_text = dado.find_next('span', class_='label_text')
            if dado_text:
                return dado_text.text.strip()
        
        return ""


    def to_json(self):
        return json.dumps(self.tratar_dados(), indent=4)

