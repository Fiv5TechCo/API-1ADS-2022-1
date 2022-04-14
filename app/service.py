from bs4 import BeautifulSoup
import requests

url_list = [
    "https://www.bne.com.br/vagas-de-emprego/?Page=1", 
    #"https://www.bne.com.br/vagas-de-emprego/?Page=2",
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
    #description = []
    dados_vaga = []
    urls = get_url_vaga(url_list)
    for url in urls:         
        dados_vaga.append(get_job_info(url))
        #description.append(get_job_desc(url))
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


job_opportunity= info_vaga(url_list)
job_description = description(url_list)





"""
key_list = ['name', 'age', 'address']
value_list = ['Johnny', '27', 'New York']

dict_from_list = dict(zip(key_list, value_list))
print(dict_from_list)
Titulo
Cargo
Local
Salário
Empresa



"""