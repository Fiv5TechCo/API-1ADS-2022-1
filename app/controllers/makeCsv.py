from encodings import utf_8
from app import app, db
from app.models.tables import Vagas
import pandas as pd
import csv, json, os

job_details = db.session.query(Vagas).all()
def make_csv(job_details):
    subject = []
    area = []
    localizacao = []
    city = []
    state = []
    task = []
    wage = []
    company = []
    url = []
    for indice in range(0, len(job_details)):
        subject.append(job_details[indice].subject)        
        localizacao.append(job_details[indice].place)
        city.append(job_details[indice].city)
        task.append(job_details[indice].task)
        wage.append(job_details[indice].wage)
        company.append(job_details[indice].company)
        state.append(job_details[indice].state)
        area.append(job_details[indice].area)
        url.append(job_details[indice].url)
    dict = {'subject': subject, 'task': task,'area': area, 'place': localizacao, 'city': city,
    'state': state, 'wage': wage, 'company':company, 'url':url}     
    df = pd.DataFrame(dict) 
    df.to_csv(os.path.join('app/models', 'for_Metricas.csv'), encoding="utf-8")


def convert_json(mycsv, myjson):
    data = []
    with open(os.path.join('app/models', mycsv), 'r', encoding='utf8') as file_csv:    
        csvreader = csv.DictReader(file_csv)
        for csvRow in csvreader:
            data.append(csvRow)
    
    with open(os.path.join('app/models', myjson), 'w', encoding='utf8') as file_json:
        file_json.write(json.dumps(data, indent=4, ensure_ascii=False))
    
