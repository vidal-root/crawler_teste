
from bs4 import BeautifulSoup

html = '''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
 
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
	<title>Consulta Pública ao Cadastro - Estado de Goiás</title>
	
	<link rel="stylesheet" type="text/css" href="/library/bootstrap4/css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="css/css.css">
	
	<link rel="stylesheet" type="text/css" href="/FolhaEstilo/formularioCss.css">
	<script language="javascript" initialize="none" src="/library/components/zion/zion.js"></script>
	<script language="javascript" initialize="none" src="/library/bootstrap4/js/bootstrap.js"></script>

</head> 

<BODY BACKGROUND="" BGCOLOR="#ffffff" TEXT="#000000" xtopmargin="50">

<div class="container doc"> 
  <div class="row justify-content-md-center"> 
	<div class="col col-12 ">

		<div align="center"><img src="/images/economia-logo-2.png" width="150" border="0" /></div>
		<div align="center" style="margin:0px 0 0px 0; font-size:19px; font-weight:bold;">Secretaria da Economia do Estado de Goiás</div>
		<div align="center" style="margin:0px 0 50px 0; font-size:21px; font-weight:bold;">Consulta Pública ao Cadastro de Contribuintes</div>
	
	
	
		<div class="row">
			
			<div class="col box">
				
					<span class="label_title">CNPJ</span>
					<span class="label_text">
						00.012.377/0001-60
					</span>
				  
			</div>
			
			<div class="col box">
				<span class="label_title">Inscri&ccedil;&atilde;o Estadual</span>
				<span class="label_text">10.107.310-0</span>
			</div>
			
			<div class="col box">
				<span class="label_title">Cadastro Atualizado em</span>
				<span class="label_text">02/10/2024 14:31:53</span>
			</div>
			
		</div>
	
	
		<div class="row">
			
			<div class="col box">
			
				<div class="item">
						 
						<span class="label_title">Nome Empresarial</span>
					
					<span class="label_text">
						CEREAL COMERCIO EXPORTACAO E REPRESENTACAO AGROPECUARIA SA
					</span>
				</div>
				
				
				<div class="item">
					<span class="label_title">Contribuinte?</span>
					<span class="label_text">Sim</span>
				</div>
				
				
					<div class="item"> 
						<span class="label_title">Nome da Propriedade:</span>
						<span class="label_text">FAZ RIO VERDINHO BARRA GRANDE</span>
					</div>
				
				
			</div>
		
		</div>
	
		
		
		<div class="row">
			
			<div class="col box">
				
				<div class="label_title">Endereço Estabelecimento </div>
	  			<span class="label_text">RODOVIA&nbsp; BR-060, nº SN, KM 381, SETOR INDUSTRIAL  - RIO VERDE GO, CEP: 75.905-025 </span>

		  
			</div> 
		
		</div> 
	
	
	
		<div class="row">
			
			<div class="col box">
				
				<div class="box_title">Atividade Econômica </div>
	  			
				
						&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="label_text"><strong>Atividade Principal</strong></span>
						<br>
					
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					1041400 - Fabricação de óleos vegetais em bruto, exceto óleo de milho
					</span>
					
				
						&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="label_text"><strong>Atividade Secundária</strong></span>
						<br>
					
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					4930202 - Transporte rodoviário de carga, exceto produtos perigosos e mudanças, intermunicipal, interestadual e internacional
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					4683400 - Comércio atacadista de defensivos agrícolas, adubos, fertilizantes e corretivos do solo
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					4692300 - Comércio atacadista de mercadorias em geral, com predominância de insumos agropecuários
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					4632001 - Comércio atacadista de cereais e leguminosas beneficiados
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					4724500 - Comércio varejista de hortifrutigranjeiros
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					4930203 - Transporte rodoviário de produtos perigosos
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					4633801 - Comércio atacadista de frutas, verduras, raízes, tubérculos, hortaliças e legumes frescos
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					4623109 - Comércio atacadista de alimentos para animais
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					5211701 - Armazéns gerais - emissão de warrant
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					1932200 - Fabricação de biocombustíveis, exceto álcool
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					1066000 - Fabricação de alimentos para animais
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					4623108 - Comércio atacadista de matérias-primas agrícolas com atividade de fracionamento e acondicionamento associada
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					7490103 - Serviços de agronomia e de consultoria às atividades agrícolas e pecuárias
					</span>
					
				
								
					<span class="label_text" style="display:block;margin-left:50px; margin-top:8px; margin-bottom:8px;">
					4619200 - Representantes comerciais e agentes do comércio de mercadorias em geral não especializado
					</span>
					
				

		  
			</div> 
		
		</div> 
		
	
	
		<div class="row">
			
			<div class="col box">
				
				<div class="box_title">Informações Complementares</div>
				
				<div class="item">
					<span class="label_title">Unidade Auxiliar:</span>
					<span class="label_text">
					
						UNIDADE PRODUTIVA<br />
						
					</span>	
				</div>
				
				<div class="item">
					<span class="label_title">Condição de Uso:</span>
					<span class="label_text">
						
							---
						
					</span>
			  	</div>
		  
		  		<div class="item">
					<span class="label_title">Data Final de Contrato:</span>
					<span class="label_text">
						
							---
						
					</span>	
		  		</div>
				
				<div class="item">
					<span class="label_title">Regime de Apuração:</span>
					<span class="label_text">Normal</span>
				</div>
				
				<div class="item">
					<span class="label_title">Situação Cadastral Vigente:</span>
					<span class="label_text">
						Ativo - HABILITADO
					</span>	
				</div>
				
				<div class="item">
					<span class="label_title">Data desta Situação Cadastral:</span>
					<span class="label_text">30/01/2009</span>	
				</div>
				
				<div class="item">
					<span class="label_title">Data de Cadastramento:</span>
					<span class="label_text">10/12/1981</span>
		  		</div>
				
				<div class="item">
					<span class="label_title">Operações com NF-E:</span> 
					<span class="label_text">
					
						Habilitado
					
					</span>
		  		</div>
				
				
			</div>
			
		</div>
	
	
		<div class="row">
			
			<div class="col box">
				
				<div class="label_title">Observações</div>
				
				<ul>
					<li>Os dados acima são baseados em informações fornecidas pelo contribuinte, estando sujeitos a posterior confirmação pelo FISCO.</li>
		  			<li>A data da situação cadastral refere-se à data da última atualização dessa situação.</li>
				</ul>
				
			</div>
		</div>
		
		
		
		<div class="row">
			
			<div class="col box">
			 	<span class="label_title">Data da Consulta</span>
			 	<span class="label_text">07/11/2024 10:58:12</span>
			</div>
			
			<div class="col">
				<!--<span class="label_title">Cadastro Atualizado em</span>
		 		<span class="label_text"></span>-->
				<div align="center">
					<a href="nEsclarecimento.asp" target="_blank">
<img src="img/duvidas.jpg" width="315" height="71" border="0"></a>
				</div>
				
			</div>
			
			
			
		</div>
		
		
	
 	</div> 
 </div> 
</div> 
 
</html>
</body>
</html>
'''


html_site = BeautifulSoup(html, 'html.parser')

def getAtividadesSecundarias():
    # Encontrar o <strong> que contém "Atividade Secundária"
    atividade_secundaria = html_site.find('strong', string="Atividade Secundária")
    if atividade_secundaria:
        # Encontrar o próximo irmão <span> com a classe 'label_text', que contém os CNAEs
        atividades_secundarias = []
        for span in atividade_secundaria.find_parent().find_all_next('span', class_='label_text'):
            # Filtrar apenas as linhas que contêm números CNAEs (formato: XXXXXXX - descrição)
            cnae_text = span.text.strip()
            if re.match(r'^\d{7} -', cnae_text):  # Verifica se é um CNAE (7 dígitos seguidos de " -")
                atividades_secundarias.append(cnae_text)
        
        return atividades_secundarias
        
    return []