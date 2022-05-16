from flask import render_template, request, redirect, url_for
from app import app, db
from app.controllers import service, createMap, makeCsv
from app.models.tables import Vagas
from app.models.forms import MyFilterForm


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/vagas", methods=["POST", "GET"])
def vagas():
    is_db_create = True
    have_filter = False

    if not is_db_create:
        job_opportunity = service.info_vaga(service.url_list)
        job_description = service.description(service.url_list)
        url_vagas = service.get_url_vaga(service.url_list)
        filterArea = service.filter_area(service.url_list, job_opportunity)
        for x in range(0, len(job_opportunity)):
            i = Vagas(job_opportunity[x]['subject'], job_opportunity[x]['task'][14:], filterArea[x],
            job_opportunity[x]['place'][12:].strip(), job_opportunity[x]['place'][12:-4].strip(), 
            job_opportunity[x]['place'][-2:], job_opportunity[x]['wage'][9:], job_opportunity[x]['company'][8:].strip(), 
            job_description[x]['description'], job_description[x]['assignment'], url_vagas[x])
            db.session.add(i)
        db.session.commit()
        
    else:      
        form_filter = MyFilterForm()
        form_filter.validate_on_submit()
        choice_filter = form_filter.my_filter.data
        if request.method == 'POST':
            return redirect(url_for('area_filter_page', choice_filter=choice_filter))    
        job_details = Vagas.query.all()
        job_details_len = len(job_details)
        makeCsv.make_csv(job_details)
        makeCsv.convert_json('for_Metricas.csv', 'for_Metricas.json')

    return render_template('vagas.html', job_details = job_details, form_filter = form_filter,
    job_details_len=job_details_len, have_filter=have_filter)


@app.route("/vagas/<choice_filter>", methods=["GET"])
def area_filter_page(choice_filter):
    have_filter = True
    form_filter = MyFilterForm()
    job_details = Vagas.query.filter_by(area=choice_filter).all()
    job_details_len = len(job_details)       
    return render_template('vagas.html', job_details = job_details, form_filter = form_filter,
    job_details_len=job_details_len, have_filter=have_filter)


@app.route("/cursos")
def cursos():
    return render_template('cursos.html')

@app.route("/metricas")
def metricas():
    return render_template('metricas.html')


@app.route("/localizacao", methods=["POST", "GET"])
def localizacao():
    if request.method == 'POST':
        coordinates = request.form["coordinates"]
        if coordinates != '':
            createMap.createMap(coordinates)
            return render_template('localizacao.html')
        else:
            return render_template('localizacao.html')
    else:
        return render_template('localizacao.html')