import requests
from bs4 import BeautifulSoup

class crawlerDOU:
    def __init__(self):
        self.base_url = "http://portal.imprensanacional.gov.br/web/guest/diario-oficial-da-uniao"
        self.links_dia = [] 

    def baixa_links_ultima(self):
        """ Este metodo baixa todos os links da ultima edicao do diario oficial 
        e guarda na lista 'links_ultima'
        """
        pagina_principal = requests.get(self.base_url)
        id_dia = pagina_principal.text.split('" id="_101_INSTANCE_')[1].split('awi_ocer')[0]
        n_paginas = int(pagina_principal.text.split('Página 1 de ')[1].split('">')[0])
        print(f'O id do dia é {id_dia} e o numero de paginas a ser buscado é {n_paginas}')
        url = f'http://portal.imprensanacional.gov.br/web/guest/diario-oficial-da-uniao?p_p_id=101_INSTANCE_{id_dia}awi&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=_118_INSTANCE_teqPmWfhUCPY__column-1&p_p_col_pos=1&p_p_col_count=2&_101_INSTANCE_{id_dia}awi_delta=20&_101_INSTANCE_{id_dia}awi_keywords=&_101_INSTANCE_{id_dia}awi_advancedSearch=false&_101_INSTANCE_{id_dia}awi_andOperator=true&p_r_p_564233524_resetCur=false&_101_INSTANCE_{id_dia}awi_cur='
        print("Baixando os links do dia...")
        for i in range(1, n_paginas+1):
            print(f'{i},', end=',')
            requests.adapters.DEFAULT_RETRIES = 100
            pagina = requests.get(url + str(i))
            self.coleta_links(pagina.text)     
        
    def coleta_links(self, pagina):
        parsed_page = BeautifulSoup(pagina,'html.parser')
        abstracts = parsed_page.find_all('div', attrs={'class':'asset-title'})
        links = [ x.find('a')['href'] for x in abstracts  ]
        self.links_dia.append(links)

