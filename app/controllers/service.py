from bs4 import BeautifulSoup
import requests

url_list = [
    "https://www.bne.com.br/vagas-de-emprego-na-area-de-informatica?Area=Inform%C3%A1tica&Sort=0&Page=1", 
]
def get_url_vaga(url_list):
    p_list = []
    urlVagas = []
    for url in url_list:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'lxml')
        p_list=(soup.find_all("a", attrs={"class":"JobListLink linkDesktop"}))
        for a in p_list:
            soupA = BeautifulSoup(str(a), "html.parser").a
            urlVagas.append("https://www.bne.com.br"+soupA['href'])
    return urlVagas


def get_job_info(url):
    dados = []
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    dados.append(soup.find("div", attrs={"class":"job__title"}).text.strip())
    div_header_detail = soup.find("div", attrs={"class":"job__header__info"}).find_all(attrs={"class":"job__detail"})
    for info in div_header_detail:
       soupinfo = BeautifulSoup(str(info), "html.parser").text.replace("\n", "").strip()
       dados.append(soupinfo)
    return dados
    

def get_job_desc(url):
    dados = []
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    div_desc = (soup.find("div",attrs={"class":"job__description"}).find_all("h3"))
    for info in div_desc:
        soup_desc = BeautifulSoup(str(info), "html.parser").text.replace("\n", "").replace("\r", "").strip()
        dados.append(soup_desc)
    return dados


def info_vaga(url_list):
    dados_vaga = []
    urls = get_url_vaga(url_list)
    for url in urls:         
        dados_vaga.append(get_job_info(url))
    key_list = ['subject', 'task', 'place', 'wage', 'company']
    info_vaga_dict = {}
    cont = 0
    for x in dados_vaga:        
        info_vaga = dict(zip(key_list, x))
        info_vaga_dict[cont] = info_vaga
        cont += 1       
                
    return info_vaga_dict


def description(url_list):
    description = []
    urls = get_url_vaga(url_list)
    for url in urls:
        description.append(get_job_desc(url))
    key_list = ['description', 'assignment']
    drescription_vaga = {}
    cont = 0
    for x in description:        
        info_vaga = dict(zip(key_list, x[0:2]))
        drescription_vaga[cont] = info_vaga
        cont += 1

    return drescription_vaga


