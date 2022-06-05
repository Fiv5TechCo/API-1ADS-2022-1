import requests, json
from app import db
from app.models.tables import Vagas


def vaga_refresh():
    urls = []
    with open('app/models/for_Metricas.json', encoding='utf_8') as my_json:
        data = data = json.load(my_json)
        for i in data:
            url = i['url']
            urls.append(url)

    for i in urls:
        if i != "Cadastrada manualmente":
            try:
                x = requests.get(i)
                continue
            except:
                url = Vagas.query.filter_by(url=i).first()
                try:
                    db.session.delete(url)
                    db.session.commit()
                except:
                    continue


