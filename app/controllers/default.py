from flask import flash, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app import app, db
from app.controllers import service, createMap, makeCsv, createGraph, createHeatmap, vagarefresh
from app.models.tables import Vagas, User
from app.models.forms import MyFilterForm , LoginForm, AddForm, ResetDb


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/vagas", methods=["POST", "GET"], defaults={"page": 1})
@app.route('/vagas/page=<int:page>', methods=["GET", "POST"])
def vagas(page):
    have_filter = False
    page = page
    per_page = 10   
    form_filter = MyFilterForm()
    form_filter.validate_on_submit()
    choice_filter = form_filter.my_filter.data
    if request.method == 'POST' and form_filter.validate_on_submit():
        return redirect(url_for('area_filter_page', choice_filter=choice_filter))    
    job_details = Vagas.query.paginate(page,per_page,error_out=False)
    #job_details_len = len(job_details)
    if request.method == 'POST':
        try:
            vaga_id = request.form['vagaId']
            vaga_id = int(vaga_id)
            r = Vagas.query.get(vaga_id)
            db.session.delete(r)
            db.session.commit()
            return redirect(url_for('vagas', job_details = job_details, form_filter = form_filter,
            have_filter=have_filter))
        except:
            return redirect(url_for('vagas', job_details = job_details, form_filter = form_filter,
            have_filter=have_filter)) 
    return render_template('vagas.html', job_details = job_details, form_filter = form_filter,
    have_filter=have_filter)


@app.route('/vagas/<choice_filter>', methods=["GET", "POST"], defaults={"page": 1})
@app.route('/vagas/<choice_filter>/page=<int:page>', methods=["GET", "POST"])
def area_filter_page(page, choice_filter):
    try:
        page = page
        have_filter = choice_filter
        per_page = 10
        form_filter = MyFilterForm()
        job_details = Vagas.query.filter_by(area=choice_filter).paginate(page,per_page,error_out=False)
        #job_details_len = len(job_details)
        if form_filter.validate_on_submit():
            return redirect(url_for('vagas', job_details = job_details, form_filter = form_filter,
        have_filter=have_filter)) 
        if request.method == 'POST':
            try:
                vaga_id = request.form['vagaId']
                vaga_id = int(vaga_id)
                r = Vagas.query.get(vaga_id)
                db.session.delete(r)
                db.session.commit()
                return redirect(url_for('area_filter_page',choice_filter=choice_filter))
            except:
                return redirect(url_for('vagas', job_details = job_details, form_filter = form_filter,
                have_filter=have_filter))    
        return render_template('vagas.html', job_details = job_details, form_filter = form_filter,
        have_filter=have_filter)
    except:
        return redirect(url_for('vagas', job_details = job_details, form_filter = form_filter,
        have_filter=have_filter))
        


@app.route("/cursos")
def cursos():
    return render_template('cursos.html')


@app.route("/metricas")
def metricas():
    createHeatmap.createHeatmap()
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


@app.route("/login", methods=["GET", "POST"])
def login():
    login_error = False
    form_login = LoginForm()
    if form_login.validate_on_submit():
        user = User.query.filter_by(username=form_login.username.data).first()
        if user and user.password == form_login.password.data:
            login_user(user)
            return redirect(url_for("index"))
        else:
            login_error = True
            flash("Login invalido.")
    return render_template('login.html', form_login=form_login, login_error=login_error)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    add_form = AddForm()
    reset_db = ResetDb()
    have_reset = False
    cadastrada = False
    if add_form.validate_on_submit():
        place = f'{add_form.city.data} / {add_form.state.data}'
        vaga_post = Vagas("Cadastrada manualmente", add_form.task.data, add_form.area.data, place, add_form.city.data,
        add_form.state.data, add_form.wage.data, add_form.company.data, add_form.description.data, add_form.assignmen.data,
        "Cadastrada manualmente")
        db.session.add(vaga_post)
        db.session.commit()
        job_details = Vagas.query.all()
        makeCsv.make_csv(job_details)
        makeCsv.convert_json('for_Metricas.csv', 'for_Metricas.json')
        createGraph.areaGraph()
        createGraph.estadoGraph()
        createGraph.cursoGraph()
        cadastrada = True
        flash("Cadastrado com sucesso.")
        return render_template('cadastro.html', add_form=add_form, cadastrada=cadastrada, reset_db=reset_db, have_reset=have_reset)
    r = Vagas.query.all()
    if reset_db.validate_on_submit():
        if not r:
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
            job_details = Vagas.query.all()
            makeCsv.make_csv(job_details)
            makeCsv.convert_json('for_Metricas.csv', 'for_Metricas.json')
            createGraph.areaGraph()
            createGraph.estadoGraph()
            createGraph.cursoGraph()
            have_reset = True
            flash("Vagas raspadas com sucesso.")
        else:
            for d in r:
                db.session.delete(d)
            db.session.commit()
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
            job_details = Vagas.query.all()
            makeCsv.make_csv(job_details)
            makeCsv.convert_json('for_Metricas.csv', 'for_Metricas.json')
            createGraph.areaGraph()
            createGraph.estadoGraph()
            createGraph.cursoGraph()
            have_reset = True
            flash("Vagas raspadas com sucesso.")
    return render_template('cadastro.html', add_form=add_form, cadastrada=cadastrada, reset_db=reset_db, have_reset=have_reset)


@app.route("/refresh")
def refresh():
    vagarefresh.vaga_refresh()
    job_details = Vagas.query.all()
    makeCsv.make_csv(job_details)
    makeCsv.convert_json('for_Metricas.csv', 'for_Metricas.json')
    createGraph.areaGraph()
    createGraph.estadoGraph()
    createGraph.cursoGraph()
    return redirect(url_for("index"))
