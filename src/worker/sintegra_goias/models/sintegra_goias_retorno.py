import json
import re

#class para tratar o html
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
        
        retorno_formatado['atividade_principal'] =  self.getAtividadePrincipal()
        
        retorno_formatado['atividade_secundaria'] =  self.getAtividadesSecundarias()
           
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
    
    #funcionamento para pegar os cnes é diferente
    def getAtividadePrincipal(self):
        dado = self.html_site.find('strong', string="Atividade Principal")
        if dado:
            dado_text = dado.find_parent().find_next_sibling('span', class_='label_text')
            if dado_text:
                return dado_text.text.strip()
        
        return ""
    
    def getAtividadesSecundarias(self):
        atividade_secundaria = self.html_site.find('strong', string="Atividade Secundária")
        if atividade_secundaria:
            # encontrar o próximo irmao que contém os CNAEs
            atividades_secundarias = []
            for span in atividade_secundaria.find_parent().find_all_next('span', class_='label_text'):
                # apenas as linhas que contem numero CNAE
                cnae_text = span.text.strip()
                if re.match(r'^\d{7} -', cnae_text):  # verifica se é um CNAE
                    atividades_secundarias.append(cnae_text)
            
            return atividades_secundarias
            
        return []

    def to_json(self):
        
        # padrao para salvar no redis
        dados = {
            "status_task": "processado",
            "dados_processados": self.tratar_dados()
        }
        
        return json.dumps(dados, indent=4)