def filter_area(url_list, job_opportunity):
    task = []
    our_area = []
    for x in range(0, len(job_opportunity)):
        task.append(job_opportunity[x]['task'][14:])
    for x in task:
        if x == 'Vendedor' or x == 'Representante Comercial' or x == 'Vendedor Externo' or x == 'Atendente' or x == 'Vendedor Interno':
            our_area.append('Comércio')
        elif x == 'Auxiliar de Cozinha' or x == 'Cozinheiro' or x == 'Cozinheira' or x == 'Garçom' or x == 'Pizzaiolo':
            our_area.append('Alimentos')
        elif x == 'Operador de Caixa' or x == 'Caixa' or x == 'Assistente Financeiro' or x == 'Analista Financeiro' or x == 'Auxiliar Financeiro':
            our_area.append('Financeiro')
        elif x == 'Analista Contábilr' or x == 'Analista Fiscal' or x == 'Assistente Contábil' or x == 'Assistente Fiscal' or x == 'Auxiliar Contábil':
            our_area.append('Contabilidade')
        elif x == 'Designer Gráfico' or x == 'Projetista' or x == 'Designer' or x == 'Web Designer' or x == 'Arte Finalista':
            our_area.append('Gráfica')
        elif x == 'Manicure' or x == 'Esteticista' or x == 'Cuidador de Idoso' or x == 'Babá' or x == 'Cabeleireiro':
            our_area.append('Servicos Pessoais')
        elif x == 'Vigilante' or x == 'Vigia' or x == 'Técnico de Segurança' or x == 'Segurança' or x == 'Operador de Monitoramento':
            our_area.append('Segurança')
        elif x == 'Estagiário' or x == 'Auxiliar Administrativo' or x == 'Recepcionista' or x == 'Assistente Administrativo' or x == 'Secretária':
            our_area.append('Administrativo')
        elif x == 'Auxiliar de Serviços Gerais' or x == 'Auxiliar de Limpeza' or x == 'Doméstica' or x == 'Ajudante Geral' or x == 'Ajudante de Serviços Gerais':
            our_area.append('Limpeza')
        elif x == 'Operador de Telemarketing' or x == 'Analista de Marketing' or x == 'Telemarketing' or x == 'Assistente de Marketing' or x == 'Televendas':
            our_area.append('Marketing')
        elif x == 'Analista de RH' or x == 'Analista de Departamento Pessoal' or x == 'Assistente de Departamento Pessoal' or x == 'Assistente de RH' or x == 'Auxiliar de Departamento Pessoal':
            our_area.append('Recursos Humanos')
        elif x == 'Professor' or x == 'Professor de Inglês' or x == 'Monitor' or x == 'Pedagogo' or x == 'Instrutor de Informática':
            our_area.append('Educação')
        elif x == 'Porteiro' or x == 'Jardineiro' or x == 'Controlador de Acesso' or x == 'Caseiro' or x == 'Controlador de Pragas':
            our_area.append('Servicos Domésticos')
        elif x == 'Marceneiro' or x == 'Montador de Móveis' or x == 'Estofador' or x == 'Meio Oficial Marceneiro' or x == 'Ajudante de Marceneiro':
            our_area.append('Móveis')
        elif x == 'Motorista' or x == 'Estoquista' or x == 'Operador de Empilhadeira' or x == 'Auxiliar de Logística' or x == 'Motorista Carreteiro':
            our_area.append('Logística')
        elif x == 'Eletricista' or x == 'Auxiliar de Manutenção' or x == 'Instalador' or x == 'Mecânico de Manutenção' or x == 'Técnico de Manutenção':
            our_area.append('Manutenção')
        elif x == 'Auxiliar de Produção' or x == 'Operador de Máquinas' or x == 'Operador de Produção' or x == 'Ajudante de Produção' or x == 'Líder de Produção':
            our_area.append('Produção')
        elif x == 'Mecânico' or x == 'Soldador' or x == 'Serralheiro' or x == 'Torneiro Mecânico' or x == 'Chapeiro':
            our_area.append('Mecânico')
        elif x == 'Mecânico Automotivo' or x == 'Pintor Automotivo' or x == 'Lavador de Carros' or x == 'Borracheiro' or x == 'Mecânico de Automóveis':
            our_area.append('Veículos')
        elif x == 'Costureira' or x == 'Costureiro' or x == 'Passadeira' or x == 'Cortador de Tecidos' or x == 'Operador de Corte':
            our_area.append('Têxteis')
        elif x == 'Promotor' or x == 'Advogado' or x == 'Assistente Jurídico' or x == 'Auxiliar Jurídico' or x == 'Advogado Trabalhista':
            our_area.append('Jurídico')
        elif x == 'Desenvolvedor' or x == 'Desenvolvedor JAVA' or x == 'Programador' or x == 'Analista de Sistemas' or x == 'Analista de Suporte':
            our_area.append('Informática')
        elif x == 'Pedreiro' or x == 'Técnico em Segurança do Trabalho' or x == 'Servente de Obras' or x == 'Pintor' or x == 'Inspetor de Qualidade':
            our_area.append('Construção')
        elif x == 'Técnico de Enfermagem' or x == 'Enfermeiro' or x == 'Fisioterapeuta' or x == 'Nutricionista' or x == 'Dentista':
            our_area.append('Saúde')
        elif x == 'Farmacêutico' or x == 'Atendente de Farmácia' or x == 'Auxiliar de Farmácia de Manipulação' or x == 'Técnico em Farmácia' or x == 'Gerente de Farmácia':
            our_area.append('Farmaceutico')
        elif x == 'Corretor de Imóveis' or x == 'Consultor Imobiliário' or x == 'Vistoriador de Imóveis' or x == 'Gerente Imobiliário' or x == 'Encarregado Imobiliário':
            our_area.append('Imobiliária')
        elif x == 'Auxiliar Técnico de Campo' or x == 'Técnico de Campo' or x == 'Trabalhador Rural' or x == 'Tratorista Agrícola' or x == 'Auxiliar de Campo':
            our_area.append('Agronegócios')
        else:
            our_area.append('Outros')
    
    return our_area

