from flask import render_template, request
from app import app
from app.controllers import service, createMap


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')



@app.route("/vagas")
def quemsomos():
    job_opportunity = service.job_opportunity
    job_description = service.job_description
    url_vagas = service.url_vagas   
    return render_template('vagas.html', job_opportunity = job_opportunity,
     job_description = job_description, url_vagas = url_vagas)



@app.route("/localizacao", methods=["POST", "GET"])
def localizacao():
    if request.method == 'POST':
        coordinates = request.form["coordinates"]
        createMap.createMap(coordinates)
        return render_template('localizacao.html')
    else:
        return render_template('localizacao.html')