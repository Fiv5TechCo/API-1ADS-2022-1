from flask import render_template
from app import app
from app import service


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')



@app.route("/vagas")
def quemsomos():
    job_opportunity = service.job_opportunity
    job_description = service.job_description   
    return render_template('vagas.html', job_opportunity = job_opportunity, job_description = job_description )


